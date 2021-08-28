from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv("./.env")
TWITTER_HANDLE = os.getenv("TWITTER_HANDLE")
PASSWORD = os.getenv("PASSWORD")

PROMISED_DOWNLOAD_SPD = 300   # in mbps
PROMISED_UPLOAD_SPD = 20
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/login"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        start_button = self.driver.find_element_by_css_selector(".start-button a")
        start_button.click()
        sleep(45)

        self.down = self.driver.find_element_by_css_selector(".result-item-download .download-speed").text
        print(self.down)

        self.up = self.driver.find_element_by_css_selector(".result-item-upload .upload-speed").text
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_LOGIN_URL)
        username_input = self.driver.find_element_by_name("session[username_or_email]")
        username_input.send_keys(TWITTER_HANDLE)
        password_input = self.driver.find_element_by_name("session[password]")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        sleep(3)
        tweet_form = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_form.send_keys(f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I "
                             f"pay for {PROMISED_DOWNLOAD_SPD}down/{PROMISED_UPLOAD_SPD}up? #100DaysOfCode")
        tweet_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet_button.click()

        sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
