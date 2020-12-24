from selenium import webdriver
from selenium .webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # предлагаеться добавить элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # ввести задание
        inputbox.send_keys('Купить павлиньи перья')

        # после ввода страница обновляется и содержит задание в качестве элемента страници
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows),
            "new element not add to the table"
        )
        # тектовое поле предлагает ввести задание
        # воодиться здание 2
        # страница обновляется и содержит  оба элемента
        # проверка сохранения списка
        # генерируеться уникальный url-адрес и выводится текст с пояснением
        # преход по указанному адресу - проверка списка заданий
        # проверка окончена заввершение работы приложения
        self.fail('!!!end test!!!')
if __name__=='__main__':
    unittest.main(warnings='ignore')
