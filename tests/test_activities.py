"""
Tests for the activities endpoint (GET /activities).

Tests fetching the list of all available activities.
Uses the AAA (Arrange-Act-Assert) pattern for clear test structure.
"""

import pytest


class TestActivitiesEndpoint:
    """Test cases for GET /activities endpoint"""

    def test_get_activities_returns_all_activities(self, client):
        """
        Test that GET /activities returns all available activities
        
        Arrange: TestClient is provided by fixture
        Act: Make GET request to /activities endpoint
        Assert: Response contains all nine activities
        """
        # Arrange
        expected_activities = {
            "Chess Club", "Programming Class", "Gym Class", "Basketball Club",
            "Track and Field", "Art Club", "Drama Club", "Debate Club", "Science Club",
        }
        
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        assert set(data) == expected_activities

    def test_get_activities_returns_valid_json(self, client):
        """
        Test that GET /activities returns valid JSON response
        
        Arrange: TestClient is provided by fixture
        Act: Make GET request to /activities endpoint
        Assert: Response is JSON and can be parsed successfully
        """
        # Arrange & Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("application/json")
        data = response.json()
        assert isinstance(data, dict)

    def test_activity_contains_required_fields(self, client):
        """
        Test that each activity contains all required fields
        
        Arrange: Define required fields for an activity
        Act: Get activities and inspect first activity
        Assert: All required fields are present in the activity object
        """
        # Arrange
        required_fields = ["description", "schedule", "max_participants", "participants"]
        
        # Act
        response = client.get("/activities")
        data = response.json()
        chess_club = data.get("Chess Club")
        
        # Assert
        assert chess_club is not None
        assert all(field in chess_club for field in required_fields)

    def test_activity_fields_have_correct_types(self, client):
        """
        Test that activity fields have the correct data types
        
        Arrange: Define expected data types
        Act: Get activities and inspect field types
        Assert: Fields match expected types (str, list, int)
        """
        # Arrange
        activity_name = "Chess Club"
        
        # Act
        response = client.get("/activities")
        data = response.json()
        activity = data[activity_name]
        
        # Assert
        assert isinstance(activity["description"], str)
        assert isinstance(activity["schedule"], str)
        assert isinstance(activity["max_participants"], int)
        assert isinstance(activity["participants"], list)
        assert all(isinstance(email, str) for email in activity["participants"])

    def test_get_activities_success_status_code(self, client):
        """
        Test that GET /activities returns HTTP 200 OK
        
        Arrange: TestClient is provided by fixture
        Act: Make GET request to /activities
        Assert: Status code is 200 (Success)
        """
        # Arrange & Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200

    def test_chess_club_has_initial_participants(self, client):
        """
        Test that Chess Club has initial participants
        
        Arrange: Verify known initial state
        Act: Get activities data
        Assert: Chess Club contains expected participant emails
        """
        # Arrange
        expected_participants = ["michael@mergington.edu", "daniel@mergington.edu"]
        
        # Act
        response = client.get("/activities")
        data = response.json()
        chess_club_participants = data["Chess Club"]["participants"]
        
        # Assert
        assert len(chess_club_participants) >= 2
        assert "michael@mergington.edu" in chess_club_participants
        assert "daniel@mergington.edu" in chess_club_participants
