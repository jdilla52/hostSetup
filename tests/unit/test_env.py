import os
from host_setup.env import Env

def test_env_auto(test_data_dir):
    os.chdir(test_data_dir)
    auto = Env()
    assert os.getenv("TEST") == "./TEST"

def test_env_file(test_data_dir):
    env = os.path.join(test_data_dir, ".env")
    env_file = Env(env=env)
    assert os.getenv("TEST") == "./TEST"

def test_env_param():
    params = {"HELLO":"./hello"}
    env_param = Env(params=params)
    assert os.getenv("HELLO") == "./hello"