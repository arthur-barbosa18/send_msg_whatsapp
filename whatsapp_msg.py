from selenium import webdriver 
import time


TIME_SLEEP = 1

class 	WhatasapMsg():
	""" Responsible by send whatsapp messages  
	"""
	def __init__(self):
		self.mensagem = "."
		self.grupos = ['Look', 'Mae']
		options = webdriver.ChromeOptions()
		options.add_argument("Lang=pt-br")
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

	def enviar_mensagem(self):
		"""
		"""

		self.driver.get('https://web.whatsapp.com')
		time.sleep(30)
		for grupo in self.grupos:
			

			chat_box1 =  self.driver.find_element_by_class_name('_3FRCZ')
			chat_box1.click()
			chat_box1.send_keys(grupo)
			
			while not any(self.driver.find_elements_by_xpath("//span[@title='{0}']".format(grupo))):
				print("procurando o GRUPO")
				continue

			user = self.driver.find_element_by_xpath("//span[@title='{0}']".format(grupo))	
			user.click()

			while not any(self.driver.find_elements_by_class_name("_3uMse")):
				print("procurando o CHAT")
				continue
			chat_box =  self.driver.find_element_by_class_name('_3uMse')
			time.sleep(TIME_SLEEP)
			chat_box.click()
			time.sleep(TIME_SLEEP)
			chat_box.send_keys(self.mensagem)
			while not any(self.driver.find_elements_by_xpath("//span[@data-icon='send']")):
				print("procurando o botao de ENVIAR")
				continue
			botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			botao_enviar.click()


whats_obj = WhatasapMsg()
whats_obj.enviar_mensagem()

