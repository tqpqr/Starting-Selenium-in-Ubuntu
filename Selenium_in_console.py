#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


# Setting the resolution of virtual display and
# starting X virtual framebuffer wrapper
display = Display(visible=0, size=(1024,768))
display.start()

# Initializing browser with required settings
# in this case - setting the default directory
# where files will be downloaded (in 'prefs')

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

prefs = {"download.default_directory" : "/var/www/pub/"}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=options)

driver.get('https://bloomberg.com')

driver.close()
driver.quit()
display.stop()
