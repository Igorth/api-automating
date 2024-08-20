# API Testing Project

## Overview
This project demonstrates API testing using pytest and includes various test cases 
for validating API responses. It is structured to provide clear documentation for setup, 
usage, and CI/CD configuration.

## Project Structure
```
project/
├── config/
│   └── config.py
├── reports/
├── tests/
│   ├── test_api_client.py
│   └── test_script.py
└── utils/
    └── api_client.py
```

## Setup Instructions

### Prerequisites
- Python 3.10 or later
- pip (Python package installer)

### Install Dependencies
1. **Clone the repository**:
```commandline
git clone https://github.com/Igorth/api-automating
cd project
```

2. **Create and activate a virtual environment**:
```commandline
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install required packages**:
```commandline
pip install -r requirements.txt
```
4. The requirements.txt file should include:
```commandline
pytest
pytest-html
```

## API Details
This project uses the JSONPlaceholder API for testing. Below are the details of the API endpoints used:

- GET /posts: Retrieve a list of posts.
- POST /posts: Create a new post.
- PUT /posts/1: updating an existing post.
- DELETE /posts/1: Deleting a post.

## Test Cases
The tests are located in the tests/ directory and are written using pytest.

## Running Tests
To run all tests:
```commandline
pytest
```
## Generating Test Reports
To generate an HTML report of the test results:
```commandline
pytest tests/test_api_client.py --html=reports/test_api_client_report.html --self-contained-html
```
## CI/CD Configuration
The CI/CD pipeline is configured using GitHub Actions. 
The configuration file is located in **.github/workflows/python-app.yml**.
It performs the following tasks:

- **Checks out the code.**
- **Sets up Python.**
- **Installs dependencies.**
- **Runs tests and generates reports.**
- **Uploads the test report as an artifact.**