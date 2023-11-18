from django.test import TestCase

# Create your tests here.
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)
    def test_air(self):
        response = self.client.get('/horoscope/type')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Air", response.content.decode())
