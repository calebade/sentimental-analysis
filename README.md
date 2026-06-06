# Automated Natural Language Processing (NLP) Sentiment Ingestion Pipeline

An enterprise-ready, modular ELT (Extract, Load, Transform) data pipeline designed to ingest unstructured customer review payloads, execute programmatic text cleaning, and load structured analytical outputs into a centralized target database warehouse.

---

## 🏗️ Data Architecture & Lineage

[ Raw TSV Ingestion ]   ──►  [ Modular Python ETL ] ──► [ Local db ] 
(data/Restaurant_Reviews)    (Regex/Text Cleaning)      (sqlite/PostgreSQL Db)

Unlike Jupyter Notebook approaches that load and manipulate data statically in-memory, this production-grade architecture decouples every phase of data processing into dedicated, decoupled Python modules with strict error boundary handling and operational logging.

---

## 🛠️ Tech Stack & Dependencies

* **Core Language:** Python 3.x (Object-Oriented, Modular Production Code)
* **Data Processing & Manipulation:** Pandas, NumPy
* **Text Analysis Engine:** NLTK / Regular Expressions (Regex)
* **Database Target Engine:** SQLAlchemy ORM, SQLite / PostgreSQL

---

## 🚀 Execution & Operational Setup

### 1. Installation & Environment Setup
Clone the repository infrastructure and install the necessary package dependencies inside a clean virtual environment:
```bash
git clone https://github.com/calebade/sentimental-analysis
cd sentimental-analysis
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Running the Data Pipeline
Execute the centralized orchestration script to trigger data extraction, cleaning transformations, and warehouse database loading steps sequentially:
```bash
python main.py
```

---

## 📈 Engineering Design Choices

* **Decoupled Architecture:** Extracted operations are completely independent of storage rules, ensuring the target database engine can be swapped seamlessly from SQLite to an enterprise warehouse like Google BigQuery without rewriting the core business logic.
* **Audit Lineage Tracks:** Every ingestion cycle programmatically generates an immutable `batch_id` and a UTC timestamp `processed_at` column, ensuring full structural accountability and simple debugging for downstream analytics teams.
* **Production Error Boundaries:** Implemented comprehensive `try/except` logging structures to catch operational file blocks, missing data schemas, or database connectivity drops without silently failing.
