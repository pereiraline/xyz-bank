

from Pages.ManagerPage import ManagerPage
from Pages.OpenAccountPage import OpenAccountPage


class Test2:
    def test_open_new_account(self, open_home_page):

        open_home_page.click_btn_bank_manager_login()
        manager_page = ManagerPage(driver=open_home_page.driver)
        manager_page.click_tab_open_account()
        open_account_page = OpenAccountPage(driver=manager_page.driver)
        assert open_account_page.is_url_open_account(), "Página não encontrada!"

        open_account_page.click_select_customer_name()
        open_account_page.select_currency()
        open_account_page.click_btn_submit()

