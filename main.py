from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path= "/Users/bon/Desktop/GasStationsBot/chromedriver_mac64/chromedriver"
# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)
service= Service(executable_path=path)

# Initialize the ChromeDriver with options
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.opet.com.tr/benzin-istasyonu-arama/ankara")

try:
    cookieReject = driver.find_element(By.CLASS_NAME, 'btn btn-white all-reject-cookie-btn')
    cookieReject.click()
    
    div_elements = driver.find_elements_by_class_name("FindStation-module_searchResultsItem--Jzp")

    # Click on each element in the list
    for div in div_elements:
        div.click()

except Exception as e:
    print("Error occurred:", e)

#finally:
    #driver.quit()
    

