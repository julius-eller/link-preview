import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from .find_cookie_match import find_cookie_match
option = webdriver.ChromeOptions()
def make_screenshot (url, foldername, sitename) :
    relativeToFolder = foldername
    '''saves screenshot from url as {sitename}.png to foldername'''
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    option = webdriver.ChromeOptions()
    option.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=option)

    # set window size
    driver.set_window_size(1558, 854)
    try:
        driver.set_page_load_timeout(8)
        driver.get(url)
    except TimeoutException as ex:
        isrunning = 0
        print("Exception has been thrown. " + str(ex))
        driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
        driver.quit()
        return relativeToFolder + "/" + sitename + ".png"
    sleep(1)
   
    found_cookies = False
    # find all buttons in page
    buttons = driver.find_elements(By.TAG_NAME, "button")
    
    # get the text description or innerHTML of all buttons
    for button in buttons:
        if find_cookie_match(button.text):
            found_cookies = True
            #press button
            try:
                button.click()
            except ElementClickInterceptedException:
                continue
            #save link preview
            driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
            break
        else:
            print("No match: --" + button.text + " --")

    if found_cookies == False:
        print ("Checking role ")
        # also check role
        role_buttons = driver.find_elements(By.CSS_SELECTOR, "[role=button]")
        for button in role_buttons:
            print(button.text)
            if find_cookie_match(button.text):
                found_cookies = True
                #press button
                try:
                    button.click()
                except ElementClickInterceptedException:
                    continue
                #save link preview
                driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
                break
            else:
                print("No match: --" + button.text + " --")

    # find all elements with onclick attribute
    if found_cookies == False:
        print ("Checking xpath")
        elements = driver.find_elements(By.XPATH, "//*[@onclick]")
        for element in elements:
            if find_cookie_match(element.text):
                found_cookies = True
                #press button
                try:
                    element.click()
                except ElementClickInterceptedException:
                    continue
                #save link preview
                driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
                break
    if found_cookies == False:
        print ("Simple screenshot")
        driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
    driver.quit()
    return relativeToFolder + "/" + sitename + ".png"