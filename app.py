import gradio as gr
from moviepy.editor import VideoFileClip
import os
import tempfile
import urllib.request

def download_sample_video():
    # Temporary placeholder animation video
    url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/video-preview.mp4"
    video_path = tempfile.mktemp(suffix=".mp4")
    urllib.request.urlretrieve(url, video_path)
    return video_path

def convert_to_gif(video_path):
    gif_path = tempfile.mktemp(suffix=".gif")
    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path, fps=10)
    return gif_path

def sketch_to_gif(image):
    # Normally you'd run the AnimateDiff model here — we simulate with placeholder for now
    video_path = download_sample_video()
    gif_path = convert_to_gif(video_path)
    return gif_path

demo = gr.Interface(
    fn=sketch_to_gif,
    inputs=gr.Image(type="filepath", label="Upload Your Sketch"),
    outputs=gr.Image(type="filepath", label="Animated GIF"),
    title="Sketch2GIF",
    description="Upload a hand-drawn sketch to turn it into an animated GIF (using AnimateDiff, soon!)"
)

demo.launch()
