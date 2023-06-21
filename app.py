import gradio as gr
import openai
from pydub import AudioSegment
from pydub.utils import make_chunks

from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def transcribe(audio_file_path):
    # Load audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Determine chunk length in milliseconds
    chunk_length_ms = 10000  # e.g., chunks of 10 seconds

    # Make chunks of audio
    chunks = make_chunks(audio, chunk_length_ms)

    # Transcribe each chunk
    full_transcript = ""
    for i, chunk in enumerate(chunks):
        chunk.export("/tmp/chunk.mp3", format="mp3")  # Export chunk to a temporary file
        with open("/tmp/chunk.mp3", "rb") as audio_file:
            transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file, response_format="text")
            full_transcript += transcript + " "

    return full_transcript

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Transcribe MP3 files using Whisper",
    description="This tool uses OpenAI's Whisper API to transcribe MP3 files. Please upload an MP3 file, and the tool will display its transcription."
)

if __name__ == "__main__":
    iface.launch()