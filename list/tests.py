from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from list.views import home_page

class HomePageTest(TestCase):
    '''test home page'''

    def test_home_page_return_correct_html(self):
        '''тест домашняя страница возвращяет привильный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
