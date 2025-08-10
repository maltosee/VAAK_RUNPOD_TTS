import runpod
import requests
import time

def handler(event):
    try:
        yield "START:test"
        yield "52494646FF00"  # Simple test hex
        yield "END:1"
    except Exception as e:
        yield f"ERROR:{e}"

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})