import runpod
import requests
import time

def handler(event):
    try:
        input_data = event.get("input", {})
        text = input_data.get("text", "Hello")
        
        print(f"🚀 Handler called - downloading real WAV file")
        
        # Download real WAV file
        wav_url = "https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav"
        response = requests.get(wav_url, timeout=10)
        
        if response.status_code != 200:
            yield "ERROR: Could not download WAV"
            return
            
        wav_data = response.content
        print(f"✅ Downloaded {len(wav_data)} bytes of real audio")
        
        # Split into 6 equal chunks
        chunk_size = len(wav_data) // 6
        
        for i in range(6):
            start_idx = i * chunk_size
            end_idx = start_idx + chunk_size if i < 5 else len(wav_data)
            
            chunk = wav_data[start_idx:end_idx]
            hex_chunk = chunk.hex()
            
            print(f"📤 Chunk {i+1}: {len(chunk)} bytes -> {len(hex_chunk)} hex chars")
            
            # Yield pure hex string - no JSON
            yield hex_chunk
            
            time.sleep(0.2)  # Small delay between chunks
            
    except Exception as e:
        print(f"❌ Error: {e}")
        yield "ERROR"

runpod.serverless.start({"handler": handler})