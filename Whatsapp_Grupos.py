from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

def Whatsapp_Grupos_Masivos():
    print('\n\n####################################  Mandador de mensajes Whatsapp by pol and the Bros  ##############################\n')
    num=int(input('\nIntroduce el número de veces que quieres mandar el mensaje: '))
    # Aquí escribe tu mensaje de puto enfermo
    texto=input('\nIntroduce tu mensaje: ')

    #AQUI CAMBIA EL NOMBRE DEL GRUPO O EL CONTACTO. Esta vez va por nombre, no por número de teléfono.
    objetivo ='"Dee Lujoo!!"'
    eleccion=input(f'\n\nSe va a enviar el siguiente mensaje:\n\n         "{texto}"   {num} veces al siguiente grupo o contacto:\n\n        {objetivo}\n\nSi todo es correcto pulse "s", en caso contario pulse "n": ')

    if eleccion is 's':
        #Simons, aqui reemplaza la ruta donde este tu chromedriver (En este caso es para Linux)
        conductor = webdriver.Chrome(r'/home/pol/Escritorio/Whatsapps_Masivos/chromedriver')

        conductor.get("https://web.whatsapp.com/") #Se abre aquí whatsapp Web en chrome

        espera = WebDriverWait(conductor, 600)   #Espera de 600 mili
        print ("Espera unos segundos mientras surge la magia.")

        #Repite el bucle de mandado de mensajes las veces que desees
        for i in range(num):
            #Busca el grupo o el contacto según el nombre dado
            x_arg = '//span[contains(@title,' + objetivo + ')]'
            titulo_grupo = espera.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            titulo_grupo.click() 
            mensaje = conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            #Mando el mensaje al grupo o contacto
            mensaje.send_keys(texto)
            enviar = conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            enviar.click()
        conductor.close()
        print('\nListo')
    else:
        print('\nHasta la vista,mariquita\n')

