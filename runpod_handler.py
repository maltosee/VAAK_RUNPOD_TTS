import runpod
import requests
import time

HANDLER_VERSION = "v5.0-TINY-CHUNKS-TEST"
print(f"🚨 HANDLER VERSION: {HANDLER_VERSION}")

def handler(event):
    print(f"🚨 HANDLER VERSION {HANDLER_VERSION} CALLED")
    print(f"🚨 Event received: {event}")
    
    try:
        print("🚨 About to yield START")
        yield "START:test"
        
        print("🚨 Downloading WAV file...")
        response = requests.get("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba-online-audio-converter.com_-1.wav")
        wav_data = response.content
        print(f"🚨 Downloaded {len(wav_data)} bytes")
        
        # Use tiny chunks - 64KB each (→ 128KB hex)
        chunk_size = 64 * 1024  # 64KB
        total_chunks = (len(wav_data) + chunk_size - 1) // chunk_size
        
        for i in range(total_chunks):
            start = i * chunk_size
            end = min(start + chunk_size, len(wav_data))
            chunk = wav_data[start:end]
            print(f"🚨 Yielding chunk {i+1}/{total_chunks}: {len(chunk)} bytes")
            yield chunk.hex()
        
        print("🚨 About to yield END")
        yield "END:1"
        
        print("🚨 All yields completed successfully")
        
    except Exception as e:
        print(f"🚨 ERROR in handler: {e}")
        yield f"ERROR:{e}"

if __name__ == "__main__":
    print(f"🚨 Starting RunPod with handler version: {HANDLER_VERSION}")
    runpod.serverless.start({"handler": handler})