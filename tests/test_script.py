from utils.request_handler import APIClient

# Initialize the API client with the base URL
client = APIClient(base_url="https://jsonplaceholder.typicode.com")


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


if __name__ == "__main__":
    test_get_all_posts()
    test_get_post_by_id()
