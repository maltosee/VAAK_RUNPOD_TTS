import runpod
import requests
import time

HANDLER_VERSION = "v3.0-REAL-WAV-TEST"
print(f"🚨 HANDLER VERSION: {HANDLER_VERSION}")

def handler(event):
    print(f"🚨 HANDLER VERSION {HANDLER_VERSION} CALLED")
    
    try:
        yield "START:test"
        
        # Download real WAV file
        print("🚨 Downloading WAV file...")
        response = requests.get("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba-online-audio-converter.com_-1.wav")

        wav_data = response.content
        print(f"🚨 Downloaded {len(wav_data)} bytes")
        
        # Stream entire WAV as hex
        yield wav_data.hex()
        
        yield "END:1"
        print("🚨 All yields completed")
        
    except Exception as e:
        print(f"🚨 ERROR: {e}")
        yield f"ERROR:{e}"

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})