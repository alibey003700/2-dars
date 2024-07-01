import requests

BOT_TOKEN="6068900832:AAESMuQLAP5P1KlLAcjcTndF5d2qt4eSa7E"
ID = "5546245446"

# xabar yuborish

#

#rasm yuborish

# def send_photo(p_url):
#     url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={ID}&photo={p_url}"
#     respons = requests.get(url)
#     if respons.status_code == 200:
#         print("xabaringiz yuborildi")

# p_url = "https://ae04.alicdn.com/kf/Hef05a54e6d614beaa73a2ca06e9c3f19l.jpg"
# send_photo(p_url)

# video yuborish


# audio yuborish

def send_video(p_url):
    url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo?chat_id={ID}&video={p_url}"
    respons = requests.get(url)
    if respons.status_code == 200:
        print("xabaringiz yuborildi")

p_url = "https://uzhits.net/dl3/2017/mobile/2018/Shahzod_Mirzo_-_Ongga_chapga_(HD_Clip)_(UzHits.Net).mp4"
send_video(p_url)
