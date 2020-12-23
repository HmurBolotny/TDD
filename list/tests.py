from django.test import TestCase

class SmokeTest(TestCase):
    '''toxic test'''

    def test_bad_maths(self):
        '''тест: неправильны математические расчеты'''
        self.assertEqual(1 + 1, 3)
# Create your tests here.
