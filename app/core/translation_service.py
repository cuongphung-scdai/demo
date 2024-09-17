import httpx
from typing import List
from app.core.config import settings
from pydantic_settings import BaseSettings

class TranslationService:
    """Service for handling translation-related API calls."""

    def __init__(self):
        """Initializes the translation service with API URL and key."""
        self.base_url = settings.TRANSLATION_API_URL
        self.api_key = settings.TRANSLATION_API_KEY

    async def translate(self, text: str, source_lang: str, target_lang: str, tone: str, domain: str) -> str:
        """
        Translates the given text from source language to target language.

        Args:
            text: The text to be translated.
            source_lang: The language code of the source text.
            target_lang: The language code to translate the text into.
            tone: The tone of the translation (e.g., formal, informal).
            domain: The domain or subject matter of the text (e.g., IT, finance).

        Returns:
            The translated text as a string.
        """
        return "This is a test."
        # Uncomment the following lines to implement the actual API call.
        # endpoint = f"{self.base_url}/translate"
        # params = {
        #     "api_key": self.api_key,
        #     "text": text,
        #     "source_lang": source_lang,
        #     "target_lang": target_lang
        # }
        # async with httpx.AsyncClient() as client:
        #     response = await client.post(endpoint, json=params)
        #     response.raise_for_status()
        #     data = response.json()
        #     return data["translated_text"]

    async def detect_language(self, text: str) -> str:
        """
        Detects the language of the given text.

        Args:
            text: The text whose language needs to be detected.

        Returns:
            The detected language code as a string.
        """
        endpoint = f"{self.base_url}/detect"
        params = {
            "api_key": self.api_key,
            "text": text,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(endpoint, json=params)
            response.raise_for_status()

            data = response.json()
            return data["detected_language"]

    async def get_supported_languages(self) -> dict:
        """
        Retrieves the list of supported languages by the translation API.

        Returns:
            A dictionary mapping domain names to their display names.
        """
        domain_map = {
            "general": "General",
            "IT": "IT",
            "finance": "Finance",
            "business": "Business",
            "entertainment": "Entertainment",
            "science": "Science",
            "technology": "Technology",
            "education": "Education",
            "health": "Health",
            "sports": "Sports",
        }
        return domain_map

    async def get_supported_tones(self) -> dict:
        """
        Retrieves the list of supported tones by the translation API.

        Returns:
            A dictionary mapping tone names to their display names.
        """
        tone_map = {
            "sad": "Sad",
            "happy": "Happy",
            "angry": "Angry",
            "relaxed": "Relaxed",
            "energetic": "Energetic",
            "focused": "Focused",
            "formal": "Formal",
            "informal": "Informal",
            "neutral": "Neutral",
        }
        return tone_map


# Instantiate the translation service for use
translation_service = TranslationService()