import requests
import time
import schedule
###########################################################################################
check_list = list()
########################################################################################### 
def check():
	requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=' + 'Чекаю апрув приложений...')
###########################################################################################	
def job(appname, applink):
	response = requests.get(applink)
	if response.status_code == 200 and str(appname) not in str(check_list):
		requests.post('https://api.telegram.org/bot1329396156:AAEtTOXNO0VeaxOe_nfkqPjY0X8AeRkVP3M/sendMessage?chat_id=-481312488&text=@pirogSmakom, Приложение '+appname+' вышло в плеймаркет!')
		check_list.append(appname)
	else:
		pass
############################################################################################
# Шаблон ссылки:
# https://play.google.com/store/apps/details?id=
###############

appname1 = "Tiger Treasure"
applink1 = "https://play.google.com/store/apps/details?id=space.moongame.gpw.twa"
##########
def job1():
	job(appname1, applink1) 
schedule.every(2).hours.do(job1)

###############

# appname2 = "Gnome Corporation"
# applink2 = "https://play.google.com/store/apps/details?id=space.artgame.gpp.twa"
# ##########
# def job2():
# 	job(appname2, applink2) 
# schedule.every(2).hours.do(job2)

###############

appname3 = "Pirate Ship"
applink3 = "https://play.google.com/store/apps/details?id=space.torularankin.gpa.twa"
##########
def job3():
	job(appname3, applink3) 
schedule.every(2).hours.do(job3)

###############

# appname4 = "Winning Robot"
# applink4 = "https://play.google.com/store/apps/details?id=space.smasheven.gpz.twa"
# ##########
# def job4():
# 	job(appname4, applink4)
# schedule.every(2).hours.do(job4)

###############

# appname5 = "Tiger Treasure"
# applink5 = "https://play.google.com/store/apps/details?id=space.moongame.gpw.twa"
# ##########
# def job5():
# 	job(appname5, applink5) 
# schedule.every(2).hours.do(job5)

# ###############

# appname6 = ""
# applink6 = "https://play.google.com/store/apps/details?id="
# ##########
# def job6():
# 	job(appname6, applink6) 
# schedule.every(2).hours.do(job6)

###############

# appname7 = ""
# applink7 = "https://play.google.com/store/apps/details?id="
# ##########
# def job7():
# 	job(appname7, applink7)
# schedule.every(2).hours.do(job7)

###############

# appname8 = ""
# applink8 = "https://play.google.com/store/apps/details?id="
# ##########
# def job8():
# 	job(appname8, applink8)
# schedule.every(2).hours.do(job8)

###############

# appname9 = ""
# applink9 = "https://play.google.com/store/apps/details?id="
# ##########
# def job9():
# 	job(appname9, applink9)
# schedule.every(2).hours.do(job9)

###############

# appname10 = ""
# applink10 = "https://play.google.com/store/apps/details?id="
# ##########
# def job10():
# 	job(appname10, applink10) 
# schedule.every(2).hours.do(job10)

###############

# appname11 = ""
# applink11 = "https://play.google.com/store/apps/details?id="
# ##########
# def job11():
# 	job(appname11, applink11) 
# schedule.every(2).hours.do(job11)

###############

# appname12 = ""
# applink12 = "https://play.google.com/store/apps/details?id="
# ##########
# def job12():
# 	job(appname12, applink12) 
# schedule.every(2).hours.do(job12)

###############

# appname13 = ""
# applink13 = "https://play.google.com/store/apps/details?id="
# ##########
# def job13():
# 	job(appname13, applink13) 
# schedule.every(2).hours.do(job13)

###############

# appname14 = ""
# applink14 = "https://play.google.com/store/apps/details?id="
# ##########
# def job14():
# 	job(appname14, applink14) 
# schedule.every(2).hours.do(job14)

###############

# appname15 = ""
# applink15 = "https://play.google.com/store/apps/details?id="
# ##########
# def job15():
# 	job(appname15, applink15) 
# schedule.every(2).hours.do(job15)

###############

# appname16 = ""
# applink16 = "https://play.google.com/store/apps/details?id="
# ##########
# def job16():
# 	job(appname16, applink16)
# schedule.every(2).hours.do(job16)

###############

# appname17 = ""
# applink17 = "https://play.google.com/store/apps/details?id="
# ##########
# def job17():
# 	job(appname17, applink17)
# schedule.every(2).hours.do(job17)

###############

# appname18 = ""
# applink18 = "https://play.google.com/store/apps/details?id="
# ##########
# def job18():
# 	job(appname18, applink18) 
# schedule.every(2).hours.do(job18)

###############

# appname19 = ""
# applink19 = "https://play.google.com/store/apps/details?id="
# ##########
# def job19():
# 	job(appname19, applink19) 
# schedule.every(2).hours.do(job19)

###############

# appname20 = ""
# applink20 = "https://play.google.com/store/apps/details?id="
# ##########
# def job20():
# 	job(appname20, applink20) 
# schedule.every(2).hours.do(job20)

###################################################################
schedule.every(30).minutes.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)