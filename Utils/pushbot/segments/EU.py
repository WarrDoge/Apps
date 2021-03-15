### EU SEGMENT ######
from deep_translator import GoogleTranslator
import time
import json
####################
class push_class(dict):
    def __str__(self):
        return json.dumps(self)
####################
EU_DAY_TIME = "11:00"
EU_EVENING_TIME = "20:00"
####################
HMM = '🎁 Bonus 100% to the deposit 💪'
CMM = 'Make a deposit and receive a bonus of 100% 💸 + 70 FREE spins 🎰 Good luck to you 🤑'
#########
HME = '🤑 Evening Madness 🤑'
CME = '🎰 Chance jackpot doubled to 2 hours! 💰 make a deposit and take the treasure mummy! 👍'
#########
HTM = '🔥 This is your chance of success! 🔥'
CTM = '👉 Luck is near and ready to please you 🎁'
#########
HTE = 'Bambaem.islam won the jackpot 👍'
CTE = '640 000 thousand in the Book Of Ra. Only 3 jackpots left! 💵'
#########
HWM = '🔥 Hurry up and register! 🔥'
CWM = '💥 100%  first deposit bonus just NOW! 💥'
#########
HWE = 'Evening bonus 🎁'
CWE = 'Chance of jackpot is increased 2 times 💵 Make a deposit and receive 100 free spins + 100% to deposit 😎'
#########
HTHM = 'Azamat777 won the JACKPOT! 🤑'
CTHM = 'Jammin_Jarz won 234 549 thousand. Make a deposit and win! 💵'
#########
HTHE = '🤨 🤨Hadn\'t had time to pick up a bonus?'
CTHE = '🕔 Only 15 minutes are remaining. Take 100% bonus to DEPOSIT and 100 FREE SPINS 🎰'
#########
HFM = '💥 RISE UP AND SHINE! 🌠'
CFM = '☄️ Winning percentage is exceeding today! 💥'
#########
HFE = 'Magomegov.samir93 won the jackpot 🤑'
CFE = '507 768 thousand JACKPOT has been won the game Book Of Ra! 💵 Claim your JACKPOT now! 💸'
##########
HSM = '🔥 This is your chance of SUCCESS! 🔥'
CSM = '👉 Luck is here and ready to please you 🎁'
##########
HSE = 'Right NOW is the maximal chance of winning 💸'
CSE = 'Make a deposit and get x2 BONUS and 100 FREE SPINS 🎁 Good luck to you 🤑'
##########
HSNM = '🍀 Odds of winning have increased by 3 times! 🍀'
CSNM = '👉 Come on, join and start winning RIGHT NOW! 🎰'
##########
HSNE = 'Rafaello22 won the JACKPOT! 🎰'
CSNE = 'Jammin_Jarz won 234 549 thousand. Make a deposit and win! 💵'
# ####################
# HMM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HMM)
# CMM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CMM)
# ##########
# HME_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HME)
# CME_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CME)
# ##########
# HTM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HTM)
# CTM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CTM)
# ##########
# HTE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HTE)
# CTE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CTE)
# ##########
# HWM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HWM)
# CWM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CWM)
# ##########
# HWE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HWE)
# CWE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CWE)
# ##########
# HTHM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HTHM)
# CTHM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CTHM)
# ##########
# HTHE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HTHE)
# CTHE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CTHE)
# ##########
# HFM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HFM)
# CFM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CFM)
# ##########
# HFE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HFE)
# CFE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CFM)
# ##########
# HSM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HSM)
# CSM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CSM)
# ##########
# HSE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HSE)
# CSE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CSE)
# ##########
# HSNM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HSNM)
# CSNM_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CSNM)
# ##########
# HSNE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=HSNE)
# CSNE_LANG = GoogleTranslator(source="en", target="LANG").translate(text=CSNE)
# ####################
####################
HMM_it = GoogleTranslator(source="en", target="it").translate(text=HMM)
CMM_it = GoogleTranslator(source="en", target="it").translate(text=CMM)
##########
HME_it = GoogleTranslator(source="en", target="it").translate(text=HME)
CME_it = GoogleTranslator(source="en", target="it").translate(text=CME)
# time.sleep(5)
##########
HTM_it = GoogleTranslator(source="en", target="it").translate(text=HTM)
CTM_it = GoogleTranslator(source="en", target="it").translate(text=CTM)
##########
HTE_it = GoogleTranslator(source="en", target="it").translate(text=HTE)
CTE_it = GoogleTranslator(source="en", target="it").translate(text=CTE)
# time.sleep(5)
##########
HWM_it = GoogleTranslator(source="en", target="it").translate(text=HWM)
CWM_it = GoogleTranslator(source="en", target="it").translate(text=CWM)
##########
HWE_it = GoogleTranslator(source="en", target="it").translate(text=HWE)
CWE_it = GoogleTranslator(source="en", target="it").translate(text=CWE)
# time.sleep(5)
##########
HTHM_it = GoogleTranslator(source="en", target="it").translate(text=HTHM)
CTHM_it = GoogleTranslator(source="en", target="it").translate(text=CTHM)
##########
HTHE_it = GoogleTranslator(source="en", target="it").translate(text=HTHE)
CTHE_it = GoogleTranslator(source="en", target="it").translate(text=CTHE)
# time.sleep(5)
##########
HFM_it = GoogleTranslator(source="en", target="it").translate(text=HFM)
CFM_it = GoogleTranslator(source="en", target="it").translate(text=CFM)
##########
HFE_it = GoogleTranslator(source="en", target="it").translate(text=HFE)
CFE_it = GoogleTranslator(source="en", target="it").translate(text=CFM)
# time.sleep(5)
##########
HSM_it = GoogleTranslator(source="en", target="it").translate(text=HSM)
CSM_it = GoogleTranslator(source="en", target="it").translate(text=CSM)
##########
HSE_it = GoogleTranslator(source="en", target="it").translate(text=HSE)
CSE_it = GoogleTranslator(source="en", target="it").translate(text=CSE)
# time.sleep(5)
##########
HSNM_it = GoogleTranslator(source="en", target="it").translate(text=HSNM)
CSNM_it = GoogleTranslator(source="en", target="it").translate(text=CSNM)
##########
HSNE_it = GoogleTranslator(source="en", target="it").translate(text=HSNE)
CSNE_it = GoogleTranslator(source="en", target="it").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_fr = GoogleTranslator(source="en", target="fr").translate(text=HMM)
CMM_fr = GoogleTranslator(source="en", target="fr").translate(text=CMM)
##########
HME_fr = GoogleTranslator(source="en", target="fr").translate(text=HME)
CME_fr = GoogleTranslator(source="en", target="fr").translate(text=CME)
# time.sleep(5)
##########
HTM_fr = GoogleTranslator(source="en", target="fr").translate(text=HTM)
CTM_fr = GoogleTranslator(source="en", target="fr").translate(text=CTM)
##########
HTE_fr = GoogleTranslator(source="en", target="fr").translate(text=HTE)
CTE_fr = GoogleTranslator(source="en", target="fr").translate(text=CTE)
# time.sleep(5)
##########
HWM_fr = GoogleTranslator(source="en", target="fr").translate(text=HWM)
CWM_fr = GoogleTranslator(source="en", target="fr").translate(text=CWM)
##########
HWE_fr = GoogleTranslator(source="en", target="fr").translate(text=HWE)
CWE_fr = GoogleTranslator(source="en", target="fr").translate(text=CWE)
# time.sleep(5)
##########
HTHM_fr = GoogleTranslator(source="en", target="fr").translate(text=HTHM)
CTHM_fr = GoogleTranslator(source="en", target="fr").translate(text=CTHM)
##########
HTHE_fr = GoogleTranslator(source="en", target="fr").translate(text=HTHE)
CTHE_fr = GoogleTranslator(source="en", target="fr").translate(text=CTHE)
# time.sleep(5)
##########
HFM_fr = GoogleTranslator(source="en", target="fr").translate(text=HFM)
CFM_fr = GoogleTranslator(source="en", target="fr").translate(text=CFM)
##########
HFE_fr = GoogleTranslator(source="en", target="fr").translate(text=HFE)
CFE_fr = GoogleTranslator(source="en", target="fr").translate(text=CFM)
# time.sleep(5)
##########
HSM_fr = GoogleTranslator(source="en", target="fr").translate(text=HSM)
CSM_fr = GoogleTranslator(source="en", target="fr").translate(text=CSM)
##########
HSE_fr = GoogleTranslator(source="en", target="fr").translate(text=HSE)
CSE_fr = GoogleTranslator(source="en", target="fr").translate(text=CSE)
# time.sleep(5)
##########
HSNM_fr = GoogleTranslator(source="en", target="fr").translate(text=HSNM)
CSNM_fr = GoogleTranslator(source="en", target="fr").translate(text=CSNM)
##########
HSNE_fr = GoogleTranslator(source="en", target="fr").translate(text=HSNE)
CSNE_fr = GoogleTranslator(source="en", target="fr").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_sk = GoogleTranslator(source="en", target="sk").translate(text=HMM)
CMM_sk = GoogleTranslator(source="en", target="sk").translate(text=CMM)
##########
HME_sk = GoogleTranslator(source="en", target="sk").translate(text=HME)
CME_sk = GoogleTranslator(source="en", target="sk").translate(text=CME)
# time.sleep(5)
##########
HTM_sk = GoogleTranslator(source="en", target="sk").translate(text=HTM)
CTM_sk = GoogleTranslator(source="en", target="sk").translate(text=CTM)
##########
HTE_sk = GoogleTranslator(source="en", target="sk").translate(text=HTE)
CTE_sk = GoogleTranslator(source="en", target="sk").translate(text=CTE)
# time.sleep(5)
##########
HWM_sk = GoogleTranslator(source="en", target="sk").translate(text=HWM)
CWM_sk = GoogleTranslator(source="en", target="sk").translate(text=CWM)
##########
HWE_sk = GoogleTranslator(source="en", target="sk").translate(text=HWE)
CWE_sk = GoogleTranslator(source="en", target="sk").translate(text=CWE)
# time.sleep(5)
##########
HTHM_sk = GoogleTranslator(source="en", target="sk").translate(text=HTHM)
CTHM_sk = GoogleTranslator(source="en", target="sk").translate(text=CTHM)
##########
HTHE_sk = GoogleTranslator(source="en", target="sk").translate(text=HTHE)
CTHE_sk = GoogleTranslator(source="en", target="sk").translate(text=CTHE)
# time.sleep(5)
##########
HFM_sk = GoogleTranslator(source="en", target="sk").translate(text=HFM)
CFM_sk = GoogleTranslator(source="en", target="sk").translate(text=CFM)
##########
HFE_sk = GoogleTranslator(source="en", target="sk").translate(text=HFE)
CFE_sk = GoogleTranslator(source="en", target="sk").translate(text=CFM)
# time.sleep(5)
##########
HSM_sk = GoogleTranslator(source="en", target="sk").translate(text=HSM)
CSM_sk = GoogleTranslator(source="en", target="sk").translate(text=CSM)
##########
HSE_sk = GoogleTranslator(source="en", target="sk").translate(text=HSE)
CSE_sk = GoogleTranslator(source="en", target="sk").translate(text=CSE)
# time.sleep(5)
##########
HSNM_sk = GoogleTranslator(source="en", target="sk").translate(text=HSNM)
CSNM_sk = GoogleTranslator(source="en", target="sk").translate(text=CSNM)
##########
HSNE_sk = GoogleTranslator(source="en", target="sk").translate(text=HSNE)
CSNE_sk = GoogleTranslator(source="en", target="sk").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_hu = GoogleTranslator(source="en", target="hu").translate(text=HMM)
CMM_hu = GoogleTranslator(source="en", target="hu").translate(text=CMM)
##########
HME_hu = GoogleTranslator(source="en", target="hu").translate(text=HME)
CME_hu = GoogleTranslator(source="en", target="hu").translate(text=CME)
# time.sleep(5)
##########
HTM_hu = GoogleTranslator(source="en", target="hu").translate(text=HTM)
CTM_hu = GoogleTranslator(source="en", target="hu").translate(text=CTM)
##########
HTE_hu = GoogleTranslator(source="en", target="hu").translate(text=HTE)
CTE_hu = GoogleTranslator(source="en", target="hu").translate(text=CTE)
# time.sleep(5)
##########
HWM_hu = GoogleTranslator(source="en", target="hu").translate(text=HWM)
CWM_hu = GoogleTranslator(source="en", target="hu").translate(text=CWM)
##########
HWE_hu = GoogleTranslator(source="en", target="hu").translate(text=HWE)
CWE_hu = GoogleTranslator(source="en", target="hu").translate(text=CWE)
# time.sleep(5)
##########
HTHM_hu = GoogleTranslator(source="en", target="hu").translate(text=HTHM)
CTHM_hu = GoogleTranslator(source="en", target="hu").translate(text=CTHM)
##########
HTHE_hu = GoogleTranslator(source="en", target="hu").translate(text=HTHE)
CTHE_hu = GoogleTranslator(source="en", target="hu").translate(text=CTHE)
# time.sleep(5)
##########
HFM_hu = GoogleTranslator(source="en", target="hu").translate(text=HFM)
CFM_hu = GoogleTranslator(source="en", target="hu").translate(text=CFM)
##########
HFE_hu = GoogleTranslator(source="en", target="hu").translate(text=HFE)
CFE_hu = GoogleTranslator(source="en", target="hu").translate(text=CFM)
# time.sleep(5)
##########
HSM_hu = GoogleTranslator(source="en", target="hu").translate(text=HSM)
CSM_hu = GoogleTranslator(source="en", target="hu").translate(text=CSM)
##########
HSE_hu = GoogleTranslator(source="en", target="hu").translate(text=HSE)
CSE_hu = GoogleTranslator(source="en", target="hu").translate(text=CSE)
# time.sleep(5)
##########
HSNM_hu = GoogleTranslator(source="en", target="hu").translate(text=HSNM)
CSNM_hu = GoogleTranslator(source="en", target="hu").translate(text=CSNM)
##########
HSNE_hu = GoogleTranslator(source="en", target="hu").translate(text=HSNE)
CSNE_hu = GoogleTranslator(source="en", target="hu").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_cs = GoogleTranslator(source="en", target="cs").translate(text=HMM)
CMM_cs = GoogleTranslator(source="en", target="cs").translate(text=CMM)
##########
HME_cs = GoogleTranslator(source="en", target="cs").translate(text=HME)
CME_cs = GoogleTranslator(source="en", target="cs").translate(text=CME)
# time.sleep(5)
##########
HTM_cs = GoogleTranslator(source="en", target="cs").translate(text=HTM)
CTM_cs = GoogleTranslator(source="en", target="cs").translate(text=CTM)
##########
HTE_cs = GoogleTranslator(source="en", target="cs").translate(text=HTE)
CTE_cs = GoogleTranslator(source="en", target="cs").translate(text=CTE)
# time.sleep(5)
##########
HWM_cs = GoogleTranslator(source="en", target="cs").translate(text=HWM)
CWM_cs = GoogleTranslator(source="en", target="cs").translate(text=CWM)
##########
HWE_cs = GoogleTranslator(source="en", target="cs").translate(text=HWE)
CWE_cs = GoogleTranslator(source="en", target="cs").translate(text=CWE)
# time.sleep(5)
##########
HTHM_cs = GoogleTranslator(source="en", target="cs").translate(text=HTHM)
CTHM_cs = GoogleTranslator(source="en", target="cs").translate(text=CTHM)
##########
HTHE_cs = GoogleTranslator(source="en", target="cs").translate(text=HTHE)
CTHE_cs = GoogleTranslator(source="en", target="cs").translate(text=CTHE)
# time.sleep(5)
##########
HFM_cs = GoogleTranslator(source="en", target="cs").translate(text=HFM)
CFM_cs = GoogleTranslator(source="en", target="cs").translate(text=CFM)
# time.sleep(5)
##########
HFE_cs = GoogleTranslator(source="en", target="cs").translate(text=HFE)
CFE_cs = GoogleTranslator(source="en", target="cs").translate(text=CFM)
##########
HSM_cs = GoogleTranslator(source="en", target="cs").translate(text=HSM)
CSM_cs = GoogleTranslator(source="en", target="cs").translate(text=CSM)
# time.sleep(5)
##########
HSE_cs = GoogleTranslator(source="en", target="cs").translate(text=HSE)
CSE_cs = GoogleTranslator(source="en", target="cs").translate(text=CSE)
##########
HSNM_cs = GoogleTranslator(source="en", target="cs").translate(text=HSNM)
CSNM_cs = GoogleTranslator(source="en", target="cs").translate(text=CSNM)
# time.sleep(5)
##########
HSNE_cs = GoogleTranslator(source="en", target="cs").translate(text=HSNE)
CSNE_cs = GoogleTranslator(source="en", target="cs").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_de = GoogleTranslator(source="en", target="de").translate(text=HMM)
CMM_de = GoogleTranslator(source="en", target="de").translate(text=CMM)
##########
HME_de = GoogleTranslator(source="en", target="de").translate(text=HME)
CME_de = GoogleTranslator(source="en", target="de").translate(text=CME)
# time.sleep(5)
##########
HTM_de = GoogleTranslator(source="en", target="de").translate(text=HTM)
CTM_de = GoogleTranslator(source="en", target="de").translate(text=CTM)
##########
HTE_de = GoogleTranslator(source="en", target="de").translate(text=HTE)
CTE_de = GoogleTranslator(source="en", target="de").translate(text=CTE)
# time.sleep(5)
##########
HWM_de = GoogleTranslator(source="en", target="de").translate(text=HWM)
CWM_de = GoogleTranslator(source="en", target="de").translate(text=CWM)
##########
HWE_de = GoogleTranslator(source="en", target="de").translate(text=HWE)
CWE_de = GoogleTranslator(source="en", target="de").translate(text=CWE)
# time.sleep(5)
##########
HTHM_de = GoogleTranslator(source="en", target="de").translate(text=HTHM)
CTHM_de = GoogleTranslator(source="en", target="de").translate(text=CTHM)
##########
HTHE_de = GoogleTranslator(source="en", target="de").translate(text=HTHE)
CTHE_de = GoogleTranslator(source="en", target="de").translate(text=CTHE)
# time.sleep(5)
##########
HFM_de = GoogleTranslator(source="en", target="de").translate(text=HFM)
CFM_de = GoogleTranslator(source="en", target="de").translate(text=CFM)
##########
HFE_de = GoogleTranslator(source="en", target="de").translate(text=HFE)
CFE_de = GoogleTranslator(source="en", target="de").translate(text=CFM)
# time.sleep(5)
##########
HSM_de = GoogleTranslator(source="en", target="de").translate(text=HSM)
CSM_de = GoogleTranslator(source="en", target="de").translate(text=CSM)
##########
HSE_de = GoogleTranslator(source="en", target="de").translate(text=HSE)
CSE_de = GoogleTranslator(source="en", target="de").translate(text=CSE)
# time.sleep(5)
##########
HSNM_de = GoogleTranslator(source="en", target="de").translate(text=HSNM)
CSNM_de = GoogleTranslator(source="en", target="de").translate(text=CSNM)
##########
HSNE_de = GoogleTranslator(source="en", target="de").translate(text=HSNE)
CSNE_de = GoogleTranslator(source="en", target="de").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_ga = GoogleTranslator(source="en", target="ga").translate(text=HMM)
CMM_ga = GoogleTranslator(source="en", target="ga").translate(text=CMM)
##########
HME_ga = GoogleTranslator(source="en", target="ga").translate(text=HME)
CME_ga = GoogleTranslator(source="en", target="ga").translate(text=CME)
# time.sleep(5)
##########
HTM_ga = GoogleTranslator(source="en", target="ga").translate(text=HTM)
CTM_ga = GoogleTranslator(source="en", target="ga").translate(text=CTM)
##########
HTE_ga = GoogleTranslator(source="en", target="ga").translate(text=HTE)
CTE_ga = GoogleTranslator(source="en", target="ga").translate(text=CTE)
# time.sleep(5)
##########
HWM_ga = GoogleTranslator(source="en", target="ga").translate(text=HWM)
CWM_ga = GoogleTranslator(source="en", target="ga").translate(text=CWM)
##########
HWE_ga = GoogleTranslator(source="en", target="ga").translate(text=HWE)
CWE_ga = GoogleTranslator(source="en", target="ga").translate(text=CWE)
# time.sleep(5)
##########
HTHM_ga = GoogleTranslator(source="en", target="ga").translate(text=HTHM)
CTHM_ga = GoogleTranslator(source="en", target="ga").translate(text=CTHM)
##########
HTHE_ga = GoogleTranslator(source="en", target="ga").translate(text=HTHE)
CTHE_ga = GoogleTranslator(source="en", target="ga").translate(text=CTHE)
# time.sleep(5)
##########
HFM_ga = GoogleTranslator(source="en", target="ga").translate(text=HFM)
CFM_ga = GoogleTranslator(source="en", target="ga").translate(text=CFM)
##########
HFE_ga = GoogleTranslator(source="en", target="ga").translate(text=HFE)
CFE_ga = GoogleTranslator(source="en", target="ga").translate(text=CFM)
# time.sleep(5)
##########
HSM_ga = GoogleTranslator(source="en", target="ga").translate(text=HSM)
CSM_ga = GoogleTranslator(source="en", target="ga").translate(text=CSM)
##########
HSE_ga = GoogleTranslator(source="en", target="ga").translate(text=HSE)
CSE_ga = GoogleTranslator(source="en", target="ga").translate(text=CSE)
# time.sleep(5)
##########
HSNM_ga = GoogleTranslator(source="en", target="ga").translate(text=HSNM)
CSNM_ga = GoogleTranslator(source="en", target="ga").translate(text=CSNM)
##########
HSNE_ga = GoogleTranslator(source="en", target="ga").translate(text=HSNE)
CSNE_ga = GoogleTranslator(source="en", target="ga").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_es = GoogleTranslator(source="en", target="es").translate(text=HMM)
CMM_es = GoogleTranslator(source="en", target="es").translate(text=CMM)
##########
HME_es = GoogleTranslator(source="en", target="es").translate(text=HME)
CME_es = GoogleTranslator(source="en", target="es").translate(text=CME)
# time.sleep(5)
##########
HTM_es = GoogleTranslator(source="en", target="es").translate(text=HTM)
CTM_es = GoogleTranslator(source="en", target="es").translate(text=CTM)
##########
HTE_es = GoogleTranslator(source="en", target="es").translate(text=HTE)
CTE_es = GoogleTranslator(source="en", target="es").translate(text=CTE)
# time.sleep(5)
##########
HWM_es = GoogleTranslator(source="en", target="es").translate(text=HWM)
CWM_es = GoogleTranslator(source="en", target="es").translate(text=CWM)
##########
HWE_es = GoogleTranslator(source="en", target="es").translate(text=HWE)
CWE_es = GoogleTranslator(source="en", target="es").translate(text=CWE)
# time.sleep(5)
##########
HTHM_es = GoogleTranslator(source="en", target="es").translate(text=HTHM)
CTHM_es = GoogleTranslator(source="en", target="es").translate(text=CTHM)
##########
HTHE_es = GoogleTranslator(source="en", target="es").translate(text=HTHE)
CTHE_es = GoogleTranslator(source="en", target="es").translate(text=CTHE)
# time.sleep(5)
##########
HFM_es = GoogleTranslator(source="en", target="es").translate(text=HFM)
CFM_es = GoogleTranslator(source="en", target="es").translate(text=CFM)
##########
HFE_es = GoogleTranslator(source="en", target="es").translate(text=HFE)
CFE_es = GoogleTranslator(source="en", target="es").translate(text=CFM)
# time.sleep(5)
##########
HSM_es = GoogleTranslator(source="en", target="es").translate(text=HSM)
CSM_es = GoogleTranslator(source="en", target="es").translate(text=CSM)
##########
HSE_es = GoogleTranslator(source="en", target="es").translate(text=HSE)
CSE_es = GoogleTranslator(source="en", target="es").translate(text=CSE)
# time.sleep(5)
##########
HSNM_es = GoogleTranslator(source="en", target="es").translate(text=HSNM)
CSNM_es = GoogleTranslator(source="en", target="es").translate(text=CSNM)
##########
HSNE_es = GoogleTranslator(source="en", target="es").translate(text=HSNE)
CSNE_es = GoogleTranslator(source="en", target="es").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_tr = GoogleTranslator(source="en", target="tr").translate(text=HMM)
CMM_tr = GoogleTranslator(source="en", target="tr").translate(text=CMM)
##########
HME_tr = GoogleTranslator(source="en", target="tr").translate(text=HME)
CME_tr = GoogleTranslator(source="en", target="tr").translate(text=CME)
# time.sleep(5)
##########
HTM_tr = GoogleTranslator(source="en", target="tr").translate(text=HTM)
CTM_tr = GoogleTranslator(source="en", target="tr").translate(text=CTM)
##########
HTE_tr = GoogleTranslator(source="en", target="tr").translate(text=HTE)
CTE_tr = GoogleTranslator(source="en", target="tr").translate(text=CTE)
# time.sleep(5)
##########
HWM_tr = GoogleTranslator(source="en", target="tr").translate(text=HWM)
CWM_tr = GoogleTranslator(source="en", target="tr").translate(text=CWM)
##########
HWE_tr = GoogleTranslator(source="en", target="tr").translate(text=HWE)
CWE_tr = GoogleTranslator(source="en", target="tr").translate(text=CWE)
# time.sleep(5)
##########
HTHM_tr = GoogleTranslator(source="en", target="tr").translate(text=HTHM)
CTHM_tr = GoogleTranslator(source="en", target="tr").translate(text=CTHM)
##########
HTHE_tr = GoogleTranslator(source="en", target="tr").translate(text=HTHE)
CTHE_tr = GoogleTranslator(source="en", target="tr").translate(text=CTHE)
# time.sleep(5)
##########
HFM_tr = GoogleTranslator(source="en", target="tr").translate(text=HFM)
CFM_tr = GoogleTranslator(source="en", target="tr").translate(text=CFM)
##########
HFE_tr = GoogleTranslator(source="en", target="tr").translate(text=HFE)
CFE_tr = GoogleTranslator(source="en", target="tr").translate(text=CFM)
# time.sleep(5)
##########
HSM_tr = GoogleTranslator(source="en", target="tr").translate(text=HSM)
CSM_tr = GoogleTranslator(source="en", target="tr").translate(text=CSM)
##########
HSE_tr = GoogleTranslator(source="en", target="tr").translate(text=HSE)
CSE_tr = GoogleTranslator(source="en", target="tr").translate(text=CSE)
# time.sleep(5)
##########
HSNM_tr = GoogleTranslator(source="en", target="tr").translate(text=HSNM)
CSNM_tr = GoogleTranslator(source="en", target="tr").translate(text=CSNM)
##########
HSNE_tr = GoogleTranslator(source="en", target="tr").translate(text=HSNE)
CSNE_tr = GoogleTranslator(source="en", target="tr").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_ro = GoogleTranslator(source="en", target="ro").translate(text=HMM)
CMM_ro = GoogleTranslator(source="en", target="ro").translate(text=CMM)
##########
HME_ro = GoogleTranslator(source="en", target="ro").translate(text=HME)
CME_ro = GoogleTranslator(source="en", target="ro").translate(text=CME)
# time.sleep(5)
##########
HTM_ro = GoogleTranslator(source="en", target="ro").translate(text=HTM)
CTM_ro = GoogleTranslator(source="en", target="ro").translate(text=CTM)
##########
HTE_ro = GoogleTranslator(source="en", target="ro").translate(text=HTE)
CTE_ro = GoogleTranslator(source="en", target="ro").translate(text=CTE)
# time.sleep(5)
##########
HWM_ro = GoogleTranslator(source="en", target="ro").translate(text=HWM)
CWM_ro = GoogleTranslator(source="en", target="ro").translate(text=CWM)
##########
HWE_ro = GoogleTranslator(source="en", target="ro").translate(text=HWE)
CWE_ro = GoogleTranslator(source="en", target="ro").translate(text=CWE)
# time.sleep(5)
##########
HTHM_ro = GoogleTranslator(source="en", target="ro").translate(text=HTHM)
CTHM_ro = GoogleTranslator(source="en", target="ro").translate(text=CTHM)
##########
HTHE_ro = GoogleTranslator(source="en", target="ro").translate(text=HTHE)
CTHE_ro = GoogleTranslator(source="en", target="ro").translate(text=CTHE)
# time.sleep(5)
##########
HFM_ro = GoogleTranslator(source="en", target="ro").translate(text=HFM)
CFM_ro = GoogleTranslator(source="en", target="ro").translate(text=CFM)
##########
HFE_ro = GoogleTranslator(source="en", target="ro").translate(text=HFE)
CFE_ro = GoogleTranslator(source="en", target="ro").translate(text=CFM)
# time.sleep(5)
##########
HSM_ro = GoogleTranslator(source="en", target="ro").translate(text=HSM)
CSM_ro = GoogleTranslator(source="en", target="ro").translate(text=CSM)
##########
HSE_ro = GoogleTranslator(source="en", target="ro").translate(text=HSE)
CSE_ro = GoogleTranslator(source="en", target="ro").translate(text=CSE)
# time.sleep(5)
##########
HSNM_ro = GoogleTranslator(source="en", target="ro").translate(text=HSNM)
CSNM_ro = GoogleTranslator(source="en", target="ro").translate(text=CSNM)
##########
HSNE_ro = GoogleTranslator(source="en", target="ro").translate(text=HSNE)
CSNE_ro = GoogleTranslator(source="en", target="ro").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_pt = GoogleTranslator(source="en", target="pt").translate(text=HMM)
CMM_pt = GoogleTranslator(source="en", target="pt").translate(text=CMM)
##########
HME_pt = GoogleTranslator(source="en", target="pt").translate(text=HME)
CME_pt = GoogleTranslator(source="en", target="pt").translate(text=CME)
# time.sleep(5)
##########
HTM_pt = GoogleTranslator(source="en", target="pt").translate(text=HTM)
CTM_pt = GoogleTranslator(source="en", target="pt").translate(text=CTM)
##########
HTE_pt = GoogleTranslator(source="en", target="pt").translate(text=HTE)
CTE_pt = GoogleTranslator(source="en", target="pt").translate(text=CTE)
# time.sleep(5)
##########
HWM_pt = GoogleTranslator(source="en", target="pt").translate(text=HWM)
CWM_pt = GoogleTranslator(source="en", target="pt").translate(text=CWM)
##########
HWE_pt = GoogleTranslator(source="en", target="pt").translate(text=HWE)
CWE_pt = GoogleTranslator(source="en", target="pt").translate(text=CWE)
# time.sleep(5)
##########
HTHM_pt = GoogleTranslator(source="en", target="pt").translate(text=HTHM)
CTHM_pt = GoogleTranslator(source="en", target="pt").translate(text=CTHM)
##########
HTHE_pt = GoogleTranslator(source="en", target="pt").translate(text=HTHE)
CTHE_pt = GoogleTranslator(source="en", target="pt").translate(text=CTHE)
# time.sleep(5)
##########
HFM_pt = GoogleTranslator(source="en", target="pt").translate(text=HFM)
CFM_pt = GoogleTranslator(source="en", target="pt").translate(text=CFM)
##########
HFE_pt = GoogleTranslator(source="en", target="pt").translate(text=HFE)
CFE_pt = GoogleTranslator(source="en", target="pt").translate(text=CFM)
# time.sleep(5)
##########
HSM_pt = GoogleTranslator(source="en", target="pt").translate(text=HSM)
CSM_pt = GoogleTranslator(source="en", target="pt").translate(text=CSM)
##########
HSE_pt = GoogleTranslator(source="en", target="pt").translate(text=HSE)
CSE_pt = GoogleTranslator(source="en", target="pt").translate(text=CSE)
# time.sleep(5)
##########
HSNM_pt = GoogleTranslator(source="en", target="pt").translate(text=HSNM)
CSNM_pt = GoogleTranslator(source="en", target="pt").translate(text=CSNM)
##########
HSNE_pt = GoogleTranslator(source="en", target="pt").translate(text=HSNE)
CSNE_pt = GoogleTranslator(source="en", target="pt").translate(text=CSNE)
# time.sleep(5)
####################
####################
HMM_pl = GoogleTranslator(source="en", target="pl").translate(text=HMM)
CMM_pl = GoogleTranslator(source="en", target="pl").translate(text=CMM)
##########
HME_pl = GoogleTranslator(source="en", target="pl").translate(text=HME)
CME_pl = GoogleTranslator(source="en", target="pl").translate(text=CME)
# time.sleep(5)
##########
HTM_pl = GoogleTranslator(source="en", target="pl").translate(text=HTM)
CTM_pl = GoogleTranslator(source="en", target="pl").translate(text=CTM)
##########
HTE_pl = GoogleTranslator(source="en", target="pl").translate(text=HTE)
CTE_pl = GoogleTranslator(source="en", target="pl").translate(text=CTE)
# time.sleep(5)
##########
HWM_pl = GoogleTranslator(source="en", target="pl").translate(text=HWM)
CWM_pl = GoogleTranslator(source="en", target="pl").translate(text=CWM)
##########
HWE_pl = GoogleTranslator(source="en", target="pl").translate(text=HWE)
CWE_pl = GoogleTranslator(source="en", target="pl").translate(text=CWE)
# time.sleep(5)
##########
HTHM_pl = GoogleTranslator(source="en", target="pl").translate(text=HTHM)
CTHM_pl = GoogleTranslator(source="en", target="pl").translate(text=CTHM)
##########
HTHE_pl = GoogleTranslator(source="en", target="pl").translate(text=HTHE)
CTHE_pl = GoogleTranslator(source="en", target="pl").translate(text=CTHE)
# time.sleep(5)
##########
HFM_pl = GoogleTranslator(source="en", target="pl").translate(text=HFM)
CFM_pl = GoogleTranslator(source="en", target="pl").translate(text=CFM)
##########
HFE_pl = GoogleTranslator(source="en", target="pl").translate(text=HFE)
CFE_pl = GoogleTranslator(source="en", target="pl").translate(text=CFM)
# time.sleep(5)
##########
HSM_pl = GoogleTranslator(source="en", target="pl").translate(text=HSM)
CSM_pl = GoogleTranslator(source="en", target="pl").translate(text=CSM)
##########
HSE_pl = GoogleTranslator(source="en", target="pl").translate(text=HSE)
CSE_pl = GoogleTranslator(source="en", target="pl").translate(text=CSE)
# time.sleep(5)
##########
HSNM_pl = GoogleTranslator(source="en", target="pl").translate(text=HSNM)
CSNM_pl = GoogleTranslator(source="en", target="pl").translate(text=CSNM)
##########
HSNE_pl = GoogleTranslator(source="en", target="pl").translate(text=HSNE)
CSNE_pl = GoogleTranslator(source="en", target="pl").translate(text=CSNE)
####################

