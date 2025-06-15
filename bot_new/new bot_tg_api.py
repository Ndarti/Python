import asyncio
import time
from curses.ascii import isdigit
from bot_new.Class import Example
import private
import requests
token='8076615041:AAGpQMozhwjlZuNKK70_Wddd_wstWfRa7rQ'
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
    dp=Example()
    offset = None
    index = 0
    while True:
        updates = get(offset)
        for update in updates:
            offset = update["update_id"] + 1
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]
            if text == "/start":
                send(chat_id, "Input A")
            else:
               if isdigit(text) and index==0:
                   index+=1
                   dp.set_Num1(int(text))
                   send(chat_id, "Input + or -")
               if index==2 and isdigit(text):
                   dp.set_Num2(int(text))
                   send(chat_id,f'answer: {dp.sum()}')
                   index=0
               if isdigit(text)==False and index==1:
                   index+=1
                   send(chat_id, "Input B")
                   dp.set_Count(text)
        time.sleep(1)  # Задержка для снижения нагрузки
if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:####
        print('bot turn-of')