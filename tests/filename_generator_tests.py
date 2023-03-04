import unittest
from datetime import datetime
from unittest.mock import patch

from file_organizer.filename_generator import generate_new_filename


class TestFilenameGenerator(unittest.TestCase):
    @patch('file_organizer.filename_generator.now')
    @patch('uuid.uuid4')
    def test_generate_new_filename_with_date_and_uuid(self, mock_uuid, mock_date):
        mock_uuid.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('old-name.txt')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0.txt', new_name)

    @patch('file_organizer.filename_generator.now')
    @patch('uuid.uuid4')
    def test_generate_new_filename_replacing_whitespaces_with_hyphen(self, mock_uuid, mock_date):
        mock_uuid.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('old name.txt')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0.txt', new_name)
