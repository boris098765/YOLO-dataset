from ..config_setup import main_settings

async def window_variables_initialise() -> dict:
    return {
        "appearance_mode": main_settings.window_settings.appearance_mode.get_secret_value(),
        "title": main_settings.window_settings.title.get_secret_value(),
        "size_x": main_settings.window_settings.size_x.get_secret_value(),
        "size_y": main_settings.window_settings.size_y.get_secret_value(),
    }