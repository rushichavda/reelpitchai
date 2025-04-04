from moviepy.editor import *

def create_video(images, audios, output_path="assets/output/final.mp4"):
    clips = []
    for img, audio in zip(images, audios):
        img_clip = ImageClip(img).set_duration(AudioFileClip(audio).duration)
        audio_clip = AudioFileClip(audio)
        clip = img_clip.set_audio(audio_clip)
        clips.append(clip)
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output_path, fps=24)
    return output_path
