import asyncio
import websockets
from googletrans import Translator

async def translate(websocket, path):
    translator = Translator()
    async for message in websocket:
        data = json.loads(message)
        source_lang = data['source_lang']
        target_lang = data['target_lang']
        text = data['text']
        translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
        await websocket.send(translated_text)

start_server = websockets.serve(translate, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
