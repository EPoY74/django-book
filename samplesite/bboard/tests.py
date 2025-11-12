# Create your tests here.

from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_index_returns_200_and_has_corect_url(self):
        url = reverse('bboard:index')
        # Check that the URL is correct
        self.assertEqual(url, '/bboard/')
        resp = self.client.get(url)
        # Check that the response is 200 OK.
        self.assertEqual(resp.status_code, 200)