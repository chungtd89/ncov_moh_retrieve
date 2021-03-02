# -*- coding: utf-8 -*-
import time
import csv
from function.browser import set_driver
from function.miscellaneous import raw_output


def retrieval():
    file = open("log/date.log", "r+")
    file.truncate()
    file.close()
    total_news = 0
    with open("log/browser.log", "r") as number:
        browser = number.readline()

    driver, browser = set_driver(browser)

    with open("log/browser.log", "w") as number:
        number.write(browser)

    driver.get("https://ncov.moh.gov.vn/en/web/guest/dong-thoi-gian")
    time_sleep = 3
    while 1:

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
            with open("log/date.log", "a") as log:
                log.write(header[i].text + "\n")
                total_news += 1
                print(header[i].text)
            with open('data/raw/vnCovid19raw.csv', mode='a+', encoding="utf-8", newline='') as t:
                t_writer = csv.writer(t, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                t_writer.writerow([header[i].text, content[i].text])
        if driver.find_element_by_link_text('Next').get_attribute("tabindex") == "-1":
            driver.quit()
            break
        driver.find_element_by_link_text('Next').click()
    print("Iterate through " + str(total_news) + ".")
    print("*Retrieve process completed! Check " + raw_output + " for raw file.*")
