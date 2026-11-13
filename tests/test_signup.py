"""
Tests for the signup endpoint (POST /activities/{activity_name}/signup).

Tests student signup functionality for extracurricular activities.
Uses the AAA (Arrange-Act-Assert) pattern for clear test structure.
"""

import pytest


class TestSignupEndpoint:
    """Test cases for POST /activities/{activity_name}/signup endpoint"""

    def test_successful_signup_for_valid_activity(self, client, sample_activity):
        """
        Test successful signup when activity exists and email is provided
        
        Arrange: Prepare activity name and student email
        Act: Make POST request to signup endpoint
        Assert: Response status is 200 and returns success message
        """
        # Arrange
        activity_name = sample_activity["name"]
        email = "newstudent@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert email in data["message"]
        assert activity_name in data["message"]

    def test_signup_returns_confirmation_message(self, client):
        """
        Test that successful signup returns proper confirmation message
        
        Arrange: Set up activity and email for signup
        Act: Submit signup request
        Assert: Response contains confirmation message format
        """
        # Arrange
        activity_name = "Programming Class"
        email = "alex@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        assert "Signed up" in data["message"]

    def test_signup_for_nonexistent_activity_returns_404(self, client):
        """
        Test that signup for non-existent activity returns 404 error
        
        Arrange: Use activity name that doesn't exist
        Act: Attempt signup for non-existent activity
        Assert: Response status is 404 and error message indicates activity not found
        """
        # Arrange
        nonexistent_activity = "Quantum Physics Club"
        email = "student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{nonexistent_activity}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 404
        data = response.json()
        assert "Activity not found" in data["detail"]

    def test_signup_adds_participant_to_activity(self, client):
        """
        Test that signup actually adds the participant to the activity
        
        Arrange: Get initial participant count
        Act: Sign up new student and fetch activities
        Assert: Participant count increases and email is in participants list
        """
        # Arrange
        activity_name = "Gym Class"
        new_email = "sarah@mergington.edu"
        
        # Get initial state
        initial_response = client.get("/activities")
        initial_participants = initial_response.json()[activity_name]["participants"].copy()
        initial_count = len(initial_participants)
        
        # Act
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": new_email}
        )
        
        # Check updated state
        updated_response = client.get("/activities")
        updated_participants = updated_response.json()[activity_name]["participants"]
        updated_count = len(updated_participants)
        
        # Assert
        assert signup_response.status_code == 200
        assert updated_count == initial_count + 1
        assert new_email in updated_participants

    def test_multiple_signups_increase_participant_count(self, client):
        """
        Test that multiple signups correctly increase participant count
        
        Arrange: Define multiple new students
        Act: Sign up each student one by one
        Assert: Participant count increases with each signup
        """
        # Arrange
        activity_name = "Chess Club"
        emails = ["student1@mergington.edu", "student2@mergington.edu", "student3@mergington.edu"]
        
        # Get initial count
        initial_response = client.get("/activities")
        initial_count = len(initial_response.json()[activity_name]["participants"])
        
        # Act
        for email in emails:
            response = client.post(
                f"/activities/{activity_name}/signup",
                params={"email": email}
            )
            assert response.status_code == 200
        
        # Get final count
        final_response = client.get("/activities")
        final_count = len(final_response.json()[activity_name]["participants"])
        
        # Assert
        assert final_count == initial_count + len(emails)

    def test_signup_response_status_is_success(self, client):
        """
        Test that successful signup returns HTTP 200 OK
        
        Arrange: Prepare signup request
        Act: Submit signup
        Assert: Status code is 200
        """
        # Arrange
        activity_name = "Programming Class"
        email = "student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200

    def test_signup_error_response_format(self, client):
        """
        Test that signup error response has correct format
        
        Arrange: Prepare request for non-existent activity
        Act: Submit invalid signup request
        Assert: Error response contains detail field with error message
        """
        # Arrange
        activity_name = "Nonexistent Activity"
        email = "student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        data = response.json()
        
        # Assert
        assert response.status_code == 404
        assert "detail" in data
        assert isinstance(data["detail"], str)
