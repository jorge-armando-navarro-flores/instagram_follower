
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = os.environ.get("DRIVER_PATH")
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ.get("USERNMAME")
PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:

    def __init__(self, driver_path):
        ser = Service(driver_path)
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

    def login(self):
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(USERNAME)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2)
        not_save_info = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save_info.click()
        time.sleep(2)
        not_notifications = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_notifications.click()
        time.sleep(3)

    def find_followers(self):
        # search_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # search_field.send_keys(SIMILAR_ACCOUNT)
        # time.sleep(3)
        # account = self.driver.find_element(By.XPATH,
        #                               '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        # account.click()
        # time.sleep(3)
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()





