import os.path
import shutil


def move_file(source, destination):
    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    shutil.move(source, destination)
