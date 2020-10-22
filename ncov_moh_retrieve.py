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

driver = webdriver.Firefox(executable_path=r'/home/jt/Desktop/chotot/geckodriver')
driver.get("https://ncov.moh.gov.vn/en/web/guest/dong-thoi-gian")

stop = 0
while (stop != 1):

    time.sleep(3)

    elems_head = driver.find_elements_by_class_name('timeline-head')
    elems_content = driver.find_elements_by_class_name('timeline-content')

    elems_len = len (elems_head)

    for i in range(elems_len):
        print (elems_head[i].text)
        print (elems_content[i].text)
        
        with open('vnncovfile.csv', mode='a+') as f:
            fwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fwrite.writerow([elems_head[i].text, elems_content[i].text])

    if (driver.find_element_by_link_text('Next').get_attribute("tabindex") == -1):
        stop = 1
        driver.close()
        break
        
    driver.find_element_by_link_text('Next').click()
