from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome

from authentication import log_in_to_sentry
from alert_handler import alert_for_new_unresolved_issues


def main():
    driver = Chrome()
    driver.wait = WebDriverWait(driver, 3)
    log_in_to_sentry(driver)
    alert_for_new_unresolved_issues(driver, driver.current_url)


if __name__ == '__main__':
    main()
