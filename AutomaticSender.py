from selenium import webdriver
import time
import platform

if platform.system() == 'Windows':
    PATH_TO_CHROMEDRIVER = ''
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
else:
    driver = webdriver.Chrome()

driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the number of times this message has to be sent : '))
interval = input('Enter the interval after which each message has to be sent in seconds : ')

#Scan the code before proceeding further
input('Enter anything after scanning QR code : ')

driver.find_element_by_class_name('C28xL').click()
searchBar = driver.find_element_by_id('input-chatlist-search')
searchBar.send_keys(name)
time.sleep(1)

input()
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('compose-btn-send').click()
    time.sleep(int(interval))
