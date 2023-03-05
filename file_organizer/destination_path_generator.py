import os.path


class DestinationPathGenerator:
    def __init__(self, destination_path: str, config: dict[str, str]):
        self.destination_path = destination_path
        self.config = config

    def generate_path(self, filename: str) -> str:
        _, ext = os.path.splitext(filename)
        new_path = self.get_destination_catalog(ext)
        return os.path.join(new_path, filename)

    def get_destination_catalog(self, ext: str) -> str:
        if ext in self.config:
            return os.path.join(self.destination_path, self.config[ext])
        elif 'default' in self.config:
            return os.path.join(self.destination_path, self.config['default'])
        return self.destination_path
