from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import datetime as dt

def isnull_(elem):
    if elem == None:
        return None
    else:
        return elem.text.strip()

WEBDRIVER_PATH:str = "chromedriver"
url:str = "https://ingatlan.com/lista/elado+lakas+budapest"
browser = webdriver.Chrome(WEBDRIVER_PATH) #letöltött chrome driver path
browser.implicitly_wait(15)

browser.get(url)    

soup = BeautifulSoup(browser.page_source, "lxml")

def parse_listings(bsoup: BeautifulSoup) -> pd.DataFrame:     
    listings = bsoup.find_all("div", class_="listing")
    
    d = []
    
    for lst in listings:
        ids = lst.find("button")["data-id"]
        price = lst.find("div", class_="price")
        pricesqm = lst.find("div", class_="price--sqm")
        addr = lst.find("div", class_="listing__address")
        area = lst.find("div", class_="listing__data--area-size")
        balc = lst.find("div", class_="listing__data--balcony-size")
        rooms = lst.find("div", class_="listing__data--room-count")
        link = lst.find("a", class_="listing__link")["href"]
        
        d.append([
            ids,
            price.text.strip(), 
            pricesqm.text.strip(), 
            addr.text.strip(), 
            area.text.strip(), 
            isnull_(balc), 
            rooms.text.strip(), 
            link, 
            dt.datetime.now().isoformat()])

    return pd.DataFrame(d, columns=["id", "price", "price_sqm", "address", "area", "balcony", "rooms", "listing_link", "datetime"])

# TODO: befejezni a részletek feldolgozását
def parse_details(bsoup:BeautifulSoup) -> pd.DataFrame:
    det = bsoup.find("div", class_="card details")
    
    d:list[str] = []
    return pd.DataFrame(d, columns=[])
    
parse_listings(soup).to_csv("minta5.csv")
    
browser.close()