from time import time

import pytest
from selenium import webdriver

from tests.locators import RegistrationLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.data import BASE_URL, BAD_USER_EMAIL, USER_PASSWORD


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def user_email():
    return f"user_{int(time() * 100)}@projecthailmary.space"


@pytest.fixture
def registered_driver(driver, user_email):
    """Регистрация пользователя"""
    driver.get(BASE_URL)

    driver.find_element(*RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
    driver.find_element(*RegistrationLocators.SUBMIT_PASSWORD_INPUT).send_keys(
        USER_PASSWORD
    )
    driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(RegistrationLocators.PROFILE_NAME))

    return {
        "driver": driver,
        "email": user_email,
        "password": USER_PASSWORD,
    }


@pytest.fixture
def fail_registered_driver(driver):
    """Регистрация пользователя c email не по маске  *******@*******.***"""
    driver.get(BASE_URL)

    driver.find_element(*RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(BAD_USER_EMAIL)
    driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    return driver


@pytest.fixture
def registered_driver_with_logout(driver, user_email):
    """Зарегистрирован новый пользователь. Совершен logout"""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    driver.find_element(*RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
    driver.find_element(*RegistrationLocators.SUBMIT_PASSWORD_INPUT).send_keys(
        USER_PASSWORD
    )
    driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    wait.until(
        EC.visibility_of_element_located(RegistrationLocators.LOGOUT_BUTTON)
    ).click()

    return {
        "driver": driver,
        "email": user_email,
        "password": USER_PASSWORD,
    }


@pytest.fixture
def registered_driver_with_already_user(registered_driver_with_logout):
    driver = registered_driver_with_logout["driver"]
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
        )
    ).click()

    driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(
        registered_driver_with_logout["email"]
    )
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(
        registered_driver_with_logout["password"]
    )
    driver.find_element(*RegistrationLocators.SUBMIT_PASSWORD_INPUT).send_keys(
        registered_driver_with_logout["password"]
    )
    driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

    return driver
