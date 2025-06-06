from aiogram.types import KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup
numbers=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='1'),KeyboardButton(text='2'),KeyboardButton(text='3')],
                                      [KeyboardButton(text='4'),KeyboardButton(text='5'),KeyboardButton(text='6')],
                                      [KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9')],
                                      ],resize_keyboard=True)
main=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/Yes'),KeyboardButton(text='/No')]],resize_keyboard=True)
choose=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='+'),KeyboardButton(text='-')]],resize_keyboard=True)
#answer=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Answer',request_contact=True)]],resize_keyboard=True)