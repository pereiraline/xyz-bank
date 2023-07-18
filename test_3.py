import time

from Pages.CustomersPage import CustomersPage
from Pages.ManagerPage import ManagerPage


class Test3:

    def test_delete_user(self, open_home_page):
        open_home_page.click_btn_bank_manager_login()
        manager_page = ManagerPage(driver=open_home_page.driver)
        manager_page.click_tab_customer()
        customers_page = CustomersPage(driver=manager_page.driver)
        assert customers_page.is_url_customers_page()
        customers_page.delete_customer()
