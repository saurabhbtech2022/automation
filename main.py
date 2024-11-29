from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Zomato page
driver.get("https://www.zomato.com/ncr/delivery/dish-biryani")

# Wait for the page to load the specific elements
try:
    # Wait until the entire body is loaded
    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    
    # Get the page source after JavaScript execution
    page_source = driver.page_source
    print(page_source)  # Check if the elements are present
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Now find all the elements containing the biryani names and prices
    biryani_items = soup.find_all('p', text='Biryani')

    for item in biryani_items:
        # Extract the name of the biryani
        name = item.text
        
        # Use relative navigation to find the price
        price = item.find_next_sibling('p').text

        print(f"Biryani Name: {name}, Price: {price}")

except Exception as e:
    print("An error occurred:", e)
#saurabh
    print("send to github")
# Close the browser after scraping
driver.quit()
