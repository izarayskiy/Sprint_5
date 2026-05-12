from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import RegistrationLocators


class TestLogout:
    def test_user_can_logout(self, registered_driver):
        wait = WebDriverWait(registered_driver["driver"], 10)
        expected_login_button_visible = True

        logout_button = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        login_button = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
            )
        )

        actual_login_button_visible = login_button.is_displayed()

        assert actual_login_button_visible == expected_login_button_visible
