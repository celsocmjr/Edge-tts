<<<<<<< HEAD
Starting the Edge-TTS FastAPI Application
Here are the different ways to start the API:

1. Using Uvicorn (Recommended for Development)
Parameters explained:
uvicorn main3:app --reload --host 0.0.0.0 --port 8000

	--reload: Auto-reload on code changes
  --host 0.0.0.0: Allow external access
  --port 8000: Run on port 8000
=======
# Edge-TTS API

A FastAPI application that provides REST endpoints for text-to-speech conversion using Microsoft Edge TTS engine.

## Features

- Text-to-speech conversion with multiple voices
- Support for various languages and accents
- Adjustable speech parameters (rate, volume, pitch)
- Voice filtering by locale, gender, and name
- Automatic cleanup of temporary audio files

## Prerequisites

- Python 3.9+
- pip
- Docker (optional)

## Installation

### Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/edge-tts-api.git
cd edge-tts-api

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Starting the API

```bash
# Using uvicorn
uvicorn main3:app --reload --host 0.0.0.0 --port 8000
```

### API Endpoints

#### List Available Voices
```bash
curl "http://localhost:8000/voices?locale=en-US&gender=Female"
```

#### Generate Speech
```bash
curl -X POST "http://localhost:8000/narrate/" \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello, this is a test",
    "voice": "en-US-JennyNeural",
    "rate": "+0%",
    "volume": "+0%",
    "pitch": "+0Hz"
}' \
--output test.mp3
```

### API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Parameters

### Voice Selection
- `locale`: Language code (e.g., "en-US", "pt-BR")
- `gender`: "Male" or "Female"
- `name_contains`: Search by voice name

### Speech Configuration
- `rate`: Speech rate (-100% to +100%)
- `volume`: Volume level (-100% to +100%)
- `pitch`: Voice pitch (-100Hz to +100Hz)

## Development

```bash
# Clone the repository
git clone https://github.com/yourusername/edge-tts-api.git

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
```

## License

[MIT License](LICENSE)