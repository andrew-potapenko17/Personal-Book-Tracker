from django.test import TestCase
from rest_framework.test import APIClient

class BookStatsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_stats_empty_database(self):
        response = self.client.get('/api/books/stats/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['average_rating'], 0)