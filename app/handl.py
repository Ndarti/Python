from aiogram import Bot, Dispatcher, F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyb as key
class Example(StatesGroup):
    Num1=State()
    Num2=State()
    Count=State()

router=Router()
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Hello',reply_markup=key.main)
    await message.reply("you are redy")

@router.message(Command('Yes'))
async def cmd_help(message:Message, state:FSMContext):
    await message.answer('lets start please input your number',reply_markup=key.numbers)
    await state.set_state(Example.Num1)


@router.message(Example.Num1)
async def safe(message:Message,state:FSMContext):
    await state.update_data(Num1=message.text)
    await state.set_state(Example.Count)
    await message.answer("let's start please input your sign", reply_markup=key.choose)

@router.message(Example.Count)
async def safe(message:Message,state:FSMContext):
    await state.update_data(Count=message.text)
    await state.set_state(Example.Num2)
    await message.answer("let's start please input your number",reply_markup=key.numbers)

@router.message(Example.Num2)
async def safe(message:Message,state:FSMContext):
    await state.update_data(Num2=message.text)
    data=await state.get_data()
    match data["Count"]:
        case '-':
            await message.answer(f'{int(data["Num1"]) - int(data["Num2"])}')

        case '+':
            await message.answer(f'{int(data["Num1"]) + int(data["Num2"])}')
        case '_':
            await message.answer('er')
@router.message(Command('help'))
async def cmd_help(message:Message):

    await message.answer("what kind of help do you need")