# class push_class(dict):
#     def __str__(self):
#         return json.dumps(self)


EU_H_MONDAY_MORNING = push_class(
                                    [['en','🎁 Bonus 100% to the deposit 💪'],
                                    ['it', HMM_it],
                                    ['fr', HMM_fr],
                                    ['sk', HMM_sk],
                                    ['hu', HMM_hu],
                                    ['cs', HMM_cs],
                                    ['de', HMM_de],
                                    ['ga', HMM_ga],
                                    ['es', HMM_es],
                                    ['tr', HMM_tr],
                                    ['ro', HMM_ro],
                                    ['pt', HMM_pt],
                                    ['pl', HMM_pl],
]
)


EU_C_MONDAY_MORNING = push_class(
                                    [['en','Make a deposit and receive a bonus of 100% 💸 + 70 FREE spins 🎰 Good luck to you 🤑'],
                                    ['it', CMM_it],
                                    ['fr', CMM_fr],
                                    ['sk', CMM_sk],
                                    ['hu', CMM_hu],
                                    ['cs', CMM_cs],
                                    ['de', CMM_de],
                                    ['ga', CMM_ga],
                                    ['es', CMM_es],
                                    ['tr', CMM_tr],
                                    ['ro', CMM_ro],
                                    ['pt', CMM_pt],
                                    ['pl', CMM_pl],
]
)


