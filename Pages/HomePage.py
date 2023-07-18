from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject
class HomePage(PageObject):

    url_home = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    css_btn_customer_login = '[ng-click="customer()"]'
    css_btn_bank_manager_login = '[ng-click="manager()"]'

    def __init__(self, browser='chrome'):
        super(HomePage, self).__init__(browser=browser)
        self.driver.get(self.url_home)

    def click_btn_bank_manager_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_bank_manager_login).click()

    def click_btn_customer_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_customer_login).click()

    def is_url_home_page(self):
        return self.is_url(url=self.url_home)

