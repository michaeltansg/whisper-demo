# whisper-demo
Demonstrates OpenAI's Whisper API. This project uses gradio for the interface to rapidly create a demo.

## Setup

### Non-WAV audio file format support

If you are uploading non-WAV audio files (like mp3, m4a, etc), you will need to install ffmpeg. FFmpeg is a free and open-source software project that produces libraries and programs for handling multimedia data. One of these programs is `ffprobe`, which is used to gather information from multimedia streams and is required by some Python libraries to handle non-WAV audio files.

Here's how you can install FFmpeg:

**On Ubuntu or other Debian-based systems**, you can install it using apt:

```
sudo apt update
sudo apt install ffmpeg
```

**On macOS**, you can install it using Homebrew:

```
brew install ffmpeg
```

**On Windows**, the process is a bit more involved:

1. Download the FFmpeg build from the [official website](https://ffmpeg.org/download.html).
2. Extract the downloaded ZIP file.
3. Add the bin folder from the extracted file to your system path.

### Python Version and Virtual Environment

`pyenv` is used for this project. This will use the version of python defined in `.python-version` file. Activate the virtual environment and install dependencies like so:

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Environment Variables

Create a `.env` environment file by making a copy of the `.env.example` file.

```bash
$ cp .env.example .env
```

Replace the OpenAI API Key `OPENAI_API_KEY` with your API key for this project.

## Running the app

```bash
$ python app.py
```