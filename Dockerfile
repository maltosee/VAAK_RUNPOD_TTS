FROM python:3.10-slim
WORKDIR /app
# Install git and other essentials
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
RUN pip install runpod requests
RUN wget -O runpod_handler.py https://raw.githubusercontent.com/maltosee/vaak_runpod_tts/main/runpod_handler.py
CMD ["python", "runpod_handler.py"]