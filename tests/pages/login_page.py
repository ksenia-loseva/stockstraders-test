from time import sleep

from selenium.webdriver.common.by import By


from tests.pages.base_page import BasePage

class LoginPage(BasePage):

    # Searching elements by id or name is preferable to searching by XPATH, as XPATH is slower, and more brittle.
    # In this case, id and name tags are generated dynamically, so there is no way to locate this input by id or name.
    # This can be solved by adding a convention that all interactable items must have unique non-generated ids
    email_input = By.XPATH, './/input[@type="email"]'
    password_input = By.XPATH, './/input[@type="password"]'

    continue_button = By.XPATH, './/ion-button//ion-label[@translate="login.Continue"]'

    allow_cookies_button = By.XPATH, './/ion-button[@translate="cookies.allow"]'


    # This is a waste of time in practice, if every test has to click this button.
    # It also adds a problem with elements becoming non-interactable for a short period of time after the button is clicked,
    # despite elements being enabled and visible.
    # We waste at least 5 seconds here, and fail if the pop-up doesn't appear.
    # It should be disabled on test envs.
    def allow_cookies(self):
        self.find(self.allow_cookies_button).click()
        sleep(1)

    def enter_email(self, email):
        inp = self.find(self.email_input)
        inp.send_keys(email)


    def enter_password(self, password):
        self.find(self.password_input).send_keys(password)

    def click_continue(self):
        self.find(self.continue_button).click()