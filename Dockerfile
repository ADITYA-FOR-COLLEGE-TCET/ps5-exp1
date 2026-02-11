FROM python:3.9-slim

WORKDIR /app

# Copy requirements first (for caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application (including templates folder)
COPY . .

# Expose ports: 5000 (Web UI), 8000 (Metrics)
EXPOSE 5000 8000

CMD ["python", "app.py"]