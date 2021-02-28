import time
import csv
from function.browser import set_driver


def retrieval():
    with open("browser/browser.log", "r", encoding="utf8") as number:
        browser = number.readline()

    driver, browser = set_driver(browser)

    with open("browser/browser.log", "w", encoding="utf8") as number:
        number.write(browser)

    driver.get("https://ncov.moh.gov.vn/en/web/guest/dong-thoi-gian")
    time_sleep = 3
    while True:

        time.sleep(time_sleep)
        header = driver.find_elements_by_class_name('timeline-head')
        content = driver.find_elements_by_class_name('timeline-content')
        """
        brief_list = []
        for con in content:
            brief_tag = con.find_element_by_tag_name('p')
            brief_list.append(brief_tag.find_element_by_xpath('./following-sibling::p'))
        """
        elem_len = len(header)
        for i in range(elem_len):
            print(header[i].text)
            print()
            with open('vnCovid19Summary.csv', mode='a+', encoding="utf-8", newline='') as target:
                writer = csv.writer(target, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(content[i].text), str(content[i].text)])
        if driver.find_element_by_link_text('Next').get_attribute("tabindex") == "-1":
            driver.quit()
            break
        driver.find_element_by_link_text('Next').click()
