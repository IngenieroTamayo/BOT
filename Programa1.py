#Se importan las librerias necesarias de Selenium para hacer la prueba de automatización.
#Este es un pequeño ejercicio de como funciona la automatización. 
from selenium import webdriver
import time
import os, time

#Con el webdriver se selecciona la ruta donde se alberga el mismo. 
driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")

#Este metodo navegará a una paguna dada por la URL. Espera hasta que se cargue. 
driver.get("http://www.python.org")
time.sleep(10)

driver.close()