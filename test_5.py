import time

from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage


class Test5:
    def test_make_a_withdrawl(self, open_home_page):
        open_home_page.click_btn_customer_login()
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)
        login_customer_page.login_customer()
        select_type_account = AccountPage(driver=login_customer_page.driver)
        assert select_type_account.is_url_account_page(), 'URL não encontrada!'
        select_type_account.click_type_account()
        effectue_withdrawl = AccountPage(driver=select_type_account.driver)
        effectue_withdrawl.make_a_withdrawl()
        assert effectue_withdrawl.message_error_withdrawl(), 'Menssagem de erro não encontrada'
