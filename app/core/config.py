from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Settings class for configuration variables using Pydantic's BaseSettings."""
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Machine Translation API"

    # CORS Settings
    ALLOWED_ORIGINS: List[str] = ["*"]

    # Translation API Settings
    TRANSLATION_API_URL: str
    TRANSLATION_API_KEY: str

    # Database Settings
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # Redis Settings
    REDIS_HOST: str 
    REDIS_USER: str 
    REDIS_PASSWORD: str
    REDIS_PORT: str

    # JWT Settings
    SECRET_KEY: str = "key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DOCKER_PORT: int = 4000

    class Config:
        """Configuration for reading environment variables."""
        env_file = ".env"
        case_sensitive = True

settings = Settings()