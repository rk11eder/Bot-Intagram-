import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import date

import time


def getNames(file_name):
    nomes = []
    file_name = "name_list.txt"

    # open file lorem.txt for reading text data
    in_file = open(file_name, "rt")

    for line in in_file:
        nomes.append(line)

       # close the file
    return nomes

nomes = getNames("name_list.txt")


today = str(date.today())
usr = "andre"
pas = "hubel123"
municipio="Santiago do Cacem"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="C:\\Users\eder.barbosa\Desktop\pyton\chromedriver.exe", chrome_options=chrome_options)


driver.get("https://www.city-mind.com/default.aspx")

elem = driver.find_element_by_name("AtusLogin$UserName")
elem.send_keys(usr)
time.sleep(1)
elem = driver.find_element_by_name("AtusLogin$Password")
elem.send_keys(pas)
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(2)

elem = driver.find_element_by_name("ctl00$mainArea$cboMunicipals").clear()
elem = driver.find_element_by_name("ctl00$mainArea$cboMunicipals");
elem.send_keys(municipio)

time.sleep(1)
elem = driver.find_element_by_name("ctl00$mainArea$btnOk");

elem.click()

time.sleep(1)

for i in nomes:
    print(nomes[nomes.index(i)]+"  "+i)

    driver.get('https://www.city-mind.com/Pages/Meter/MeterCards.aspx?mid='+nomes[nomes.index(i)])
    
    
    driver.find_element_by_id("ctl00_mainArea_meterdetails").click()
  
    
  
    nsMedidor = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbMeterSN').get_attribute('value')
 
    driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbMeterSN').clear()
    
    
    
    nsMedidor = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbTransponderID').get_attribute('value')
   
    driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbTransponderID').clear()
    
   
    subzona = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$cboSubZone').get_attribute('value')
    

    elem = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$cboZone')
    zona = elem.get_attribute('value')
    elem.send_keys(Keys.ARROW_UP)

  
    varOb="ns "+nsMedidor +"\ntran "+  nsMedidor +"\nzona "+zona+"/sub z "+subzona+"\neliminiado",today
    
   
    elem = driver.find_element_by_name("ctl00$mainArea$meterDetailsUC1$IntbRemarks").clear()
    elem = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbRemarks').send_keys("ns "+nsMedidor +"\ntran "+  nsMedidor +"\nzona "+zona+"/sub z "+subzona+"\neliminiado "+today )



    IntbCoordinateE = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateE').get_attribute('value')

    IntbCoordinateN = driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateN').get_attribute('value')

    driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateE').clear()
    driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateN').clear()

    IntbCoordinateE= IntbCoordinateE.replace(",", ".")

    IntbCoordinateN= IntbCoordinateN.replace(",", ".")

    if IntbCoordinateE != "":
        
        driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateE').send_keys(IntbCoordinateE)
        driver.find_element_by_name('ctl00$mainArea$meterDetailsUC1$IntbCoordinateN').send_keys(IntbCoordinateN)
    
   



 
   
    #elem = driver.find_element_by_id("ShowUpdateDiv")
   # elem = driver.find_element_by_name("ctl00$mainArea$btnUpdate")
 
    #elem.click();    
    time.sleep(10)
driver.quit()
