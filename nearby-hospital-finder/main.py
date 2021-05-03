from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests as r

name="Ritik"
carinfo="DLXXXX"
lat="28.6818237"
lon="77.1562096"
speed=120


driver = webdriver.Chrome()
driver.get(f"https://www.openstreetmap.org/search?query=hopital%20at%20{lat}%2C{lon}")

elem = driver.find_elements_by_xpath("//li")
#elem = driver.find_element_by_id("query")
#elem.send_keys(f"{lat},{lon}")
#elem.send_keys(Keys.RETURN)
hospital =[]
for i in elem:
    data = str(i.text)
    if "hospital" in (data).lower():
        hospital.append(data)
print(hospital)

d = {"name": name, "carinfo":carinfo,"coordinates":lat+','+lon ,"speed":speed }
response = r.post("http://localhost:5000/users",data=d)
print(response.text)

#driver.close()