import requests
import schedule
import time


def job():
	response = requests.get("https://app91.liveapp.tech/")
	if response.status_code == 200:
		print('Success!')
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'C SkakRing всё айс')
	if response.status_code == 404:
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + '@JJBrunoo, Домен SkakRing ОТЪЕХАЛ!')


	response = requests.get("https://app168.liveapp.tech/")
	if response.status_code == 200:
		print('Success!')
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'C MangRing всё айс')
	if response.status_code == 404:
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + '@JJBrunoo, Домен MangRing ОТЪЕХАЛ!')


	response = requests.get("https://app169.liveapp.tech/")
	if response.status_code == 200:
		print('Success!')
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'C MagicRing всё айс')
	if response.status_code == 404:
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + '@JJBrunoo, Домен MagicRing ОТЪЕХАЛ!')


		response = requests.get("https://app177.liveapp.tech/")
	if response.status_code == 200:
		print('Success!')
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'C SoliankaRing всё айс')
	if response.status_code == 404:
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + '@JJBrunoo, Домен SoliankaRing ОТЪЕХАЛ!')

		response = requests.get("https://app174.liveapp.tech/")
	if response.status_code == 200:
		print('Success!')
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'C KIT Ring всё айс')
	if response.status_code == 404:
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + '@JJBrunoo, Домен KIT Ring ОТЪЕХАЛ!')

schedule.every().hour.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)