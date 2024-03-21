import unittest
from unittest.mock import MagicMock
from backend.models.base import BaseModel
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock(spec=sessionmaker())
        self.base_model_data = {
            "id": "1",
            "created_at": datetime(2023, 1, 1, 12, 0, 0),
            "updated_at": datetime(2023, 1, 1, 12, 0, 0),
            "example_attr": "example_value"
        }

    def test_init_method_with_given_data(self):
        base_model = BaseModel(**self.base_model_data)
        self.assertEqual(base_model.id, "1")
        self.assertEqual(base_model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(base_model.updated_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(base_model.example_attr, "example_value")

    def test_init_method_with_default_values(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save_method(self):
        base_model = BaseModel(**self.base_model_data)
        base_model.save(self.session)
        self.session.add.assert_called_once_with(base_model)
        self.session.commit.assert_called_once()

    def test_to_dict_method(self):
        base_model = BaseModel(**self.base_model_data)
        result_dict = base_model.to_dict()
        self.assertEqual(result_dict, {
            "id": "1",
            "created_at": "2023-01-01 12:00:00",
            "updated_at": "2023-01-01 12:00:00",
            "example_attr": "example_value",
            "__class__": "BaseModel"
        })

    def test_delete_method(self):
        base_model = BaseModel(**self.base_model_data)
        base_model.delete(self.session)
        self.session.delete.assert_called_once_with(base_model)
        self.session.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
