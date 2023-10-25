from django.test import TestCase, Client

class reviewTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/review/')
        self.assertEqual(response.status_code, 200)