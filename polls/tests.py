from django.test import TestCase, Client

# Create your tests here.


class SmokeTests(TestCase):
    def test_index_loads(self):
        client = Client()
        response = client.get("/polls/")
        self.assertEqual(response.status_code, 200)
