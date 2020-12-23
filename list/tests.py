from django.test import TestCase
from django.urls import resolve
from list.views import home_page

class HomePageTest(TestCase):
    '''test home page'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест преобразования корневого url  в представление домашней страници'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
