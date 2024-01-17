from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set the path to the Firefox binary
firefox_binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Create Firefox options object and set the binary location
options = Options()
options.binary_location = firefox_binary

# Create Firefox driver with options
driver = webdriver.Firefox(options=options)
driver.get('https://www.w3schools.com/')

i = 1
driver.implicitly_wait(1)
driver.find_element('xpath', '//*[@id="navbtn_tutorials"]').click()
element = driver.find_element('xpath', '//*[@id="nav_tutorials"][h3]').get_attribute("innerHTML")
print(element)
print('HTML and CSS')
while True:
    
    try:
        element = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[' + str(i) + ']').get_attribute("innerHTML")
        elementhref = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[' + str(i) + ']').get_attribute("href")
        print(element + ' - ' + elementhref)
        i += 1
    except:
        break 

print('Javascript')
while True:
    
    try:
        element = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[3]/a[' + str(i) + ']').get_attribute("innerHTML")
        elementhref = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[3]/a[' + str(i) + ']').get_attribute("href")
        print(element + ' - ' + elementhref)
        i += 1
    except:
        break 

driver.close()
