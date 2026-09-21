import requests
from PIL import Image
from glmocr import GlmOcr

# --- Configuration ---
LOCAL_FILENAME = "7cf7af6c-0581-4fdc-a20f-7123aab8c0a2_3308x2339.jpg"

def run_sdk_ocr(image_path):
    # Optional: Resize to speed up CPU inference (1024px is the sweet spot)
    with Image.open(image_path) as img:
        if max(img.size) > 1024:
            img.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
            img.save(image_path)
            print(f"🪄 Resized {image_path} for faster CPU processing.")

    print(f"🚀 Initializing GLM-OCR SDK...")
    
    # Initialize the SDK in self-hosted mode
    with GlmOcr(config_path='./config.yaml') as parser:
        print("🔍 Analyzing document structure...")
        result = parser.parse(image_path)
        
        # Output the Markdown result
        print("\n" + "="*20 + " OCR RESULT " + "="*20)
        print(result.markdown_result)
        print("="*52)


if __name__ == "__main__":
    try:
        run_sdk_ocr(LOCAL_FILENAME)
        
    except Exception as e:
        print(f"❌ Error: {e}")