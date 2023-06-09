from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/DELL/chromedriver_win32/chromedriver.exe")
driver.get("https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas")

products = driver.find_elements(By.CSS_SELECTOR, ".shelfProductTile-content")
for product in products:
    name = product.find_element(By.CSS_SELECTOR, ".shelfProductTile-descriptionLink").text
    price = product.find_element(By.CSS_SELECTOR, ".price-dollars").text
    print("Nom du produit :", name)
    print("Prix du produit :", price)

