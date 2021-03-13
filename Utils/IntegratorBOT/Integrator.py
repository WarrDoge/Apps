import requests
import json
from NewApp import *
#############################################
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
	'Content-Type': 'application/json',
}
data = '{"campaign_id":'+str(ringid)+',"type":"forced","name":"'+AppName+'","position":"1","action_options":null,"comments":null,"state":"active","schema":"action","action_type":"campaign","action_payload":"'+str(compid)+'","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_2","mode":"accept","payload":["'+str(subid2)+'"]}],"triggers":null,"landings":[],"offers":[]}'
response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
############################################################################################################################################################################################################## -> Main
# geo = "BE"
# offerid_1 = "247"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "AU"
# offerid_1 = "376"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "CA"
# offerid_1 = "274"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "CH"
# offerid_1 = "305"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "DE"
# offerid_1 = "179"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "FR"
# offerid_1 = "378"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "IE"
# offerid_1 = "375"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "IT"
# offerid_1 = "283"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "NO"
# offerid_1 = "157"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "PL"
# offerid_1 = "87"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "NZ"
# offerid_1 = "380"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "NL"
# offerid_1 = "380"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "RO"
# offerid_1 = "141"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "RU"
# offerid_1 = "99"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "UA"
# offerid_1 = "261"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "CL"
# offerid_1 = "284"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "CZ"
# offerid_1 = "381"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "KR"
# offerid_1 = "206"
# offerid_1_1 = "239"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":50,"state":"active"},{"offer_id":'+offerid_1_1+',"share":50,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "HU"
# offerid_1 = "379"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "NL"
# offerid_1 = "382"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "SK"
# offerid_1 = "342"
# offerid_1_1 = "341"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":50,"state":"active"},{"offer_id":'+offerid_1_1+',"share":50,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "LU"
# offerid_1 = "241"
# offerid_1_1 = "229"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":50,"state":"active"},{"offer_id":'+offerid_1_1+',"share":50,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
# #######################################################################################################
# geo = "PT"
# offerid_1 = "457"

# headers = {
# 	'accept': 'application/json',
# 	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
# 	'Content-Type': 'application/json',
# }

# data = '{"campaign_id":"300","type":"forced","name":"Trident / '+ geo +' / Main","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_6","mode":"accept","payload":["'+str(subid5)+'"]},{"id":0,"name":"country","mode":"accept","payload":["'+geo+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid_1+',"share":100,"state":"active"}]}'

# response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
##############################################################################################################################################################################################################
def job(response, subid2, AppName, form):
#################
	stream_list = list()
	for i in r:
		if 'sub_id_2' in str(i) and 'sub_id_3' in str(i):
############################################################################################			
			if i['filters'][0]['payload'][0][3:6] == str(int(subid2[3:6]) - 1):
				del i['id']
				for n in i['offers']:
					del n['id']
					del n['stream_id']
				offers = i['offers']
				for n in i['filters']:
					del n['id']
					del n['stream_id']				
				i['filters'][0]['payload'][0] = subid2
				i['filters'][1]['payload'][0] = i['filters'][1]['payload'][0].replace('_', form).replace('/', form).replace('-', form)
				name = i['name']
				name  = name.split('/')
				name[-1] = str(subid2[0:6].upper()) + '|' + str(AppName)
				name = str(name).replace(' ', '').replace('[', '').replace(']', '').replace("'", '').replace(',', ' / ').replace('|', ' ')
				i['name'] = name
				i.update(offers = offers)
				result = json.dumps(i)							
				if str(name).replace(' ', '') not in str(stream_list).replace(' ', ''):				
#############################################
					headers = {
						'accept': 'application/json',
						'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
						'Content-Type': 'application/json',
					}
					data = result
					response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
					stream_list.append(str(name.replace(' ', '')))	
					print(i['name'])								
############################################################################################			
			if i['filters'][1]['payload'][0][3:6] == str(int(subid2[3:6]) - 1):
				del i['id']
				for n in i['offers']:
					del n['id']
					del n['stream_id']		
				offers = i['offers']
				for n in i['filters']:
					del n['id']		
					del n['stream_id']								
				i['filters'][1]['payload'][0] = subid2
				i['filters'][0]['payload'][0] = i['filters'][0]['payload'][0].replace('_', form).replace('/', form).replace('-', form)
				name = i['name']
				name  = name.split('/')
				name[-1] = str(subid2[0:6].upper()) + '|' + str(AppName)
				name = str(name).replace(' ', '').replace('[', '').replace(']', '').replace("'", '').replace(',', ' / ').replace('|', ' ')
				i['name'] = name
				i.update(offers = offers)
				result = json.dumps(i)	
				if str(name).replace(' ', '') not in str(stream_list).replace(' ', ''):				
#############################################
					headers = {
						'accept': 'application/json',
						'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
						'Content-Type': 'application/json',
					}
					data = result
					response = requests.post('https://trackmeup.xyz/admin_api/v1/streams', headers=headers, data=data)
					stream_list.append(str(name.replace(' ', '')))	
					print(i['name'])
#######################################################################################################
print('Starting Sydney...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/309/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Tenerife...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/278/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Lemon...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/200/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Dubai...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/151/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Moskow...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/146/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting SecretVictory...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/32/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Graf...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/31/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Dem...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/24/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Anelin...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/20/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Iceman...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/13/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Finished!')