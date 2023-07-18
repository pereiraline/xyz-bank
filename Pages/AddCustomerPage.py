from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class AddCustomerPage(PageObject):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    first_name = '[placeholder="First Name"]'
    last_name = '[placeholder="Last Name"]'
    post_code = '[placeholder="Post Code"]'
    btn_add_customer = 'btn-default'

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)

    def click_btn_add_customer(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_add_customer).click()

    def add_costumer(self, firstname='Edvan', lastname='Andrade', postcode='000'):
        self.driver.find_element(By.CSS_SELECTOR, self.first_name).send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, self.last_name).send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, self.post_code).send_keys(postcode)
        self.click_btn_add_customer()

    def is_url_add_customer(self):
        return self.is_url(url=self.url_add_customer)


