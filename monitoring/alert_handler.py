import time

SENTRY_PROJECT_NAME = ""


def alert_for_new_unresolved_issues(driver, current_url):
    navigate_to_project(driver, current_url)
    unresolved_issue_number = get_latest_unresolved_issue_number(driver)
    sentr_project_url = get_project_url(current_url)


def navigate_to_project(driver, current_url):
    SENTRY_PROJECT_URL = f"{current_url}{SENTRY_PROJECT_NAME}"
    driver.get(SENTRY_PROJECT_URL)
    time.sleep(2)


def get_project_url(current_url):
    return f"{current_url}{SENTRY_PROJECT_NAME}"


def get_latest_unresolved_issue_number(driver):
    return driver.find_element_by_class_name("query-count-value").text
