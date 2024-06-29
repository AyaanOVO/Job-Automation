from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()
driver.get("https://appbrewery.github.io/Zillow-Clone/")

prices = driver.find_elements(By.CLASS_NAME, "PropertyCardWrapper__StyledPriceLine")
all_address = driver.find_elements(By.TAG_NAME, "address")
links = driver.find_elements(By.CSS_SELECTOR, ".StyledPropertyCardPhotoBody a")

actual_links = [link.get_attribute("href") for link in links]
actual_address = [address.text for address in all_address]
actual_price = [price.text.split('+')[0] if '+' in price.text else price.text.split('/')[0] for price in prices]

for i in range(0, len(actual_price)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeDs5utT6Z_gccZ8gX4TAIXCaMB2VgyifXFWSZq_9W2nWMWNA/viewform?usp=sf_link")
    time.sleep(2)

    address_ans = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price_ans = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_ans = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_ans.send_keys(actual_address[i])
    price_ans.send_keys(actual_price[i])
    link_ans.send_keys(actual_address[i])
    submit.click()
