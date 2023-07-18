from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject

class ListTxPage(PageObject):
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    btn_reset = '[ng-click="reset()"]'
    text_btn_reset = 'Reset'
    btn_back = '[ng-click="back()]'
    text_btn_back = 'Back'

    def __init__(self, driver):
        super(ListTxPage, self).__init__(driver=driver)
        self.driver.get(self.url_transactions)

    def del_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_reset).click()

    def is_list_tx(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.btn_reset).text == self.text_btn_reset

    def is_url_list_tx(self):
        return self.is_url(url=self.url_transactions)