EU_H_MONDAY_EVENING = push_class(
                                    [['en','🤑 Evening Madness 🤑'],
                                    ['it', HME_it],
                                    ['fr', HME_fr],
                                    ['sk', HME_sk],
                                    ['hu', HME_hu],
                                    ['cs', HME_cs],
                                    ['de', HME_de],
                                    ['ga', HME_ga],
                                    ['es', HME_es],
                                    ['tr', HME_tr],
                                    ['ro', HME_ro],
                                    ['pt', HME_pt],
                                    ['pl', HME_pl],
]
)

EU_C_MONDAY_EVENING = push_class(
                                    [['en','🎰 Chance jackpot doubled to 2 hours! 💰 make a deposit and take the treasure mummy! 👍'],
                                    ['it', CME_it],
                                    ['fr', CME_fr],
                                    ['sk', CME_sk],
                                    ['hu', CME_hu],
                                    ['cs', CME_cs],
                                    ['de', CME_de],
                                    ['ga', CME_ga],
                                    ['es', CME_es],
                                    ['tr', CME_tr],
                                    ['ro', CME_ro],
                                    ['pt', CME_pt],
                                    ['pl', CME_pl],
]
)

EU_H_TUESDAY_MORNING = push_class(
                                    [['en','🔥 This is your chance of success! 🔥'],
                                    ['it', HTM_it],
                                    ['fr', HTM_fr],
                                    ['sk', HTM_sk],
                                    ['hu', HTM_hu],
                                    ['cs', HTM_cs],
                                    ['de', HTM_de],
                                    ['ga', HTM_ga],
                                    ['es', HTM_es],
                                    ['tr', HTM_tr],
                                    ['ro', HTM_ro],
                                    ['pt', HTM_pt],
                                    ['pl', HTM_pl],
]
)

