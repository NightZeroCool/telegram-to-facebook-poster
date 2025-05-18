from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_facebook(text):
    email = os.getenv("FB_EMAIL")
    password = os.getenv("FB_PASSWORD")
    group_url = os.getenv("FB_GROUP_URL")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.facebook.com/login")
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        time.sleep(5)

        driver.get(group_url)
        time.sleep(5)

        post_box = driver.find_element(By.XPATH, "//div[@aria-label='Создать публичное сообщение...']")
        post_box.click()
        time.sleep(2)

        active_box = driver.switch_to.active_element
        active_box.send_keys(text)
        active_box.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(5)
    finally:
        driver.quit()