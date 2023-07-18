from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.PageObject import PageObject


class CustomerLoginPage(PageObject):
    url_customer_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    select_name = 'userSelect'
    btn_login = 'btn-default'
    user_name = 'Hermoine Granger'

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)

    def login_customer(self):
        select = Select(self.driver.find_element(By.ID, self.select_name))
        select.select_by_visible_text(self.user_name)
        self.driver.find_element(By.CLASS_NAME,self.btn_login).click()

