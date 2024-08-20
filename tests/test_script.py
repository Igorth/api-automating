from utils.api_client import APIClient
from config.config import BASE_URL

# Initialize the API client with the base URL
client = APIClient(base_url=BASE_URL)


# Test the GET request to retrieve all posts
def test_get_all_posts():
    response = client.get("posts")
    if response:
        print(f"GET /posts - Status Code: {response.status_code}")
        print(f"GET /posts - Response JSON: {response.json()[:1]}")


def test_get_post_by_id():
    response = client.get("posts/1")
    if response:
        print(f"GET /posts/1 - Status Code: {response.status_code}")
        print(f"GET /posts/1 - Response JSON: {response.json()}")


def test_create_post():
    new_post = {
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post."
    }
    response = client.post("posts", data=new_post)
    if response:
        print(f"POST /posts - Status Code: {response.status_code}")
        print(f"POST /posts - Response JSON: {response.json()}")


def test_update_post():
    updated_post = {
        "userId": 1,
        "title": "Updated Test Post",
        "body": "This is an updated test post.",
    }
    response = client.put("posts/1", data=updated_post)
    if response:
        print(f"PUT /posts/1 - Status Code: {response.status_code}")
        print(f"PUT /posts/1 - Response JSON: {response.json()}")


def test_delete_post():
    response = client.delete("posts/1")
    if response:
        print(f"DELETE /posts/1 - Status Code: {response.status_code}")


if __name__ == "__main__":
    test_get_all_posts()
    test_get_post_by_id()
    test_create_post()
    test_update_post()
    test_delete_post()
