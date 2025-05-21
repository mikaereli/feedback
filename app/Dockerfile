FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt from the root directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure python-multipart is installed
RUN pip install --no-cache-dir python-multipart>=0.0.6

COPY . /app

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
