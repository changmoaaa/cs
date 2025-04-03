import random
from time import localtime
from requests import get, post
from datetime import datetime, date
from zhdate import ZhDate
import sys
import os





def get_daily_love():
    # 每日一句情话
    url = "https://api.lovelive.tools/api/SweetNothings/Serialization/Json"
    r = requests.get(url)
    all_dict = json.loads(r.text)
    sentence = all_dict['returnObj'][0]
    daily_love = sentence
    return daily_love
def get_ciba():
    # 每日一句英语（来自爱词霸）
    url = "http://open.iciba.com/dsapi/"
    r = get(url)
    note_en = r.json()["content"]
    note_ch = r.json()["note"]
    return note_ch, note_en
 # 获取每日情话
    daily_love = get_daily_love()
    # 获取每日一句英语
    note_qch, note_qen = get_ciba()

    # 公众号推送消息
    for user in users:
        send_message(user, accessToken, region, weather, temp, wind_dir, note_ch, note_en, max_temp, min_temp, sunrise,
                     sunset, category, pm2p5, proposal, chp)
    os.system("pause")
