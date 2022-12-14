import telebot
from telebot import types
from googletrans import Translator

with open('token.txt', 'r') as t:
    TOKEN = t.read().strip()
    
transl = Translator()
language = ''

bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.InlineKeyboardMarkup(row_width=2)
  item1 = types.InlineKeyboardButton('🇬🇧', callback_data='EN')
  item2 = types.InlineKeyboardButton('🇫🇷', callback_data='FR')
  item3 = types.InlineKeyboardButton('🇩🇪', callback_data='DE')
  item4 = types.InlineKeyboardButton('🇮🇹', callback_data='IT')
  markup.add(item1,item2,item3,item4)

  bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ✌️ \nЯ бот-переводчик \nВыбери язык на какой будем переводить', reply_markup=markup)

@bot.message_handler(commands=['language'])
def language(message):
  markup = types.InlineKeyboardMarkup(row_width=2)
  item1 = types.InlineKeyboardButton('🇬🇧', callback_data='EN')
  item2 = types.InlineKeyboardButton('🇫🇷', callback_data='FR')
  item3 = types.InlineKeyboardButton('🇩🇪', callback_data='DE')
  item4 = types.InlineKeyboardButton('🇮🇹', callback_data='IT')
  markup.add(item1,item2,item3,item4)

  bot.send_message(message.chat.id, f'Выбери язык', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
  global language
  if call.message:
    if call.data == 'EN':
      language = 'en'
      bot.send_message(call.message.chat.id, 'Можешь начинать вводить текст для перевода \nДля смены языка напиши - /language')
    elif call.data == 'FR':
      language = 'fr'
      bot.send_message(call.message.chat.id, 'Можешь начинать вводить текст для перевода \nДля смены языка напиши - /language')
    elif call.data == 'DE':
      language = 'de'
      bot.send_message(call.message.chat.id, 'Можешь начинать вводить текст для перевода \nДля смены языка напиши - /language')
    elif call.data == 'IT':
      language = 'it'
      bot.send_message(call.message.chat.id, 'Можешь начинать вводить текст для перевода \nДля смены языка напиши - /language')

@bot.message_handler()
def echo_callback(message: types.Message):
  if language != '':
    sentence = message.text
    word = transl.translate(sentence, dest=language).text
    bot.send_message(message.from_user.id, word)
  else: 
    bot.send_message(message.from_user.id, 'Язык не выбран \n/language - для выбора языка')

bot.polling(non_stop=True)
