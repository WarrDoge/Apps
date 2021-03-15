import requests
import json
import schedule
import time

DATE_NOW = time.ctime()


def push_template(APPNAME, APIKEY, APPID, SEGMENT, PHEADER, PCONTENT):

    header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic " + APIKEY + " "}

    payload = {"app_id": APPID,
           "included_segments": SEGMENT,
           "headings":  PHEADER,
           "contents":  PCONTENT

                         }

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

    print(req.status_code, req.reason)

    if req.status_code == 200:
      
        requests.post("https://api.telegram.org/bot804769924:AAFShtkmrrUZJ5i4E5vZZSdbiS4lWZj2Aj8/sendMessage?chat_id=-474130414&text=" + "Пуши отправлены, прилка - " + APPNAME + "\n\n " + str(PHEADER.items()) + "\n\n" + str(PCONTENT.items()) )
    else:
        requests.post("https://api.telegram.org/bot804769924:AAFShtkmrrUZJ5i4E5vZZSdbiS4lWZj2Aj8/sendMessage?chat_id=-474130414&text=" + "Какие-то проблемы с пушем на прилке " + APPNAME + " Пуши за " + DATE_NOW + " не отправлены!")





