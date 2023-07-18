from Pages.AddCustomerPage import AddCustomerPage
from Pages.ManagerPage import ManagerPage


class Test1:

    def test_add_new_customer(self, open_home_page):

        open_home_page.click_btn_bank_manager_login()
        assert open_home_page.is_url_home_page(), "Página não encontrada"

        manager_page = ManagerPage(driver=open_home_page.driver)
        manager_page.click_tab_add_customer()
        add_customer_page = AddCustomerPage(driver=manager_page.driver)
        add_customer_page.add_costumer()






