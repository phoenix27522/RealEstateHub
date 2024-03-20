import unittest
from unittest.mock import patch
from backend import RealEstateHub_db

class TestRealEstateHubDB(unittest.TestCase):

    @patch('os.getenv', return_value='admin')
    @patch('os.getenv', return_value='nk0701540135')
    @patch('os.getenv', return_value='localhost')
    @patch('os.getenv', return_value='db_RealEstateHub')
    def test_init(self, mock_db, mock_host, mock_pwd, mock_user):
        # Create an instance of RealEstateHub_db
        db = RealEstateHub_db()

        # Check if the engine is initialized
        self.assertIsNotNone(db._RealEstateHub_db__engine)

        # Check if the engine uses the correct connection string
        expected_url = 'mysql+mysqldb://admin:nk0701540135@localhost/db_RealEstateHub'
        self.assertEqual(db._RealEstateHub_db__engine.url.__str__(), expected_url)

if __name__ == '__main__':
    unittest.main()
