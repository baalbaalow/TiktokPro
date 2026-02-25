import os
import sys
from pathlib import Path

# Ensure local .venv is used when running from VS Code terminal
# Add user's FFmpeg to PATH (adjust if your ffmpeg is in a different subfolder)
ffmpeg_dir = r"C:\Users\abdih\Downloads\ffmpeg-2026-02-23-git-7b15039cdb-full_build\bin"
os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")

from tiktok_remix_pro import process_remix

TEST_URL = "https://www.tiktok.com/@yuqimovie/video/7584113372539456781"
VOICE = 'en-US-AvaMultilingualNeural'

def main():
    print("Starting end-to-end test for:", TEST_URL)
    result = process_remix(TEST_URL, VOICE)
    # result is (rephrased_script, synced_audio_path, final_video_path) or (errorstr, None, None)
    print("Result:")
    print(result)

if __name__ == '__main__':
    main()
