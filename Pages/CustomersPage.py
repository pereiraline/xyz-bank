from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CustomersPage(PageObject):
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    user_name = 'Hermoine'
    search_customers = '[placeholder="Search Customer"]'
    btn_delete = '[ng-click="deleteCust(cust)"]'

    def __init__(self, driver):
        super(CustomersPage,self).__init__(driver=driver)
        self.driver.get(self.url_customers)

    def delete_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_customers).send_keys(self.user_name)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_delete).click()

    def is_url_customers_page(self):
        return self.is_url(url=self.url_customers)