import runpod
import requests
import time

HANDLER_VERSION = "v4.0-CHUNKED-WAV-TEST"
print(f"🚨 HANDLER VERSION: {HANDLER_VERSION}")

def handler(event):
    print(f"🚨 HANDLER VERSION {HANDLER_VERSION} CALLED")
    
    try:
        yield "START:test"
        
        print("🚨 Downloading WAV file...")
        response = requests.get("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba-online-audio-converter.com_-1.wav")
        wav_data = response.content
        print(f"🚨 Downloaded {len(wav_data)} bytes")
        
        # Split into smaller chunks (1MB each)
        chunk_size = 1024 * 1024  # 1MB
        total_chunks = (len(wav_data) + chunk_size - 1) // chunk_size
        
        for i in range(total_chunks):
            start = i * chunk_size
            end = min(start + chunk_size, len(wav_data))
            chunk = wav_data[start:end]
            print(f"🚨 Yielding chunk {i+1}/{total_chunks}: {len(chunk)} bytes")
            yield chunk.hex()
        
        yield "END:1"
        print("🚨 All yields completed")
        
    except Exception as e:
        print(f"🚨 ERROR: {e}")
        yield f"ERROR:{e}"

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})