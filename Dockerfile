# Dockerfile
#
# Builds a lightweight image to run the FastAPI application.

FROM python:3.12-slim

# Prevents Python from writing .pyc files and buffers output (better logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY app ./app

EXPOSE 8000

# Start the API with auto-reload (handy for development)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
