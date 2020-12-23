from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''test new visiter'''
    def setUp(self):
        '''install'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''uninstall'''
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):
        ''''''
        # проверка домашней страници
        self.browser.get('http://localhost:8000')
        # проверка заголовка и шапки о списке дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('end test')
        # предлагаеться добавить элемент списка
        # ввести задание
        # после воода страница обновляется и содержит задание в качестве элемента страници
        # тектовое поле предлагает ввести задание
        # воодиться здание 2
        # страница обновляется и содержит  оба элемента
        # проверка сохранения списка
        # генерируеться уникальный url-адрес и выводится текст с пояснением
        # преход по указанному адресу - проверка списка заданий
        # проверка окончена заввершение работы приложения
if __name__=='__main__':
    unittest.main(warnings='ignore')
