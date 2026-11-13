"""
Tests for the root endpoint (/).

Tests the redirect behavior from the root path to the static index.html page.
Uses the AAA (Arrange-Act-Assert) pattern for clear test structure.
"""

import pytest


class TestRootEndpoint:
    """Test cases for GET / endpoint"""

    def test_root_redirects_to_static_index(self, client):
        """
        Test that the root endpoint redirects to /static/index.html
        
        Arrange: TestClient is provided by fixture
        Act: Make GET request to root path
        Assert: Response status is 307 (redirect) and location header points to index.html
        """
        # Arrange
        expected_redirect_url = "/static/index.html"
        
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert response.status_code == 307
        assert response.headers["location"] == expected_redirect_url

    def test_root_redirect_status_code(self, client):
        """
        Test that root endpoint returns appropriate redirect status code
        
        Arrange: TestClient is provided by fixture
        Act: Make GET request to root
        Assert: Status code is 307 (Temporary Redirect)
        """
        # Arrange & Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert response.status_code == 307
