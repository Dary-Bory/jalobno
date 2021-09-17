import sys
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

with open('out.txt', 'a') as f:
        
        f.write('start\n')
        button_res = KeyboardButton('Готово!')
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_res)

        TOKEN = ('1895289364:AAGILrq64NjnlF5nK_ApuBVD3iiHfoaBQ-g')

        bot = Bot(token=TOKEN)
        dp = Dispatcher(bot)

        @dp.message_handler(commands=['bolno'])
        async def process_bolno_command(message: types.Message):
                await message.reply("расскажи что в последнее время тебя расстраивает в учебном процессе \n1. можно матом \n2. увидят только студенты \n3. все отзывы анонимные \nНажми \'Готово!\' когда закончишь", reply_markup=greet_kb)
                print('bolno')

        @dp.message_handler(commands=['horosho'])
        async def process_horosho_command(message: types.Message):
                await message.reply("поделись что особенно тебя порадовало в учебе за последнее время! \nесли хочешь поблагодарить препода - не забудь написать его фамилию и предмет\nНажми \'Готово!\' когда закончишь", reply_markup=greet_kb)
                print('horosho')

        @dp.message_handler(commands=['help'])
        async def process_command_1(message: types.Message):
                await message.reply('если есть проблема, но ты не знаешь, к кому пойти или боишься этим поделиться — пиши сюда, мы поможем. обязательно напиши имя, курс и как с тобой можно связаться, чтобы мы знали, кому помогать!', reply_markup=greet_kb)
                print('help')

        @dp.message_handler(commands=['hi'])
        async def process_command_2(message: types.Message):
                await message.reply('Ну привет, ничего себе ты тут что удумал, кыш-кыш-кыш', reply_markup=greet_kb)
	
        @dp.message_handler()
        async def echo(msg: types.Message):
                if (msg.text == 'Готово!'):
                        await msg.reply('Cпааасибо большое! :3', reply_markup=ReplyKeyboardRemove())
                else:
                        res = ('{'+ str(msg.from_user.id) +'} '+ msg.text)
                        f.write(res + '\n')
                        print(res)

        if __name__ == '__main__':
                executor.start_polling(dp)
