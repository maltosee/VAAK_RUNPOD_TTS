FROM python:3.10-slim
WORKDIR /app

# Add cache buster to force fresh git pull
RUN echo "Cache bust: $(date)" > /tmp/cachebust

# Clone the repo
RUN git clone https://github.com/maltosee/vaak_runpod_tts.git .

# Install dependencies  
RUN pip install runpod requests

CMD ["python", "runpod_handler.py"]