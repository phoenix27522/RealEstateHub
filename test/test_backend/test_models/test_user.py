from hashlib import md5
import unittest
from unittest.mock import MagicMock
from backend.models.user import User
from sqlalchemy.exc import SQLAlchemyError

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword"
        }

    def test_save_method_hashes_password(self):
        session = MagicMock()
        user = User(**self.user_data)
        user.save(session)
        hashed_password = md5(self.user_data["password"].encode()).hexdigest()
        self.assertEqual(user.password, hashed_password)

    def test_save_method_raises_exception_on_failure(self):
        session = MagicMock()
        session.add.side_effect = SQLAlchemyError()
        user = User(**self.user_data)
        with self.assertRaises(SQLAlchemyError):
            user.save(session)

    def test_init_method_with_empty_data(self):
        user = User()
        self.assertIsNone(user.email)
        self.assertIsNone(user.username)
        self.assertIsNone(user.password)

    def test_init_method_with_given_data(self):
        user = User(**self.user_data)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.password, self.user_data["password"])

    def test_repr_method(self):
        user = User(**self.user_data)
        expected_repr = f"User(email='{self.user_data['email']}', username='{self.user_data['username']}')"
        self.assertEqual(repr(user), expected_repr)

if __name__ == "__main__":
    unittest.main()
