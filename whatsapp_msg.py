from selenium import webdriver 
import time


TIME_SLEEP = 5

class 	WhatasapMsg():
	""" Responsible by send whatsapp messages  
	"""
	def __init__(self):
		self.mensagem = "."
		self.grupos = ['Fica frio aí',"Victor Aluno"]
		options = webdriver.ChromeOptions()
		options.add_argument("Lang=pt-br")
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

	def enviar_mensagem(self):
		"""
		"""

		self.driver.get('https://web.whatsapp.com')
		time.sleep(30)
		for grupo in self.grupos:
			
			user = self.driver.find_element_by_xpath("//span[@title='{0}']".format(grupo))	
			user.click()

			time.sleep(TIME_SLEEP)
			chat_box =  self.driver.find_element_by_class_name('_3uMse')
			time.sleep(TIME_SLEEP)
			chat_box.click()
			time.sleep(TIME_SLEEP)
			chat_box.send_keys(self.mensagem)

			botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			time.sleep(TIME_SLEEP)
			botao_enviar.click()

			time.sleep(TIME_SLEEP)

whats_obj = WhatasapMsg()
whats_obj.enviar_mensagem()
