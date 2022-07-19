import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import HTML_helpers as h
import unittest
from selenium.webdriver import ActionChains
import warnings
import HtmlTestRunner

class ChromeCaMarketing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test1_Chrome_validation_title_logo_on_homepage(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "CALIFORNIA MARCKETING")))

        # assert 'California Marketing' title
        self.assertIn("California Marcketing", driver.title)
        print("Page has", driver.title + " as page title")

        driver.close()

    def test2_Chrome_check_LogIn_button(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        # Validate if title California Marketing is presented
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, h.log_in_button)))
            print("Log in tab is presented!")
        except TimeoutException:
            print("Loading took too much time!")

        driver.close()


    def test3_Chrome_verify_blog_search_functional(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        # Find Blog button and click on it and navigate to search field
        btn_for_blog = driver.find_element(By.XPATH, h.blog).click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//*[@class='EKJcYR']")
        ActionChains(driver) \
            .click(search) \
            .perform()
        input_search = driver.find_element(By.XPATH,"//*[@class='m2yAmK blog-desktop-header-search-text-color blog-desktop-header-search-font search-input__input']")
        input_search.clear()
        input_search.send_keys("wall")
        input_search.send_keys(Keys.ENTER)
        time.sleep(5)

        # Validate that result is populating after input word in a field
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='FAMRGA search-results-list']")))
            print("Result is here!")
        except TimeoutException:
            print("Loading took too much time!")

        driver.close()

    def test4_Chrome_get_in_touch_link(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        wait = WebDriverWait(driver, 20)

        # assert 'California Marketing' in title
        self.assertIn('California Marcketing', driver.title)
        print("Page has", driver.title + " as Page title")

        time.sleep(1)

        # validate that 'Get In Touch' link is functional
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wQYUw"))).click()
            print("Get in touch link is functional")
        except TimeoutException:
            print("Oops something went wrong :(")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Get in Touch' link text is correct")
        else:
            print("Incorrect link text")

        time.sleep(2)

        # check that site email address is correct
        email = driver.find_element(By.XPATH, "//span[contains(.,'Get In Touch')]")
        email.get_attribute("href")

        time.sleep(2)

        # print on page email and supposed email
        print(email)
        print(h.main_email)

        driver.close()

    def test5_Chrome_email_subscription_form(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'CALIFORNIA MARCKETING')]")))

        # Locate Subscribe Form and fill out information
        driver.find_element(By.LINK_TEXT, "CALIFORNIA MARCKETING").send_keys(Keys.PAGE_DOWN)
        elem = driver.find_element(By.ID, "input_comp-ksocylga1")
        elem.clear()
        elem.send_keys("123@abc.com")
        submit = driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        time.sleep(5)

        #validate that email has been initiated and sumbmitted
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.ID, "comp-ksocylgv1")))
            print("Email is ready")
        except TimeoutException:
            print("Loading taking forever")


        # assert 'California Marketing' in title
        self.assertIn("California Marcketing", driver.title)
        print("Current page has", driver.title + " as Page title")
        driver.close()

    def tearDown(self):
        self.driver.quit()  # Close the browser.

class FireFoxCaMarketing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test1_FireFox_validation_title_logo_on_homepage(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "CALIFORNIA MARCKETING")))

        # assert 'California Marketing' title
        self.assertIn("California Marcketing", driver.title)
        print("Page has", driver.title + " as page title")

        driver.close()

    def test2_Firefox_check_LogIn_tab(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        # Validate if title California Marketing is presented
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, h.log_in_button)))
            print("Log in tab is presented!")
        except TimeoutException:
            print("Loading took too much time!")

        driver.close()


    def test3_Firefox_verify_blog_search_functional(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        # Find Blog button and click on it and navigate to search field
        btn_for_blog = driver.find_element(By.XPATH, h.blog).click()
        time.sleep(2)
        search = driver.find_element(By.XPATH, "//*[@class='EKJcYR']")
        ActionChains(driver) \
            .click(search) \
            .perform()
        input_search = driver.find_element(By.XPATH,"//*[@class='m2yAmK blog-desktop-header-search-text-color blog-desktop-header-search-font search-input__input']")
        input_search.clear()
        input_search.send_keys("wall")
        input_search.send_keys(Keys.ENTER)
        time.sleep(5)

        # Validate that result is populating after input word in a field
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='FAMRGA search-results-list']")))
            print("Result is here!")
        except TimeoutException:
            print("Loading took too much time!")

        driver.close()

    def test4_Firefox_get_in_touch_link(self):

        # open URL
        driver = self.driver
        driver.get(h.main_url)

        wait = WebDriverWait(driver, 20)

        # assert 'California Marketing' in title
        self.assertIn('California Marcketing', driver.title)
        print("Page has", driver.title + " as Page title")

        time.sleep(1)

        # validate that 'Get In Touch' link is functional
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wQYUw"))).click()
            print("Get in touch link is functional")
        except TimeoutException:
            print("Oops something went wrong :(")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Get in Touch' link text is correct")
        else:
            print("Incorrect link text")

        time.sleep(2)

        # check that site email address is correct
        email = driver.find_element(By.XPATH, "//span[contains(.,'Get In Touch')]")
        email.get_attribute("href")

        time.sleep(2)

        # print on page email and supposed email
        print(email)
        print(h.main_email)

        driver.close()

    def test5_Firefox_email_subscription_form(self):

        driver = self.driver
        driver.get(h.main_url)
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'CALIFORNIA MARCKETING')]")))

        # Locate Subscribe Form and fill out information
        driver.find_element(By.LINK_TEXT, "CALIFORNIA MARCKETING").send_keys(Keys.PAGE_DOWN)
        elem = driver.find_element(By.ID, "input_comp-ksocylga1")
        elem.clear()
        elem.send_keys("123@abc.com")
        submit = driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()

        # validate that email has been initiated and sumbmitted
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.ID, "comp-ksocylgv1")))
            print("Email is ready")
        except TimeoutException:
            print("Loading taking forever")
            time.sleep(5)

        # assert 'California Marketing' in title
        self.assertIn("California Marcketing", driver.title)
        print("Current page has", driver.title + " as Page title")

    def tearDown(self):
        self.driver.quit()  # Close the browser.


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))