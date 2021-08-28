from selenium import webdriver
from time import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
five_secs = time() + 5
timeout = time() + (60 * 5)  # 5 minutes from now

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

cookie_button = driver.find_element_by_id("cookie")

upgrades_divs = driver.find_elements_by_css_selector("#store div")
upgrade_ids = [div.get_attribute("id") for div in upgrades_divs]
print(upgrade_ids)

# click on cookie
game_on = True
while game_on:
    cookie_button.click()

    if time() > five_secs:
        # convert b tag to an int price
        upgrade_b_tags = driver.find_elements_by_css_selector("#store b")
        upgrade_split_labels = [tag.text.split(" ") for tag in upgrade_b_tags if tag.text != ""]
        print(upgrade_split_labels)

        # grab last index in list with split items (which is the price)
        # replace commas with nothing
        # convert each price from string to int
        upgrade_prices = [int(lst[len(lst) - 1].replace(",", "")) for lst in upgrade_split_labels]
        print(upgrade_prices)

        # current cookie count
        cookie_count = driver.find_element_by_id("money").text
        if "," in cookie_count:
            cookie_count = int(cookie_count.replace(",", ""))
        else:
            cookie_count = int(cookie_count)

        # dictionary of store items and prices
        cookie_upgrades = {}
        for index in range(0, len(upgrade_prices)):
            cookie_upgrades[upgrade_ids[index]] = upgrade_prices[index]

        # find upgrades that can be bought with current cookie count
        available_upgrades = {}
        for upgrade_id, cost in cookie_upgrades.items():    # convert each dictionary item into a key-value tuple
            if cookie_count > cost:
                available_upgrades[upgrade_id] = cost

        # purchase the most expensive available upgrade
        # get key/upgrade id with the highest value
        most_expensive_upgrade_id = max(available_upgrades, key=available_upgrades.get)
        print(most_expensive_upgrade_id)
        driver.find_element_by_id(f"{most_expensive_upgrade_id}").click()

        # add 5 more seconds until the next check
        five_secs = time() + 5

    if time() > timeout:
        cookies_per_sec = driver.find_element_by_id("cps").text
        print(f"Cookies/second: {cookies_per_sec}")
        break

