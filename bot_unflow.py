import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import operator
import time
	
def getFlowers(file_name):
	nomes=[]


	in_file = open(file_name, "rt") # open file lorem.txt for reading text data
	

	for line in in_file:
		nomes.append(line)

               # close the file
	return nomes 	

nameSegui=[]
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
'''

driver.get("https://www.instagram.com/leilamorenohairstylist/")
seguidores = int(driver.find_elements_by_class_name('_fd86t')[1].text)
elem = driver.find_elements_by_class_name('_fd86t')[1]
elem.click()
time.sleep(1)
keyboard.press_and_release('tab')

for x in range(seguidores):
	keyboard.press_and_release('down')
	keyboard.press_and_release('down')
	
	time.sleep(0.1)
	elem = driver.find_elements_by_class_name('_2g7d5')[x].text
	print("x:",x)
	print("nome:",elem)
	nameSegui.append(elem)
	a = open("nome_real_flowrs.txt","a")
	print(elem, file=a)  
	a.close


'''
seguindo=getFlowers("nome_flow.txt")
seguidores=getFlowers("nome_real_flowrs.txt")





for x in seguindo:
	delflow=0;	
	for j in seguidores:	


		
		print(delflow);		
		if operator.eq(seguindo[seguindo.index(x)], seguidores[seguidores.index(j)]):
			delflow=1;

	if delflow==0:
	
		nameUrl="https://www.instagram.com/"+seguindo[seguindo.index(x)]+"/"
		driver.get(nameUrl)
		time.sleep(0.5)
		try:
	
			elem = driver.find_element_by_css_selector("._qv64e").text
			print(elem);
			if elem!="Seguir":
					
					time.sleep(1)
					elem = driver.find_element_by_css_selector("._qv64e")
					elem.click()
					'''nameBloc=flowes[flowes.index(x)]
					nameUrl="https://www.instagram.com/"+nameBloc+"/"
					driver.get(nameUrl)
			'''
		except NoSuchElementException:
			print("Errro garago")