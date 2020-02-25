from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import os

class Whatsapp_Grupos:

    def __init__(self, opcion,foto=None):
       self.opcion = opcion
       self.opc_dicc = {1: 'Mandar mensajes masivos',
                         2: 'Mandar links masivos',
                         3: 'Mandar fotos Masivas'}
       self.foto = foto

    def whatsapp(self):
        self.datos()
        
        self.eleccion=input(f'\n\nSe va a enviar el siguiente mensaje:\n\n         "{self.texto}"   {self.num} veces al siguiente grupo o contacto:\n\n        {self.objetivo} en el siguiente modo:\n\n        {self.opc_dicc[self.opcion]}\n\nSi todo es correcto pulse "s", en caso contario pulse "n": ')
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
        self.conductor = webdriver.Chrome('/home/pol/Escritorio/Whatsapps_Masivos/chromedriver')
        self.conductor.get("https://web.whatsapp.com/") #Se abre aquí whatsapp Web en chrome
        self.espera = WebDriverWait(self.conductor, 600)   #Espera de 600 mili
        
    def sending(self):
        for i in range(self.num):
            if self.opcion is 1:
                self.mandar_mensajes()
            elif self.opcion is 2:
                self.mandar_links()
            elif self.opcion is 3:
                self.mandar_fotos()
                
        self.conductor.close()
        print ("\nEspera unos segundos mientras surge la magia.↓\n")
        print('\nListo')

    def mandar_links(self):
        self.busqueda_grupo()
        self.escribir_mensaje()
        time.sleep(3)
        self.mandar_informacion()
    
    def mandar_fotos(self):
        self.busqueda_grupo()
        self.busqueda_clip()
        time.sleep(1)
        self.fotos_videos()

    def mandar_mensajes(self):
        self.busqueda_grupo()
        self.escribir_mensaje()
        self.mandar_informacion()

    def busqueda_grupo(self):
        #Busca el grupo o el contacto según el nombre dado
        x_arg = '//span[contains(@title,' + self.objetivo + ')]'
        titulo_grupo = self.espera.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        titulo_grupo.click()
    
    def busqueda_clip(self):
        clip = self.conductor.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clip.click()

    def fotos_videos(self):
        
        dir_path = os.getcwd()
        imagen = dir_path + self.foto
        
        fotos = self.conductor.find_element_by_css_selector("input[type='file']")
        fotos.send_keys(imagen)
        time.sleep(3)
        ruta='//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'
        envio = self.conductor.find_element_by_xpath(ruta)
        envio.click()

    def sacar_foto(self):                              
        camara = self.conductor.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[2]')
        camara.click()
        permitir = self.conductor.find_element_by_xpath('// * [ @ id = "app"] / div / span[2] / div / div / div / div / div / div / div / div[4]')[0]
        permitir.click()
        instantanea = self.conductor.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]')
        instantanea.click()
    def escribir_mensaje(self):
        mensaje = self.conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        mensaje.send_keys(self.texto)

    def mandar_informacion(self):
        enviar = self.conductor.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        enviar.click()       

################################################## AQUÍ EMPIEZA EL PROGRAMA  ########################################################################

#CAMBIA LA RUTA DE TU FOTO O VIDEO
ruta_foto = '/amor.jpg'

tipo_envio=int(input('\nElige una opción:\n\nMandar mensajes masivos --> 1\nMandar links masivos    --> 2\nMandar fotos Masivas    --> 3\n\n---> '))
enviador = Whatsapp_Grupos(tipo_envio,ruta_foto)
enviador.whatsapp()
