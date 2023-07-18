from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.PageObject import PageObject

class OpenAccountPage(PageObject):

    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    id_user = 'userSelect'
    id_currency = 'currency'
    btn_process = '/html/body/div/div/div[2]/div/div[2]/div/div/form/button'
    user_name = 'Hermoine Granger'
    value = '1'
    currency = 'Dollar'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)
        self.driver.get(self.url_open_account)

    def click_btn_submit(self):
        botao = self.driver.find_element(By.XPATH, self.btn_process)
        botao.click()

    def click_select_customer_name(self):
        select = Select(self.driver.find_element(By.ID, self.id_user))
        select.select_by_visible_text(self.user_name)
        select.select_by_value(self.value)

    def select_currency(self):
        select = Select(self.driver.find_element(By.ID, self.id_currency))
        select.select_by_visible_text(self.currency)

    def is_url_open_account(self):
        return self.is_url(url=self.url_open_account)