EU_C_TUESDAY_MORNING = push_class(
                                    [['en','👉 Luck is near and ready to please you 🎁'],
                                    ['it', CTM_it],
                                    ['fr', CTM_fr],
                                    ['sk', CTM_sk],
                                    ['hu', CTM_hu],
                                    ['cs', CTM_cs],
                                    ['de', CTM_de],
                                    ['ga', CTM_ga],
                                    ['es', CTM_es],
                                    ['tr', CTM_tr],
                                    ['ro', CTM_ro],
                                    ['pt', CTM_pt],
                                    ['pl', CTM_pl],                               
]
)

EU_H_TUESDAY_EVENING = push_class(
                                    [['en','bambaem.islam won the jackpot 👍'],
                                    ['it', HTE_it],
                                    ['fr', HTE_fr],
                                    ['sk', HTE_sk],
                                    ['hu', HTE_hu],
                                    ['cs', HTE_cs],
                                    ['de', HTE_de],
                                    ['ga', HTE_ga],
                                    ['es', HTE_es],
                                    ['tr', HTE_tr],
                                    ['ro', HTE_ro],
                                    ['pt', HTE_pt],
                                    ['pl', HTE_pl],
]
)

EU_C_TUESDAY_EVENING = push_class(
                                    [['en','Just hit the jackpot 640 000 thous. In the Book Of Ra. It left 3 jackpot! 💵'],
                                    ['it', CTE_it],
                                    ['fr', CTE_fr],
                                    ['sk', CTE_sk],
                                    ['hu', CTE_hu],
                                    ['cs', CTE_cs],
                                    ['de', CTE_de],
                                    ['ga', CTE_ga],
                                    ['es', CTE_es],
                                    ['tr', CTE_tr],
                                    ['ro', CTE_ro],
                                    ['pt', CTE_pt],
                                    ['pl', CTE_pl],                               
]
)

