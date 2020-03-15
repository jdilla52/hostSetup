import os
from typing import Dict, Optional
from dotenv import load_dotenv, find_dotenv


class Env:
    def __init__(self, env: Optional[str] = None, params: Optional[Dict] = None):
        # build in overrides for testing
        self.env = env
        self.params = params
        self.load_global_env()

    def load_global_env(self):
        switcher = {
            (True, True): self.auto_load,
            (True, False): self.load_env_file,
            (False, True): self.load_params,
            (False, False): self.load_params,
        }

        f = switcher.get(self.check_vals)
        try:
            f()
        except:
            raise ValueError("the env couldn't be set")

    @property
    def check_vals(self):
        return self.params is None, self.env is None

    def auto_load(self):
        print("auto loading -------")
        load_dotenv(find_dotenv(raise_error_if_not_found=True, usecwd=True))

    def load_env_file(self):

        if os.path.isfile(self.env):
            load_dotenv(self.env)
        else:
            raise ValueError(
                f"couldn't load the file, maybe it's here: {find_dotenv()}"
            )

    def load_params(self):
        for key, val in self.params.items():
            os.environ[key] = str(val)
