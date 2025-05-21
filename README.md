# Feedback Python FastAPI

## Installation

### Docker environment
```bash
docker compose build --no-cache
```

```bash
docker compose up
```


### Own environment
```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn app.main:app --reload
```

## Swagger

http://localhost:8000/docs