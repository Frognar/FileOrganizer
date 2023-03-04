import os.path


class DestinationPathGenerator:
    def __init__(self, destination_path: str, config: {}):
        self.destination_path = destination_path
        self.config = config

    def generate_path(self, filename):
        _, ext = os.path.splitext(filename)
        if ext in self.config:
            return f'{self.destination_path}/{self.config[ext]}/{filename}'
