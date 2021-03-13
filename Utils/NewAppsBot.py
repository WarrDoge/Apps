import requests
import json
import schedule
import time
###################################################################
blacklist = list()
###################################################################
headers = {
    'accept': 'application/json',
    'authorization': 'Basic NTA6dkNfUU9NR0lSMkhCWGcxQ2t0a2k5N2dKR2dNWW96ZEU=',
}
response = requests.get('https://uclient.skakapp.com/api/app/list-available', headers=headers)
old = json.loads(response.text)
old = old.get('items')
for i in old:
	if str(i['category']) == str('GAMBLING'):
		blacklist.append(i['name'])	
###################################################################	
def job():
###################################################################
	headers = {
	    'accept': 'application/json',
	    'authorization': 'Basic NTA6dkNfUU9NR0lSMkhCWGcxQ2t0a2k5N2dKR2dNWW96ZEU=',
	}
	params = (
	    ('active', '0'),
	)
	response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
	deleted = json.loads(response.text)
	deleted = deleted.get('items')
###################################################################
	headers = {
	    'accept': 'application/json',
	    'authorization': 'Basic NTA6dkNfUU9NR0lSMkhCWGcxQ2t0a2k5N2dKR2dNWW96ZEU=',
	}
	params = (
	    ('active', '1'),
	)
	response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
	active = json.loads(response.text)
	active = active.get('items')
###################################################################
	headers = {
	    'accept': 'application/json',
	    'authorization': 'Basic NTA6dkNfUU9NR0lSMkhCWGcxQ2t0a2k5N2dKR2dNWW96ZEU=',
	}
	response = requests.get('https://uclient.skakapp.com/api/app/list-available', headers=headers)
	appdata = json.loads(response.text)
	appdata = appdata.get('items')
	i = 0
	while i <= len(appdata) - 1:
		if 'GAMBLING' in appdata[i].get('category'):
			if appdata[i].get('name') not in str(deleted) and appdata[i].get('name') not in str(active) and appdata[i].get('name') not in str(blacklist):
				requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=@JJBrunoo, @pirogSmakom, @mark_first_cpa, @Richi_RT,  SkakApp добавил приложение! '+appdata[i].get('name')+'')
			else:
				print('Checking...')
			i = i + 1
		else:
			i = i + 1			
###################################################################
def check():
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=Чекаю Скаков...')
###################################################################
schedule.every(10).seconds.do(job)
schedule.every(5).minutes.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)