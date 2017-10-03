from selenium import webdriver

usernameStr = 'user'
passwordStr = 'pass'

browser = webdriver.Chrome()
browser.get(('https://192.168.10.3/connect/PortalMain'))

# fill in username and hit the next button

username = browser.find_element_by_id('LoginUserPassword_auth_username')
username.send_keys(usernameStr)

password = browser.find_element_by_id('LoginUserPassword_auth_password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('UserCheck_Login_Button')
signInButton.click()
