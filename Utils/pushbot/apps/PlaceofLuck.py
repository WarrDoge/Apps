import sys
sys.path.insert(1, "/root/pushbot/")

from templates.push_template import *
from segments.EU import *
from segments.SNG import *
from segments.KZ import *
from segments.AZ import *
from segments.KR import *
from segments.AU import *


APPNAME = "PlaceofLuck"
APIKEY = "YjRkNmJmNjAtYWIxNi00ZWZiLTkwZjgtYWIwOTY0NThlOGQ3"
APPID = "173e5067-0bb2-49b2-8ea5-3c505e2b3381"
SEGMENT_EU  = "EU"
SEGMENT_SNG  = "SNG"
SEGMENT_KZ  = "KZ"
SEGMENT_AZ  = "AZ"
SEGMENT_KR  = "KR"
SEGMENT_AU  = "AU"


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

schedule.every().friday.at(EU_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_EU, EU_H_FRIDAY_MORNING, EU_C_FRIDAY_MORNING)

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

schedule.every().friday.at(SNG_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_SNG, SNG_H_FRIDAY_MORNING, SNG_C_FRIDAY_MORNING)

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

###################################################################################################################################################

############## KZ_MONDAY_MORNING ###################

schedule.every().monday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_MONDAY_MORNING, KZ_C_MONDAY_MORNING)

############## KZ_MONDAY_EVENING ###################

schedule.every().monday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_MONDAY_EVENING, KZ_C_MONDAY_EVENING)

############## KZ_TUESDAY_MORNING ###################

schedule.every().tuesday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_TUESDAY_MORNING, KZ_C_TUESDAY_MORNING)

############## KZ_TUESDAY_EVENING ###################

schedule.every().tuesday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_TUESDAY_EVENING, KZ_C_TUESDAY_EVENING)

############## KZ_WEDNESDAY_MORNING ###################

schedule.every().wednesday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_WEDNESDAY_MORNING, KZ_C_WEDNESDAY_MORNING)

############## KZ_WEDNESDAY__EVENING ###################

schedule.every().wednesday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_WEDNESDAY_EVENING, KZ_C_WEDNESDAY_EVENING)

############## KZ_THURSDAY_MORNING ###################

schedule.every().thursday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_THURSDAY_MORNING, KZ_C_THURSDAY_MORNING)

############## KZ_THURSDAY__EVENING ###################

schedule.every().thursday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_THURSDAY_EVENING, KZ_C_THURSDAY_EVENING)

############## KZ_FRIDAY_MORNING ###################

schedule.every().friday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_FRIDAY_MORNING, KZ_C_FRIDAY_MORNING)

############## KZ_FRIDAY__EVENING ###################

schedule.every().friday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_FRIDAY_EVENING, KZ_C_FRIDAY_EVENING)

############## KZ_SATURDAY_MORNING ###################

schedule.every().saturday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SATURDAY_MORNING, KZ_C_SATURDAY_MORNING)

############## KZ_SATURDAY__EVENING ###################

schedule.every().saturday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SATURDAY_EVENING, KZ_C_SATURDAY_EVENING)

############## KZ_SUNDAY_MORNING ###################

schedule.every().sunday.at(KZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SUNDAY_MORNING, KZ_C_SUNDAY_MORNING)

############## KZ_SUNDAY__EVENING ###################

schedule.every().sunday.at(KZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SUNDAY_EVENING, KZ_C_SUNDAY_EVENING)

###################################################################################################################################################

############## KZ_MONDAY__NOON ###################

schedule.every().monday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_MONDAY_NOON, KZ_C_MONDAY_NOON)

############## KZ_TUESDAY_NOON ###################

schedule.every().tuesday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_TUESDAY_NOON, KZ_C_TUESDAY_NOON)

############## KZ_WEDNESDAY_NOON ###################

schedule.every().wednesday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_WEDNESDAY_NOON, KZ_C_WEDNESDAY_NOON)

############## KZ_THURSDAY_NOON ###################

schedule.every().thursday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_THURSDAY_NOON, KZ_C_THURSDAY_NOON)

############## KZ_FRIDAY_NOON ###################

schedule.every().friday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_FRIDAY_NOON, KZ_C_FRIDAY_NOON)

############## KZ_SATURDAY_NOON ###################

schedule.every().saturday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SATURDAY_NOON, KZ_C_SATURDAY_NOON)

############## KZ_SUNDAY_NOON ###################

schedule.every().sunday.at(KZ_NOON_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KZ, KZ_H_SUNDAY_NOON, KZ_C_SUNDAY_NOON)

###################################################################################################################################################

