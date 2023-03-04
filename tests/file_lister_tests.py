import unittest
from unittest.mock import patch

from file_organizer.file_lister import list_files


class TestFileLister(unittest.TestCase):
    @patch('os.listdir')
    def test_list_files_returns_correct_number_of_files(self, listdir):
        listdir.return_value = ['file1', 'file2', 'file3']
        directory_path = "test_directory"
        expected_files_count = 3

        files = list_files(directory_path)
        self.assertEqual(len(files), expected_files_count)

    @patch('os.listdir')
    def test_list_files_returns_correct_file_names(self, listdir):
        expected_files = ["file1.txt", "file2.txt", "file3.jpg"]
        listdir.return_value = expected_files
        directory_path = "test_directory"

        files = list_files(directory_path)
        self.assertEqual(files, expected_files)

    @patch('os.listdir')
    def test_list_files_returns_empty_list_if_directory_is_empty(self, listdir):
        expected_files = []
        listdir.return_value = expected_files
        directory_path = "empty_directory"

        files = list_files(directory_path)
        self.assertEqual(files, expected_files)

    @patch('os.listdir')
    def test_list_files_returns_empty_list_if_directory_does_not_exist(self, listdir):
        listdir.side_effect = FileNotFoundError
        directory_path = "non_existing_directory"
        expected_files = []

        files = list_files(directory_path)
        self.assertEqual(files, expected_files)
