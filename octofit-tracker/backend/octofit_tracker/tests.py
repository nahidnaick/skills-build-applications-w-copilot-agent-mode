from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(email="ironman@marvel.com", username="IronMan", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Upper body workout")
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration=30, date="2023-01-01")
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)

    def test_users_endpoint(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get("/teams/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get("/activities/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get("/workouts/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get("/leaderboard/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
