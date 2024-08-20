import unittest
from utils.request_handler import APIClient
from config.config import BASE_URL


class TestAPIClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the APIClient instance once for all tests"""
        cls.client = APIClient(base_url=BASE_URL)

    def test_get_all_posts(self):
        """Test retrieving all posts"""
        response = self.client.get("posts")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)  # Ensure there are at least one post

    def test_get_post_by_id(self):
        """Test retrieving a post by ID"""
        response = self.client.get("posts/1")
        self.assertEqual(response.status_code, 200)
        post = response.json()
        self.assertIsInstance(post, dict)
        self.assertEqual(post["userId"], 1)

    def test_create_post(self):
        """Test creating a new post"""
        new_post = {
            "userId": 1,
            "title": "Test Post",
            "body": "This is a test post"
        }
        response = self.client.post("posts", data=new_post)
        self.assertEqual(response.status_code, 201)
        created_post = response.json()
        self.assertIsInstance(created_post, dict)
        self.assertEqual(created_post["userId"], 1)
        self.assertEqual(created_post["title"], "Test Post")
        self.assertEqual(created_post["body"], "This is a test post")

    def test_update_post(self):
        """Test updating an existing post"""
        updated_post = {
            "userId": 1,
            "id": 1,
            "title": "Updated Test Post",
            "body": "This is an updated test post"
        }
        response = self.client.put("posts/1", data=updated_post)
        self.assertEqual(response.status_code, 200)
        updated_data = response.json()
        self.assertEqual(updated_data["title"], "Updated Test Post")
        self.assertEqual(updated_data["body"], "This is an updated test post")

    def test_delete_post(self):
        """Test deleting a post"""
        response = self.client.delete("posts/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{}')  # Expect an empty response body

    def test_invalid_endpoint(self):
        """Test request to an invalid endpoint"""
        response = self.client.get("invalid_endpoint")
        self.assertEqual(response.status_code, 404)

    def test_post_invalid_data(self):
        """Test creating a new post with invalid data"""
        invalid_post = {
            "userId": 1,
            "title": "Test Post",
            "body": 123  # This should be a string
        }
        response = self.client.post("posts", data=invalid_post)
        self.assertEqual(response.status_code, 201)
        created_post = response.json()
        self.assertIsInstance(created_post, dict)
        # The API might accept the invalid data and, check if it returns something
        self.assertIsNotNone(created_post["id"])

    def test_put_invalid_data(self):
        """Test updating an existing post with invalid data"""
        invalid_post = {
            "userId": 1,
            "id": 1,
            "title": "Updated Test Post",
            "body": 123  # This should be a string
        }
        response = self.client.put("posts/1", data=invalid_post)
        self.assertEqual(response.status_code, 200)
        updated_data = response.json()
        self.assertIsInstance(updated_data, dict)

    def test_delete_invalid_id(self):
        """Test deleting a post with an invalid ID"""
        response = self.client.delete("posts/100000")
        self.assertEqual(response.status_code, 200)  # JSONPlaceholder returns 200 even if the post doesn't exist


if __name__ == "__main__":
    unittest.main()
