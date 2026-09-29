Absolutely. I’d make this the **master project plan** you can paste into a new ChatGPT Project and use as the source of truth for our work.

# PDF Q&A — Data Engineering Project

## 1. Project Mission

Build a **production-style local PDF Q&A system** while using the project to strengthen Data Engineering skills.

This is **not primarily an AI chatbot project**.

The learning priority is:

```text
Python
   ↓
ETL
   ↓
SQL
   ↓
Database ETL
   ↓
API
   ↓
Testing + Logging
   ↓
Docker
   ↓
AWS
   ↓
RAG / AI
```

The final system should demonstrate that I can design, build, test, and explain a complete data pipeline.

---

# 2. Current Starting Point

### Already completed

* 30-day Python/ETL challenge
* Expense ETL pipeline
* Python fundamentals
* SQL fundamentals

### Current project phase

**Day 1 — Project Foundation**

### Current ability

I know Python and SQL basics, but I am still developing engineering depth.

Therefore:

* Don't assume advanced Python.
* Don't jump immediately into frameworks.
* Don't give me huge amounts of code.
* Make me understand each layer before moving on.

---

# 3. Final Architecture

This is the master architecture for the project:

```text
                         PDF Q&A SYSTEM
                              │
                              ▼
                         ┌─────────┐
                         │  PDFs   │
                         └────┬────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ PDF Extraction  │
                     │   + ETL         │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Clean / Chunk   │
                     │ / Validate      │
                     └────────┬────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
               SQL Database        Vector Store
               Metadata            Embeddings
                    │                   │
                    └─────────┬─────────┘
                              ▼
                         Query / API
                              │
                              ▼
                       Retrieval (RAG)
                              │
                              ▼
                         AI / LLM
                              │
                              ▼
                       Answer + Sources
                              │
                              ▼
                         Streamlit UI
```

---

# 4. Two Main Pipelines

The system should eventually contain two distinct pipelines.

## A. Ingestion Pipeline

```text
PDF
 ↓
Extract
 ↓
Clean
 ↓
Transform
 ↓
Chunk
 ↓
Validate
 ├──────────────→ SQL metadata
 │
 └──────────────→ Embeddings
                       ↓
                  Vector Store
```

## B. Query Pipeline

```text
User Question
 ↓
Query/API
 ↓
Question Embedding
 ↓
Vector Search
 ↓
Relevant Chunks
 ↓
RAG Context
 ↓
LLM
 ↓
Answer + Sources
```

This distinction is important.

**Ingestion prepares the data.**

**Query retrieves and uses the data.**

---

# 5. Technology Strategy

## Start simple

Initial technologies:

```text
Python
PyMuPDF / pypdf
SQLite
Sentence Transformers
FAISS
Ollama
Streamlit
Git
```

Later:

```text
PostgreSQL
FastAPI
pytest
Docker
AWS
Vector DB
```

Potential vector databases to investigate later:

```text
pgvector
Qdrant
Chroma
Milvus
```

We will **not** use all of them.

The purpose is to understand the trade-offs.

---

# 6. Engineering Principle

## Don't add technology without a problem.

For example:

Don't say:

> "I need PostgreSQL because real projects use PostgreSQL."

Instead:

> "I need persistent structured metadata, so I need a relational database."

Don't say:

> "I need FAISS because RAG tutorials use FAISS."

Instead:

> "I need semantic similarity search over embeddings."

Don't say:

> "I need FastAPI because backend developers use FastAPI."

Instead:

> "I need an API layer so the UI is separated from the processing/query service."

This mindset is one of the major goals of the project.

---

# 7. Sprint Roadmap

## PHASE 1 — Foundation

### Sprint 1 — Project Setup

### Goal

Understand the project and create its foundation.

### Learn

* Git
* GitHub
* virtual environments
* project structure
* requirements
* `.gitignore`
* README
* configuration
* basic logging

### Build

Initial structure:

```text
pdf-qa-system/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── database/
│   ├── embeddings/
│   ├── retrieval/
│   └── llm/
│
├── tests/
│
└── app/
```

### Deliverable

Project repository runs successfully.

### Questions I should be able to answer

1. Why do we have `raw` and `processed`?
2. Why separate `src` and `tests`?
3. Why shouldn't everything be inside `app.py`?
4. What is configuration?
5. Why should secrets not be committed?

---

# PHASE 2 — PDF Data Engineering

## Sprint 2 — PDF Ingestion

### Goal

Build:

```text
PDF
 ↓
Python
 ↓
Page-level text
```

### Learn

* `pathlib`
* file handling
* PDF extraction
* page handling
* metadata
* exceptions

### Deliverable

Given a PDF:

```text
document.pdf
```

produce structured information such as:

```text
document
page
text
```

### Important questions

