from django.http import HttpRequest
from django.test import TestCase
from snippets.views import top


# Create your tests here.
class TopPageViewTest(TestCase):

    def test_top_returns_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(first=response.status_code, second=200)

    def test_to_returns_expected_content(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.content, b"Hello World")

