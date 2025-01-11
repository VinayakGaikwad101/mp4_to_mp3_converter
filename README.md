# Video to Audio Converter

This project converts video files to audio files using the `pydub` library and `ffmpeg`.

## Requirements

- Python 3.x
- `pydub`
- `ffmpeg`

## Setup

1. Go to the root directory (where you can directly see the README.md file).

2. Place your .mp4 file in the root directory and rename it input.mp4

3. Create and Activate Virtual Environment

   ```bash
   python -m venv newenv
   .\newenv\Scripts\activate  # On Windows
   source newenv/bin/activate  # On macOS and Linux
   ```

4. Install Dependencies from `requirements.txt`

   ```bash
   pip install -r requirements.txt
   ```

5. Download and Install `ffmpeg`
   - Visit [ffmpeg.org](https://ffmpeg.org/download.html) and download the appropriate version for your operating system.
   - Follow the instructions to install `ffmpeg` and ensure it's added to your system's PATH.

## Usage

Run the script to convert a video file to an audio file:

```bash
python video_to_audio_pydub.py
```

This will convert your input.mp4 file into an output.mp3 file in the root directory

## License

This project is licensed under the MIT License.
