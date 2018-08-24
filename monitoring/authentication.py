import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable
)

from settings import (
    SENTRY_LOGIN_URL,
    SENTRY_USERNAME,
    SENTRY_PASSWORD
)


def log_in_to_sentry(driver):
    driver.get(SENTRY_LOGIN_URL)
    time.sleep(3)
    enter_email_and_password(driver)
    time.sleep(3)


def enter_email_and_password(driver):
    # Enter the email address.
    email = driver.wait.until(element_to_be_clickable((By.ID, "id_username")))
    email.clear()
    email.send_keys(SENTRY_USERNAME)

    # Enter the password.
    password = driver.wait.until(
        element_to_be_clickable((By.ID, "id_password"))
    )
    password.clear()
    password.send_keys(SENTRY_PASSWORD)
    time.sleep(2)

    # Click Log in button.
    driver.find_element(By.XPATH, '//button[text()="Continue"]').click()
    time.sleep(2)
