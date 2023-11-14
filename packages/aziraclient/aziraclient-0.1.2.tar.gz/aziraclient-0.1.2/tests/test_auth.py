import unittest
import sys
import os

# Adjust the path to import the library correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aziraclient.auth.auth_client import AuthClient

class TestAuthClient(unittest.TestCase):
    """
    Test cases for the AuthClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up that runs once before all tests.
        """
        cls.base_url = "http://localhost:8000"
        cls.token_file = "user_token.txt"
        cls.auth_client = AuthClient(base_url=cls.base_url)

    def test_register_user(self):
        """
        Test the register_user method.
        """
        response = self.auth_client.register_user("username1", "password")
        # TODO: Need to properly work on the assertion
        self.assertIn("Registration successful", response)

    def test_login_user(self):
        """
        Test the login_user method.
        """
        response = self.auth_client.login_user("username1", "password")
        self.assertIn("Login successful", response)

if __name__ == '__main__':
    unittest.main()
