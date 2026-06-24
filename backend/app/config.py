from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "My FastAPI Application"
    debug: bool = True
    database_url: str = "sqlite:///./fastapi.db"
    cors_origins: list[str] = ["*"] # Allow all origins for CORS
    static_files_path: str = "static"
    images_path: str = "static/images"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
settings = Settings()
