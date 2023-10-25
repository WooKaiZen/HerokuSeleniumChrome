print("STARTING MAIN")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
print("SELENIUM IMPORTED")
import os
print("OS IMPORTED")
chrome_options = webdriver.ChromeOptions()
print("OPTIONS CREATED")
'''chrome_options.add_argument("--headless")
print("HEADLESS DONE")'''
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_SHIM")
print("CHROME SHIM DONE")
chrome_options.add_argument("--disable-dev-shm-usage")
print("DISABLE DEV SHM USAGE DONE")
'''chrome_options.add_argument("--no-sandbox")
print("NO SANDBOX DONE")
chrome_options.add_argument("--disable-gpu")
print("DISABLE GPU DONE")
chrome_options.add_argument("--remote-debugging-port=9222")
print("REMOTE DEBUGGING PORT SET")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
print("CHROME BINARY LOCATION SET")'''
service = Service(executable_path="CHROMEDRIVER_PATH")
driver = webdriver.Chrome(service=service, options=chrome_options)
print("DRIVER CREATED")
driver.get("https://medium.com")
print("WEBPAGE OPEN")
print(driver.page_source)
print("Finished!")
