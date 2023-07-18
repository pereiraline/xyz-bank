from selenium import webdriver


class PageObject:

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception('Browser não suportado')

            self.driver.implicitly_wait(5)

    def is_url(self, url):
        return self.driver.current_url == url