EU_H_WEDNESDAY_MORNING = push_class(
                                    [['en','🔥 Hurry to register! 🔥'],
                                    ['it', HWM_it],
                                    ['fr', HWM_fr],
                                    ['sk', HWM_sk],
                                    ['hu', HWM_hu],
                                    ['cs', HWM_cs],
                                    ['de', HWM_de],
                                    ['ga', HWM_ga],
                                    ['es', HWM_es],
                                    ['tr', HWM_tr],
                                    ['ro', HWM_ro],
                                    ['pt', HWM_pt],
                                    ['pl', HWM_pl],
]
)

EU_C_WEDNESDAY_MORNING = push_class(
                                    [['en','💥 Only now 100%  first deposit bonus! 💥'],
                                    ['it', CWM_it],
                                    ['fr', CWM_fr],
                                    ['sk', CWM_sk],
                                    ['hu', CWM_hu],
                                    ['cs', CWM_cs],
                                    ['de', CWM_de],
                                    ['ga', CWM_ga],
                                    ['es', CWM_es],
                                    ['tr', CWM_tr],
                                    ['ro', CWM_ro],
                                    ['pt', CWM_pt],
                                    ['pl', CWM_pl],                                 
]
)

EU_H_WEDNESDAY_EVENING = push_class(
                                    [['en','Evening bonus 🎁'],
                                    ['it', HWE_it],
                                    ['fr', HWE_fr],
                                    ['sk', HWE_sk],
                                    ['hu', HWE_hu],
                                    ['cs', HWE_cs],
                                    ['de', HWE_de],
                                    ['ga', HWE_ga],
                                    ['es', HWE_es],
                                    ['tr', HWE_tr],
                                    ['ro', HWE_ro],
                                    ['pt', HWE_pt],
                                    ['pl', HWE_pl],
]
)

