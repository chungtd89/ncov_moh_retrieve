'''
https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python
https://requests.readthedocs.io/en/master/
https://requests.readthedocs.io/projects/requests-html/en/latest/
https://nha.chotot.com/
https://selenium-python.readthedocs.io/getting-started.html
https://www.techbeamers.com/locate-elements-selenium-python/
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Firefox(executable_path=r'D:\GitHub\ncov_moh_retrieve\geckodriver.exe')
driver.get("https://ncov.moh.gov.vn/en/web/guest/dong-thoi-gian")

time_sleep = 3
while (1):

    time.sleep(time_sleep)

    elems_head = driver.find_elements_by_class_name('timeline-head')
    elems_content = driver.find_elements_by_class_name('timeline-content')

    elems_len = len(elems_head)

    for i in range(elems_len):
        #print (elems_head[i].text)
        #print (elems_content[i].text)

        with open('vnCovid19Summary.csv', mode='a+', encoding="utf-8", newline='') as f:
            fwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fwrite.writerow([str(elems_head[i].text), str(elems_content[i].text)])

    if int(driver.find_element_by_link_text('Next').get_attribute("tabindex")) == -1:
        driver.quit()
        break

    driver.find_element_by_link_text('Next').click()