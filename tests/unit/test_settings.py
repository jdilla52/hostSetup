from host_setup.settings import Settings
import os

def test_settings(test_data_dir):
    path = os.path.join(test_data_dir, "input.toml")
    settings = Settings(path)
    settings.generate_call_stack()