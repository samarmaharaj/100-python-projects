from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_stock_price(symbol):
    # Set up the WebDriver (Chrome in this case)
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open the NSE India website
        driver.get(f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}")
        
        # Wait for the stock price element to be present
        wait = WebDriverWait(driver, 50)
        price_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='quoteLtp']"))
        )
        
        # Get the stock price
        price = price_element.text
        print(f"The current stock price of {symbol} is {price}")
    
    finally:
        # Close the browser
        driver.quit()

symbol = "RVNL"  # Example stock symbol
get_stock_price(symbol)