############## AZ_MONDAY_MORNING ###################

schedule.every().monday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_MONDAY_MORNING, AZ_C_MONDAY_MORNING)

############## AZ_MONDAY_EVENING ###################

schedule.every().monday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_MONDAY_EVENING, AZ_C_MONDAY_EVENING)

############## AZ_TUESDAY_MORNING ###################

schedule.every().tuesday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_TUESDAY_MORNING, AZ_C_TUESDAY_MORNING)

############## AZ_TUESDAY_EVENING ###################

schedule.every().tuesday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_TUESDAY_EVENING, AZ_C_TUESDAY_EVENING)

############## AZ_WEDNESDAY_MORNING ###################

schedule.every().wednesday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_WEDNESDAY_MORNING, AZ_C_WEDNESDAY_MORNING)

############## AZ_WEDNESDAY__EVENING ###################

schedule.every().wednesday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_WEDNESDAY_EVENING, AZ_C_WEDNESDAY_EVENING)

############## AZ_THURSDAY_MORNING ###################

schedule.every().thursday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_THURSDAY_MORNING, AZ_C_THURSDAY_MORNING)

############## AZ_THURSDAY__EVENING ###################

schedule.every().thursday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_THURSDAY_EVENING, AZ_C_THURSDAY_EVENING)

############## AZ_FRIDAY_MORNING ###################

schedule.every().friday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_FRIDAY_MORNING, AZ_C_FRIDAY_MORNING)

############## AZ_FRIDAY__EVENING ###################

schedule.every().friday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_FRIDAY_EVENING, AZ_C_FRIDAY_EVENING)

############## AZ_SATURDAY_MORNING ###################

schedule.every().saturday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_SATURDAY_MORNING, AZ_C_SATURDAY_MORNING)

############## AZ_SATURDAY__EVENING ###################

schedule.every().saturday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_SATURDAY_EVENING, AZ_C_SATURDAY_EVENING)

############## AZ_SUNDAY_MORNING ###################

schedule.every().sunday.at(AZ_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_SUNDAY_MORNING, AZ_C_SUNDAY_MORNING)

############## AZ_SUNDAY__EVENING ###################

schedule.every().sunday.at(AZ_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_AZ, AZ_H_SUNDAY_EVENING, AZ_C_SUNDAY_EVENING)

###################################################################################################################################################

############## KR_MONDAY_EVENING ###################

schedule.every().monday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_MONDAY_EVENING, KR_C_MONDAY_EVENING)

############## KR_TUESDAY_MORNING ###################

schedule.every().tuesday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_TUESDAY_MORNING, KR_C_TUESDAY_MORNING)

############## KR_TUESDAY_EVENING ###################

schedule.every().tuesday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_TUESDAY_EVENING, KR_C_TUESDAY_EVENING)

############## KR_WEDNESDAY_MORNING ###################

schedule.every().wednesday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_WEDNESDAY_MORNING, KR_C_WEDNESDAY_MORNING)

############## KR_WEDNESDAY__EVENING ###################

schedule.every().wednesday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_WEDNESDAY_EVENING, KR_C_WEDNESDAY_EVENING)

############## KR_THURSDAY_MORNING ###################

schedule.every().thursday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_THURSDAY_MORNING, KR_C_THURSDAY_MORNING)

############## KR_THURSDAY__EVENING ###################

schedule.every().thursday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_THURSDAY_EVENING, KR_C_THURSDAY_EVENING)

############## KR_FRIDAY_MORNING ###################

schedule.every().friday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_FRIDAY_MORNING, KR_C_FRIDAY_MORNING)

############## KR_FRIDAY__EVENING ###################

schedule.every().friday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_FRIDAY_EVENING, KR_C_FRIDAY_EVENING)

############## KR_SATURDAY_MORNING ###################

schedule.every().saturday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_SATURDAY_MORNING, KR_C_SATURDAY_MORNING)

############## KR_SATURDAY__EVENING ###################

schedule.every().saturday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_SATURDAY_EVENING, KR_C_SATURDAY_EVENING)

############## KR_SUNDAY_MORNING ###################

schedule.every().sunday.at(KR_DAY_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_SUNDAY_MORNING, KR_C_SUNDAY_MORNING)

############## KR_SUNDAY__EVENING ###################

schedule.every().sunday.at(KR_EVENING_TIME).do(push_template, APPNAME, APIKEY, APPID, SEGMENT_KR, KR_H_SUNDAY_EVENING, KR_C_SUNDAY_EVENING)

###################################################################################################################################################






while True:
    schedule.run_pending()
    time.sleep(1)



