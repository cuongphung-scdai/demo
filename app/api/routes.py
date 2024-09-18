from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from app.core.translation_service import translation_service
from app.schemas.translation import (
    TranslationRequest, 
    TranslationResponse, 
    LanguageDetectionRequest, 
    LanguageDetectionResponse
)
from PIL import Image
from io import BytesIO
from fastapi_limiter.depends import RateLimiter

router = APIRouter()


@router.post(
    "/translate", 
    response_model=TranslationResponse,
    dependencies=[Depends(RateLimiter(times=2, seconds=5))]
)
async def translate_text(request: TranslationRequest):
    """Endpoint to translate text from one language to another."""
    try:
        translated_text = await translation_service.translate(
            text=request.text,
            source_lang=request.source_lang,
            target_lang=request.target_lang,
            tone=request.tone,
            domain=request.domain
        )
        return TranslationResponse(translated_text=translated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/detect-language", response_model=LanguageDetectionResponse)
async def detect_language(request: LanguageDetectionRequest):
    """Endpoint to detect the language of the given text."""
    try:
        detected_language = await translation_service.detect_language(text=request.text)
        return LanguageDetectionResponse(detected_language=detected_language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supported-languages", response_model=dict)
async def get_supported_languages():
    """Endpoint to get a list of supported languages."""
    try:
        supported_languages = await translation_service.get_supported_languages()
        return supported_languages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supported-tones", response_model=dict)
async def get_supported_tones():
    """Endpoint to get a list of supported tones."""
    try:
        supported_tone = await translation_service.get_supported_tones()
        return supported_tone
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supported-domains", response_model=dict)
async def get_supported_domains():
    """Endpoint to get a list of supported domains."""
    try:
        supported_domains = await translation_service.get_supported_domains()
        return supported_domains
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/translate-image", response_class=StreamingResponse)
async def translate_image(request: TranslationRequest):
    """Endpoint to translate text within an image."""
    try:
        image = Image.open(BytesIO(request.image))
        translated_image = await translation_service.translate_image(
            image, request.source_lang, request.target_lang
        )
        return StreamingResponse(translated_image.tobytes(), media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
