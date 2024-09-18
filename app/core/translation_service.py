import httpx
import torch
from typing import List, Literal
from fast_langdetect import detect_language
from app.core.config import settings
from pydantic_settings import BaseSettings
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class TranslationService:
    """Service for handling translation-related API calls."""

    def __init__(self):
        """Initializes the translation service with model and tokenizer."""
        # Load pre-trained model and tokenizer
        self.tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
        self.model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")

        # Check if a GPU is available and move model to GPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

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
        # Encode the input text with source language
        encoded_text = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        self.tokenizer.src_lang = source_lang
        self.tokenizer.tgt_lang = target_lang

        # Move the encoded text to the same device as the model
        input_ids = encoded_text["input_ids"].to(self.device)
        attention_mask = encoded_text["attention_mask"].to(self.device)

        # Generate the translation
        with torch.no_grad():
            translated_tokens = self.model.generate(input_ids=input_ids, attention_mask=attention_mask)

        # Decode the translated text
        translated_text = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        return translated_text
    
    async def detect_language(self, text: str) -> str:
        """
        Detects the language of the given text.

        Args:
            text: The text whose language needs to be detected.

        Returns:
            The detected language code as a string.
        """
        # Using langdetect library
        try:
            language = detect_language(text)
            return language
        except Exception as e:
            raise Exception(f"Error detecting language: {e}")
        
    async def get_supported_domains(self) -> dict:
        
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

    async def get_supported_languages(self) -> dict:
        """Retrieves the list of supported languages by the translation API.

        Returns:
            
        """
        supported_languages = {
            "VI": "Vietnamese",
            "KO": "Korean",
            "JA": "Japanese",
            "ZH": "Chinese",  
        }
        return supported_languages

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