* What if the PDF doesn't exist?
* What if the PDF is empty?
* What if a page has no text?
* What if extraction fails?
* How do we identify the document?

---

# Sprint 3 — ETL Pipeline

Now turn extraction into a real ETL process.

```text
Extract
   ↓
Transform
   ↓
Load
```

### Extract

PDF → raw text

### Transform

Clean:

* whitespace
* empty text
* unwanted characters
* malformed data

### Load

Initially store processed output locally.

Later we'll load it into SQL.

### Learn

* ETL
* transformations
* data validation
* pipeline stages
* idempotency concepts
* error handling

### Deliverable

A repeatable PDF processing pipeline.

---

# Sprint 4 — Chunking

Now solve the problem:

> A document can contain thousands of words. How do we divide it into useful searchable pieces?

Pipeline:

```text
Pages
 ↓
Clean text
 ↓
Chunks
```

Each chunk should retain metadata.

Conceptually:

```text
{
    document_id,
    page_number,
    chunk_id,
    text
}
```

### Learn

* chunk size
* chunk overlap
* metadata
* boundaries
* trade-offs

### Experiment

Compare:

```text
small chunks
medium chunks
large chunks
```

and observe retrieval quality later.

---

# PHASE 3 — SQL / Database ETL

## Sprint 5 — Database Design

Now introduce SQL properly.

Start with **SQLite**.

Potential schema:

### documents

```text
documents
----------------
id
filename
file_hash
file_size
uploaded_at
status
```

### chunks

```text
chunks
----------------
id
document_id
page_number
chunk_number
text
created_at
```

Later:

### chat_history

```text
chat_history
----------------
id
question
answer
created_at
```

### Learn

* primary keys
* foreign keys
* relationships
* normalization
* indexes
* constraints
* CRUD
* transactions

---

# Sprint 6 — Database ETL

Build:

```text
PDF
 ↓
Extract
 ↓
Clean
 ↓
Chunk
 ↓
Validate
 ↓
Load → SQL
```

Now the project becomes a genuine ETL pipeline.

### Important engineering problem

What happens if:

```text
same PDF uploaded twice?
```

We should eventually detect duplicates using something like:

```text
file hash
```

This introduces:

* idempotency
* data quality
* duplicate handling

### Deliverable

PDF metadata and chunks persist in SQL.

---

# PHASE 4 — Vector Data

## Sprint 7 — Embeddings

Now introduce embeddings.

```text
Chunk
 ↓
Embedding Model
 ↓
Vector
```

Learn:

* embeddings
* vector dimensions
* semantic similarity
* cosine similarity

Start with small experiments before connecting it to the whole system.

### Experiment

Given:

```text
Python is a programming language.

Python supports exception handling.

Dogs are animals.

Cats are animals.
```

Ask:

```text
What is Python?
```

Find which sentences are semantically closest.

### Deliverable

Understand and generate embeddings.

---

# Sprint 8 — Vector Store / FAISS

Now:

```text
Chunks
 ↓
Embeddings
 ↓
FAISS
```

Query:

```text
Question
 ↓
Question embedding
 ↓
FAISS
 ↓
Top-K chunks
```

### Learn

* vector index
* similarity search
* distance
* top-K
* retrieval

### Deliverable

The system can retrieve relevant chunks **without using an LLM**.

This is an important checkpoint.

---

# PHASE 5 — Query / API

## Sprint 9 — Query Service

Create the query logic:

```text
Question
 ↓
Embedding
 ↓
Vector Search
 ↓
Relevant Chunks
```

At this point the system can answer:

> "Which parts of the document are relevant to my question?"

but not necessarily generate a polished answer.

### Deliverable

A reusable retrieval function/service.

---

# Sprint 10 — API Layer

Introduce FastAPI only when the query service is understood.

Architecture:

```text
Streamlit
    ↓
FastAPI
    ↓
Query Service
    ↓
Vector Store
    ↓
SQL
```

Potential endpoints:

```text
POST /documents
GET  /documents
POST /query
GET  /health
```

Don't build 20 endpoints.

Start with the minimum needed.

### Learn

* HTTP
* REST
* endpoints
* request/response
* JSON
* status codes
* validation

---

# PHASE 6 — RAG / AI

## Sprint 11 — Local LLM

Introduce Ollama.

Understand:

```text
Context
 +
Question
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

Learn:

* local models
* prompts
* context
* temperature
* token/context limits
* hallucination

---

# Sprint 12 — Complete RAG

Combine everything:

```text
Question
 ↓
API
 ↓
Embedding
 ↓
Vector Search
 ↓
Top-K Chunks
 ↓
Context
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

Answer should include sources:

```text
Answer:
...

Sources:
- Page 12
- Page 14
```

### Critical behavior

If the document doesn't contain enough information:

```text
"I couldn't find enough information in the provided document."
```

rather than inventing an answer.

---

