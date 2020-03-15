import os
from typing import Dict
from dotenv import load_dotenv, find_dotenv


class Global:
    def __init__(self, env: str = None, override: Dict = None):
        # build in overrides for testing
        self.env = env
        self.override = override
        self.load_global_env()

    def load_global_env(self):
        switcher = {
            (False, False): self.auto_load,
            (False, True): self.load_env_file,
            (True, False): self.load_params,
            (True, True): self.load_params,
        }

        f = switcher.get(self.check_vals)

        try:
            f()
        except:
            raise ValueError("the env couldn't be set")

    @property
    def check_vals(self):
        return (self.override is None, self.env is None)

    def auto_load(self):
        auto = find_dotenv()
        if auto is not None:
            load_dotenv(auto)
        else:
            raise ValueError("couldn't find the env file")

    def load_env_file(self):
        if not load_dotenv(self.env):
            raise ValueError(
                f"couldn't load the file, maybe it's here: {find_dotenv()}"
            )

    def load_params(self):
        for key, val in self.override.items():
            os.environ[key] = str(val)
