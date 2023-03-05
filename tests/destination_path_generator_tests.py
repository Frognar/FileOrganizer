import unittest

from file_organizer.destination_path_generator import DestinationPathGenerator


class TestDestinationPathGenerator(unittest.TestCase):
    def test_generate_path_returns_correct_path(self):
        config = {
            '.jpg': 'Images'
        }
        destination_path = 'C:/dev'
        generator = DestinationPathGenerator(destination_path, config)
        file_name = 'test.jpg'
        expected_path = 'C:/dev/Images/test.jpg'

        new_path = generator.generate_path(file_name)

        self.assertEqual(expected_path, new_path)

    def test_generate_path_returns_correct_path_using_default_catalog(self):
        config = {
            'default': 'Other'
        }
        destination_path = 'C:/dev'
        generator = DestinationPathGenerator(destination_path, config)
        file_name = 'test.jpg'
        expected_path = 'C:/dev/Other/test.jpg'

        new_path = generator.generate_path(file_name)

        self.assertEqual(expected_path, new_path)

    def test_generate_path_returns_correct_path_without_catalog(self):
        config = {}
        destination_path = 'C:/dev'
        generator = DestinationPathGenerator(destination_path, config)
        file_name = 'test.jpg'
        expected_path = 'C:/dev/test.jpg'

        new_path = generator.generate_path(file_name)

        self.assertEqual(expected_path, new_path)

    def test_generate_path_returns_correct_path_without_extension(self):
        config = {
            'default': 'Other'
        }
        destination_path = 'C:/dev'
        generator = DestinationPathGenerator(destination_path, config)
        file_name = 'test'
        expected_path = 'C:/dev/Other/test'

        new_path = generator.generate_path(file_name)

        self.assertEqual(expected_path, new_path)
