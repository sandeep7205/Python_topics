# PDF Q&A Chatbot --- Project Memory

## User Goal

The user is on a path toward **Data Engineering** and wants to learn by
building something useful rather than following tutorials passively.

The current project idea is a:

> **Local PDF Q&A Chatbot / RAG Data Pipeline**

The user knows some basics of **Python and SQL** and wants mentor-style
guidance.

### Important learning preference

-   Do **not** give full code unless absolutely necessary.
-   Prefer:
    -   explanations
    -   hints
    -   small experiments
    -   questions that make the user think
    -   debugging/review of their code
    -   guidance on what to search for
-   The user wants a **brutally honest mentor style**, but still
    practical and supportive.
-   The goal is to **learn while building**, not merely finish a
    chatbot.
-   Avoid overwhelming the user with too many technologies at once.

------------------------------------------------------------------------

# Project Goal

Build a useful local application where a user can:

1.  Upload a PDF.
2.  Extract text.
3.  Clean the text.
4.  Split it into chunks.
5.  Generate embeddings.
6.  Store/search embeddings using a vector index.
7.  Retrieve relevant chunks for a question.
8.  Send the relevant context to a local LLM.
9.  Generate an answer.
10. Show the answer with source/page references.

High-level pipeline:

``` text
PDF
 ↓
Extract text
 ↓
Clean text
 ↓
Chunk text
 ↓
Generate embeddings
 ↓
Vector index / FAISS
 ↓
User question
 ↓
Question embedding
 ↓
Similarity search
 ↓
Relevant chunks
 ↓
Prompt
 ↓
Local LLM
 ↓
Answer + sources
```

The project should eventually become more than a basic chatbot: it
should demonstrate **data ingestion, transformation, storage, retrieval,
pipeline design, testing, and engineering practices**.

------------------------------------------------------------------------

# Suggested Technology Stack

## Initial stack

``` text
Python
PyMuPDF / pypdf
Sentence Transformers
FAISS
Ollama
Streamlit
SQL
Git
```

## Later / optional

``` text
PostgreSQL
Docker
FastAPI
A dedicated vector database
Airflow
Cloud deployment
```

Important rule:

> Do not add infrastructure just because it is popular. Add a technology
> when there is a clear problem it solves.

------------------------------------------------------------------------

# Architecture Concepts

## Ingestion

``` text
PDF
 ↓
Python
 ↓
Page-level text
```

Example conceptual structure:

``` python
{
    "page": 1,
    "text": "..."
}
```

------------------------------------------------------------------------

## Cleaning and chunking

Raw text should be transformed into manageable chunks.

Conceptually:

``` text
document
 ↓
pages
 ↓
clean text
 ↓
chunks + metadata
```

A chunk could look like:

``` python
{
    "document": "python.pdf",
    "page": 12,
    "chunk_id": 45,
    "text": "..."
}
```

Important concepts:

-   whitespace normalization
-   empty pages
-   duplicate/unwanted content
-   chunk size
-   chunk overlap
-   metadata
-   page references

Chunk size and overlap should eventually be treated as
experiments/trade-offs rather than magic numbers.

------------------------------------------------------------------------

# Embeddings

The user should understand embeddings before using them through a
framework.

Concept:

``` text
Text
 ↓
Embedding model
 ↓
Vector
```

Example conceptually:

``` text
"What is Python?"
        ↓
[0.21, -0.43, 0.82, ...]
```

The important idea:

> Similar meanings should produce vectors that are mathematically close
> enough for semantic search.

Learning topics:

-   embeddings
-   vector dimensions
-   cosine similarity
-   semantic similarity
-   sentence-transformers

Suggested searches:

``` text
sentence transformers Python embeddings
cosine similarity Python
```

------------------------------------------------------------------------

# FAISS

FAISS should initially be treated as:

> **A vector similarity search/indexing library**

rather than a replacement for every type of database.

Concept:

``` text
chunks
 ↓
embeddings
 ↓
FAISS index
```

Query:

``` text
question
 ↓
question embedding
 ↓
FAISS
 ↓
top-K relevant chunks
```

Important concepts:

-   vector index
-   similarity search
-   distance
-   top-K
-   retrieval

The user should first build retrieval **without an LLM**.

Milestone:

``` text
Question
 ↓
Embedding
 ↓
FAISS
 ↓
Top 3/5 relevant chunks
```