EU_C_WEDNESDAY_EVENING = push_class(
                                    [['en','Chance jackpot increased 2 times 💵 Do deposit and receive 100 spins stock + 100% to replenish 😎'],
                                    ['it', CWE_it],
                                    ['fr', CWE_fr],
                                    ['sk', CWE_sk],
                                    ['hu', CWE_hu],
                                    ['cs', CWE_cs],
                                    ['de', CWE_de],
                                    ['ga', CWE_ga],
                                    ['es', CWE_es],
                                    ['tr', CWE_tr],
                                    ['ro', CWE_ro],
                                    ['pt', CWE_pt],
                                    ['pl', CWE_pl],                               
]
)

EU_H_THURSDAY_MORNING = push_class(
                                    [['en','Azamat777 jackpot! 🤑'],
                                    ['it', HTHM_it],
                                    ['fr', HTHM_fr],
                                    ['sk', HTHM_sk],
                                    ['hu', HTHM_hu],
                                    ['cs', HTHM_cs],
                                    ['de', HTHM_de],
                                    ['ga', HTHM_ga],
                                    ['es', HTHM_es],
                                    ['tr', HTHM_tr],
                                    ['ro', HTHM_ro],
                                    ['pt', HTHM_pt],
                                    ['pl', HTHM_pl],
]
)

