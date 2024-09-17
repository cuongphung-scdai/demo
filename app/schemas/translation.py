from pydantic import BaseModel, Field

class TranslationRequest(BaseModel):
    """Request model for text translation."""

    text: str = Field(
        ...,
        description="The text to be translated"
    )
    source_lang: str = Field(
        ...,
        description="The source language code (e.g., 'en' for English)"
    )
    target_lang: str = Field(
        ...,
        description="The target language code (e.g., 'vi' for Vietnamese)"
    )
    tone: str = Field(
        ...,
        description="The desired tone of the translation (e.g., 'formal', 'informal')"
    )
    domain: str = Field(
        ...,
        description="The domain or context of the translation (e.g., 'legal', 'technical', 'medical')"
    )

class ImageTranslationRequest(BaseModel):
    """Request model for image translation."""

    image: bytes = Field(
        ...,
        description="The image to be translated"
    )
    source_lang: str = Field(
        ...,
        description="The source language code (e.g., 'en' for English)"
    )
    target_lang: str = Field(
        ...,
        description="The target language code (e.g., 'vi' for Vietnamese)"
    )
    tone: str = Field(
        ...,
        description="The desired tone of the translation (e.g., 'formal', 'informal')"
    )
    domain: str = Field(
        ...,
        description="The domain or context of the translation (e.g., 'legal', 'technical', 'medical')"
    )

class TranslationResponse(BaseModel):
    """Response model for text translation."""

    translated_text: str = Field(
        ...,
        description="The translated text"
    )

class LanguageDetectionRequest(BaseModel):
    """Request model for language detection."""

    text: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The text to detect the language of"
    )

class LanguageDetectionResponse(BaseModel):
    """Response model for language detection."""

    detected_language: str = Field(
        ...,
        min_length=2,
        max_length=5,
        description="The detected language code"
    )

class ErrorResponse(BaseModel):
    """Response model for error details."""

    detail: str = Field(
        ...,
        description="Error detail message"
    )
