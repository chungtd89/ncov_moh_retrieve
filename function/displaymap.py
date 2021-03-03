from function.browser import set_driver
import os


def display():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__).replace("function", "map"), "map.html"))
    with open("log/browser.log", "r") as number:
        browser = number.readline()

    driver, browser = set_driver(browser)

    driver.get(path)
