import unittest

from file_organizer.file_lister import FileLister


class TestFileLister(unittest.TestCase):
    def test_list_files_returns_correct_number_of_files(self):
        directory_path = "test_directory"
        expected_files_count = 3

        def listdir_func(_):
            return ['file1', 'file2', 'file3']

        file_lister = FileLister(listdir_func)
        files = file_lister.list_files(directory_path)

        self.assertEqual(len(files), expected_files_count)

    def test_list_files_returns_correct_file_names(self):
        directory_path = "test_directory"
        expected_files = ["file1.txt", "file2.txt", "file3.jpg"]

        def listdir_func(_):
            return expected_files

        file_lister = FileLister(listdir_func)
        files = file_lister.list_files(directory_path)

        self.assertEqual(files, expected_files)

    def test_list_files_returns_empty_list_if_directory_is_empty(self):
        directory_path = "empty_directory"

        def listdir_func(_):
            return []

        file_lister = FileLister(listdir_func)
        files = file_lister.list_files(directory_path)

        self.assertEqual(files, [])

    def test_list_files_returns_empty_list_if_directory_does_not_exist(self):
        directory_path = "non_existing_directory"

        def listdir_func(_):
            raise FileNotFoundError

        file_lister = FileLister(listdir_func)
        files = file_lister.list_files(directory_path)

        self.assertEqual(files, [])
