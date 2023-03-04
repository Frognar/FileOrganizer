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
