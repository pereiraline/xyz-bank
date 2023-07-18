from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ManagerPage(PageObject):

    url_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    css_add_customer = '[ng-click="addCust()"]'
    css_open_account = '[ng-click="openAccount()"]'
    css_show_customers = '[ng-click="showCust()"]'

    def __init__(self,driver):
        super(ManagerPage, self).__init__(driver=driver)

    def click_tab_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_add_customer).click()

    def click_tab_open_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_open_account).click()

    def click_tab_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_show_customers).click()

    def is_url_manager(self):
        return self.is_url(url=self.url_manager)