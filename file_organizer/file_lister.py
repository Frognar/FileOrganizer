import os


def list_files(directory_path: str) -> list[str]:
    try:
        return [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    except FileNotFoundError:
        return []
