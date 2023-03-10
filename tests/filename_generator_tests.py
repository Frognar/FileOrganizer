import unittest
from datetime import datetime
from unittest.mock import patch

from file_organizer.filename_generator import generate_new_filename


class TestFilenameGenerator(unittest.TestCase):
    @patch('file_organizer.filename_generator.now')
    @patch('file_organizer.filename_generator.generate_identifier')
    def test_generate_new_filename_with_date_and_uuid(self, mock_generate_identifier, mock_date):
        mock_generate_identifier.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('old-name.txt')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0.txt', new_name)

    @patch('file_organizer.filename_generator.now')
    @patch('file_organizer.filename_generator.generate_identifier')
    def test_generate_new_filename_replacing_whitespaces_with_hyphen(self, mock_generate_identifier, mock_date):
        mock_generate_identifier.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('old name.txt')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0.txt', new_name)

    @patch('file_organizer.filename_generator.now')
    @patch('file_organizer.filename_generator.generate_identifier')
    def test_generate_new_filename_using_lowercase(self, mock_generate_identifier, mock_date):
        mock_generate_identifier.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('OLD-NAME.txt')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0.txt', new_name)

    @patch('file_organizer.filename_generator.now')
    @patch('file_organizer.filename_generator.generate_identifier')
    def test_generate_new_filename_without_extension(self, mock_generate_identifier, mock_date):
        mock_generate_identifier.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('old-name')

        self.assertEqual('2023-03-04_old-name_f50ec0b7-f960-400d-91f0-c42a6d44e3d0', new_name)

    @patch('file_organizer.filename_generator.now')
    @patch('file_organizer.filename_generator.generate_identifier')
    def test_generate_new_filename_for_empty_name(self, mock_generate_identifier, mock_date):
        mock_generate_identifier.return_value = 'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'
        mock_date.return_value = datetime(2023, 3, 4, 14, 5)

        new_name = generate_new_filename('')

        self.assertEqual('2023-03-04_f50ec0b7-f960-400d-91f0-c42a6d44e3d0', new_name)
