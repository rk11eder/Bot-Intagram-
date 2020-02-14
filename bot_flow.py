import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
	
def getNames(file_name):
	nomes=[]
	file_name="name_list.txt"

	in_file = open(file_name, "rt") # open file lorem.txt for reading text data
	

	for line in in_file:
		nomes.append(line)

               # close the file
	return nomes 	


usr = "leilamorenohairstylist"
pas = "ederbarbosa"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver= webdriver.Chrome(executable_path="C:\\Users\Eder Barbosa\Desktop\python\chromedriver.exe",chrome_options=chrome_options)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
elem = driver.find_element_by_name("username")
elem.send_keys(usr)
time.sleep(1)
elem = driver.find_element_by_name("password")
elem.send_keys(pas)
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(2)

driver.get("https://www.instagram.com/mbeatrizquaresma/")

elem = driver.find_element_by_css_selector("._qv64e").text

print(elem);

nomes=getNames("name_list.txt")
tabVal=0;
nameSub=[]
for i in nomes:
	tabVal=0;
	for x in range(40):
			
		tabVal+=1;
		driver.get("https://www.instagram.com/")
		time.sleep(0.2)
		elem = driver.find_element_by_css_selector("._avvq0")
		elem.send_keys(nomes[nomes.index(i)]) 
		time.sleep(2)
		print("dqwd1",tabVal)
		
		for x in range(tabVal):
			keyboard.press_and_release('tab')
			
		
		keyboard.press_and_release('enter')
		
		time.sleep(2)
		try:
			elem = driver.find_elements_by_class_name('_fd86t')[1]
			num_seguidor=elem.get_attribute("title")
			num_seguidor=num_seguidor.replace(" ", "")
			num_seguindo = driver.find_elements_by_class_name('_fd86t')[2].text
			num_seguindo=num_seguindo.replace(" ", "")
			num_seguidor=float(num_seguidor)
			num_seguindo=float(num_seguindo)
			num_seguidor+=1
			num_seguindo+=1
			print(num_seguindo)
			print(num_seguidor)
			print(num_seguidor/num_seguindo)
			elem = driver.find_element_by_css_selector("._qv64e").text


			if elem=="Seguir":
				
				if num_seguidor/num_seguindo < 1.50:
				
					time.sleep(1)
					elem = driver.find_element_by_css_selector("._qv64e")
					elem.click()
					elem = driver.find_element_by_css_selector("._rf3jb").text
					print("nome:",elem)
					a = open("nome_flow.txt","a")
					print(elem, file=a)  
					a.close
					time.sleep(0.1)	
			
				

		except IndexError:
			print("Errro garago")
		



time.sleep(2)
driver.quit()
