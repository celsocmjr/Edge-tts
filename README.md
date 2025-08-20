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

## Voice Options and Examples

### Available Languages
- English (en)
  - `en-US`: United States
  - `en-GB`: United Kingdom
  - `en-AU`: Australia
  - `en-CA`: Canada
  - `en-IN`: India

- Portuguese (pt)
  - `pt-BR`: Brazil
  - `pt-PT`: Portugal

- Spanish (es)
  - `es-ES`: Spain
  - `es-MX`: Mexico
  - `es-AR`: Argentina
  - `es-CO`: Colombia

### Common Voice Examples

#### English Voices
```bash
# US English Female
curl "http://localhost:8000/voices?locale=en-US&gender=Female"
# Popular voices: en-US-JennyNeural, en-US-AriaNeural

# British English Male
curl "http://localhost:8000/voices?locale=en-GB&gender=Male"
# Popular voices: en-GB-RyanNeural
```

#### Portuguese Voices
```bash
# Brazilian Portuguese
curl "http://localhost:8000/voices?locale=pt-BR&gender=Female"
# Popular voices: pt-BR-FranciscaNeural, pt-BR-AntonioNeural

# European Portuguese
curl "http://localhost:8000/voices?locale=pt-PT"
# Popular voices: pt-PT-RaquelNeural
```

#### Spanish Voices
```bash
# Spanish (Spain)
curl "http://localhost:8000/voices?locale=es-ES"
# Popular voices: es-ES-ElviraNeural, es-ES-AlvaroNeural

# Spanish (Mexico)
curl "http://localhost:8000/voices?locale=es-MX"
# Popular voices: es-MX-DaliaNeural, es-MX-JorgeNeural
```

### Voice Generation Examples

#### English Example
```bash
curl -X POST "http://localhost:8000/narrate/" \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello, this is a test",
    "voice": "en-US-JennyNeural",
    "rate": "+0%",
    "volume": "+50%"
}' \
--output english.mp3
```

#### Portuguese Example
```bash
curl -X POST "http://localhost:8000/narrate/" \
-H "Content-Type: application/json" \
-d '{
    "text": "Olá, isto é um teste",
    "voice": "pt-BR-FranciscaNeural",
    "rate": "+0%",
    "volume": "+50%"
}' \
--output portuguese.mp3
```

#### Spanish Example
```bash
curl -X POST "http://localhost:8000/narrate/" \
-H "Content-Type: application/json" \
-d '{
    "text": "Hola, esta es una prueba",
    "voice": "es-ES-ElviraNeural",
    "rate": "+0%",
    "volume": "+50%"
}' \
--output spanish.mp3
```

### Advanced Query Examples
```bash
# List all Portuguese variants
curl "http://localhost:8000/voices?locale=pt&locale_mode=startswith"

# Find specific voice by name
curl "http://localhost:8000/voices?name_contains=Neural"

# Combined filters
curl "http://localhost:8000/voices?locale=es-ES&gender=Female&name_contains=Elvira"
```

### API Endpoints

#### List Available Voices with Parameters
```bash
# List all voices
curl "http://localhost:8000/voices"

# Filter by language (locale)
curl "http://localhost:8000/voices?locale=pt-BR"  # Brazilian Portuguese
curl "http://localhost:8000/voices?locale=en-US"  # US English

# Filter by gender
curl "http://localhost:8000/voices?gender=Female"
curl "http://localhost:8000/voices?gender=Male"

# Search by name
curl "http://localhost:8000/voices?name_contains=Antonio"

# Combined filters
curl "http://localhost:8000/voices?locale=pt-BR&gender=Female"
curl "http://localhost:8000/voices?locale=en-US&gender=Male"

# Using locale modes
curl "http://localhost:8000/voices?locale=pt&locale_mode=startswith"  # All Portuguese variants
curl "http://localhost:8000/voices?locale=en-US&locale_mode=exact"    # Exact locale match

# Pretty print JSON output (macOS)
curl "http://localhost:8000/voices?locale=en-US&gender=Female" | python -m json.tool
```


## License

[MIT License](LICENSE)
