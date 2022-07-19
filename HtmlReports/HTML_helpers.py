# Helpers file for project California-Marketing
import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



main_url = 'https://qasvus.wixsite.com/ca-marketing'
log_in_button = "//*[@class='_1UDJF']"
shop_btn = "comp-ksocy9ii__more__label"
marquee = "//*[@class='A9N6Yv']"
#input_search = "//*[@class='m2yAmK blog-desktop-header-search-text-color blog-desktop-header-search-font search-input__input']"
blog = "//*[@id='comp-ksocy9ii1label']"
main_email = "mailto:qasv.us@gmail.com.com"
