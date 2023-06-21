# whisper-demo
Demonstrates OpenAI's Whisper API. This project uses gradio for the interface to rapidly create a demo.

## Setup

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