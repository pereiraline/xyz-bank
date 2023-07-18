from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.PageObject import PageObject


class AccountPage(PageObject):
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    id_account_select = 'accountSelect'
    value_number_account = 'number:1001'
    css_btn_deposit = '[ng-click="deposit()"]'
    css_btn_withdrawl = '[ng-click="withdrawl()"]'
    css_amount = '[placeholder="amount"]'
    value_deposit = '500'
    value_withdrawl = '300'
    class_btn_deposit = 'btn-default'
    class_btn_withdrawl = 'btn-default'
    btn_transactions = 'btn-lg'
    text_message_deposit = 'Deposit Successful'
    class_message_deposit = '[ng-show="message"]'
    text_message_withdrawl = 'Transaction successful'
    class_message_withdrawl = '[ng-show="message"]'

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)
        self.driver.get(self.url_account_page)

    def click_type_account(self):
        select = Select(self.driver.find_element(By.ID, self.id_account_select))
        select.select_by_value(self.value_number_account)

    def make_a_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_deposit).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_amount).send_keys(self.value_deposit)
        self.driver.find_element(By.CLASS_NAME, self.class_btn_deposit).click()

    def message_error_deposit(self):
        error_message = self.driver.find_element(By.CSS_SELECTOR, self.class_message_deposit).text
        return error_message == self.text_message_deposit

    def make_a_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_withdrawl).click()
        self.driver.find_element(By.CSS_SELECTOR, self.css_amount).send_keys(self.value_withdrawl)
        self.driver.find_element(By.CLASS_NAME, self.class_btn_withdrawl).click()

    def message_error_withdrawl(self):
        error_message = self.driver.find_element(By.CSS_SELECTOR, self.class_message_withdrawl).text
        return error_message == self.text_message_withdrawl

    def open_page_transactions(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_transactions).click()

    def is_url_account_page(self):
        return self.is_url(url=self.url_account_page)

