from selenium import webdriver
from getpass import getpass

usr= input('bạn nhập sđt hoặc email ')
pwd=getpass('nhập mật khẩu ')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username_box=driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box=driver.find_element_by_id("pass")
username_box.send_keys(pwd)

login_btn =driver.find_element_by_id("u_0_a")
login_btn.submit()