------------------------------------------------------------------------

# SQL vs Vector Search

SQL and vector search are not necessarily competing technologies.

SQL can store structured metadata such as:

``` text
documents
----------------
id
filename
uploaded_at
file_size
hash
```

and:

``` text
chunks
----------------
id
document_id
page_number
chunk_number
text
```

Potentially:

``` text
chat_history
----------------
id
question
answer
created_at
```

Vector search can handle semantic retrieval:

``` text
FAISS / Vector DB
 ↓
embedding similarity search
```

Potential architecture:

``` text
                 PostgreSQL
                     │
              metadata/chunks
                     │
PDF → processing ────┼────→ FAISS
                           │
                           ↓
                      vector search
```

Important engineering principle:

> Technology should follow the problem, not the other way around.

NoSQL should not be introduced unless the project has a clear reason for
needing it.

------------------------------------------------------------------------

# Local LLM / Ollama

Ollama should be introduced **after retrieval works**.

The LLM's role is generation, not primary document search.

Concept:

``` text
Retrieved context
       +
User question
       ↓
     Prompt
       ↓
     Ollama
       ↓
Generated answer
```

Prompt concept:

``` text
You are answering questions about a document.

Use ONLY the supplied context.

Context:
---------
chunk 1
chunk 2
chunk 3
---------

Question:
...

Answer:
```

Important learning topics:

-   local LLM
-   prompts
-   context
-   temperature
-   context window
-   tokens
-   hallucination
-   model limitations

Important distinction:

``` text
Retrieval = finding relevant information
Generation = producing the natural-language answer
```

------------------------------------------------------------------------

# RAG

The project is fundamentally a **Retrieval-Augmented Generation (RAG)**
system.

RAG flow:

``` text
Question
 ↓
Embedding
 ↓
Vector search
 ↓
Relevant chunks
 ↓
Prompt + context
 ↓
Local LLM
 ↓
Answer
```

The user should understand RAG conceptually before relying heavily on
frameworks such as LangChain.

Preferred learning order:

``` text
Understand
 ↓
Build simply
 ↓
Test
 ↓
Then use frameworks
```

Avoid:

``` text
Copy LangChain tutorial
 ↓
Everything magically works
 ↓
Claim "I learned RAG"
```

------------------------------------------------------------------------

# Streamlit

Streamlit should be introduced after the core pipeline works.

Its purpose is primarily the user interface.

Possible UI:

``` text
PDF Q&A Assistant

Upload PDF
[ Choose file ]

Status: Processing...

You: What is exception handling?

AI: Exception handling is...

Sources: Page 14, Page 15
```

Learning topics:

-   file upload
-   session state
-   chat interface
-   displaying metadata
-   error handling

Important:

> Do not start the project with Streamlit. Build the core Python
> pipeline first.

------------------------------------------------------------------------

# Project Structure

A possible structure:

``` text
pdf-rag/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── embedding/
│   ├── retrieval/
│   └── llm/
│
├── tests/
│
└── app/
```

Another possible modular structure discussed:

``` text
pdf_chatbot/
│
├── app.py
├── pdf_reader.py
├── chunker.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── llm.py
└── config.py
```

The exact structure is not fixed yet.

The key principle is separation of responsibilities:

``` text
PDF module
 ↓
Chunk module
 ↓
Embedding module
 ↓
Vector module
 ↓
Retriever module
 ↓
LLM module
 ↓
UI
```

Avoid a giant `app.py` containing every responsibility.

------------------------------------------------------------------------

# Roadmap / Sprint Plan

The project was divided into four phases and initially 10+ sprints.

------------------------------------------------------------------------

## PHASE 1 --- Data Pipeline Fundamentals

### Sprint 1 --- Project Foundation

Goal:

Understand the problem and create the project skeleton.

Learn:

-   Git
-   Python virtual environment
-   project structure
-   requirements/dependencies
-   configuration
-   README
-   basic logging

Deliverable:

A Git repository with a basic project structure and a Python program
that runs.

Mentor question:

> Why did we separate `raw` and `processed` data?

Initial README questions:

1.  What problem am I solving?
2.  Who would use this?
3.  What happens to a PDF after upload?
4.  Where does SQL fit?
5.  Where does vector search fit?

Do not Google the answers initially. Write the user's current
understanding first.

