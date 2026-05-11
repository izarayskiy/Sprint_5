from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import RegistrationLocators


def test_user_can_register_with_new_email(registered_driver):
    """Пользователь может зарегистрироваться с валидным email и паролем"""

    wait = WebDriverWait(registered_driver["driver"], 10)
    expected_profile_name = True
    expected_avatar_visible = True

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


def test_user_cant_register_with_bad_email(fail_registered_driver):
    """Пользователь не может зарегистрироваться с невалидным email"""

    wait = WebDriverWait(fail_registered_driver, 10)
    expected_error_text = "Ошибка"
    expected_email_error = True
    expected_password_error = True
    expected_submit_password_error = True

    email_error_field = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_FIELD)
    )
    password_error_field = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR_FIELD)
    )
    submit_password_error_field = wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.SUBMIT_PASSWORD_ERROR_FIELD
        )
    )
    error_text = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.ERROR_TEXT)
    ).text

    actual_error_text = error_text
    actual_email_error = email_error_field.is_displayed()
    actual_password_error = password_error_field.is_displayed()
    actual_submit_password_error = submit_password_error_field.is_displayed()

    assert actual_error_text == expected_error_text
    assert actual_email_error == expected_email_error
    assert actual_password_error == expected_password_error
    assert actual_submit_password_error == expected_submit_password_error


def test_registered_already_user(registered_driver_with_already_user):
    """Регистрация уже существующего пользователя"""
    wait = WebDriverWait(registered_driver_with_already_user, 10)
    expected_error_text = "Ошибка"
    expected_email_error = True
    expected_password_error = True
    expected_submit_password_error = True

    email_error_field = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR_FIELD)
    )
    password_error_field = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR_FIELD)
    )
    submit_password_error_field = wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.SUBMIT_PASSWORD_ERROR_FIELD
        )
    )
    error_text = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.ERROR_TEXT)
    ).text

    actual_error_text = error_text
    actual_email_error = email_error_field.is_displayed()
    actual_password_error = password_error_field.is_displayed()
    actual_submit_password_error = submit_password_error_field.is_displayed()

    assert actual_error_text == expected_error_text
    assert actual_email_error == expected_email_error
    assert actual_password_error == expected_password_error
    assert actual_submit_password_error == expected_submit_password_error
