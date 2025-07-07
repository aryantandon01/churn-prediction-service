# Use official lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (FastAPI default)
EXPOSE 8000

# Run API on container start
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
