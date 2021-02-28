from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def set_driver(browser):
    options = ["1", "2", "3"]
    while browser != "exit":
        if browser not in options:
            browser = input(
                "Enter number of your browser: "
                "\n1. Chrome"
                "\n2. Edge"
                "\n3. Firefox"
                "\nYour choice: "
            )
        if browser == "1":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            return driver, browser
        elif browser == "2":
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            return driver, browser
        elif browser == "3":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return driver, browser
        else:
            print("Valid value only in range 1->3")
