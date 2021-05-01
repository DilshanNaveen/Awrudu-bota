from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

accounts= open("./comments.txt","r")
data=accounts.readlines()
line_counter=0

driver =webdriver.Chrome('./chromedriver')

driver.get("https://www.facebook.com/")

user_name= driver.find_element_by_xpath('//*[@id="email"]')
user_name.send_keys("username")

password= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
password.send_keys("password")

login=driver.find_element_by_xpath('//html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
login.click()

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.facebook.com/rotaractkelaniya/photos/a.1855646581271384/1858284324340943/?comment_id=1858399554329420&reply_comment_id=459523761940634&force_theater=true&notif_id=1619886562697893&notif_t=photo_reply&ref=notif")
time.sleep(3)

for line in data:
    comment= driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div')
    comment.send_keys(line)
    time.sleep(0.5)
    driver.find_element_by_class_name('_1mf').send_keys(Keys.RETURN)
    print("sending : " + line)
    time.sleep(1)