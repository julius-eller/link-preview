"""Application entry point."""
from scraper import scrape_page_metadata
import matcher.find_cookie_match as find_cookie_match
from config import URL
from selenium import webdriver
from time import sleep
import os
import json
import shutil

from .screenshot import make_screenshot

def main(url):
    scrape = scrape_page_metadata(url)
    description = scrape['description']
    sitename = scrape['sitename']
    title = scrape['title']
    print (description)
    print (sitename)
    print (title)
    sleep(1)

    foldername = sitename

    dirpath = foldername
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(dirpath)
    os.mkdir(foldername)

    # save description
    
    with open(foldername + '/description.json', 'w') as f:
        # save title/ sitename and description
        if description is not None:
            if title: 
                data = {"title": title, "description": description}
                json.dump(data, f)
            else:
                data = {"title": sitename, "description": description}
                json.dump(data, f)
    print(make_screenshot(url, foldername, sitename))
   
main("https://figma.com")

