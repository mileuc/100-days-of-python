from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from pprint import pprint
from time import sleep

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdD8aM3lDS0z7sapPIUkx9NFko5sZNwxBQAijdk6BusORRSZA/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept-Language": "en-US,en;q=0.5"
}


class DataEntry:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.all_listing_links = []
        self.all_listing_prices = []
        self.all_listing_addresses = []

    def get_listing_info(self, url, header):
        # use BeautifulSoup/Requests to scrape all listings from Zillow URL
        response = requests.get(url=url, headers=header)
        webpage_html = response.text
        # print(webpage_html)

        soup = BeautifulSoup(webpage_html, "html.parser")
        # print(soup.prettify())

        # create list of links from the scraped listings
        listing_link_tags = soup.select(selector=".list-card-info a")
        # print(listing_link_tags)
        # self.all_listing_links = [tag.get("href") for tag in listing_link_tags]
        for tag in listing_link_tags:
            href = tag.get("href")
            if "http" not in href:
                self.all_listing_links.append(f"https://www.zillow.com{href}")
            else:
                self.all_listing_links.append(href)
        pprint(self.all_listing_links)

        # create list of prices per month for all listings scraped
        listing_price_tags = soup.select(selector=".list-card-price")
        self.all_listing_prices = [tag.getText().split("+")[0].replace("/mo", "") for tag in listing_price_tags if "$" in tag.text]
        pprint(self.all_listing_prices)

        # create list of addresses for all listings scraped
        listing_address_tags = soup.select(selector=".list-card-info address")
        self.all_listing_addresses = [tag.getText().split(" | ")[-1] for tag in listing_address_tags]
        pprint(self.all_listing_addresses)

    def fill_form(self, url):
        # use selenium to fill in Google form and create a Google sheet from the form responses
        self.driver.get(url)

        list_length = len(self.all_listing_links)
        # all() returns true if all elements of a given iterable( List, Dictionary, Tuple, set, etc) are True
        if all(len(lst) == list_length for lst in [self.all_listing_prices, self.all_listing_addresses]):
            for index in range(list_length):
                self.driver.get(GOOGLE_FORM_URL)
                sleep(3)
                address_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                address_form.send_keys(self.all_listing_addresses[index])

                price_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price_form.send_keys(self.all_listing_prices[index])

                link_form = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link_form.send_keys(self.all_listing_links[index])

                submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
                submit_button.click()


data_entry_clerk = DataEntry(CHROME_DRIVER_PATH)
data_entry_clerk.get_listing_info(ZILLOW_URL, HEADER)
data_entry_clerk.fill_form(GOOGLE_FORM_URL)


# responses_tab = driver.find_element_by_xpath('//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
# responses_tab.click()
# sleep(3)
# create_sheet_icon = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div/div[1]')
# create_sheet_icon.click()
