# PDF Q&A System

## What problem does this solve?

Reading and searching through large documents such as PDFs, Word documents, CSVs, Markdown files, or HTML files can take a lot of time.

This project aims to make that process faster by allowing users to upload a document and ask questions about its content. Instead of manually searching through the entire document, the system retrieves the relevant information and provides an answer.

For the first version, we will focus on **PDF documents**. Other document types can be added later.

---

## Who will use this?

Initially, I will build and use this system myself.

Once the system is working correctly and the architecture is stable, I plan to deploy it so that other users can also use it.

---

## What happens when a PDF is uploaded?

The basic flow will be:

1. The user uploads a PDF through the UI.
2. The system extracts the content from the PDF.
3. The extracted content is cleaned and validated.
4. The content is divided into smaller chunks.
5. The chunks are converted into embeddings.
6. Document metadata and other application information are stored in an SQL database.
7. The embeddings and searchable document content are stored in a vector database.
8. When the user asks a question, the API receives the request.
9. The system searches the vector database for relevant content.
10. The retrieved content is sent to an LLM.
11. The LLM generates an answer based on the retrieved document content.
12. The answer is returned to the UI.

The system should eventually support both:

* **Local LLMs** — for privacy and running without a cloud AI provider.
* **Cloud LLMs** — for easier deployment and access to more powerful models.

---

## Why ETL?

We don't want to read and process the entire PDF every time a user asks a question.

Instead, we process the document once and prepare the data for future queries.

**ETL gives us a structured pipeline:**

**Extract → Transform → Load**

* **Extract:** Get content from the document.
* **Transform:** Clean, validate, and chunk the content.
* **Load:** Store the processed data in SQL and the vector database.

This makes the system more efficient because the document has already been processed before the user starts asking questions.

---

## Why SQL?

SQL will store the **structured information and metadata** related to the application.

For example:

* Document details
* Document name
* Document type
* Upload information
* Processing status
* User details
* Document relationships
* Chunk/embedding references
* Processing errors
* Timestamps

SQL will act as the structured source of information about the documents and the application.

---

## Why a Vector Store?

SQL is good at storing structured data, but it is not designed for semantic similarity searches.

The vector store will contain the document chunks and their **embeddings**.

When a user asks a question, the system converts the question into an embedding and searches for document chunks that are semantically similar to the question.

For example:

> **PDF:** AWS Data Engineering documentation
> **Question:** "What is the purpose of AWS Glue?"

The vector store can retrieve the relevant sections of the document even when the exact words in the question don't appear in the document.

So:

**SQL → structured information and metadata**

**Vector Store → searchable document content and embeddings**

---

## Why an API?

The API will act as the communication layer between the UI and the backend services.

Instead of connecting the Streamlit UI directly to databases and other components, the UI will communicate with the backend through APIs.

For example:

**Streamlit → API → Processing / Database / Vector Store / LLM**

The API can handle operations such as:

* Uploading documents
* Starting document processing
* Checking processing status
* Asking questions
* Retrieving answers
* Managing documents
* Managing users

This also makes it easier to replace Streamlit with another frontend in the future.

---

## Why an LLM?

The LLM is responsible for generating a natural-language answer from the relevant information retrieved from the document.

The LLM itself should not be responsible for searching the entire document.

Instead, the system will first retrieve relevant document chunks and then provide those chunks to the LLM.

The basic flow is:

**User Question → Retrieve Relevant Chunks → LLM → Answer**

This approach is the foundation of **Retrieval-Augmented Generation (RAG)**.

---

## Why Streamlit?

Streamlit will provide the initial user interface for the project.

The UI will allow users to:

* Upload documents
* Start document processing
* View processing status
* Chat with their documents
* Ask questions
* View answers and sources
* Manage uploaded documents

In the future, it can also include:

* User authentication
* User details
* Chat history
* Document history
* Multiple document conversations
* Settings for choosing a local or cloud LLM

For the first version, Streamlit keeps the UI simple so that the main focus can remain on the **Data Engineering pipeline and backend architecture**.
