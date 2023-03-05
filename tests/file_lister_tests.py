import unittest
from unittest.mock import patch

from file_organizer.file_lister import list_files


class TestFileLister(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files_returns_correct_number_of_files(self, mock_isfile, mock_listdir):
        mock_isfile.return_value = True
        mock_listdir.return_value = ['file1', 'file2', 'file3']
        directory_path = "test_directory"
        expected_files_count = 3

        files = list_files(directory_path)
        self.assertEqual(expected_files_count, len(files))

    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files_returns_correct_file_names(self, mock_isfile, mock_listdir):
        mock_isfile.return_value = True
        expected_files = ["file1.txt", "file2.txt", "file3.jpg"]
        mock_listdir.return_value = expected_files
        directory_path = "test_directory"

        files = list_files(directory_path)
        self.assertEqual(expected_files, files)

    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files_returns_empty_list_if_directory_is_empty(self, mock_isfile, mock_listdir):
        mock_isfile.return_value = True
        expected_files = []
        mock_listdir.return_value = expected_files
        directory_path = "empty_directory"

        files = list_files(directory_path)
        self.assertEqual(expected_files, files)

    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files_returns_empty_list_if_directory_does_not_exist(self, mock_isfile, mock_listdir):
        mock_isfile.return_value = True
        mock_listdir.side_effect = FileNotFoundError
        directory_path = "non_existing_directory"
        expected_files = []

        files = list_files(directory_path)
        self.assertEqual(expected_files, files)

    @patch('os.listdir')
    @patch('os.path.isfile')
    def test_list_files_returns_without_directories(self, mock_isfile, mock_listdir):
        def mock_responses(responses, default_response=True):
            return lambda argument: responses[argument] if argument in responses else default_response

        mock_isfile.side_effect = mock_responses({'existing_directory\\directory': False})
        mock_listdir.return_value = ["file1.txt", "file2.jpg", "directory"]
        directory_path = "existing_directory"
        expected_files = ["file1.txt", "file2.jpg"]

        files = list_files(directory_path)
        self.assertEqual(expected_files, files)
