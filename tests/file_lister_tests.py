import os
import unittest
from unittest.mock import patch

from file_organizer.file_lister import FileLister


class TestFileLister(unittest.TestCase):
    def test_list_files_returns_correct_number_of_files(self):
        directory_path = "test_directory"
        expected_files_count = 3

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1', 'file2', 'file3']
            file_lister = FileLister(os.listdir)
            files = file_lister.list_files(directory_path)
            self.assertEqual(len(files), expected_files_count)

    def test_list_files_returns_correct_file_names(self):
        directory_path = "test_directory"
        expected_files = ["file1.txt", "file2.txt", "file3.jpg"]

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = expected_files
            file_lister = FileLister(os.listdir)
            files = file_lister.list_files(directory_path)
            self.assertEqual(files, expected_files)

    def test_list_files_returns_empty_list_if_directory_is_empty(self):
        directory_path = "empty_directory"
        expected_files = []

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = expected_files
            file_lister = FileLister(os.listdir)
            files = file_lister.list_files(directory_path)
            self.assertEqual(files, expected_files)

    def test_list_files_returns_empty_list_if_directory_does_not_exist(self):
        directory_path = "non_existing_directory"
        expected_files = []

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.side_effect = FileNotFoundError
            file_lister = FileLister(os.listdir)
            files = file_lister.list_files(directory_path)
            self.assertEqual(files, expected_files)
