import os


def list_files(directory_path: str) -> list[str]:
    try:
        return os.listdir(directory_path)
    except FileNotFoundError:
        return []
