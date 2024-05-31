#import webbrowser
import telebot
from telebot import types

mytoken = ('6534817472:AAGjnz01eGar8k_hiHI_hmQLlgMXzG8U1mA(change)')
bot = telebot.TeleBot(mytoken)

BACK = 'Артқа'

answers = ['Кешіріңіз мен сізді түсінбедім']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('1')
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    button5 = types.KeyboardButton('5')
    button6 = types.KeyboardButton('6')
    button7 = types.KeyboardButton('7')
    button8 = types.KeyboardButton('8')
    button9 = types.KeyboardButton('9')
    button10 = types.KeyboardButton('10')
    button11 = types.KeyboardButton('Байланыс телефондары')
    markup.row(button1, button2, button3)
    markup.row(button4, button5, button6)
    markup.row(button7, button8, button9)
    markup.row(button10)
    markup.row(button11)



    if message.text == '/start':
        bot.send_message(
            message.chat.id,
            f'''
Сәлеметсіз бе?, {message.from_user.first_name}!
Қайырлы күн. Бұл жерде сіз абитуренттердің жиі қойылатын сұрақтарына жауап ала аласыз\n
1. Smart Arsu –ға тіркеле алмай жатырмын?\n
2. Smart Arsu қате (ошибка)  шығып тұрса\n 
3. 1 курс Smart Arsu- ға студент ретінде тіркеле алмай жатырмын\n
4. Басқа жатақханаға орналасуға болады ма?\n
5. Жатақханаға оқуға тапсырған медициналық анықтама жарай ма?\n
6. Жатақханаға қай уақыттан бастап орналасуға болады?\n
7. Жатақхананың ақысын бөліп төлеуге болады ма? \n
8. Алдын ала жатақхананың ішін көре аламын ба?\n
9. Жатақханаға орналасқаннан кейін бөлме ауыстыруға болады ма?\n 
10.Жатақханада тұрып сабақтан тыс уақытта жұмыс жасауға болады ма?\n 
            ''',
            reply_markup=markup
        )
    else:
        bot.send_message(message.chat.id, f'''
Сіз сұрақтар бетіне қайта оралдыңыз, сұрақтардың біреуін таңдаңыз\n
1. Smart Arsu –ға тіркеле алмай жатырмын?\n
2. Smart Arsu қате (ошибка)  шығып тұрса\n 
3. 1 курс Smart Arsu- ға студент ретінде тіркеле алмай жатырмын\n
4. Басқа жатақханаға орналасуға болады ма?\n
5. Жатақханаға оқуға тапсырған медициналық анықтама жарай ма?\n
6. Жатақханаға қай уақыттан бастап орналасуға болады?\n
7. Жатақхананың ақысын бөліп төлеуге болады ма? \n
8. Алдын ала жатақхананың ішін көре аламын ба?\n
9. Жатақханаға орналасқаннан кейін бөлме ауыстыруға болады ма?\n 
10.Жатақханада тұрып сабақтан тыс уақытта жұмыс жасауға болады ма?\n 
            ''', reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него.
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'Фото қарауға мүмкіндік жоқ :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '1':
        Chapter1(message)
    elif message.text == '2':
        Chapter2(message)
    elif message.text == '3':
        Chapter3(message)
    elif message.text == '4':
        Chapter4(message)
    elif message.text == '5':
        Chapter5(message)
    elif message.text == '6':
        Chapter6(message)
    elif message.text == '7':
        Chapter7(message)
    elif message.text == '8':
        Chapter8(message)
    elif message.text == '9':
        Chapter9(message)
    elif message.text == '10':
        Chapter10(message)
    elif message.text == 'Байланыс телефондары':
        Chapter11(message)
    elif message.text == BACK:
        welcome(message)
    # Если пользователь написал свое сообщение, то бот отвечает answers !!!!!!!!????????
    else:
        bot.send_message(message.chat.id, answers)

# Функция, отвечающая за 1 вопрос
@bot.message_handler(['1'])
def Chapter1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'Ең бірінші унверситетке оқуға құжаттар тапсыру керек ↙  \nОқуға құжаттар қабылдағаннан кейін 24 сағат жаңарту (обновление) болады', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 2 вопрос
def Chapter2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Кеңесшілерге ИИН, тіркелген телефон нөмер жіберу қажет, базадан не үшін қате шыққанын анықтау үшін''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 3 вопрос
def Chapter3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''1 курс студенті қонақ рөлінде тіркеледі''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 4 вопрос
def Chapter4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Жатақханаға  факультеттер бойынша орналасады, тек бір отбасынан шыққан студенттер бір жатақханаға орналаса алады''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 5 вопрос
def Chapter5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Жоқ, жатақханаға орналасу кезінде университеттің студенттік емханасынан  медициналық тексерістен өтеді''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 6 вопрос
def Chapter6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '25 тамыздан бастап орналасуға болады', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 7 вопрос
def Chapter7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id,'Жатақханаға тұру ақшасын өтініш расталғаннан кейін бірден жылдық ақысын төлеп орналасады' , reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 8 вопрос
def Chapter8(message):
    markup = types.InlineKeyboardMarkup()
    button_back = types.InlineKeyboardButton("Артқа", callback_data='back')
    button_first_corpus = types.InlineKeyboardButton("№1 студенттер үйі", callback_data='first_corpus')
    button_second_corpus = types.InlineKeyboardButton("№2 студенттер үйі", callback_data='second_corpus')
    button_third_corpus = types.InlineKeyboardButton("№3 студенттер үйі", callback_data='third_corpus')
    button_zhastar = types.InlineKeyboardButton("Жастар үйі", callback_data='zhastar')
    markup.add(button_back, button_first_corpus, button_second_corpus, button_third_corpus, button_zhastar)

    bot.send_message(
        message.chat.id,
        "Жатақханаға орналасуға рұқсат алғаннан кейін көре аласыз. Алдын ала тек осы суреттерді көре аласыз.\nСтуденттер үйін таңдаңыз:",
        reply_markup=markup
    )

# Обработка inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    if call.data == 'back':
        welcome(call.message)
    elif call.data == 'first_corpus':
        send_corpus_photos(call.message, 'first_corpus')
    elif call.data == 'second_corpus':
        send_corpus_photos(call.message, 'second_corpus')
    elif call.data == 'third_corpus':
        send_corpus_photos(call.message, 'third_corpus')
    elif call.data == 'zhastar':
        send_corpus_photos(call.message, 'zhastar')

# Функция для отправки фотографий корпусов
def send_corpus_photos(message, corpus):
    photo_urls = {
        'first_corpus': ['https://i.postimg.cc/44cjrL31/DSC-3737.jpg', 'https://i.postimg.cc/Y078cxXX/DSC-8030.jpg', 'https://i.postimg.cc/dQ8w8tGv/DSC-8494.jpg', 'https://i.postimg.cc/HLG64HwD/DSC-8047.jpg'],
        'second_corpus': ['https://i.postimg.cc/hGdP68QQ/DSC-3757.jpg', 'https://i.postimg.cc/fy3Hfbrs/DSC-8119.jpg', 'https://i.postimg.cc/T2mN1Kgj/DSC-8538.jpg', 'https://i.postimg.cc/fbp5Tsbg/DSC-8125.jpg'],
        'third_corpus': ['https://i.postimg.cc/SNpTZyDW/DSC-1495.jpg', 'https://i.postimg.cc/WzmnRkX0/DSC-1533.jpg', 'https://i.postimg.cc/8z76MvMw/DSC-8127.jpg', 'https://i.postimg.cc/bYM8d2Yq/DSC-8539.jpg'],
        'zhastar': ['https://i.postimg.cc/htdJZBvq/image.jpg', 'https://i.postimg.cc/VshLxV3s/DSC-8528.jpg', 'https://i.postimg.cc/NM5LTqWV/DSC-8530.jpg', 'https://i.postimg.cc/RFkCH316/DSC-8535.jpg']

    }

    for url in photo_urls[corpus]:
        bot.send_photo(message.chat.id, photo=url)

    bot.send_message(message.chat.id, 'Сізді жатақханамызда қуана күтеміз!')

# Функция, отвечающая за 9 вопрос
def Chapter9(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Smart Arsu  мобильдік қосымшасы арқылы таңдаған бөлмеде ғана орналаса аласыз''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 10 вопрос
def Chapter10(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Жатақханада тұратын білім алушыларға жұмыс жасауға рұқсат берілмейді''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 11 вопрос
def Chapter11(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'Байланыс телефондары: \n+77782721042, +77751216301 - \nконсультация үшін осы нөмірлерге хабарласыңыз', reply_markup=markup)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Веб сайтқа өту", url="https://zhubanov.edu.kz/"))
    markup.add(types.InlineKeyboardButton("Инстаграм парақшамыз", url="https://www.instagram.com/zhubanov.university/"))
    bot.send_message(message.chat.id, 'Егер де университет туралы қызықты жаңалықтар мен керекті мәліметтерді білгіңіз келсе біздін басты сайтымыздан іздей аласыз. Сілтеме ⬇ ', reply_markup=markup)
    markup.row(button1)




if __name__ == '__main__':

    bot.polling(none_stop=True)