EU_C_THURSDAY_MORNING = push_class(
                                    [['en','234 549 thousand. Jammin jarz won the game. Make a deposit and win! 💵'],
                                    ['it', CTHM_it],
                                    ['fr', CTHM_fr],
                                    ['sk', CTHM_sk],
                                    ['hu', CTHM_hu],
                                    ['cs', CTHM_cs],
                                    ['de', CTHM_de],
                                    ['ga', CTHM_ga],
                                    ['es', CTHM_es],
                                    ['tr', CTHM_tr],
                                    ['ro', CTHM_ro],
                                    ['pt', CTHM_pt],
                                    ['pl', CTHM_pl],                            
]
)

EU_H_THURSDAY_EVENING = push_class(
                                    [['en','🤨 Not had time to pick up a bonus?'],
                                    ['it', HTHE_it],
                                    ['fr', HTHE_fr],
                                    ['sk', HTHE_sk],
                                    ['hu', HTHE_hu],
                                    ['cs', HTHE_cs],
                                    ['de', HTHE_de],
                                    ['ga', HTHE_ga],
                                    ['es', HTHE_es],
                                    ['tr', HTHE_tr],
                                    ['ro', HTHE_ro],
                                    ['pt', HTHE_pt],
                                    ['pl', HTHE_pl],
]
)

EU_C_THURSDAY_EVENING = push_class(
                                    [['en','🕔 There are remaining 15 minutes. Take 100% bonus to supplement and 100 FREE SPINS 🎰'],
                                    ['it', CTHE_it],
                                    ['fr', CTHE_fr],
                                    ['sk', CTHE_sk],
                                    ['hu', CTHE_hu],
                                    ['cs', CTHE_cs],
                                    ['de', CTHE_de],
                                    ['ga', CTHE_ga],
                                    ['es', CTHE_es],
                                    ['tr', CTHE_tr],
                                    ['ro', CTHE_ro],
                                    ['pt', CTHE_pt],
                                    ['pl', CTHE_pl],                                
]
)

EU_H_FRIDAY_MORNING = push_class(
                                    [['en','💥 Go climb! 🌠'],
                                    ['it', HFM_it],
                                    ['fr', HFM_fr],
                                    ['sk', HFM_sk],
                                    ['hu', HFM_hu],
                                    ['cs', HFM_cs],
                                    ['de', HFM_de],
                                    ['ga', HFM_ga],
                                    ['es', HFM_es],
                                    ['tr', HFM_tr],
                                    ['ro', HFM_ro],
                                    ['pt', HFM_pt],
                                    ['pl', HFM_pl],
]
)

