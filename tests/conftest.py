"""
Pytest configuration and fixtures for FastAPI tests.

Provides shared fixtures including TestClient for API testing.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """
    Fixture that provides a TestClient for testing the FastAPI application.
    
    The TestClient allows us to make requests to the app without running
    a live server, making tests fast and isolated.
    
    Yields:
        TestClient: A client configured for the FastAPI app
    """
    return TestClient(app)


@pytest.fixture
def sample_activity():
    """
    Fixture that provides sample activity data for tests.
    
    Yields:
        dict: Sample activity information
    """
    return {
        "name": "Chess Club",
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "email": "student@mergington.edu"
    }
