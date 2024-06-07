from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import credentials 
# Function to generate random sleep times
def random_sleep(min_time=2, max_time=5):
    time.sleep(random.uniform(min_time, max_time))

# Function to simulate human-like typing
def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# Set up the webdriver for Firefox with a realistic user-agent
firefox_options = webdriver.FirefoxOptions()
firefox_profile = webdriver.FirefoxProfile()

# Set a realistic user-agent
firefox_profile.set_preference("general.useragent.override", 
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# Disable the automation controlled flag
firefox_profile.set_preference("dom.webdriver.enabled", False)
firefox_profile.set_preference('useAutomationExtension', False)

# Initialize the WebDriver
driver = None
try:
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_page_load_timeout(30)  # Set a page load timeout
    print("WebDriver initialized successfully.")

    # Navigate to the Instagram login page
    print("Navigating to Instagram login page...")
    driver.get("https://www.instagram.com/accounts/login/")
    random_sleep(3, 5)
    print("Page loaded successfully.")

    # Locate the username and password fields
    print("Locating the username field...")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    print("Username field located.")

    print("Locating the password field...")
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    print("Password field located.")

    # Locate the login button and wait for it to be enabled
    print("Locating the login button...")
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    print("Login button located.")
    
    # # Wait for the login button to become enabled
    # WebDriverWait(driver, 10).until(
    #     lambda driver: not login_button.get_attribute('disabled')
    # )
    # print("Login button is now enabled.")

    # Enter credentials
    print("Entering username...")
    human_typing(username_field, credentials.USERNAME)
    random_sleep(1, 3)
    
    print("Entering password...")
    human_typing(password_field, credentials.PASSWORD)
    random_sleep(1, 3)
    
    # Click the login button
    print("Clicking the login button...")
    login_button.click()
    random_sleep(5, 7)


    # Locate and click the "Not now" button
    print("Locating the 'Not now' button...")
    not_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now' and @role='button']"))
    )
    print("'Not now' button located.")
    
    print("Clicking the 'Not now' button...")
    not_now_button.click()
    random_sleep(1, 3)
    
    print("'Not now' button clicked. Proceeding with further interactions.")

    not_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9_1")))
    not_now_button.click()
    random_sleep(1, 3)

    print("Login attempted. Check the browser for results.")
    # Additional steps can be added here, such as navigating to other pages, etc.

    # Keep the browser open for further interactions
    print("Browser will remain open for further interactions.")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Only close the browser if it was successfully initialized
    if driver is not None:
        print("Closing the browser.")
        driver.quit()
