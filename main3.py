from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from fastapi.responses import FileResponse, JSONResponse
import edge_tts
import asyncio
import tempfile
import os
import logging
import re

app = FastAPI()
logging.basicConfig(level=logging.INFO)

# ----------- MODELO DE REQUISIÇÃO -----------
class NarrationRequest(BaseModel):
    text: str
    voice: str = "en-US-AnaNeural"  # Default voice
    rate: str = "+0%"                    # Speech rate (e.g., "-50%", "+0%", "+50%")
    volume: str = "+0%"                  # Volume (e.g., "-50%", "+0%", "+100%")
    pitch: str = "+0Hz"                  # Pitch (e.g., "-50Hz", "+0Hz", "+50Hz")

# ----------- ENDPOINT PARA NARRAÇÃO -----------
@app.post("/narrate/")
async def narrate(request: NarrationRequest):
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    audio_path = temp_audio.name
    temp_audio.close()

    try:
        logging.info(f"Gerando áudio com voz: {request.voice}")
        communicate = edge_tts.Communicate(
            text=request.text,
            voice=request.voice,
            rate=request.rate,
            volume=request.volume,
            pitch=request.pitch
        )
        await communicate.save(audio_path)

        # Remover arquivo temporário após envio
        asyncio.create_task(remove_temp_file(audio_path))

        return FileResponse(
            path=audio_path,
            media_type="audio/mpeg",
            filename="narracao.mp3"
        )

    except Exception as e:
        logging.error(f"Erro ao gerar áudio: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ----------- ENDPOINT PARA LISTAGEM DE VOZES -----------
@app.get("/voices/")
async def list_voices(
    locale: str = Query(default=None, description="Ex: pt-BR, en-US"),
    locale_mode: str = Query(default="exact", description="exact, startswith ou regex"),
    gender: str = Query(default=None, description="Male ou Female"),
    name_contains: str = Query(default=None, description="Parte do nome da voz")
):
    try:
        voices = await edge_tts.list_voices()

        # Validação de modo regex
        if locale_mode == "regex" and not (locale and locale.strip()):
            raise HTTPException(status_code=400, detail="Para usar 'locale_mode=regex', o parâmetro 'locale' deve ser preenchido.")

        # Filtro por locale
        if locale and locale.strip():
            locale = locale.lower()
            if locale_mode == "exact":
                voices = [v for v in voices if v["Locale"].lower() == locale]
            elif locale_mode == "startswith":
                voices = [v for v in voices if v["Locale"].lower().startswith(locale)]
            elif locale_mode == "regex":
                try:
                    pattern = re.compile(locale)
                    voices = [v for v in voices if pattern.search(v["Locale"].lower())]
                except re.error:
                    raise HTTPException(status_code=400, detail="Expressão regex inválida para 'locale'")
            else:
                raise HTTPException(status_code=400, detail="Valor inválido para 'locale_mode'. Use: exact, startswith ou regex.")

        # Filtro por gênero
        if gender and gender.strip():
            voices = [v for v in voices if v["Gender"].lower() == gender.lower()]

        # Filtro por nome da voz
        if name_contains and name_contains.strip():
            voices = [v for v in voices if name_contains.lower() in v["ShortName"].lower()]

        return JSONResponse(content=voices)

    except Exception as e:
        logging.error(f"Erro ao listar vozes: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ----------- FUNÇÃO PARA LIMPAR ARQUIVOS TEMPORÁRIOS -----------
async def remove_temp_file(file_path: str):
    await asyncio.sleep(3)
    if os.path.exists(file_path):
        os.remove(file_path)
        logging.info(f"Arquivo temporário removido: {file_path}")
