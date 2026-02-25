import os
import re
import asyncio
import tempfile
import yt_dlp
import whisper
import edge_tts
import gradio as gr
from pydub import AudioSegment
from moviepy import VideoFileClip, AudioFileClip

# --- Helper Functions ---

def download_tiktok(url):
    """Downloads TikTok video using yt-dlp."""
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': tempfile.mktemp() + '.mp4',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def transcribe_video(video_path):
    """Transcribes video audio using OpenAI Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result['text']

def simple_rephrase(text):
    """Simple synonym-based rephrasing to avoid basic copyright flags."""
    synonyms = {
        "good": "excellent", "bad": "unpleasant", "happy": "joyful", "sad": "unhappy",
        "very": "extremely", "really": "truly", "like": "enjoy", "love": "adore",
        "think": "believe", "say": "state", "go": "proceed", "make": "create",
        "get": "obtain", "know": "understand", "people": "individuals", "time": "duration",
        "new": "fresh", "first": "initial", "last": "final", "long": "extensive",
        "great": "terrific", "little": "small", "own": "possess", "other": "alternative",
        "old": "ancient", "right": "correct", "big": "large", "high": "lofty",
        "different": "diverse", "small": "tiny", "large": "huge", "next": "subsequent",
        "early": "premature", "young": "youthful", "important": "crucial", "few": "several",
        "public": "communal", "same": "identical", "able": "capable", "video": "clip",
        "watch": "view", "look": "observe", "want": "desire", "need": "require"
    }
    
    words = text.split()
    new_words = []
    for word in words:
        clean_word = re.sub(r'[^\w\s]', '', word).lower()
        if clean_word in synonyms:
            replacement = synonyms[clean_word]
            if word[0].isupper():
                replacement = replacement.capitalize()
            # Restore punctuation
            punct_match = re.search(r'[^\w\s]+$', word)
            if punct_match:
                replacement += punct_match.group()
            new_words.append(replacement)
        else:
            new_words.append(word)
    return " ".join(new_words)

async def generate_tts_async(text, voice, output_path):
    """Generates TTS audio using edge-tts."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

def generate_tts(text, voice):
    """Wrapper for async TTS generation."""
    output_path = tempfile.mktemp() + ".mp3"
    asyncio.run(generate_tts_async(text, voice, output_path))
    return output_path

def process_remix(tiktok_url, voice_choice):
    """Main pipeline for TikTok Remix Pro."""
    try:
        # 1. Download
        print(f"Downloading: {tiktok_url}")
        video_path = download_tiktok(tiktok_url)
        
        # 2. Transcribe
        print("Transcribing...")
        original_transcript = transcribe_video(video_path)
        
        # 3. Rephrase
        print("Rephrasing...")
        rephrased_script = simple_rephrase(original_transcript)
        
        # 4. Generate TTS
        print(f"Generating TTS with voice: {voice_choice}")
        tts_audio_path = generate_tts(rephrased_script, voice_choice)
        
        # 5. Duration Sync & Merge using pydub for audio speed change
        print("Syncing duration and merging...")
        video_clip = VideoFileClip(video_path)

        video_duration = video_clip.duration

        # Load TTS audio with pydub to perform reliable time-stretch (frame-rate trick)
        tts_audio_seg = AudioSegment.from_file(tts_audio_path)
        audio_duration = len(tts_audio_seg) / 1000.0

        # Calculate speed factor to match video duration exactly
        # speed_factor > 1 means audio is longer than video, so we speed it up
        speed_factor = audio_duration / video_duration if video_duration > 0 else 1.0

        def _change_speed_pydub(sound: AudioSegment, factor: float) -> AudioSegment:
            if factor == 1.0:
                return sound
            new_frame_rate = int(sound.frame_rate * factor)
            sped = sound._spawn(sound.raw_data, overrides={"frame_rate": new_frame_rate})
            return sped.set_frame_rate(sound.frame_rate)

        synced_seg = _change_speed_pydub(tts_audio_seg, speed_factor)

        synced_audio_path = tempfile.mktemp() + "_synced.mp3"

        # Normalize/amplify if audio is too quiet
        try:
            seg_dbfs = synced_seg.dBFS if hasattr(synced_seg, 'dBFS') else None
            target_dbfs = -14.0
            if seg_dbfs is not None and seg_dbfs < target_dbfs:
                gain = target_dbfs - seg_dbfs
                synced_seg = synced_seg.apply_gain(gain)
        except Exception:
            pass

        synced_seg.export(synced_audio_path, format="mp3")

        # Load synced audio into moviepy and ensure exact duration
        synced_audio_clip = AudioFileClip(synced_audio_path)

        try:
            # If audio longer, trim; if shorter, pad using pydub and reload
            if synced_audio_clip.duration > video_duration:
                synced_audio_clip = synced_audio_clip.subclip(0, video_duration)
            elif synced_audio_clip.duration < video_duration:
                pad_ms = int((video_duration - synced_audio_clip.duration) * 1000)
                padded = synced_seg + AudioSegment.silent(duration=pad_ms)
                padded.export(synced_audio_path, format="mp3")
                synced_audio_clip.close()
                synced_audio_clip = AudioFileClip(synced_audio_path)
        except Exception:
            # If any moviepy operation fails, proceed with available clip
            pass

        # 6. Final Merge
        final_video_clip = video_clip.with_audio(synced_audio_clip)
        final_video_path = tempfile.mktemp() + "_final.mp4"
        final_video_clip.write_videofile(
            final_video_path,
            codec="libx264",
            audio_codec="aac",
            audio_bitrate="192k",
            audio_fps=44100,
            logger=None,
        )

        # Cleanup original clips to free memory/file handles
        try:
            video_clip.close()
        except Exception:
            pass
        try:
            synced_audio_clip.close()
        except Exception:
            pass

        return rephrased_script, synced_audio_path, final_video_path

    except Exception as e:
        return f"Error: {str(e)}", None, None

# --- Gradio UI ---

voices = [
    'en-US-AvaMultilingualNeural',
    'en-US-AndrewMultilingualNeural',
    'en-US-AriaNeural',
    'en-US-GuyNeural',
    'en-US-JennyNeural',
    'en-US-SteffanNeural'
]

iface = gr.Interface(
    fn=process_remix,
    inputs=[
        gr.Textbox(label="TikTok URL", placeholder="https://www.tiktok.com/@user/video..."),
        gr.Dropdown(choices=voices, label="Select TTS Voice", value='en-US-AvaMultilingualNeural')
    ],
    outputs=[
        gr.Textbox(label="Rewritten Script"),
        gr.File(label="Synced Audio (MP3)"),
        gr.File(label="Final Remixed Video (MP4)")
    ],
    title="TikTok Remix Pro",
    description="Download TikToks, transcribe them, rephrase for copyright safety, and replace audio with AI voiceovers synced to the original duration."
)

if __name__ == "__main__":
    # pass theme to launch() per Gradio 6.x
    iface.launch(theme="soft")
