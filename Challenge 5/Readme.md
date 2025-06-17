
# Alaska Snow Department AI Agent

This project implements a secure, production-ready Generative AI agent for the Alaska Department of Snow. It uses RAG (Retrieval-Augmented Generation) and integrates safety filtering and backend API functionality. It is built with Python and Streamlit and deployed on GCP.

## Project URL:
```bash
https://streamlit-app-716529206847.us-central1.run.app/
```

## Folder Structure

```
.
├── app/
│   ├── backend.py          # Backend logic to handle responses
│   ├── filters.py          # Safety filter functions
│   └── __init__.py
├── config/
│   └── settings.py         # Configuration parameters and environment variables
├── ui/
│   └── main.py             # Streamlit UI for chatbot interface
├── evaluation/
│   └── evaluator.py        # Evaluation using Google Eval API (e.g., BLEU, fluency)
├── tests/
│   ├── test_backend_agent.py  # Unit tests for backend
│   └── test_filters.py        # Unit tests for prompt filtering
├── requirements.txt        # Python dependencies
├── DockerFile              # Docker configuration for GCP deployment
```

## Features

- Prompt filtering with LLM safety check (`app/filters.py`)
- Backend RAG response generation (`app/backend.py`)
- Evaluation metrics integration (`evaluation/evaluator.py`)
- Unit tests for all core logic (`tests/`)
- Streamlit web UI (`ui/main.py`)
- Docker-ready deployment setup

## Running Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Start Streamlit app
streamlit run ui/main.py
```

## Deployment on GCP Cloud Run

Build and push your image:
```bash
gcloud builds submit --tag gcr.io/[PROJECT-ID]/streamlit-app
```

Deploy to Cloud Run:
```bash
gcloud run deploy streamlit-app --image gcr.io/[PROJECT-ID]/streamlit-app --platform managed
```

## Evaluation

Uses Google Evaluation API to benchmark:
- Fluency
- Relevance
- BLEU and other text metrics

## Safety & Security

- Local and LLM-based prompt filtering
- Validations before sending prompts to models
- Response block if flagged for safety

## Data Source

This project uses backend data and documents from:
```
gs://labs.roitraining.com/alaska-dept-of-snow
```
and the DataStore is created using Big Query from rag_bigquery_datastore_notebook/RAG_BigQuery_Datastore.ipynb

## Testing

```bash
python -m unittest discover -s tests -p "test_*.py"
```

I have added the evaluation metrics for 2 cases in the **outputs** folder.

## Authors

Developed by: Varun Venkatasubramanian

## Note

1. For local testing service account json is used for GCP authentcation.
2. Line from backend.py is commented during the gcloud run deployment.
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "alaska_admin_key.json")
```
---

