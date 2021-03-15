from push_template import *
from EU import *
from SNG import *


APPNAME = ""
APIKEY = ""
APPID = ""
SEGMENT_EU  = "EU"
SEGMENT_SNG  = "SNG"



############## EU_MONDAY_MORNING ###################

schedule.every().monday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_MONDAY_MORNING, EU_C_MONDAY_MORNING)

############## EU_MONDAY_EVENING ###################

schedule.every().monday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_MONDAY_EVENING, EU_C_MONDAY_EVENING)

############## EU_TUESDAY_MORNING ###################

schedule.every().tuesday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_TUESDAY_MORNING, EU_C_TUESDAY_MORNING)

############## EU_TUESDAY_EVENING ###################

schedule.every().tuesday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_TUESDAY_EVENING, EU_C_TUESDAY_EVENING)

############## EU_WEDNESDAY_MORNING ###################

schedule.every().wednesday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_WEDNESDAY_MORNING, EU_C_WEDNESDAY_MORNING)

############## EU_WEDNESDAY__EVENING ###################

schedule.every().wednesday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_WEDNESDAY_EVENING, EU_C_WEDNESDAY_EVENING)

############## EU_THURSDAY_MORNING ###################

schedule.every().thursday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_THURSDAY_MORNING, EU_C_THURSDAY_MORNING)

############## EU_THURSDAY__EVENING ###################

schedule.every().thursday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_THURSDAY_EVENING, EU_C_THURSDAY_EVENING)

############## EU_FRIDAY_MORNING ###################

schedule.every().friday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_C_FRIDAY_MORNING, EU_C_FRIDAY_MORNING)

############## EU_FRIDAY__EVENING ###################

schedule.every().friday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_FRIDAY_EVENING, EU_C_FRIDAY_EVENING)

############## EU_SATURDAY_MORNING ###################

schedule.every().saturday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_SATURDAY_MORNING, EU_C_SATURDAY_MORNING)

############## EU_SATURDAY__EVENING ###################

schedule.every().saturday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_SATURDAY_EVENING, EU_C_SATURDAY_EVENING)

############## EU_SUNDAY_MORNING ###################

schedule.every().sunday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_SUNDAY_MORNING, EU_C_SUNDAY_MORNING)

############## EU_SUNDAY__EVENING ###################

schedule.every().sunday.at(EU_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_SUNDAY_EVENING, EU_C_SUNDAY_EVENING)

###################################################################################################################################################

############## SNG_MONDAY_MORNING ###################

schedule.every().monday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_MONDAY_MORNING, SNG_C_MONDAY_MORNING)

############## SNG_MONDAY_EVENING ###################

schedule.every().monday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_MONDAY_EVENING, SNG_C_MONDAY_EVENING)

############## SNG_TUESDAY_MORNING ###################

schedule.every().tuesday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_TUESDAY_MORNING, SNG_C_TUESDAY_MORNING)

############## SNG_TUESDAY_EVENING ###################

schedule.every().tuesday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_TUESDAY_EVENING, SNG_C_TUESDAY_EVENING)

############## SNG_WEDNESDAY_MORNING ###################

schedule.every().wednesday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_WEDNESDAY_MORNING, SNG_C_WEDNESDAY_MORNING)

############## SNG_WEDNESDAY__EVENING ###################

schedule.every().wednesday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_WEDNESDAY_EVENING, SNG_C_WEDNESDAY_EVENING)

############## SNG_THURSDAY_MORNING ###################

schedule.every().thursday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_THURSDAY_MORNING, SNG_C_THURSDAY_MORNING)

############## SNG_THURSDAY__EVENING ###################

schedule.every().thursday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_THURSDAY_EVENING, SNG_C_THURSDAY_EVENING)

############## SNG_FRIDAY_MORNING ###################

schedule.every().friday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_C_FRIDAY_MORNING, SNG_C_FRIDAY_MORNING)

############## SNG_FRIDAY__EVENING ###################

schedule.every().friday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_FRIDAY_EVENING, SNG_C_FRIDAY_EVENING)

############## SNG_SATURDAY_MORNING ###################

schedule.every().saturday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_SATURDAY_MORNING, SNG_C_SATURDAY_MORNING)

############## SNG_SATURDAY__EVENING ###################

schedule.every().saturday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_SATURDAY_EVENING, SNG_C_SATURDAY_EVENING)

############## SNG_SUNDAY_MORNING ###################

schedule.every().sunday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_SUNDAY_MORNING, SNG_C_SUNDAY_MORNING)

############## SNG_SUNDAY__EVENING ###################

schedule.every().sunday.at(SNG_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_SUNDAY_EVENING, SNG_C_SUNDAY_EVENING)







while True:
    schedule.run_pending()
    time.sleep(1)



