import asyncio
import time

import requests
token='7817172796:AAEpCDT_1nXbhSm9Uy_FJ8QlOmSx-eUq2W8'
URL= f'https://api.telegram.org/bot{token}/'

def send(id, text):
    params = {
        "chat_id": id,
        "text":text,
        "timeout": 30
    }
    res = requests.get(URL + "sendMessage", params=params)
    return res.json()
def get(offset):#take text with requests
    params = {"offset": offset, "timeout": 30} if offset else {"timeout": 30}
    response = requests.get(URL + "getUpdates", params=params)
    print(response.json().get("result", []))
    return response.json().get("result", [])

def main ():
    offset = None
    print(f"Бот запущен на {time.strftime('%H:%M %Z, %A, %B %d, %Y')}")  # 05:15 PM CEST, Friday, June 13, 2025
    while True:
        updates = get(offset)
        print(updates)
        for update in updates:
            offset = update["update_id"] + 1
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]

            if text == "/start":
                send(chat_id, "Привет")
            else:

                send(chat_id, f": {text}")
        time.sleep(1)  # Задержка для снижения нагрузки
if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:####
        print('bot turn-of')