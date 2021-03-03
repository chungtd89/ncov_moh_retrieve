# -*- coding: utf-8 -*-
import time
from function.browser import set_driver
from function.miscellaneous import raw_output
from pandas import DataFrame


def retrieval():
    file = open("log/date.log", "a+")
    file.truncate()
    total_news = 0
    with open("log/browser.log", "r") as number:
        browser = number.readline()

    driver, browser = set_driver(browser)

    with open("log/browser.log", "w") as number:
        number.write(browser)

    driver.get("https://ncov.moh.gov.vn/en/web/guest/dong-thoi-gian")
    time_sleep = 3
    header_final = []
    content_final = []
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
        for i in range(len(header)):
            header_final.append(header[i].text)
            content_final.append(content[i].text)
            file.write(header[i].text)
            total_news += 1
        if driver.find_element_by_link_text('Next').get_attribute("tabindex") == "-1":
            driver.quit()
            file.close()
            break
        driver.find_element_by_link_text('Next').click()
    DataFrame(zip(header_final, content_final)).to_csv('data/raw/vnCovid19raw.csv', index=False, header=False)
    print("Iterate through " + str(total_news) + " news.")
    print("*Retrieve process completed! Check " + raw_output + " for raw file.*")