------------------------------------------------------------------------

### Sprint 2 --- PDF Ingestion

Goal:

``` text
PDF
 ↓
Python
 ↓
structured text
```

Learn:

-   pathlib
-   files/directories
-   PDF libraries
-   pages
-   metadata
-   exceptions

Deliverable:

``` text
PDF → page-level text
```

Suggested search:

``` text
Python PyMuPDF extract text from PDF
```

or:

``` text
pypdf extract text page Python
```

Do not start with a complete PDF chatbot tutorial.

------------------------------------------------------------------------

### Sprint 3 --- Cleaning + Chunking

Goal:

Understand data transformation:

``` text
raw data
 ↓
clean data
 ↓
transformed data
```

Learn:

-   whitespace normalization
-   empty text
-   duplicate content
-   chunk size
-   chunk overlap
-   metadata

Deliverable:

``` text
PDF
 ↓
pages
 ↓
clean text
 ↓
chunks + metadata
```

Experiment with small/medium/large chunk sizes and understand the
trade-offs.

------------------------------------------------------------------------

## PHASE 2 --- Retrieval

### Sprint 4 --- Embeddings

Goal:

``` text
Text
 ↓
Embedding model
 ↓
Vector
```

Learn:

-   embeddings
-   vector dimensions
-   similarity
-   cosine similarity
-   semantic search

Experiment with a small set of sentences and determine which are
semantically closest to a question.

Deliverable:

A small program that can find semantically similar sentences without
using an LLM.

------------------------------------------------------------------------

### Sprint 5 --- FAISS

Goal:

Understand vector indexing/search.

Pipeline:

``` text
chunks
 ↓
embeddings
 ↓
FAISS index
```

Query:

``` text
question
 ↓
question embedding
 ↓
FAISS
 ↓
top K chunks
```

Deliverable:

Example:

``` text
Question:
"What does the document say about exception handling?"

Retrieved:
1. Page 14 — chunk 32
2. Page 15 — chunk 35
3. Page 13 — chunk 29
```

Still no LLM.

------------------------------------------------------------------------

### Sprint 6 --- Retrieval Pipeline

Combine:

``` text
PDF
 ↓
Extract
 ↓
Clean
 ↓
Chunk
 ↓
Embed
 ↓
FAISS
```

Query:

``` text
Question
 ↓
Embed
 ↓
FAISS
 ↓
Top 3/5 chunks
```

This becomes the first real pipeline.

Test:

-   question where answer clearly exists
-   question where answer exists indirectly
-   question where answer doesn't exist
-   question requiring multiple pages

Focus on failure cases.

------------------------------------------------------------------------

## PHASE 3 --- RAG Application

### Sprint 7 --- Local LLM

Goal:

Understand what the LLM actually does.

Pipeline:

``` text
Retrieved context
       +
User question
       ↓
      Prompt
       ↓
     Ollama
       ↓
Generated answer
```

Experiment with different contexts and observe how the answer changes.

Deliverable:

``` text
question + retrieved chunks → answer
```

------------------------------------------------------------------------

### Sprint 8 --- Complete RAG

Combine retrieval and generation:

``` text
             PDF
              ↓
          ingestion
              ↓
            chunks
              ↓
          embeddings
              ↓
            FAISS
              ↑
              │
Question → embedding
              │
              ↓
       relevant chunks
              ↓
            prompt
              ↓
           Ollama
              ↓
            answer
```

MVP requirement:

Upload a PDF and ask a question.

Receive:

``` text
Answer:
...

Sources:
Page 12
Page 14
Page 19
```

This is the first complete RAG MVP.

------------------------------------------------------------------------

### Sprint 9 --- Streamlit

Create a usable local application.

Learn:

-   Streamlit
-   file upload
-   session state
-   chat UI
-   metadata/source display
-   error handling

Deliverable:

A local browser-based PDF Q&A application.

------------------------------------------------------------------------

## PHASE 4 --- Engineering Upgrade

### Sprint 10 --- Persistence + SQL

Problem:

``` text
Restart application
 ↓
everything disappears
```

Introduce SQL for structured persistent information.

Potential tables:

``` text
documents
chunks
chat_history
```

Keep vector search separate:

``` text
PostgreSQL
 ↓
metadata / structured data

FAISS / Vector DB
 ↓
vector similarity search
```

