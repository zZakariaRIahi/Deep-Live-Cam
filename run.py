#!/usr/bin/env python3

import os
import sys
import requests
from modules import core

# Define paths to local models
models_path = os.path.join(os.path.dirname(sys.argv[0]), "models")
inswapper_model_path = os.path.join(models_path, "inswapper_128_fp16.onnx")
gfpgan_model_path = os.path.join(models_path, "GFPGANv1.4.pth")

# Check if models exist
if not os.path.exists(inswapper_model_path):
    print(f"Error: ONNX model not found at {inswapper_model_path}")
    exit()

if not os.path.exists(gfpgan_model_path):
    print(f"Error: GFPGAN model not found at {gfpgan_model_path}")
    exit()

# FFmpeg path
ffmpeg_path = os.path.join(os.path.dirname(sys.argv[0]), "ffmpeg", "ffmpeg")

# If FFmpeg doesn't exist, download it
if not os.path.exists(ffmpeg_path):
    print("FFmpeg not found locally. Downloading from Google Drive...")
    try:
        ffmpeg_url = "https://drive.google.com/uc?export=download&id=1byJEivvxlWrotJ6jPKTFpTxHreKKk4MK"
        response = requests.get(ffmpeg_url, stream=True)
        response.raise_for_status()
        os.makedirs(os.path.dirname(ffmpeg_path), exist_ok=True)
        with open(ffmpeg_path, "wb") as ffmpeg_file:
            for chunk in response.iter_content(chunk_size=8192):
                ffmpeg_file.write(chunk)
        os.chmod(ffmpeg_path, 0o755)  # Make it executable
        print("FFmpeg downloaded successfully.")
    except Exception as e:
        print(f"Error downloading FFmpeg: {e}")
        exit()

# Use the local FFmpeg path in your code
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Start the app
if __name__ == '__main__':
    core.run()
