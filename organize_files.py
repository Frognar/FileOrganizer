import argparse
import json

from file_organizer.organizer import organize_files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize files in a directory')
    parser.add_argument('source_directory', type=str, help='Path to the directory with files to be organized')
    parser.add_argument('-d', '--destination_directory', type=str,
                        help='Path to the destination directory where the organized files will be moved')
    args = parser.parse_args()
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    if destination_directory is None:
        destination_directory = source_directory

    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    organize_files(
        source_directory,
        destination_directory,
        config)