This is where SQL becomes meaningful rather than being added just for
the resume.

------------------------------------------------------------------------

### Sprint 11 --- Quality + Testing

Create a small evaluation dataset:

``` text
question
expected_answer
expected_pages
```

Test:

-   Did retrieval find the right page?
-   Did the LLM answer correctly?
-   Did it hallucinate?
-   Did it cite the correct source?

This introduces evaluation and quality thinking.

------------------------------------------------------------------------

### Sprint 12 --- Docker

Only after the system works.

Learn:

-   Dockerfile
-   image
-   container
-   environment variables
-   volumes
-   networking

Potential architecture:

``` text
┌──────────────┐
│ Streamlit    │
└──────┬───────┘
       │
┌──────▼───────┐
│ Python/RAG   │
└──────┬───────┘
       │
 ┌─────┴─────┐
 ▼           ▼
FAISS      Ollama
```

------------------------------------------------------------------------

# Learning Priorities

## Level 1 --- MUST understand

``` text
Python
Data structures
File processing
SQL
ETL concepts
Text processing
Embeddings
Vector search
RAG
```

## Level 2 --- Build with

``` text
PyMuPDF
Sentence Transformers
FAISS
Ollama
Streamlit
Git
```

## Level 3 --- Later

``` text
PostgreSQL
Docker
FastAPI
Vector databases
Cloud deployment
Airflow
```

------------------------------------------------------------------------

# Definition of Done

The final project should ideally include:

``` text
☐ PDF ingestion
☐ Text extraction
☐ Cleaning
☐ Chunking
☐ Metadata
☐ Embeddings
☐ Vector indexing
☐ Semantic retrieval
☐ Local LLM
☐ RAG
☐ Source/page references
☐ Streamlit UI
☐ SQL persistence
☐ Logging
☐ Error handling
☐ Tests
☐ Evaluation dataset
☐ Docker
☐ README
☐ Architecture diagram
☐ Git history
```

The goal is not merely:

> "It opens a PDF and answers questions."

The stronger portfolio outcome is:

> Built a local RAG-based document Q&A pipeline using Python, vector
> similarity search, embeddings, SQL persistence, and a locally hosted
> LLM.

The user should be able to explain the data flow, transformations,
storage choices, retrieval mechanism, failure points, and trade-offs.

------------------------------------------------------------------------

# Working Method / Mentorship Rules

For every feature:

``` text
1. Explain the problem
       ↓
2. User designs it
       ↓
3. Give hints
       ↓
4. User implements
       ↓
5. User shows code
       ↓
6. Review it
       ↓
7. Improve it
```

When stuck, use progressive hints:

``` text
Hint 1 → conceptual
Hint 2 → technical
Hint 3 → pseudo-code
Hint 4 → small code example
```

Only give the full solution when genuinely necessary.

The user wants to develop engineering ability rather than copy
solutions.

------------------------------------------------------------------------

# Consistency Strategy

The project should not depend on long motivational sessions.

Use small sessions:

``` text
Day 1
Understand concept

Day 2
Small experiment

Day 3
Build

Day 4
Debug/test

Day 5
Explain what was built
```

Even 20--30 minutes can count as a session.

The emphasis is:

> **Learn → Build → Break → Understand → Improve → Document**

Avoid planning a huge project and then abandoning it because the daily
workload became unrealistic.

------------------------------------------------------------------------

# Current Starting Point

The immediate task is:

## Sprint 1 --- Project Foundation

Create the project repository and a `README.md`.

Write answers to:

``` text
1. What problem am I solving?

2. Who would use this?

3. What happens to a PDF after upload?

4. Where does SQL fit?

5. Where does vector search fit?
```

Do not Google the answers initially.

Write the user's current understanding first.

Then review the README together.

The next step after the README review is **Sprint 1 / Task 1**, followed
by the first small implementation task.

------------------------------------------------------------------------

# Reference

The user found the initial project idea from:

The Product Space --- "Build Your Own PDF Chatbot with Python"

https://theproductspace.in/blogs/artificial-intelligence/build-your-own-pdf-chatbot-with-python

The reference article uses the general pattern:

``` text
PDF
 ↓
chunks
 ↓
embeddings
 ↓
FAISS
 ↓
retriever
 ↓
local LLM
 ↓
Streamlit
```

Use the article as a reference, not as a tutorial to blindly copy.
