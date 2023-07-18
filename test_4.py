import time

from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage


class Test4:
    def test_make_a_deposit(self, open_home_page):
        open_home_page.click_btn_customer_login()
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)
        login_customer_page.login_customer()
        select_type_account = AccountPage(driver=login_customer_page.driver)
        assert select_type_account.is_url_account_page(), 'URL não encontrada!'
        select_type_account.click_type_account()
        effectue_deposit = AccountPage(driver=select_type_account.driver)
        effectue_deposit.make_a_deposit()
        assert effectue_deposit.message_error_deposit(), 'Menssagem de erro não encontrada'






