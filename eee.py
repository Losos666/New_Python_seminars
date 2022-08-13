# Ютуб ( скачиваем видео)


# import pytube
# link = "https://www.youtube.com/watch?v=M27MkCUMxj8"
# yt = pytube.YouTube(link)
# stream = yt.streams.first()
# stream.download()




# Погода 9551e63c7045ba6e55a112b0fdf6c636

# import requests
# s_city = "Petersburg,RU"
# city_id = 0
# appid = "9551e63c7045ba6e55a112b0fdf6c636"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                  params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
#     data = res.json()
#     cities = ["{} ({})".format(d['name'], d['sys']['country'])
#               for d in data['list']]
#     print("city:", cities)
#     city_id = data['list'][0]['id']
#     print('city_id=', city_id)
# except Exception as e:
#     print("Exception (find):", e)
#     pass


# import telebot;
# bot = telebot.TeleBot('5485529608:AAGA9uc-u0vH65dqV_fGy4K6dY4PdohmdJA');
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#   if message.text == "Привет":
#       bot.send_message(message.from_user.id, "ну Привет")
#   elif message.text == "/help":
#       bot.send_message(message.from_user.id, "Напиши Привет")
#   else:
#       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# bot.polling(none_stop=True, interval=0)        

# import telebot
# # Создаем экземпляр бота
# bot = telebot.TeleBot('5485529608:AAGA9uc-u0vH65dqV_fGy4K6dY4PdohmdJA')
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0) 



# телеграмм бот wiki

import telebot, wikipedia, re
bot = telebot.TeleBot('5485529608:AAGA9uc-u0vH65dqV_fGy4K6dY4PdohmdJA')
#русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0) 