# PHASE 7 — Streamlit

## Sprint 13 — UI

Build the interface last.

Features:

```text
Upload PDF
      ↓
Processing status
      ↓
Ask question
      ↓
Answer
      ↓
Sources
```

Potential UI:

```text
┌──────────────────────────────┐
│       PDF Q&A System         │
├──────────────────────────────┤
│ Upload PDF                   │
│ [ Choose file ]              │
│                              │
│ Ask a question               │
│ [________________________]   │
│                              │
│ Answer                       │
│                              │
│ Sources                      │
│ Page 12 | Page 14            │
└──────────────────────────────┘
```

---

# PHASE 8 — Engineering Quality

## Sprint 14 — Testing

Introduce `pytest`.

Test:

### Unit tests

```text
PDF extraction
chunking
cleaning
validation
database functions
retrieval
```

### Integration tests

```text
PDF
 ↓
ETL
 ↓
SQL
 ↓
Embedding
 ↓
Vector search
```

### Learn

* unit tests
* integration tests
* fixtures
* mocking
* edge cases

---

# Sprint 15 — Logging + Error Handling

Replace random `print()` statements with useful logging.

Example levels:

```text
INFO
WARNING
ERROR
```

Log things such as:

```text
PDF received
Extraction started
Pages extracted
Chunks created
Database load completed
Embedding generation started
Retrieval completed
LLM request completed
```

But don't log sensitive information.

---

# Sprint 16 — Data Quality / Evaluation

Create an evaluation dataset.

Example:

```text
question
expected_page
expected_concept
expected_answer
```

Test:

```text
Did retrieval find the correct content?

Did the LLM answer using the content?

Did it hallucinate?

Were sources correct?
```

This is an important step toward production thinking.

---

# PHASE 9 — Docker

## Sprint 17 — Containerization

Learn:

* Dockerfile
* image
* container
* environment variables
* volumes
* networking

Eventually:

```text
Docker
 ├── Streamlit
 ├── API
 ├── Database
 └── supporting services
```

Ollama/model handling may need a separate approach depending on the local setup.

---

# PHASE 10 — AWS

## Sprint 18 — Cloud Architecture

Only after the local architecture works.

Learn the AWS equivalents gradually.

Potential components:

```text
S3
 ↓
PDF storage

RDS
 ↓
SQL metadata

EC2 / ECS
 ↓
Application

CloudWatch
 ↓
Logs
```

Vector storage can be evaluated separately depending on the final architecture.

Don't try to put the whole project on AWS immediately.

---

# PHASE 11 — Final Portfolio Version

## Sprint 19 — Architecture Cleanup

Review:

```text
Code
Database
ETL
API
Vector search
RAG
UI
Testing
Logging
Docker
AWS
```

Remove unnecessary complexity.

---

## Sprint 20 — Documentation

README should contain:

### 1. Problem

What does the application solve?

### 2. Architecture

```text
PDF
 ↓
ETL
 ↓
SQL + Vector Store
 ↓
API
 ↓
RAG
 ↓
LLM
 ↓
Streamlit
```

### 3. Technology choices

Explain **why** each technology was selected.

### 4. Data flow

Explain ingestion and query pipelines.

### 5. Database schema

Include ER diagram.

### 6. API

Document endpoints.

### 7. Setup

Explain how to run locally.

### 8. Testing

Explain test strategy.

### 9. Limitations

Be honest about limitations.

### 10. Future improvements

Examples:

```text
authentication
multi-user support
better vector DB
cloud deployment
monitoring
document versioning
```

---

# 8. Final Definition of Done

The finished system should ideally have:

```text
PROJECT
☐ Git repository
☐ Clean project structure
☐ README
☐ Configuration management

DATA ENGINEERING
☐ PDF ingestion
☐ ETL pipeline
☐ Cleaning
☐ Chunking
☐ Validation
☐ Duplicate detection
☐ Data quality checks

DATABASE
☐ SQL schema
☐ Documents table
☐ Chunks table
☐ Chat history
☐ Relationships
☐ Indexes
☐ Database ETL

VECTOR
☐ Embeddings
☐ Vector index
☐ Similarity search
☐ Top-K retrieval

API
☐ FastAPI
☐ Upload endpoint
☐ Query endpoint
☐ Health endpoint
☐ Request validation

AI
☐ Local LLM
☐ Prompt construction
☐ RAG
☐ Hallucination handling
☐ Source references

UI
☐ Streamlit
☐ PDF upload
☐ Question input
☐ Answer display
☐ Source display

QUALITY
☐ Unit tests
☐ Integration tests
☐ Logging
☐ Error handling
☐ Evaluation dataset

DEPLOYMENT
☐ Docker
☐ Environment variables
☐ AWS architecture
☐ Cloud deployment

PORTFOLIO
☐ Architecture diagram
☐ README
☐ Screenshots
☐ Demo
☐ Technical explanation
☐ Design decisions
```

