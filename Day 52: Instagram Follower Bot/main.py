from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv(".env")
IG_HANDLE = os.getenv("IG_HANDLE")
IG_PASSWORD = os.getenv("IG_PASSWORD")
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TARGET_ACCOUNT = "buzzfeedtasty"
IG_SIGN_IN = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self, sign_in_page):
        self.driver.get(sign_in_page)
        sleep(3)
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(IG_HANDLE)

        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        sleep(2)

    def find_followers(self, target_account):
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(target_account)
        sleep(2)
        account_page = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]')
        account_page.click()
        sleep(2)
        num_of_followers_string = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title")
        num_of_followers_int = int(num_of_followers_string.replace(",", ""))
        print(num_of_followers_int)
        sleep(2)
        open_followers_window = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        open_followers_window.click()
        sleep(2)
        followers_popup_window = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        followers_popup_window.click()
        sleep(5)

        # if number of followers is an odd number, add 1 to it to make it an even number
        if num_of_followers_int % 2 != 0:
            num_of_followers_int += 1

        # for i in range(int(num_of_followers_int/2)):
        for i in range(10):  # scroll 10 times for testing purposes
            # to see more followers beyond the first ~15, we need to scroll down in the popup (not the main webpage)
            # execute_script method synchronously executes JavaScript in the current window/frame
            # followers_window becomes the arguments[0] being referred to
            # scroll the top of the popup window down by the height of the modal/popup
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup_window)
            sleep(3)

    def follow(self):
        try:
            sleep(3)
            follow_buttons = self.driver.find_elements_by_css_selector("li button")
            # follow_buttons = follow_buttons[0:7]
            for button in follow_buttons:
                button.click()
                sleep(3)
                follow_buttons.remove(button)
            # follow_buttons.clear()
        except ElementClickInterceptedException:
            cancel_unfollow_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            cancel_unfollow_button.click()
            sleep(2)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(IG_SIGN_IN)
bot.find_followers(TARGET_ACCOUNT)
bot.follow()