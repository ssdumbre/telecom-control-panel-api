FROM python:3.11-slim
LABEL maintainer="Sarang"
WORKDIR /app
# Copy and install dependencies
COPY requirements.txt /app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    --default-timeout=100 \
    --retries 10 \
    -r requirements.txt
# Copy application code
COPY . /app 
# Install kubectl (required for your FastAPI app)
RUN apt-get update && apt-get install -y curl && \
    curl -LO https://dl.k8s.io/release/v1.29.0/bin/linux/amd64/kubectl && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/ && \
    apt-get clean
EXPOSE 8000
CMD ["uvicorn", "getamfpod:app", "--host", "0.0.0.0", "--port", "8000"]