import unittest
from utils.request_handler import APIClient


class TestAPIClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the APIClient instance once for all tests"""
        cls.client = APIClient(base_url="https://jsonplaceholder.typicode.com")

    def test_get_all_posts(self):
        """Test retrieving all posts"""
        response = self.client.get("posts")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)  # Ensure there are at least one post


if __name__ == "__main__":
    unittest.main()
