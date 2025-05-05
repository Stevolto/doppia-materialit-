# Double Materiality Measurement App

Questo repository contiene l'applicazione Python per misurare la doppia materialità in quattro fasi.

## Setup
```bash
git clone https://github.com/Stevolto/double-materiality-complete-app.git
cd double-materiality-complete-app
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Run locally
```bash
flask run --host=0.0.0.0 --port=5000
```

## Testing
```bash
pytest -q
```

## Deployment
Build: `pip install -r requirements.txt`
Start: `gunicorn app:app`
