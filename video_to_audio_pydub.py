from pydub import AudioSegment
import subprocess


def video_to_audio(input_video_path, output_audio_path):
    # Extract audio using ffmpeg
    command = f"ffmpeg -i {input_video_path} -q:a 0 -map a {output_audio_path}"
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    input_video_path = "input.mp4"
    output_audio_path = "output.mp3"
    video_to_audio(input_video_path, output_audio_path)
