from file_organizer.file_lister import list_files
from file_organizer.filename_generator import generate_new_filename
from file_organizer.destination_path_generator import DestinationPathGenerator
from file_organizer.file_mover import move_file
import os


def organize_files(source_directory: str, destination_directory: str, config: dict[str, str]):
    path_generator = DestinationPathGenerator(destination_directory, config)
    files = list_files(source_directory)
    for file in files:
        organize_file(source_directory, file, path_generator)


def organize_file(source_directory: str, file: str, path_generator: DestinationPathGenerator):
    source_file_path = os.path.join(source_directory, file)
    new_filename = generate_new_filename(file)
    destination_file_path = path_generator.generate_path(new_filename)
    move_file(source_file_path, destination_file_path)
