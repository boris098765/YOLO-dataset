import os
from .initialise import main_variables_initalise

async def setup_directories():
    config = await main_variables_initalise()

    # Root directory
    os.makedirs(config.get("data_path"), exist_ok=True)

    # Images for dataset
    os.makedirs(config.get("images_path"), exist_ok=True)
    os.makedirs(config.get("detect_images_path"), exist_ok=True)
    os.makedirs(config.get("pose_images_path"), exist_ok=True)

    # Other directories
    os.makedirs(config.get("datasets_path"), exist_ok=True)
    os.makedirs(config.get("models_path"), exist_ok=True)
    os.makedirs(config.get("my_models_path"), exist_ok=True)