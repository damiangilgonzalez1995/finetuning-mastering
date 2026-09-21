import requests
import base64
import ollama
import sys
import time
from io import BytesIO
from PIL import Image

# 1. Configuration
IMAGE_URL = "https://marketplace.canva.com/EAE92Pl9bfg/6/0/1131w/canva-black-and-gray-minimal-freelancer-invoice-wPpAXSlmfF4.jpg"
MODEL_NAME = "glm-ocr-optimized"
MAX_DIMENSION = 1024

def get_optimized_image_b64(url):
    print(f"📥 Downloading image...")
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    original_width, original_height = img.size
    print(f"📐 Original Size: {original_width}x{original_height}")
    
    if max(img.size) > MAX_DIMENSION:
        img.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.Resampling.LANCZOS)
        print(f"🪄 Resized to: {img.width}x{img.height}")
    else:
        print("✅ Image is already small enough, skipping resize.")

    buffered = BytesIO()
    img.save(buffered, format="JPEG", quality=85)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def run_ocr():
    try:
        image_b64 = get_optimized_image_b64(IMAGE_URL)

        print(f"🚀 Sending to Ollama (waiting for first token)...")
        start_time = time.time()
        first_token = True

        client = ollama.Client(host='http://localhost:11434')  # <-- esto es lo que cambia
        stream = client.generate(
            model=MODEL_NAME,
            prompt="Text recognition:",
            images=[image_b64],
            stream=True
        )

        for chunk in stream:
            if first_token:
                print(f"⏱️ Time to first token: {time.time() - start_time:.2f}s\n")
                first_token = False
            
            print(chunk['response'], end='', flush=True)

        print(f"\n\n✅ Total Processing Time: {time.time() - start_time:.2f}s")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    run_ocr()