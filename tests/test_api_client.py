import pytest
from utils.api_client import APIClient
from config.config import BASE_URL


@pytest.fixture()
def client():
    return APIClient(base_url=BASE_URL)


def test_get_all_posts(client):
    """Test retrieving all posts"""
    response = client.get("posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Ensure there are at least one post


def test_get_post_by_id(client):
    """Test retrieving a post by ID"""
    response = client.get("posts/1")
    assert response.status_code == 201
    post = response.json()
    assert isinstance(post, dict)
    assert post["userId"] == 1


def test_create_post(client):
    """Test creating a new post"""
    new_post = {
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post"
    }
    response = client.post("posts", data=new_post)
    assert response.status_code == 201
    created_post = response.json()
    assert isinstance(created_post, dict)
    assert created_post["userId"] == 1
    assert created_post["title"] == "Test Post"
    assert created_post["body"] == "This is a test post"


def test_update_post(client):
    """Test updating an existing post"""
    updated_post = {
        "userId": 1,
        "id": 1,
        "title": "Updated Test Post",
        "body": "This is an updated test post"
    }
    response = client.put("posts/1", data=updated_post)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data["title"] == "Updated Test Post"
    assert updated_data["body"] == "This is an updated test post"


def test_delete_post(client):
    """Test deleting a post"""
    response = client.delete("posts/1")
    assert response.status_code == 200
    assert response.text == '{}'  # Expect an empty response body


def test_invalid_endpoint(client):

    """Test request to an invalid endpoint"""
    response = client.get("invalid_endpoint")
    assert response.status_code == 404


def test_post_invalid_data(client):
    """Test creating a new post with invalid data"""
    invalid_post = {
        "userId": 1,
        "title": "Test Post",
        "body": 123  # This should be a string
    }
    response = client.post("posts", data=invalid_post)
    assert response.status_code == 201
    created_post = response.json()
    assert isinstance(created_post, dict)
    # The API might accept the invalid data and, check if it returns something
    assert created_post["id"] is not None


def test_put_invalid_data(client):
    """Test updating an existing post with invalid data"""
    invalid_post = {
        "userId": 1,
        "id": 1,
        "title": "Updated Test Post",
        "body": 123  # This should be a string
    }
    response = client.put("posts/1", data=invalid_post)
    assert response.status_code == 200
    updated_data = response.json()
    assert isinstance(updated_data, dict)


def test_delete_invalid_id(client):
    """Test deleting a post with an invalid ID"""
    response = client.delete("posts/100000")
    assert response.status_code == 200  # JSONPlaceholder returns 200 even if the post doesn't exist
