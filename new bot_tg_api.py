import asyncio
import time

import requests
token='7817172796:AAEpCDT_1nXbhSm9Uy_FJ8QlOmSx-eUq2W8'
URL= f'https://api.telegram.org/bot{token}/'

def send(id, text):
    params = {
        "chat_id": id,
        "text":text
    }
    res = requests.get(URL + "sendMessage", params=params)
    res.raise_for_status()
    return res.json()
def get(offset):#take text with requests
    params = {"offset": offset, "timeout": 30} if offset else {"timeout": 30}
    response = requests.get(URL + "getUpdates", params=params)
    return response.json().get("result", [])

def main ():
    off = None
    while True:
        updates = get(off)
        for update in updates:
            offset = update["update_id"] + 1
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]
            print(send(chat_id, "Привет"))
            if text == "/start":

                send(chat_id, "Привет")
            else:
                send(chat_id, f"Ты написал: {text}")

if __name__ == "__main__":
    main()