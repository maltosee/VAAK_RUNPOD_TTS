FROM python:3.10-slim
WORKDIR /app

# Install git and other essentials
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Add cache buster to force fresh git pull
RUN echo "Cache bust: $(date)" > /tmp/cachebust

# Clone the repo
RUN git clone https://github.com/maltosee/vaak_runpod_tts.git .

# Install dependencies  
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for the TTS model
ENV PYTHONPATH=/app
ENV TORCH_HOME=/app/models
ENV HF_HOME=/app/models
ENV TRANSFORMERS_CACHE=/app/models

# Create models directory
RUN mkdir -p /app/models

CMD ["python3","-u", "runpod_handler.py"]