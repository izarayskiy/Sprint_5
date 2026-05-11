from pathlib import Path

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import RegistrationLocators, LoginLocators, CreateAdLocators

BASE_URL = "https://qa-desk.education-services.ru/"


def test_unregistered_user_cant_create_ad(driver):
    """Незарегистрированный ползователь не может создать объявление"""
    driver.get(BASE_URL)
    driver.find_element(*RegistrationLocators.CREATE_ADD_BUTTON).click()

    wait = WebDriverWait(driver, 10)

    expected_url_part = "/login"
    expected_auth_modal_visible = True

    actual_url = driver.current_url
    auth_modal = wait.until(EC.visibility_of_element_located(LoginLocators.AUTH_MODAL))

    actual_auth_model_visible = auth_modal.is_displayed()

    assert expected_url_part in actual_url
    assert actual_auth_model_visible == expected_auth_modal_visible


def test_registered_user_can_create_ad(registered_driver):
    """Зарегистрированный пользователь может создать объявление"""
    driver = registered_driver["driver"]
    wait = WebDriverWait(driver, 10)
    image_path = Path("tests/files/test_image.jpg").resolve()
    ad_name = "Project Hail Mary 11389"
    ad_description = "Craft a microscale replica of the Hail Mary interstellar spacecraft as featured in the epic space movie."
    ad_price = "7500"

    create_ad_button = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.CREATE_ADD_BUTTON)
    )
    create_ad_button.click()

    wait.until(EC.visibility_of_element_located(CreateAdLocators.CREATE_AD_FORM))

    image_input = wait.until(
        EC.presence_of_element_located(CreateAdLocators.IMAGE_INPUT)
    )
    image_input.send_keys(str(image_path))

    name_input = wait.until(
        EC.visibility_of_element_located(CreateAdLocators.NAME_INPUT)
    )
    name_input.send_keys(ad_name)

    wait.until(
        EC.element_to_be_clickable(CreateAdLocators.CATEGORY_DROPDOWN_BUTTON)
    ).click()
    wait.until(
        EC.element_to_be_clickable(CreateAdLocators.HOBBY_CATEGORY_OPTION)
    ).click()

    used_condition_radio = wait.until(
        EC.element_to_be_clickable(CreateAdLocators.USED_CONDITION_CIRCLE)
    )
    used_condition_radio.click()

    wait.until(
        EC.element_to_be_clickable(CreateAdLocators.CITY_DROPDOWN_BUTTON)
    ).click()
    wait.until(
        EC.element_to_be_clickable(CreateAdLocators.NOVOSIBIRSK_CITY_OPTION)
    ).click()

    description_textarea = wait.until(
        EC.visibility_of_element_located(CreateAdLocators.DESCRIPTION_TEXTAREA)
    )
    description_textarea.send_keys(ad_description)

    price_input = wait.until(
        EC.visibility_of_element_located(CreateAdLocators.PRICE_INPUT)
    )
    price_input.send_keys(ad_price)

    wait.until(EC.element_to_be_clickable(CreateAdLocators.PUBLISH_BUTTON)).click()

    created_ad_title = wait.until(
        EC.visibility_of_element_located(
            CreateAdLocators.created_ad_title(ad_name)
        )
    ).text

    assert created_ad_title == ad_name
