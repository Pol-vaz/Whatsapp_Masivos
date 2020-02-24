from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

class Whatsapp_Grupos:

    def whatsapp(self):
        self.datos()
        
        self.eleccion=input(f'\n\nSe va a enviar el siguiente mensaje:\n\n         "{self.texto}"   {self.num} veces al siguiente grupo o contacto:\n\n        {self.objetivo}\n\nSi todo es correcto pulse "s", en caso contario pulse "n": ')
        if self.eleccion is 's':
            self.driver()
            self.sending()
        else:
            print('\nHasta la vista.\n')

    def datos(self):
        print('\n\n####################################  Mandador de mensajes Whatsapp by pol and the Bros  ##############################\n')
        nombre=input('\nIntroduce el nombre del grupo o contacto al que quieres mandar el mensaje: ')
        self.objetivo = '''"'''+nombre+'''"'''
        self.num=int(input('\nIntroduce el número de veces que quieres mandar el mensaje: '))
        # Aquí escribe tu mensaje de puto enfermo
        self.texto=input('\nIntroduce tu mensaje: ')

    def driver(self):
        self.conductor = webdriver.Chrome(r'/home/pol/Escritorio/Whatsapps_Masivos/chromedriver')
        self.conductor.get("https://web.whatsapp.com/") #Se abre aquí whatsapp Web en chrome
        self.espera = WebDriverWait(self.conductor, 600)   #Espera de 600 mili
        
    def sending(self):
        for i in range(self.num):
            #Busca el grupo o el contacto según el nombre dado
            x_arg = '//span[contains(@title,' + self.objetivo + ')]'
            titulo_grupo = self.espera.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            titulo_grupo.click() 
            mensaje = self.conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            #Mando el mensaje al grupo o contacto
            mensaje.send_keys(self.texto)
            enviar = self.conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            enviar.click()
        self.conductor.close()
        print ("\nEspera unos segundos mientras surge la magia.↓\n")
        print('\nListo')

       
enviador = Whatsapp_Grupos()
enviador.whatsapp()
