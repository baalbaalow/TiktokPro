Hugging Face Spaces Deployment
================================

Steps to deploy this Gradio app to Hugging Face Spaces:

1. Create a Hugging Face account: https://huggingface.co/
2. Create a new Space and select the **Gradio** SDK.
3. Choose hardware: select **GPU** if you expect to use `whisper`/`torch` models (recommended).
4. Connect your GitHub repository to the Space or upload files directly. Ensure the repo root contains:
   - `app.py` (entrypoint that launches the Gradio `iface`)
   - `tiktok_remix_pro.py` (the pipeline and Gradio interface)
   - `requirements.txt` (Python dependencies)
   - `apt.txt` (lists `ffmpeg`, so the Space installs it via apt)
5. If your app requires API keys, add them under the Space Settings → Secrets.
6. Wait for the build to finish; the Space will show a URL where the app is hosted.

Notes and caveats
-----------------
- Builds that install heavy packages (e.g., `torch`, `whisper`) can be slow or exceed Space limits. If the build fails, consider deploying the backend using the supplied `Dockerfile` on a host like Render, Fly, or Railway.
- Using GPU hardware reduces inference time but may increase build duration.
- The `apt.txt` file requests `ffmpeg` be installed on the Space image so `moviepy`/`pydub` can work.
