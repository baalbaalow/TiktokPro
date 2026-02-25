# TikTok Remix Pro

Quick start — tested on Windows 10/11

Prerequisites:
- Python 3.11+ (recommended)
- Node.js (for frontend) — `npm install` already used
- FFmpeg installed and on PATH. Example on this machine:
  C:\Users\abdih\Downloads\ffmpeg-2026-02-23-git-7b15039cdb-full_build\bin

Setup (Python):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the Gradio app (dev):
```powershell
python tiktok_remix_pro.py
```

Quick end-to-end test (what I ran):
```powershell
# ensure .venv is active or use full path to interpreter
.venv\Scripts\python run_test.py
```

Outputs
- Generated files are copied to the `outputs/` folder when you run the test runner. Files produced include `*_synced.mp3` and `*_final.mp4`.

Notes
- Ensure FFmpeg is available on PATH so `moviepy` and `pydub` can encode/decode audio.
- If you want commits/tags created, tell me and I will commit the repo changes.<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/9b857ace-2d47-411a-814c-6474095686fa

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`
