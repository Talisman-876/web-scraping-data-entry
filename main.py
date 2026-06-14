import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.system("cls")

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

website_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url= website_url, headers= headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

property_link = soup.find_all(name= "a", class_= "property-card-link")
p_link = [link["href"] for link in property_link]

property_price = soup.find_all(name= "span", class_= "PropertyCardWrapper__StyledPriceLine")
p_price = [prices.getText().strip("").rstrip("/mo").rstrip("+ 1 bd") for prices in property_price]

addresses = soup.find_all(attrs= {"data-test": "property-card-addr"})
p_address = [address.getText().strip().replace(" | ", "") for address in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options= chrome_options)
wait = WebDriverWait(driver, 10)

load_dotenv()
forms_url = os.getenv("FORMS_URL")

driver.get(url= forms_url)

for i in range(len(p_address)):
    inputs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".whsOnd")))
    
    inputs[0].click()
    inputs[0].send_keys(p_address[i])
    
    inputs[1].click()
    inputs[1].send_keys(p_price[i])
    
    inputs[2].click()
    inputs[2].send_keys(p_link[i])
    
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".NPEfkd")))
    submit_btn.click()
    
    another = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
    another.click()






