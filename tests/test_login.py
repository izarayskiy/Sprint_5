from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import RegistrationLocators


def test_user_can_login(registered_driver_with_logout):
    """Пользователь может совершить login"""
    wait = WebDriverWait(registered_driver_with_logout["driver"], 10)
    expected_profile_name = True
    expected_avatar_visible = True

    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
        )
    ).click()

    registered_driver_with_logout["driver"].find_element(
        *RegistrationLocators.EMAIL_INPUT
    ).send_keys(registered_driver_with_logout["email"])
    registered_driver_with_logout["driver"].find_element(
        *RegistrationLocators.PASSWORD_INPUT
    ).send_keys(registered_driver_with_logout["password"])
    registered_driver_with_logout["driver"].find_element(
        *RegistrationLocators.LOGIN_BUTTON
    ).click()

    profile_name = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.PROFILE_NAME)
    ).text
    avatar_button = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.AVATAR_BUTTON)
    )

    actual_profile_name = "User" in profile_name
    actual_avatar_visible = avatar_button.is_displayed()

    assert actual_profile_name == expected_profile_name
    assert actual_avatar_visible == expected_avatar_visible
