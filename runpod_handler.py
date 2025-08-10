import runpod
import requests
import time

# Add version identifier at top
HANDLER_VERSION = "v2.0-SIMPLE-TEST"
print(f"🚨 HANDLER VERSION: {HANDLER_VERSION}")
print(f"🚨 Handler file loaded at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

def handler(event):
    print(f"🚨 HANDLER CALLED - VERSION: {HANDLER_VERSION}")
    print(f"🚨 Event received: {event}")
    
    try:
        print("🚨 About to yield START")
        yield "START:test"
        
        print("🚨 About to yield hex data")
        yield "52494646FF00"
        
        print("🚨 About to yield END")
        yield "END:1"
        
        print("🚨 All yields completed successfully")
        
    except Exception as e:
        print(f"🚨 ERROR in handler: {e}")
        yield f"ERROR:{e}"

if __name__ == "__main__":
    print(f"🚨 Starting RunPod with handler version: {HANDLER_VERSION}")
    runpod.serverless.start({"handler": handler})