
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Download the appropriate web driver and specify its path here
PATH_TO_WEB_DRIVER = 'path/to/webdriver'

def register_account(username, password, email):
    # Navigate to the dating site's registration page
    driver.get('https://happn.app/registration/first-name')

    # Fill in the username, password, and email fields
    username_field = driver.find_element()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('password')
    password_field.send_keys(password)

    email_field = driver.find_element_by_id('email')
    email_field.send_keys(email)

    # Click the registration button
    registration_button = driver.find_element_by_id('registration-button')
    registration_button.click()

    # Wait for the account creation to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'registration-complete'))
    )

    print(f'Successfully registered account for {username}')

if __name__ == '__main__':
    # Initialize the Selenium web driver
    driver = webdriver.Chrome(PATH_TO_WEB_DRIVER)

    # Define the account registration data
    accounts = [
        {'username': 'John123', 'password': 'johnpassword', 'email': 'john@email.com'},
        {'username': 'Jane123', 'password': 'janepassword', 'email': 'jane@email.com'},
        # Add more accounts as needed
    ]

    # Register the accounts
    for account in accounts:
        register_account(account['username'], account['password'], account['email'])

    # Close the web driver
    driver.quit()