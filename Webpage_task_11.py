from selenium import webdriver

# Define the credentials
username = "standard_user"
password = "secret_sauce"

# Start a Selenium webdriver session
driver = webdriver.Chrome()

# Open the URL
url = "https://www.saucedemo.com/"
driver.get(url)

# Find the username and password input fields and enter the credentials
username_field = driver.find_element_by_id("user-name")
password_field = driver.find_element_by_id("password")
username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element_by_css_selector(".btn_action")
login_button.click()

# Fetch the title and current URL of the webpage
title = driver.title
current_url = driver.current_url

print("Title of the webpage:", title)
print("Current URL of the webpage:", current_url)

# Close the browser window
driver.quit()