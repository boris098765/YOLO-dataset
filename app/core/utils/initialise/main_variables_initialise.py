from ..config_setup import main_settings

async def main_variables_initalise() -> dict:
    return {
        "data_path": main_settings.data_path.get_secret_value(),
        "images_path": main_settings.images_path.get_secret_value(),
        "detect_images_path": main_settings.detect_images_path.get_secret_value(),
        "pose_images_path": main_settings.pose_images_path.get_secret_value(),
        "datasets_path": main_settings.datasets_path.get_secret_value(),
        "models_path": main_settings.models_path.get_secret_value(),
        "my_models_path": main_settings.my_models_path.get_secret_value()
    }