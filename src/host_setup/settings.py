from host_setup.media.media_target import MediaTarget
import toml


class Settings:
    "a class for parsing a toml and generating a call stack"

    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.settings = toml.load(settings_path)
        self.run_typs = self.generate_call_stack()

    def generate_call_stack(self):
        """roll through toml and formal them into something useful
        TODO add checking to inputs later
        """

        call_stack = []
        for val in self.settings.values():
            call_stack.append(MediaTarget(**val))
        return call_stack
