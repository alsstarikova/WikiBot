import telebot
import wikipedia
import re


# Создание экземпляра бота
bot = telebot.TeleBot('Ваш токен')

# Устанавливаем для Wikipedia русский язык
wikipedia.set_lang('ru')

# Чистим текст статьи и ограничиваем его 1000 символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получим первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всё после последней точки
        wikimas = wikimas[:-1]
        # Создаём пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знака "равно" (заголовков)
        for x in wikimas:
            if not('==' in x):
                # Если в строке останется больше трёх символов, добавляем
                # её к нашей переменной и восстанавливаем утеряные точки
                if len(x.strip()) > 3:
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        # При помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Функция обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово и я найду его значение в Wikipedia')


# Получаем сообщение от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True, interval=0)








