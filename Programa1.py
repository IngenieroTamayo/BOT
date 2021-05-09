#Se importan las librerias necesarias de Selenium para hacer la prueba de automatización.
#Este es un pequeño ejercicio de como funciona la automatización. 
from selenium import webdriver
import time
import os, time

#Con el webdriver se selecciona la ruta donde se alberga el mismo. 
driver = webdriver.Chrome(executable_path=r"C:\driverchrome\chromedriver.exe")

#Automaticamente el driver acepta la solicitud de ingresar, en este caso, a Python.
driver.get("http://www.python.org")
time.sleep(10)

driver.close()