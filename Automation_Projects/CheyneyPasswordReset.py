#Project: Cheyney Password Reset
#Purpose: To reset Cheyney Password
#By: Isaiah DeSantis

#imports
from selenium import webdriver

#input username:
user = input("Enter Username: ")

#StudentID:
Student_ID = input("Enter Student ID (i.e. 000141311): ")

#Birthday:
#Set your birthday in the '' in form of: mm/dd/yyyy(include '/')
Birthday = ''

#input new password:
password = input('Enter new password here: ')


#Open website to change password:
driver = webdriver.Chrome()
driver.get('https://reset.cheyney.edu:9251/showLogin.cc')

#Clicking links:
reset_link = driver.find_element_by_xpath('//*[@id="hrefReset"]/font[1]').click()
user_name = driver.find_element_by_xpath('//*[@id="userName"]')
user_name.send_keys(user)
continue_button = driver.find_element_by_xpath('//*[@id="loginButton"]').click()

#Entering Student ID Info:
ID_Box = driver.find_element_by_xpath('//*[@id="1501_ans"]')
ID_Box.send_keys(Student_ID)

#Entering Birthday:
Birthday_Box = driver.find_element_by_xpath('//*[@id="1050324_ans"]')
Birthday_Box.send_keys(Birthday)

#Captcha
Captcha_One_Answer = input('Enter Captcha here: ')
Captcha_One = driver.find_element_by_xpath('//*[@id="captchaVal"]')
Captcha_One.send_keys(Captcha_One_Answer)
Continue = driver.find_element_by_xpath('//*[@id="Continue"]').click()

#New Password Entry
New_Password = driver.find_element_by_xpath('//*[@id="newPassword"]')
New_Password.send_keys(password)
#Confirm Password
Confirm_Password = driver.find_element_by_xpath('//*[@id="confirmPassword"]')
Confirm_Password.send_keys(password)

#Second Captcha
Captcha_Two_Answer = input('Enter Captcha Answer here: ')
Captcha_Two = driver.find_element_by_xpath('//*[@id="captchaVal"]')
Captcha_Two.send_keys(Captcha_Two_Answer)

#Reset Password Button
Reset_Password = driver.find_element_by_xpath('//*[@id="save"]').click()

#Printout Confirmation
print('You Cheyney Password had Successfully Been Updated!')
