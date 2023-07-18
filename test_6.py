

from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.ListTxPage import ListTxPage


class Test6:

    def test_delete_transactions(self, open_home_page):
        open_home_page.click_btn_customer_login()
        name_customer = CustomerLoginPage(driver=open_home_page.driver)
        name_customer.login_customer()
        efecctue_login = CustomerLoginPage(driver=name_customer.driver)
        efecctue_login.login_customer()
        open_page_transactions = AccountPage(driver=efecctue_login.driver)
        open_page_transactions.open_page_transactions()
        verify_transactions = ListTxPage(driver=open_page_transactions.driver)
        assert verify_transactions.is_list_tx(), 'Botão Reset não localizado!'
        assert verify_transactions.is_url_list_tx(), 'URL da página não localizado!'
        verify_transactions.del_list()

