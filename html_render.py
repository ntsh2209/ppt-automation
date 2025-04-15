from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def render_html_to_image(html_path, image_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1200x800")
    driver = webdriver.Chrome(options=chrome_options)

    abs_path = os.path.abspath(html_path)
    driver.get("file://" + abs_path)

    time.sleep(2)  # wait for rendering (increase if needed)
    driver.save_screenshot(image_path)
    driver.quit()
