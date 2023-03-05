import os.path
import unittest
from unittest import mock
from unittest.mock import patch
from file_organizer.destination_path_generator import DestinationPathGenerator

from file_organizer.organizer import organize_files


class TestFileOrganizer(unittest.TestCase):
    @patch('file_organizer.organizer.move_file')
    @patch.object(DestinationPathGenerator, 'generate_path')
    @patch('file_organizer.organizer.generate_new_filename')
    @patch('file_organizer.organizer.list_files')
    def test_move_files_if_destination_path_not_exists(
            self,
            mock_list_files,
            mock_generate_new_filename,
            mock_generate_path,
            mock_move_file
    ):
        source_directory = 'source\\directory'
        destination_directory = 'destination\\directory'
        config = {}
        mock_list_files.return_value = ['file1.txt', 'file2.jpg', 'file3.pdf']
        mock_generate_new_filename.side_effect = lambda x: f'test_{x}'
        mock_generate_path.side_effect = lambda x: os.path.join(destination_directory, x)

        organize_files(source_directory, destination_directory, config)

        self.assertEqual(3, mock_move_file.call_count)
        self.assertEqual(mock_move_file.mock_calls, [
            mock.call('source\\directory\\file1.txt', 'destination\\directory\\test_file1.txt'),
            mock.call('source\\directory\\file2.jpg', 'destination\\directory\\test_file2.jpg'),
            mock.call('source\\directory\\file3.pdf', 'destination\\directory\\test_file3.pdf')
        ])
