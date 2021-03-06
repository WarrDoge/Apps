import requests
import json
#################
webid = 32
Stream_Name = "WINSPARK / BE / CPA /"
#######
offer_id_1 = 215
offer_id_2 = 458
offer_id_3 = 458
share_1 = 50
share_2 = 50
share_3 = 50
#######
starting_num = 290
final_num = 500
#################
print('Starting!')
headers = {
    'accept': 'application/json',
    'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
#################
r = json.loads(response.text)
stream_list = list()
for i in r:
	if str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
		m = starting_num
		n = final_num
		while m <= n:
			if 'app'+str(m) in str(i):
				stream_list.append(i['id'])		
			m = m + 1		
#################
for i in stream_list:
	headers = {
	    'accept': 'application/json',
	    'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
	}
	response = requests.get('https://trackmeup.xyz/admin_api/v1/streams/'+str(i)+'', headers=headers)
	r = json.loads(response.text)
	r.update(offers = [{'offer_id': offer_id_1, 'share': share_1, 'state': 'active'},{'offer_id': offer_id_2, 'share': share_2, 'state': 'active'},{'offer_id': offer_id_3, 'share': share_3, 'state': 'active'}])
	name = r['name']
	r = json.dumps(r)
	#################
	headers = {
	    'accept': 'application/json',
	    'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
	    'Content-Type': 'application/json',
	}
	#################
	data = r
	response = requests.put('https://trackmeup.xyz/admin_api/v1/streams/'+str(i)+'', headers=headers, data=data)
################
	print(name)
print('Finished!')
################
print('Starting test...')
headers = {
    'accept': 'application/json',
    'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
r = json.loads(response.text)
for i in r:
	if str(i['offers']) == str([{'offer_id': offer_id_1, 'share': share_1, 'state': 'active'},{'offer_id': offer_id_2, 'share': share_2, 'state': 'active'},{'offer_id': offer_id_3, 'share': share_3, 'state': 'active'}]):
		pass
	else: 
		print(str(i['name']) + ' Не изменился!')	
print('Done testing!')	
################
print('Starting test...')
headers = {
    'accept': 'application/json',
    'Api-Key': 'f3ed6f01f93ecd9591cdaddf98649b14',
}
response = requests.get('https://trackmeup.xyz/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
r = json.loads(response.text)
stream_list = list()
for i in r:
	if str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
		m = starting_num
		n = final_num
		while m <= n:
			if 'app'+str(m) in str(i) and str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
				stream_list.append(i)		
			m = m + 1	
for i in stream_list:
	if str(i['offers'][0]['offer_id']) == str(offer_id_1) and str(i['offers'][1]['offer_id']) == str(offer_id_2) and str(i['offers'][2]['offer_id']) == str(offer_id_3):
		pass
	else: 
		print(str(i['name']) + ' Не изменился!')	
print('Done testing!')