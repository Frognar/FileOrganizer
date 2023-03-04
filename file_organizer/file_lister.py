class FileLister:
    def __init__(self, listdir_func):
        self.listdir_func = listdir_func

    def list_files(self, directory_path):
        try:
            return self.listdir_func(directory_path)
        except FileNotFoundError:
            return []
