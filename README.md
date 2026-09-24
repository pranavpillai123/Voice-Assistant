# Voice Assistant Alpha Production

Version: 0.0.1alpha

A Python-based voice assistant prototype for desktop use. It listens for a wake word, recognizes spoken commands, opens websites, plays music shortcuts, fetches news, and responds using Ollama-powered AI.

## Overview

This project is an early alpha build intended for experimentation and rapid iteration. It combines:

- speech recognition
- text-to-speech
- browser automation
- music shortcut links
- local AI responses through Ollama

## Current release

- Version: 0.0.1alpha
- Status: Alpha prototype

## Project files

- `main.py` - main assistant loop and command handling
- `prototype.py` - simplified voice assistant prototype
- `client.py` - alternate chat assistant/test client
- `musiclibrary.py` - music URL mapping for commands like `play stealth`
- `llama test.py` - basic Ollama model interaction check
- `requirements.txt` - project dependencies
- `pyproject.toml` - Python project metadata
- `VERSION` - version marker file
- `CHANGELOG.md` - release notes

## Features

- Wake word detection with Google Speech Recognition
- Voice command processing for basic actions
- Web browser shortcuts for Google, YouTube, and Facebook
- Music playback through configured YouTube links
- News retrieval using the News API
- AI chat responses using the Ollama runtime and the llama3 model

## Requirements

- Python 3.10 or newer
- Microphone access
- Internet access for speech recognition and news fetching
- Ollama installed and running locally
- The `llama3` model available in Ollama

## Setup

1. Open a terminal in the project folder.
2. Create a virtual environment:

   python -m venv .venv

3. Activate it:

   .venv\Scripts\activate

4. Install dependencies:

   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

5. Make sure Ollama is installed and running:

   ollama pull llama3

6. Start the assistant:

   python main.py

## Usage

Say the wake word:

- Jarvis

Then speak commands such as:

- open google
- open youtube
- play stealth
- tell me the news
- exit

## Notes

- This project is intentionally a lightweight prototype.
- Some features are designed for early-stage testing and experimentation.
- The repository version is currently aligned to 0.0.1alpha.

## Release versioning

When preparing a release, keep version information synchronized in all of these files:

- `pyproject.toml`
- `VERSION`
- `CHANGELOG.md`
