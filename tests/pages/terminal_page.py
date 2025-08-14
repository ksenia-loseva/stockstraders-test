from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.pages.base_page import BasePage


class TerminalPage(BasePage):

    deposit_button = By.XPATH, '//ion-button//ion-label[@translate="accounts.operations.deposit"]'
    balance = By.XPATH, '//div[div[@translate="accounts.props.balance"]]/div'

    def check_deposit_button_present(self):
        self.wait_for_element(ec.presence_of_element_located(self.deposit_button), timeout=15)

    def check_balance_present(self):
        self.wait_for_element(ec.presence_of_element_located(self.balance), timeout=15)
