from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")

driver.get("https://web.whatsapp.com/")
time.sleep(5)

celular = "573122787169"
mensaje = "Hola, mi primer bot"

driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(3)

btn = driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a")
btn.click()
time.sleep(3)

btn = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(3)

print (" --fin de Bot--")

driver.close()