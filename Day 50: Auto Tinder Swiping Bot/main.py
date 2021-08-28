from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv("./.env")
FB_LOGIN = os.getenv("FB_LOGIN")
FB_PASSWORD = os.getenv("FB_PASSWORD")
PHONE = os.getenv("PHONE")
TINDER_URL = "https://tinder.com"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(TINDER_URL)

# log in button
login_button = driver.find_element_by_xpath('//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

# privacy consent button
privacy_consent = driver.find_element_by_xpath('//*[@id="q-84965404"]/div/div[2]/div/div/div[1]/button')
privacy_consent.click()

time.sleep(3)

# log in with facebook
to_fb_login = driver.find_element_by_xpath('//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/div[2]/button')
to_fb_login.click()

# switch windows to the facebook login page that pops up
# print(driver.window_handles)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(f"Switched windows to {driver.title}")  # verify that the facebook login window is the current target

# fill in facebook login form
fb_email_form = driver.find_element_by_name("email")
fb_email_form.send_keys(FB_LOGIN)
fb_password_form = driver.find_element_by_name("pass")
fb_password_form.send_keys(FB_PASSWORD)
fb_password_form.send_keys(Keys.ENTER)
# fb_login_button = driver.find_element_by_name("login")
# fb_login_button.click()
time.sleep(3)
# fb_confirm_button = driver.find_element_by_name("__CONFIRM__")
# fb_confirm_button.click()

# switch back to base window
time.sleep(10)
driver.switch_to.window(base_window)
print(f"Switched windows to {driver.title}")

# give enough time to bypass manual verification
time.sleep(30)
# fill phone number and continue
phone_form = driver.find_element_by_name("phone_number")
phone_form.send_keys(PHONE)
time.sleep(5)
continue_button = driver.find_element_by_xpath('//*[@id="q-1813346480"]/div/div/div[1]/button')
continue_button.click()

# give enough time to receive confirmation code and manually enter it

# Tinder free tier only allows 100 "Likes" per day - swipe 100 times
for n in range(100):
    time.sleep(1)  # wait a second between swipes

    try:
        # find swipe left button by XPath
        swipe_left_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button")
        swipe_left_button.click()
    # cases where a Match occurs and a pop-up overlaps the swipe buttons
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        # cases where the swipe buttons have not yet loaded - wait another two seconds before trying again
        except NoSuchElementException:
            time.sleep(2)

driver.quit()

