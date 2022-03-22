import requests
from datetime import datetime
import json
from  pprint import pprint as print
oyatlar = [
    7,286,200,176,120,165,206,75,129,109,123,111,42,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,
    60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,12,14,11,11,
    18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,
    11,11,8,3,9,5,4,7,3,6,3,5,4,5,6
          ]
def oyat_tarjima(number_sura,number_oyat):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json"
    respone = requests.get(url)
    sura = number_sura
    oyat = number_oyat
    summa = sum(oyatlar[:(sura-1)])
    number_oyat = summa+oyat-1
    data = respone.json()
    result = data['quran'][number_oyat]['text']
    return  result

def oyat_audio(number_sura,number_oyat):
    url = f"https://api.quran.sutanlab.id/surah/{number_sura}/{number_oyat}"

    respone = requests.get(url)
    data = respone.json()
    result = data['data']['audio']['primary']
    return  result

def namoz_time(city):
    hozir = datetime.now()
    bugun = hozir.strftime("%d-%m-%Y")
    soat = hozir.strftime("%H:%M:%S")
    url = f"https://api.aladhan.com/v1/timingsByAddress/{bugun}?address={city}&method=2&school=1&latitudeAdjustmentMethod=3&timezonestring=Asia/Tashkent"
    r = requests.get(url)
    #print(r.status_code)
    res = r.json()
    data = res['data']['date']['gregorian']['date']
    info = f"📆 Bugun - {data} \n"
    info += f"📆 Hijriy - {res['data']['date']['hijri']['date']} \n"
    info += f"⏰ Soat - {str(soat)}\n"
    info += f"<b>➖➖➖➖➖➖</b>\n"
    info += f"🌆 <b>Bomdod: {res['data']['timings']['Fajr']} </b>\n"
    info += f"🌅 <b>Quyosh: {res['data']['timings']['Sunrise']} </b>\n"
    info+= f"🏙 <b>Peshin: {res['data']['timings']['Dhuhr']} </b>\n"
    info += f"🌅 <b>Asr: {res['data']['timings']['Asr']} </b>\n"
    info += f"🌉 <b>Shom: {res['data']['timings']['Maghrib']} </b>\n"
    info += f"🌃 <b>Xufton: {res['data']['timings']['Isha']} </b>"
    return info
