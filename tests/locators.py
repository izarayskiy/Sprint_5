from selenium.webdriver.common.by import By


class RegistrationLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Вход и регистрация']",
    )
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")
    PROFILE_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    ERROR_TEXT = (By.XPATH, "//span[normalize-space()='Ошибка']")
    EMAIL_ERROR_FIELD = (
        By.XPATH,
        "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]",
    )
    PASSWORD_ERROR_FIELD = (
        By.XPATH,
        "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]",
    )
    SUBMIT_PASSWORD_ERROR_FIELD = (
        By.XPATH,
        "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]",
    )
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    CREATE_ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Разместить объявление']",
    )


class LoginLocators:
    AUTH_MODAL = (
        By.XPATH,
        "//form[.//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']]",
    )


class CreateAdLocators:

    @staticmethod
    def created_ad_title(ad_name):
        return (
            By.XPATH,
            f"//h2[normalize-space()='{ad_name}']",
        )

    CREATE_AD_FORM = (
        By.XPATH,
        "//form[.//input[@name='img1'] and .//input[@name='name']]",
    )
    IMAGE_INPUT = (By.NAME, "img1")
    NAME_INPUT = (By.NAME, "name")
    CATEGORY_INPUT = (By.NAME, "category")
    HOBBY_CATEGORY_OPTION = (
        By.XPATH,
        "//button[.//span[normalize-space()='Хобби']]",
    )
    CATEGORY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='category']/following-sibling::button",
    )
    USED_CONDITION_CIRCLE = (
        By.XPATH,
        "//label[normalize-space()='Б/У']/preceding-sibling::div",
    )
    CITY_INPUT = (By.NAME, "city")
    CITY_DROPDOWN_BUTTON = (
        By.XPATH,
        "//input[@name='city']/following-sibling::button",
    )
    NOVOSIBIRSK_CITY_OPTION = (
        By.XPATH,
        "//button[.//span[normalize-space()='Новосибирск']]",
    )
    DESCRIPTION_TEXTAREA = (
        By.CSS_SELECTOR,
        "textarea[name='description']",
    )
    PRICE_INPUT = (
        By.NAME,
        "price",
    )
    PUBLISH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Опубликовать']",
    )
