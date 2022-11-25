from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import winsound
from os import walk



list_link = []
count = 1
tag = input('Тег: ')
link = f'https://www.vidsplay.com/tag/{tag}/'
count_download = 0

def waitUntilDownloadCompleted(driver, maxTime=600):
    driver.execute_script("window.open()")
    # switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    # navigate to chrome downloads
    driver.get('chrome://downloads')
    # define the endTime
    endTime = time.time() + maxTime
    while True:
        try:
            # get the download percentage
            downloadPercentage = driver.execute_script(
                "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
            # check if downloadPercentage is 100 (otherwise the script will keep waiting)
            if downloadPercentage == 100:
                # exit the method once it's completed
                return downloadPercentage
        except:
            pass
        # wait for 1 second before checking the percentage next time
        time.sleep(1)
        # exit method if the download not completed with in MaxTime.
        if time.time() > endTime:
            break

def links(br):
    link = []
    elements = br.find_elements(By.CSS_SELECTOR,'.video-title')
    for el in elements:
        link.append(el.get_attribute('href'))
    return link
    

try:
    browser = webdriver.Chrome()
    browser.get(link)

    while True:
        
        list_link.extend(links(browser))
        element = browser.find_element(By.CSS_SELECTOR,".inactive.show-for-medium .fa-chevron-right")
        element.click()
        
finally:
    browser.quit()
    
    for el in list_link:
        try:
            browser = webdriver.Chrome()
            browser.get(el)
            element = browser.find_element(By.CSS_SELECTOR, "a[download]")
            name_file = element.get_attribute('href').split('/')[-1].split('%')[0]
            download_dir = 'D:\\Python\\moviepy\\res\\clip'
            list_dir_file = iter(walk(download_dir))
            list_file = next(list_dir_file)[2]
            if name_file not in str(list_file):
                element.click()
                waitUntilDownloadCompleted(browser, 120)
                time.sleep(2)
                count_download += 1
        finally:
            browser.quit()
         
    
    





