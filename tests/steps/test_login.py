import os
from dotenv import load_dotenv
from pytest_bdd import scenario, given, when, then

from tests.pages.login_page import LoginPage
from tests.pages.terminal_page import TerminalPage


@scenario('../features/login.feature', 'Successful Login')
def test_successful_login(driver):
    pass

@given("I am a registered user", target_fixture="credentials")
def get_user_credentials():
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return email, password


@when("I go to login page", target_fixture="login_page")
def login_page(driver):
    driver.get('https://stockstrader.roboforex.com/login')
    page = LoginPage(driver)
    page.allow_cookies()
    return LoginPage(driver)


@when("I enter email")
def enter_email(login_page, credentials):
    login_page.enter_email(credentials[0])


@when("I enter password")
def enter_password(login_page, credentials):
    login_page.enter_password(credentials[1])


@when("I click Continue button")
def click_continue(login_page):
    login_page.click_continue()


@then("trading interface should load")
def check_interface(driver):
    page = TerminalPage(driver)
    page.check_balance_present()
    page.check_deposit_button_present()