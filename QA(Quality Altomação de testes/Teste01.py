
#Exemplo 0:
#abra um novo navegador Firefox

#carregue a página no URL fornecido
'''
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')
'''
#Exemplo 1:
#abra um novo navegador Firefox

#carregue a página inicial do Yahoo

#procure por “selêniohq”

#feche o navegador
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()

'''

#Exemplo 2:
#O Selenium WebDriver é frequentemente usado como base para testar aplicativos da web. Aqui está um exemplo simples usando a biblioteca unittest padrão do Python :

import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)