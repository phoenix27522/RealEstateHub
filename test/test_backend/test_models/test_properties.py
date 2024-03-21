import unittest
from unittest.mock import MagicMock
from backend.models.properties import Properties
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class TestProperties(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock(spec=sessionmaker())
        self.properties_data = {
            "user_id": "1",
            "name": "Test Property",
            "description": "This is a test property.",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "price": 100000,
            "latitude": 40.7128,
            "longitude": -74.0060
        }

    def test_init_method_with_given_data(self):
        properties = Properties(**self.properties_data)
        self.assertEqual(properties.user_id, "1")
        self.assertEqual(properties.name, "Test Property")
        self.assertEqual(properties.description, "This is a test property.")
        self.assertEqual(properties.number_rooms, 3)
        self.assertEqual(properties.number_bathrooms, 2)
        self.assertEqual(properties.price, 100000)
        self.assertEqual(properties.latitude, 40.7128)
        self.assertEqual(properties.longitude, -74.0060)

    def test_init_method_with_default_values(self):
        properties = Properties()
        self.assertIsNone(properties.user_id)
        self.assertIsNone(properties.name)
        self.assertIsNone(properties.description)
        self.assertEqual(properties.number_rooms, 1)
        self.assertEqual(properties.number_bathrooms, 0)
        self.assertEqual(properties.price, 0)
        self.assertIsNone(properties.latitude)
        self.assertIsNone(properties.longitude)

    def test_save_method(self):
        properties = Properties(**self.properties_data)
        properties.save(self.session)
        self.session.add.assert_called_once_with(properties)
        self.session.commit.assert_called_once()

    def test_to_dict_method(self):
        properties = Properties(**self.properties_data)
        result_dict = properties.to_dict()
        self.assertEqual(result_dict, {
            "user_id": "1",
            "name": "Test Property",
            "description": "This is a test property.",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "price": 100000,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "__class__": "Properties"
        })

    def test_delete_method(self):
        properties = Properties(**self.properties_data)
        properties.delete(self.session)
        self.session.delete.assert_called_once_with(properties)
        self.session.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
