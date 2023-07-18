import pytest

from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.CustomersPage import CustomersPage
from Pages.HomePage import HomePage
from Pages.OpenAccountPage import OpenAccountPage
from Pages.ListTxPage import ListTxPage


@pytest.fixture()
def open_home_page():
    home_page = HomePage()
    yield home_page

@pytest.fixture()
def open_new_account(open_home_page):
    new_account = OpenAccountPage()
    yield new_account

@pytest.fixture()
def open_customers_page(open_home_page):
    delete_customers = CustomersPage
    yield delete_customers
@pytest.fixture()
def page_login(open_home_page):
    is_login = CustomerLoginPage()
    yield is_login

@pytest.fixture()
def make_deposit(page_login):
    is_deposit = AccountPage()
    yield is_deposit

@pytest.fixture()
def make_withdrawl(page_login):
    is_withdrawl = AccountPage()
    yield is_withdrawl

@pytest.fixture()
def del_history_transactions(page_login):
    del_history = ListTxPage()
    yield del_history


