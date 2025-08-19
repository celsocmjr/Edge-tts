Starting the Edge-TTS FastAPI Application
Here are the different ways to start the API:

1. Using Uvicorn (Recommended for Development)
Parameters explained:
uvicorn main3:app --reload --host 0.0.0.0 --port 8000

	--reload: Auto-reload on code changes
  --host 0.0.0.0: Allow external access
  --port 8000: Run on port 8000
