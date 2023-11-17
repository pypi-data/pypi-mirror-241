from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import logging
import requests
import os


def get_time():
    return datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")


def get_time_save():
    return datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")


def download_images(urls, save_folder):
    save_folder = save_folder[:225].rstrip()
    try:
        timestamp_folder = os.path.join(save_folder, get_time_save())
        if not os.path.exists(timestamp_folder):
            os.makedirs(timestamp_folder)

        for index, url in enumerate(urls):
            response = requests.get(url)
            response.raise_for_status()
            filename = os.path.join(timestamp_folder, f"{save_folder} ({index + 1}).png")
            with open(filename, 'wb') as file:
                file.write(response.content)

            logging.info(f'{get_time()} Image downloaded successfully and saved to "{filename}"')

    except requests.exceptions.RequestException as e:
        logging.critical(f"Image download failed: {str(e)}")


class Dalle:
    def __init__(self, cookie_value, headless=True):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        if headless:
            options.add_argument("--headless")

        self.driver = Chrome(options=options)
        self.cookie_value = cookie_value

    def create(self, query):
        cookie = {"name": "_U", "value": self.cookie_value}

        self.driver.get(f'https://www.bing.com/images/create')
        logging.info(f"{get_time()} Bing Image Creator (Dalle-3) Opened")

        self.driver.add_cookie(cookie)
        self.driver.refresh()
        logging.info(f"{get_time()} Cookie values added ")

        input_element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#sb_form_q')))
        input_element.send_keys(query)
        input_element.send_keys(Keys.RETURN)
        logging.info(f"{get_time()} Sent query to Bing Image Creator (Dalle-3)")

        return True

    def get_urls(self):
        try:
            urls = list(set([element.get_attribute("src") for element in WebDriverWait(
                self.driver, 180).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg")))]))  # waiting for 3 minutes max

            urls = [url.split('?')[0] for url in urls]

            return urls
        except Exception as e:
            logging.critical(
                f"{get_time()} Error while extracting image urls. Maybe something is wrong about your prompt. "
                f"(You can check your prompt manually) \n{e}")
            return False

    def get_credits(self):
        try:
            remaining_credits = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, "token_bal")))
            return remaining_credits.text

        except Exception as e:
            logging.error(f"{get_time()} Error while extracting remaining credits. \n{e}")

    def run(self, queries, save_folder="", get_credits=True):
        if type(queries) == str:  # if it is a string making a 1 len list
            queries = [queries]

        for query in queries:
            self.create(query)
            urls = self.get_urls()
            if urls:
                download_images(urls, save_folder + query)

        remain_credits = self.get_credits() if get_credits else None
        self.driver.close()
        return remain_credits
