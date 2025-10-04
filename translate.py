from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# LibreTranslate API endpoint
LIBRETRANSLATE_URL = "https://libretranslate.de/translate"

# Request body model
class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "en"  # default English
    target_lang: str = "es"  # default Spanish

@app.post("/translate")
def translate(req: TranslationRequest):
    payload = {
        "q": req.text,
        "source": req.source_lang,
        "target": req.target_lang,
        "format": "text"
    }
    response = requests.post(LIBRETRANSLATE_URL, data=payload)
    if response.status_code == 200:
        translated_text = response.json().get("translatedText")
        return {"translated_text": translated_text}
    else:
        return {"error": "Translation failed"}
