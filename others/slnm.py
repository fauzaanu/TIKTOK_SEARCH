import chromedriver_autoinstaller
from selenium.webdriver.support import expected_conditions as xEC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def browsing(url):
    # Requests cannot do this as tiktok loads the videos a bit later... Thats why Selenium is used.

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    return driver


def sel_search(tag, driver):
    # Search for a tag in the html
    links = WebDriverWait(driver, 1000).until(xEC.presence_of_all_elements_located(
        (By.XPATH, f"//{tag}",)))

    return links


def user_control():
    x = input("Solve any captcha and load more as needed. Then press any key")
