from selenium import webdriver

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Users\lxy\chrome\Google Chrome\chrome.exe'
driver = webdriver.Chrome(r"C:\Users\lxy\chrome\Google Chrome\chromedriver.exe")
driver.get('https://www.baidu.com')