import os
import json
import requests
import numpy as np
import faiss
import gradio as gr
from pypdf import PdfReader

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"  
FAISS_INDEX_FILE = "local_vectors.index"
TEXT_CACHE_FILE = "text_chunks.json"

# --- FUNCTION 1: INCREMENTAL BATCH-SAFE PDF INGESTION ---
def process_uploaded_pdf(file_obj):
    if file_obj is None:
        return "⚠️ No file uploaded. Please select a PDF."
        
    try:
        # 1. LOAD OR INITIALIZE EXISTING STORAGE FILES
        existing_chunks = []
        if os.path.exists(TEXT_CACHE_FILE) and os.path.exists(FAISS_INDEX_FILE):
            print("⚡ Found existing database. Loading files to append new data...")
            with open(TEXT_CACHE_FILE, "r") as f:
                existing_chunks = json.load(f)
            faiss_index = faiss.read_index(FAISS_INDEX_FILE)
        else:
            print("✨ No existing database found. Creating a brand new one...")
            faiss_index = None

        # 2. EXTRACT TEXT
        print("📄 Reading PDF pages...")
        reader = PdfReader(file_obj.name)
        raw_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text: raw_text += text + "\n"

        if not raw_text.strip():
            return "⚠️ This PDF seems to be empty or lacks selectable text."

        # 3. CHUNK TEXT (1500 chars window)
        chunks = []
        start = 0
        while start < len(raw_text):
            chunks.append(raw_text[start:start+1500])
            start += 1350

        # 4. LOOP & SAVE IN INCREMENTAL SAFETY BATCHES
        batch_vectors = []
        batch_texts = []
        batch_size = 20  # Saves to your hard drive every 20 chunks
        
        print(f"🔢 Processing {len(chunks)} chunks incrementally...")
        for i, chunk in enumerate(chunks):
            # Skip if this exact chunk text was already processed in a previous crash run
            if chunk in existing_chunks:
                continue
                
            # Get embedding vector from local Ollama
            res = requests.post(f"{OLLAMA_URL}/api/embeddings", json={"model": EMBED_MODEL, "prompt": chunk})
            vector = res.json()["embedding"]
            
            batch_vectors.append(vector)
            batch_texts.append(chunk)
            
            # Trigger safe disk commit when batch is full or we hit the final element
            if len(batch_vectors) == batch_size or (i + 1) == len(chunks):
                np_batch = np.array(batch_vectors).astype('float32')
                faiss.normalize_L2(np_batch)
                
                # Initialize index framework on the very first batch if it didn't exist
                if faiss_index is None:
                    vector_dimension = np_batch.shape[1]
                    faiss_index = faiss.IndexFlatIP(vector_dimension)
                
                # Append vectors directly to the active math index layout
                faiss_index.add(np_batch)
                
                # Append strings directly to our running text array cache
                existing_chunks.extend(batch_texts)
                
                # --- SOLIDIFY COMMIT TO HARD DRIVE ---
                faiss.write_index(faiss_index, FAISS_INDEX_FILE)
                with open(TEXT_CACHE_FILE, "w") as f:
                    json.dump(existing_chunks, f)
                
                print(f"💾 Safety checkpoint saved to disk: Chunks processed up to {i+1}/{len(chunks)}")
                
                # Clear temporary batch arrays for the next loop run
                batch_vectors = []
                batch_texts = []

        return f"✅ Success! Document processed completely. Total chunks stored: {len(existing_chunks)}"
        
    except Exception as e:
        return f"❌ Error processing PDF: {str(e)}"

# --- FUNCTION 2: CHAT RESPONSE LOGIC (MULTI-CONTEXT STREAMING) ---
def chat_with_pdf(message, history):
    if history is None:
        history = []

    if not os.path.exists(FAISS_INDEX_FILE) or not os.path.exists(TEXT_CACHE_FILE):
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": "⚠️ Please upload a PDF file on the left panel first!"})
        yield "", history
        return

    try:
        faiss_index = faiss.read_index(FAISS_INDEX_FILE)
        with open(TEXT_CACHE_FILE, "r") as f:
            chunks = json.load(f)

        query_res = requests.post(f"{OLLAMA_URL}/api/embeddings", json={"model": EMBED_MODEL, "prompt": message})
        query_vector = np.array([query_res.json()["embedding"]]).astype('float32')
        faiss.normalize_L2(query_vector)

        # Search for the top 3 relevant chunks
        D, I = faiss_index.search(query_vector, k=3) 
        
        merged_context = ""
        for idx in I[0]:
            if idx != -1 and idx < len(chunks):  
                merged_context += chunks[idx] + "\n\n---\n\n"

        system_prompt = (
            "You are an expert educator who explains complex topics in simple layman's terms. "
            "Act exactly like ChatGPT's 'Explain Like I'm 5' mode. Use real-world analogies, short sentences, and bullet points. "
            f"Answer the question using ONLY this context extracted from the document:\n\n{merged_context}"
        )

        reply = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                "stream": True  
            },
            stream=True
        )
        
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": ""})
        
        for line in reply.iter_lines():
            if line:
                chunk_data = json.loads(line.decode('utf-8'))
                token = chunk_data.get("message", {}).get("content", "")
                history[-1]["content"] += token
                yield "", history
                
    except Exception as e:
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})
        yield "", history

# --- LAYOUT BUILDER ---
with gr.Blocks() as demo:
    gr.Markdown("# 📚 Private Offline Incremental PDF Chatbot")
    gr.Markdown("Robust storage architecture designed to continuously append chunks safely to disk.")
    
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="Upload Heavy PDF Here", file_types=[".pdf"])
            upload_btn = gr.Button("⚙️ Ingest and Process Book", variant="primary")
            status_output = gr.Textbox(label="System Status Log", value="Ready...")
            
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(height=450)
            msg_input = gr.Textbox(placeholder="Ask anything about the document...", container=False)
            clear_btn = gr.ClearButton([msg_input, chatbot])

    upload_btn.click(fn=process_uploaded_pdf, inputs=file_input, outputs=status_output)
    msg_input.submit(fn=chat_with_pdf, inputs=[msg_input, chatbot], outputs=[msg_input, chatbot])

if __name__ == "__main__":
    demo.launch(theme="soft")
