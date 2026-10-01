from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "ComicCraft"
    app_env: str = "development"
    host: str = "127.0.0.1"
    port: int = 8000

    ai_mode: str = "mock"
    gemini_api_key: str | None = None
    gemini_outline_model: str = "gemini-3.6-flash"
    gemini_story_model: str = "gemini-3.1-pro-preview"

    image_provider: str = "placeholder"
    diffusion_model: str = "stabilityai/stable-diffusion-xl-base-1.0"
    hf_token: str | None = None

    panel_count: int = 5
    image_width: int = 768
    image_height: int = 512

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def static_dir(self) -> Path:
        return BASE_DIR / "static"

    @property
    def panels_dir(self) -> Path:
        return self.static_dir / "panels"

    @property
    def exports_dir(self) -> Path:
        return self.static_dir / "exports"

    @property
    def templates_dir(self) -> Path:
        return BASE_DIR / "templates"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.panels_dir.mkdir(parents=True, exist_ok=True)
    settings.exports_dir.mkdir(parents=True, exist_ok=True)
    return settings
