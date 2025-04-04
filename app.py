import gradio as gr
from utils.ppt_parser import extract_slide_texts
from utils.summarizer import summarize_slide_texts
from utils.tts_generator import generate_tts_audio
from utils.ppt_to_image import convert_ppt_to_images
from utils.video_creator import create_video

def ppt_to_video(pptx_file):
    slides = extract_slide_texts(pptx_file.name)
    narrations = summarize_slide_texts(slides)
    audio_paths = generate_tts_audio(narrations)
    image_paths = convert_ppt_to_images(pptx_file.name)
    video_path = create_video(image_paths, audio_paths)
    return video_path

gr.Interface(fn=ppt_to_video,
             inputs=gr.File(label="Upload PPTX"),
             outputs=gr.Video(label="Generated Video")).launch()