EU_C_FRIDAY_MORNING = push_class(
                                    [['en','☄️ Oh yeah, winning percentage surpasses today! 💥'],
                                    ['it', CFM_it],
                                    ['fr', CFM_fr],
                                    ['sk', CFM_sk],
                                    ['hu', CFM_hu],
                                    ['cs', CFM_cs],
                                    ['de', CFM_de],
                                    ['ga', CFM_ga],
                                    ['es', CFM_es],
                                    ['tr', CFM_tr],
                                    ['ro', CFM_ro],
                                    ['pt', CFM_pt],
                                    ['pl', CFM_pl],                                
]
)

EU_H_FRIDAY_EVENING = push_class(
                                    [['en','Magomegov.samir93 won the jackpot 🤑'],
                                    ['it', HFE_it],
                                    ['fr', HFE_fr],
                                    ['sk', HFE_sk],
                                    ['hu', HFE_hu],
                                    ['cs', HFE_cs],
                                    ['de', HFE_de],
                                    ['ga', HFE_ga],
                                    ['es', HFE_es],
                                    ['tr', HFE_tr],
                                    ['ro', HFE_ro],
                                    ['pt', HFE_pt],
                                    ['pl', HFE_pl],
]
)

EU_C_FRIDAY_EVENING = push_class(
                                    [['en','Jackpot 507 768 thousand. Won the game Book Of Ra! 💵 Take your jackpot now! 💸'],
                                    ['it', CFE_it],
                                    ['fr', CFE_fr],
                                    ['sk', CFE_sk],
                                    ['hu', CFE_hu],
                                    ['cs', CFE_cs],
                                    ['de', CFE_de],
                                    ['ga', CFE_ga],
                                    ['es', CFE_es],
                                    ['tr', CFE_tr],
                                    ['ro', CFE_ro],
                                    ['pt', CFE_pt],
                                    ['pl', CFE_pl],                               
]
)

EU_H_SATURDAY_MORNING = push_class(
                                    [['en','🔥 This is your chance of success! 🔥'],
                                    ['it', HSM_it],
                                    ['fr', HSM_fr],
                                    ['sk', HSM_sk],
                                    ['hu', HSM_hu],
                                    ['cs', HSM_cs],
                                    ['de', HSM_de],
                                    ['ga', HSM_ga],
                                    ['es', HSM_es],
                                    ['tr', HSM_tr],
                                    ['ro', HSM_ro],
                                    ['pt', HSM_pt],
                                    ['pl', HSM_pl],
]
)

EU_C_SATURDAY_MORNING = push_class(
                                    [['en','👉 Luck is near and ready to please you 🎁'],
                                    ['it', CSM_it],
                                    ['fr', CSM_fr],
                                    ['sk', CSM_sk],
                                    ['hu', CSM_hu],
                                    ['cs', CSM_cs],
                                    ['de', CSM_de],
                                    ['ga', CSM_ga],
                                    ['es', CSM_es],
                                    ['tr', CSM_tr],
                                    ['ro', CSM_ro],
                                    ['pt', CSM_pt],
                                    ['pl', CSM_pl],                                
]
)

EU_H_SATURDAY_EVENING = push_class(
                                    [['en','Now the maximum chance of winning 💸'],
                                    ['it', HSE_it],
                                    ['fr', HSE_fr],
                                    ['sk', HSE_sk],
                                    ['hu', HSE_hu],
                                    ['cs', HSE_cs],
                                    ['de', HSE_de],
                                    ['ga', HSE_ga],
                                    ['es', HSE_es],
                                    ['tr', HSE_tr],
                                    ['ro', HSE_ro],
                                    ['pt', HSE_pt],
                                    ['pl', HSE_pl],
]
)

EU_C_SATURDAY_EVENING = push_class(
                                    [['en','Make a deposit and get x2 to replenish and 100 FREE SPINS 🎁 Good luck to you 🤑'],
                                    ['it', CSE_it],
                                    ['fr', CSE_fr],
                                    ['sk', CSE_sk],
                                    ['hu', CSE_hu],
                                    ['cs', CSE_cs],
                                    ['de', CSE_de],
                                    ['ga', CSE_ga],
                                    ['es', CSE_es],
                                    ['tr', CSE_tr],
                                    ['ro', CSE_ro],
                                    ['pt', CSE_pt],
                                    ['pl', CSE_pl],                            
]
)

EU_H_SUNDAY_MORNING = push_class(
                                    [['en','🍀 Odds of winning have increased by 3 times! 🍀'],
                                    ['it', HSNM_it],
                                    ['fr', HSNM_fr],
                                    ['sk', HSNM_sk],
                                    ['hu', HSNM_hu],
                                    ['cs', HSNM_cs],
                                    ['de', HSNM_de],
                                    ['ga', HSNM_ga],
                                    ['es', HSNM_es],
                                    ['tr', HSNM_tr],
                                    ['ro', HSNM_ro],
                                    ['pt', HSNM_pt],
                                    ['pl', HSNM_pl],
]
)

EU_C_SUNDAY_MORNING = push_class(
                                    [['en','👉 Come, enjoy and win now! 🎰'],
                                    ['it', CSNM_it],
                                    ['fr', CSNM_fr],
                                    ['sk', CSNM_sk],
                                    ['hu', CSNM_hu],
                                    ['cs', CSNM_cs],
                                    ['de', CSNM_de],
                                    ['ga', CSNM_ga],
                                    ['es', CSNM_es],
                                    ['tr', CSNM_tr],
                                    ['ro', CSNM_ro],
                                    ['pt', CSNM_pt],
                                    ['pl', CSNM_pl],                                  
]
)

EU_H_SUNDAY_EVENING = push_class(
                                    [['en','Rafaello22 jackpot! 🎰'],
                                    ['it', HSNE_it],
                                    ['fr', HSNE_fr],
                                    ['sk', HSNE_sk],
                                    ['hu', HSNE_hu],
                                    ['cs', HSNE_cs],
                                    ['de', HSNE_de],
                                    ['ga', HSNE_ga],
                                    ['es', HSNE_es],
                                    ['tr', HSNE_tr],
                                    ['ro', HSNE_ro],
                                    ['pt', HSNE_pt],
                                    ['pl', HSNE_pl],
]
)

EU_C_SUNDAY_EVENING = push_class(
                                    [['en','💵 222,549 thousand. Jammin jarz won the game. Make a deposit and win! 💵'],
                                    ['it', CSNE_it],
                                    ['fr', CSNE_fr],
                                    ['sk', CSNE_sk],
                                    ['hu', CSNE_hu],
                                    ['cs', CSNE_cs],
                                    ['de', CSNE_de],
                                    ['ga', CSNE_ga],
                                    ['es', CSNE_es],
                                    ['tr', CSNE_tr],
                                    ['ro', CSNE_ro],
                                    ['pt', CSNE_pt],
                                    ['pl', CSNE_pl],                           
]
)



print(EU_C_SUNDAY_EVENING)