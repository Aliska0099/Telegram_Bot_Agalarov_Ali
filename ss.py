import telebot
from config import TOKEN, exchanger
from extenxios import Convertor, ConverterExeption
import traceback

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands = ["start", "help"])
def start(message: telebot.types.Message):
    text = "Здарово бро, рад тебя тут видеть!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in exchanger.keys():
        text = "\n".join((text, i))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise ConverterExeption('Неверное количество параметров!')
        base, sym, amount = values
        new_price = Convertor.get_price(sym, base, amount)
        bot.reply_to(message, f'Цена {amount} {sym} в {base}: {new_price}')
        answer = Convertor.get_price(*values)
    except ConverterExeption as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()



