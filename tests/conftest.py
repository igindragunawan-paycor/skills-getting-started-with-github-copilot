"""
Pytest configuration and fixtures for FastAPI tests.

Provides shared fixtures including TestClient for API testing.
"""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def client(monkeypatch):
    """
    Fixture that provides a TestClient for testing the FastAPI application.
    
    The TestClient allows us to make requests to the app without running
    a live server, making tests fast and isolated.
    
    Yields:
        TestClient: A client configured for the FastAPI app
    """
    monkeypatch.setattr(app_module, "activities", deepcopy(app_module.activities))
    with TestClient(app_module.app) as test_client:
        yield test_client


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
