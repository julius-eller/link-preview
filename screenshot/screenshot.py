import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from .find_cookie_match import find_cookie_match
option = webdriver.ChromeOptions()
def make_screenshot (url, foldername, sitename) :
    relativeToFolder = foldername
    '''saves screenshot from url as {sitename}.png to foldername'''
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    # Configure the driver and options based on your browser and machine
    # This might take a bit of googling to find the correct settings
    # currently I am using Brave Browser on Mac M1 Pro
    option = webdriver.ChromeOptions()
    option.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    # This hides a banner that would pop up otherwise
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=option)

    # set window size (https://yizeng.me/2014/02/23/how-to-get-window-size-resize-or-maximize-window-using-selenium-webdriver/#heading-python)
    driver.set_window_size(1558, 854)
    try:
        # set page load timeout
        driver.set_page_load_timeout(8)
        driver.get(url)
    except TimeoutException as ex:
        print("Exception has been thrown. " + str(ex))
        driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
        driver.quit()
        return relativeToFolder + "/" + sitename + ".png"
    sleep(1)
    button = find_cookie_match(driver)
    if button != False:
        try:
            button.click()
            sleep(1)
        except ElementClickInterceptedException:
            print("Couldn't click the cookie banner because something is in the way.")
    driver.get_screenshot_as_file(relativeToFolder + "/" + sitename + ".png")
    driver.quit()
    return relativeToFolder + "/" + sitename + ".png"