from selenium import webdriver
# custom exceptions raised when element cannot be found
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import time
from dotenv import load_dotenv

load_dotenv("./.env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SEARCH_URL = "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Calgary%2C%20Alberta%2C%20Canada&geoId=102199904&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
# "https://www.linkedin.com/login"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(SEARCH_URL)

# go to sign in page
to_sign_in_page_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
to_sign_in_page_button.click()

time.sleep(2)   # wait for page to fully load

# fill in forms and sign in
email_form = driver.find_element_by_name("session_key")
email_form.send_keys(EMAIL)
password_form = driver.find_element_by_name("session_password")
password_form.send_keys(PASSWORD)
sign_in_button = driver.find_element_by_css_selector(".login__form_action_container  button")
sign_in_button.click()

# apply for the first job that only requires you to enter your phone number or save all jobs and follow the company
posting_link_buttons = driver.find_elements_by_css_selector(".job-card-container")
num_of_listings =  len(posting_link_buttons)
# print(posting_link_buttons)

for index in range(num_of_listings):
    posting_link_buttons = driver.find_elements_by_css_selector(".job-card-container")
    posting_link = posting_link_buttons[index]
    posting_link.click()
    time.sleep(3)
    try:
        save_button = driver.find_element_by_css_selector(".jobs-box .jobs-save-button")
        save_button.click()
        # issue - "Follow" button doesn't exist until you scroll to it
        # alternative: go to company page to follow, then go back
        to_company_page = driver.find_element_by_css_selector(".jobs-details-top-card__company-info "
                                                              ".jobs-details-top-card__company-url")
        to_company_page.click()
        time.sleep(5)
        # using this general org-top-card-primary-actions__action class because i'm trying to click button regardless of follow/unfollow
        # use org-company-follow-button class if trying to just click follow
        try:
            follow_button = driver.find_element_by_css_selector(".org-company-follow-button")
            follow_button.click()
        except ElementClickInterceptedException:
            print("Button not found, skipped.")
        finally:
            driver.back()

        #Wait for Apply button to load
        # apply_button = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "jobs-apply-button")))
        # if apply_button.text == "Easy Apply":
        #     apply_to_job()
    except NoSuchElementException:
        print("Button not found, skipped.")
        pass



