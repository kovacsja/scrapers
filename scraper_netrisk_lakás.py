from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

WEBDRIVER_PATH:str = "chromedriver"
url:str = "https://www.netrisk.hu/lakasbiztositas.html"

browser = webdriver.Chrome(WEBDRIVER_PATH)
browser.get(url)

browser.find_element_by_link_text("nrx-next-step").click()
sleep(3)
browser.find_element_by_class_name("nrx-next-step").click()