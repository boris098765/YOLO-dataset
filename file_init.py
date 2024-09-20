import os
import config


def create_folders():
    # Основная папка
    os.makedirs(config.data_path, exist_ok=True)

    # Изображения для датасета
    os.makedirs(config.images_path, exist_ok=True)
    os.makedirs(config.detect_images_path, exist_ok=True)
    os.makedirs(config.pose_images_path, exist_ok=True)

    # Остальные папки
    os.makedirs(config.datasets_path, exist_ok=True)
    os.makedirs(config.models_path, exist_ok=True)
    os.makedirs(config.my_models_path, exist_ok=True)
