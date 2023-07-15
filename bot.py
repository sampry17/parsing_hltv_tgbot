import random
import telebot
from telebot import types
import logging
from parsing import massage_rating


TOKEN = 'your token'
bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(func=lambda message: message.text.lower() == "start")
# приветствие поль-я
def start(message):
    mess = f'Добро пожаловать, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(func=lambda message: message.text.lower() == "help")
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
    website_help = types.InlineKeyboardButton('/website')
    start_help = types.InlineKeyboardButton('/start')
    about_help = types.InlineKeyboardButton('/about')
    help_help = types.InlineKeyboardButton('/help')
    markup.add(start_help, website_help, about_help, help_help, more_help)
    bot.send_message(message.chat.id, f'about - Информация о боте\n'
                                      f'\nrank - Актуальный рейтинг команд\n/more - ещё больше вещей!', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() == "rank")
def ranking_team(message):
    bot.send_message(message.chat.id, f'Топ 10 HLTV:\n{massage_rating}')


if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling()