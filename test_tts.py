import asyncio
import edge_tts

async def main():
    communicate = edge_tts.Communicate("Olá, este é um teste com edge tts", "pt-BR-AntonioNeural")
    await communicate.save("saida.mp3")

asyncio.run(main())