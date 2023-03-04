import os


class FileLister:
    @staticmethod
    def list_files(directory_path):
        try:
            return os.listdir(directory_path)
        except FileNotFoundError:
            return []
