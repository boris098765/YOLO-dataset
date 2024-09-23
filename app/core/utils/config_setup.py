from pydantic import SecretStr, BaseModel
from decouple import config
from enum import Enum

# Logs settings
class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"

class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"

class LoggingSettings(BaseModel):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False

    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"


# Main settings
class MainSettings(BaseModel):
    data_path: SecretStr = SecretStr(config('DATA_PATH'))

    images_path: SecretStr = SecretStr(config('IMAGES_PATH'))
    detect_images_path: SecretStr = SecretStr(config('DETECT_IMAGES_PATH'))
    pose_images_path: SecretStr = SecretStr(config('POSE_IMAGES_PATH'))
    datasets_path: SecretStr = SecretStr(config('DATASETS_PATH'))

    models_path: SecretStr = SecretStr(config('MODELS_PATH'))
    my_models_path: SecretStr = SecretStr(config('MY_MODELS_PATH'))

    # .env path
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Exporting the settings
main_settings = MainSettings()
log_settings = LoggingSettings()