---

# 9. How We Will Work Together

This is **very important**.

You don't want me to build the project for you.

Our workflow:

```text
             YOU
              │
              ▼
       Try to understand
              │
              ▼
        Design yourself
              │
              ▼
          Write code
              │
              ▼
        Show me code
              │
              ▼
      ┌───────────────┐
      │ Mentor Review │
      └───────┬───────┘
              │
       ┌──────┴──────┐
       ▼             ▼
    Correct       Improve
       │             │
       └──────┬──────┘
              ▼
          Next task
```

When you're stuck:

### Hint 1

Conceptual hint.

### Hint 2

Technical direction.

### Hint 3

Pseudo-code.

### Hint 4

Small implementation example.

### Full solution

Only when genuinely necessary.

---

# 10. Rules for Me as Your Mentor

When working on this project, I should:

* Be direct and honest.
* Explain complicated concepts simply.
* Assume Python/SQL fundamentals, not advanced expertise.
* Give hints before solutions.
* Avoid unnecessary frameworks.
* Explain **why** before **how**.
* Make you write the implementation.
* Review your code rather than replacing it.
* Point out bad engineering practices.
* Make you think about failure cases.
* Introduce technologies only when they solve an actual problem.
* Connect concepts back to Data Engineering.
* Keep the project practical.
* Prevent scope creep.
* Break large work into small tasks.

I should **not**:

* Dump huge code blocks.
* Build the whole project for you.
* Introduce Kafka/Airflow/Kubernetes/etc. just for the resume.
* Tell you to copy a tutorial.
* Assume that "working" means "understood."
* Over-engineer the first version.

---

# 11. Habit Rule

The minimum commitment is:

> **15 minutes.**

Not:

> "I must study for 2 hours every day."

If you have more time, great.

If you only have 15 minutes:

```text
15 minutes → one concept
15 minutes → one experiment
15 minutes → one small implementation
```

The rule is:

> **Miss → return → continue.**

A missed day does **not** reset the project.

No guilt-driven restart.

---

# 12. Definition of Progress

Progress is not measured only by:

```text
☑ Feature completed
```

It is also measured by whether I can explain:

```text
Why?
What?
How?
What can fail?
Why this technology?
What alternative exists?
What trade-off did we make?
```

For example, I should eventually be able to explain:

> Why do we need both SQL and a vector store?

> Why are chunks needed?

> Why can't we simply search the PDF using SQL `LIKE`?

> Why do we embed the question?

> Why does retrieval happen before the LLM?

> What happens when retrieval returns bad chunks?

> What happens when the document doesn't contain the answer?

> Why use FAISS initially?

> When would PostgreSQL + pgvector make more sense?

> Why put an API between the UI and backend?

Those are the kinds of questions that turn this from a tutorial project into engineering experience.

---

# 13. Current Status

```text
PHASE 1 — Foundation

Sprint 1 — Project Setup
Status: 🟡 CURRENT

Sprint 2 — PDF Ingestion
Status: ⬜

Sprint 3 — ETL
Status: ⬜

Sprint 4 — Chunking
Status: ⬜

Sprint 5 — Database Design
Status: ⬜

Sprint 6 — Database ETL
Status: ⬜

Sprint 7 — Embeddings
Status: ⬜

Sprint 8 — FAISS
Status: ⬜

Sprint 9 — Query Service
Status: ⬜

Sprint 10 — API
Status: ⬜

Sprint 11 — Local LLM
Status: ⬜

Sprint 12 — RAG
Status: ⬜

Sprint 13 — Streamlit
Status: ⬜

Sprint 14 — Testing
Status: ⬜

Sprint 15 — Logging
Status: ⬜

Sprint 16 — Evaluation
Status: ⬜

Sprint 17 — Docker
Status: ⬜

Sprint 18 — AWS
Status: ⬜

Sprint 19 — Architecture Cleanup
Status: ⬜

Sprint 20 — Portfolio Documentation
Status: ⬜
```

---

# 14. Our Immediate Next Step

**Do not start Sprint 2 yet.**

We're at:

> ## Sprint 1 — Project Foundation

### Task 1

Create the project repository.

Then create:

```text
README.md
```

Write your current understanding of:

```text
1. What problem are we solving?

2. Who is going to use this?

3. What happens when a PDF is uploaded?

4. Why do we need ETL?

5. Why do we need SQL?

6. Why do we need a vector store?

7. Why do we need an API?

8. Why do we need an LLM?

9. Why do we need Streamlit?
```

**Don't look for perfect answers.**

Write what you currently believe.

Then bring it here.

I'll review it, challenge your assumptions, and give you **Task 2**.

That way this project grows **from your understanding**, rather than becoming another tutorial you completed but can't explain.
