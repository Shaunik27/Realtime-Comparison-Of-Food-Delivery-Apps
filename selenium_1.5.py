from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

location = input("Delivery Location: ")
time.sleep(2)
fooditem  = input("\nEnter food item: ")
driver  = webdriver.Chrome()    
driver.maximize_window()

try:
    # taking differernt locations
    website = 'https://www.swiggy.com/'
    driver.get(website)
    time.sleep(2)
    e = driver.find_element("xpath",'.//*[@id="location"]')
    e.send_keys(location)
    time.sleep(2)
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]').click()
    time.sleep(2)
    url = driver.current_url
    print(url)
    #clickonsearch 
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/header/div/div/ul/li[5]/div/a').click()
    time.sleep(4)
    search_textbox =  driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div[1]/div/form/div/div[1]/input')
    search_textbox.send_keys(fooditem)
    url_two = driver.current_url
    print(url_two)
    time.sleep(2) 
    driver.get(url_two+'?query='+fooditem)
    time.sleep(1)
    print(driver.current_url)
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/a/div[2]').click()
    print(driver.current_url)
    time.sleep(2)
    #select burger
    driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div').click()
    time.sleep(2)
    #addburger to cart
    driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
    time.sleep(2)
    #view cart
    driver.find_element("xpath",'.//*[@id="view-cart-btn"]/span/span[2]').click()
    time.sleep(2)
    url_5 = driver.current_url
    print(url_5)
    element = driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div[2]').text
    print("Amount in INR to pay on SWIGGY: "+element)

    driver.quit()
except NoSuchElementException: 
    print(NoSuchElementException)
    driver.get('https://www.swiggy.com/')
    time.sleep(3)