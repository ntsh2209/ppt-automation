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



import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Style the DataFrame and assign a class name
styled_df = df.style.applymap(lambda x: 'background-color: yellow' if x > 5 else '',
                              subset=['A', 'B', 'C']) \
                   .set_table_attributes('class="my-custom-class"')  # Set the class name

# Render the DataFrame as HTML
html_output = styled_df.render()

# Print the generated HTML with the class
print(html_output)
