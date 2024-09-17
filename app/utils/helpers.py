import re
from typing import List

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by removing extra whitespace and normalizing punctuation.
    
    Args:
        text (str): The input text to preprocess.
    
    Returns:
        str: The preprocessed text.
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Normalize punctuation
    text = re.sub(r'([.!?])\s*(?=[A-Z])', r'\1\n', text)
    
    return text

def split_into_sentences(text: str) -> List[str]:
    """
    Split the input text into sentences.
    
    Args:
        text (str): The input text to split.
    
    Returns:
        List[str]: A list of sentences.
    """
    return re.split(r'(?<=[.!?])\s+', text)

def truncate_text(text: str, max_length: int = 1000) -> str:
    """
    Truncate the input text to a maximum length while preserving whole sentences.
    
    Args:
        text (str): The input text to truncate.
        max_length (int): The maximum length of the truncated text.
    
    Returns:
        str: The truncated text.
    """
    if len(text) <= max_length:
        return text
    
    sentences = split_into_sentences(text)
    truncated = []
    current_length = 0
    
    for sentence in sentences:
        if current_length + len(sentence) <= max_length:
            truncated.append(sentence)
            current_length += len(sentence)
        else:
            break
    
    return ' '.join(truncated)

def validate_language_code(language_code: str) -> bool:
    """
    Validate if the given language code is in the correct format (e.g., 'en', 'fr', 'de').
    
    Args:
        language_code (str): The language code to validate.
    
    Returns:
        bool: True if the language code is valid, False otherwise.
    """
    return bool(re.match(r'^[a-z]{2}$', language_code))

def format_translation_result(original: str, translated: str, source_lang: str, target_lang: str) -> dict:
    """
    Format the translation result into a dictionary.
    
    Args:
        original (str): The original text.
        translated (str): The translated text.
        source_lang (str): The source language code.
        target_lang (str): The target language code.
    
    Returns:
        dict: A formatted dictionary containing the translation result.
    """
    return {
        "original": original,
        "translated": translated,
        "source_language": source_lang,
        "target_language": target_lang,
        "character_count": len(original)
    }