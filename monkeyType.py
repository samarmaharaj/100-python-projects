from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
driver.get("https://monkeytype.com/")

# Wait for the page to load
time.sleep(3)

# Click on the page to ensure it's focused
driver.find_element(By.TAG_NAME, "body").click()

# Find all words in the typing test
words = driver.find_elements(By.CLASS_NAME, "word")

# Type each word followed by a space
for word in words:
    driver.switch_to.active_element.send_keys(word.text + " ")  # Send the word followed by a space
    time.sleep(0.05)  # Adjust speed if needed

# Wait before closing
time.sleep(5)
driver.quit()
