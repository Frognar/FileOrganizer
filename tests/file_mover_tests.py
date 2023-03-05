import unittest
from unittest.mock import patch

from file_organizer.file_mover import move_file


class TestFileMover(unittest.TestCase):
    @patch('os.path.exists')
    @patch('os.mkdir')
    @patch('shutil.move')
    def test_move_files_if_destination_path_not_exists(self, mock_move, mock_makedir, mock_exists):
        mock_exists.return_value = False
        move_file('/path/to/file.txt', '/new/path/to/file.txt')

        mock_makedir.assert_called_once_with('/new/path/to')
        mock_move.assert_any_call('/path/to/file.txt', '/new/path/to/file.txt')

    @patch('os.path.exists')
    @patch('os.mkdir')
    @patch('shutil.move')
    def test_move_files_if_destination_path_exists(self, mock_move, mock_makedir, mock_exists):
        mock_exists.return_value = True
        move_file('/path/to/file.txt', '/new/path/to/file.txt')

        mock_makedir.assert_not_called()
        mock_move.assert_any_call('/path/to/file.txt', '/new/path/to/file.txt')
