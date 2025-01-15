#!/usr/bin/env python3

import os
import sys
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
if not os.path.exists(ffmpeg_path):
    print(f"Error: FFmpeg not found at {ffmpeg_path}")
    exit()

# Use the local FFmpeg path in your code
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Start the app
if __name__ == '__main__':
    core.run()
