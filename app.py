from tiktok_remix_pro import iface

if __name__ == "__main__":
    # Launch Gradio app (Hugging Face Spaces will run this file)
    iface.launch(server_name="0.0.0.0", server_port=7860)
