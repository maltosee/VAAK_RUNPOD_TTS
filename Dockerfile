FROM python:3.10-slim
WORKDIR /app
RUN pip install runpod requests

# Version-specific cache buster
RUN echo "Build version: v5" > /tmp/buildversion

# Download handler with version-specific timestamp
RUN wget -O runpod_handler.py "https://raw.githubusercontent.com/maltosee/vaak_runpod_tts/main/runpod_handler.py"

# Force refresh by reading file
RUN head -5 runpod_handler.py

CMD ["python", "runpod_handler.py"]