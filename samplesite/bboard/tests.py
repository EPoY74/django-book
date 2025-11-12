# Create your tests here.

from django.test import TestCase
from django.urls import reverse, resolve
from bboard import views
import inspect


class IndexViewTests(TestCase):
    def test_index_url_is_correct(self):
        url = reverse('bboard:index')
        self.assertEqual(url, '/bboard/')

    def test_public_path_resolves_to_named_route(self):
        match = resolve('/bboard/')
        self.assertEqual(match.view_name, 'bboard:index')
    
    def test_public_path_resolves_to_correct_fbv(self):
        match = resolve('/bboard/')
        # Распакуем декораторы, чтобы сравнить с исходной функцией
        self.assertIs(inspect.unwrap(match.func), views.index)

    def test_index_returns_200(self):
        url = reverse('bboard:index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)