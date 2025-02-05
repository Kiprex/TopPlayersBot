import telebot
from telebot import types
import gspread
from oauth2client.service_account import ServiceAccountCredentials
token = '8078432537:AAF8cXWYItDDCxFdVu0npjhBJfgseZ--oe8'
bot = telebot.TeleBot(token)

place = 0
name = 1
peak_pos = 2
peak_score = 3
score = 4

current_list = 'Топ РК'

def getdata(list_name):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
    client = gspread.authorize(credentials)
    spreadsheet_id = '1L9OANeoGCz4oIfadKvZG07xCPCxe3kbWTfiVPF94uss'
    spreadsheet = client.open_by_key(spreadsheet_id)
    sheet = spreadsheet.worksheet(list_name)
    if list_name == 'Топ РК':
        span = 'A1:N121'
    else:
        span = 'A1:S250'
    return sheet.get(span)

dashboard = types.InlineKeyboardMarkup()
top_rc_btn = types.InlineKeyboardButton(text='Топ 120 РК', callback_data='top_rc')
top_world_btn = types.InlineKeyboardButton(text='Топ мира', callback_data='top_w')
dashboard.add(top_rc_btn, top_world_btn)

top_board = types.InlineKeyboardMarkup()
prev_btn = types.InlineKeyboardButton(text='Предыдущая страница', callback_data='prev')
next_btn = types.InlineKeyboardButton(text='Следующая страница', callback_data='next')
pages = types.InlineKeyboardButton(text='Перейти на страницу:', callback_data='pages')
select_profile = types.InlineKeyboardButton(text='Выбрать профиль', callback_data='select_ps')
main_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
top_board.row(prev_btn, next_btn)
top_board.add(pages)
top_board.add(select_profile)
top_board.add(main_menu)

top_rc_pages_board = types.InlineKeyboardMarkup()
p1 = types.InlineKeyboardButton(text='1', callback_data='page1')
p2 = types.InlineKeyboardButton(text='2', callback_data='page2')
p3 = types.InlineKeyboardButton(text='3', callback_data='page3')
p4 = types.InlineKeyboardButton(text='4', callback_data='page4')
p5 = types.InlineKeyboardButton(text='5', callback_data='page5')
p6 = types.InlineKeyboardButton(text='6', callback_data='page6')
p7 = types.InlineKeyboardButton(text='7', callback_data='page7')
p8 = types.InlineKeyboardButton(text='8', callback_data='page8')
p9 = types.InlineKeyboardButton(text='9', callback_data='page9')
p10 = types.InlineKeyboardButton(text='10', callback_data='page10')
p11 = types.InlineKeyboardButton(text='11', callback_data='page11')
p12 = types.InlineKeyboardButton(text='12', callback_data='page12')
ppages = [p1, p2, p3, p4, p5, p6]
ppages2 = [p7, p8, p9, p10, p11, p12]
prev_btn = types.InlineKeyboardButton(text='Предыдущая страница', callback_data='prev')
next_btn = types.InlineKeyboardButton(text='Следующая страница', callback_data='next')
hide_btn = types.InlineKeyboardButton(text='Спрятать страницы', callback_data='hide_pages')
main_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
top_rc_pages_board.row(prev_btn, next_btn)
top_rc_pages_board.row(ppages)
top_rc_pages_board.row(ppages2)
top_rc_pages_board.add(hide_btn)
top_rc_pages_board.add(main_menu)

top_w_pages_board = types.InlineKeyboardMarkup()


prev_btn = types.InlineKeyboardButton(text='Предыдущая страница', callback_data='prev')
next_btn = types.InlineKeyboardButton(text='Следующая страница', callback_data='next')
hide_btn = types.InlineKeyboardButton(text='Спрятать страницы', callback_data='hide_pages')
main_menu = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
top_w_pages_board.row(prev_btn, next_btn)
for i in range(6):
    temp = []
    for j in range(5):
        temp.append(types.InlineKeyboardButton(text='1', callback_data=f'page{i * 5 + j + 1}'))
    top_w_pages_board.row(temp)
top_w_pages_board.add(hide_btn)
top_w_pages_board.add(main_menu)

profile_select_board = types.InlineKeyboardMarkup()
pr1 = types.InlineKeyboardButton(text='1', callback_data='prof1')
pr2 = types.InlineKeyboardButton(text='2', callback_data='prof2')
pr3 = types.InlineKeyboardButton(text='3', callback_data='prof3')
pr4 = types.InlineKeyboardButton(text='4', callback_data='prof4')
pr5 = types.InlineKeyboardButton(text='5', callback_data='prof5')
pr6 = types.InlineKeyboardButton(text='6', callback_data='prof6')
pr7 = types.InlineKeyboardButton(text='7', callback_data='prof7')
pr8 = types.InlineKeyboardButton(text='8', callback_data='prof8')
pr9 = types.InlineKeyboardButton(text='9', callback_data='prof9')
pr10 = types.InlineKeyboardButton(text='10', callback_data='prof10')
back = types.InlineKeyboardButton(text='Назад', callback_data='home')
profile_select_board.row(pr1, pr2, pr3, pr4, pr5)
profile_select_board.row(pr6, pr7, pr8, pr9, pr10)
profile_select_board.add(back)

profile_board = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton(text='Назад', callback_data='back_to_top')
profile_board.add(back1)

countries = {}


data = getdata(current_list)

def update_data():
    global data
    data = getdata(current_list)
    getcountriestop(data)

def getcountriestop(data):
    for row in data[1:]:
        if row != []:
            country = row[1][:2]
            name = row[1].split()[0][2:]
            if country in countries.keys():
                countries[country].append(name)
            else:
                countries[country] = [name]

@bot.message_handler(content_types=['photo'])
def main(message):
    bot.reply_to(message, 'нахуй ты мне картинки шлешь убежище')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.from_user.id, 'Выберите команду:', reply_markup=dashboard)
    

@bot.message_handler()
def info(message):
    text = message.text.lower()
    if 'эйрили' in text or 'eiriley' in text or 'вернам' in text or 'vernam' in text or 'ani' in text:
        bot.reply_to(message, 'ААААА МАРШЛАЛ РК')
    elif 'бесплатно' in text:
        with open('бесплатно.gif', 'rb') as f:
            bot.send_video(message.chat.id, f)
    elif 'платно' in text:
        with open('платно.gif', 'rb') as f:
            bot.send_video(message.chat.id, f)
    elif 'sakupen circles' in message.text.lower() or 'степа' in message.text.lower() or 'стёпа' in message.text.lower():
        bot.reply_to(message, 'СТЁПА ПРОШЕЛ SAKUPEN CIRCLES!!!! (ПРЫЖОК С ВИНДИ ЛЭНДСКЕЙП)))')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global data, current_list
    max_list_size = 0
    if current_list == 'Топ РК':
        max_list_size = 120
    else:
        max_list_size = 300
    if callback.data == 'prev':
        if callback.message.text.split()[0] != '1.':
            output = ''
            for i in range(int(callback.message.text.split()[0].split('.')[0]) - 10, int(callback.message.text.split()[0].split('.')[0])):                    
                row = data[i]
                output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
            bot.edit_message_text(output, callback.message.chat.id, callback.message.message_id, parse_mode='html', reply_markup=callback.message.reply_markup)
    elif callback.data == 'next':
        if int(callback.message.text.split()[0].split('.')[0]) != max_list_size - 9:
            output = ''
            for i in range(int(callback.message.text.split()[0].split('.')[0]) + 10, int(callback.message.text.split()[0].split('.')[0]) + 20):
                row = data[i]
                output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
            bot.edit_message_text(output, callback.message.chat.id, callback.message.message_id, parse_mode='html', reply_markup=callback.message.reply_markup)
    elif callback.data == 'pages':
        if current_list == 'Топ РК':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=top_rc_pages_board)
        else:
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=top_w_pages_board)
    elif callback.data[:4] == 'page':
        output = ''
        for i in range((int(callback.data[4:]) - 1) * 10 + 1, (int(callback.data[4:]) - 1) * 10 + 11):                    
            row = data[i]
            output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
        bot.edit_message_text(output, callback.message.chat.id, callback.message.message_id, parse_mode='html', reply_markup=callback.message.reply_markup)
    elif callback.data == 'top_rc':
        current_list = 'Топ РК'
        update_data()
        output = ''
        for i in range(1, 11):
            row = data[i]
            output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
        bot.send_message(callback.message.chat.id, output, parse_mode='html', reply_markup=top_board)
    elif callback.data == 'home':
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=top_board)
    elif callback.data == 'top_w':
        current_list = 'Топ мира новый'
        update_data()
        output = ''
        for i in range(1, 11):
            row = data[i]
            output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
        bot.send_message(callback.message.chat.id, output, parse_mode='html', reply_markup=top_board)
    elif callback.data == 'main_menu':
        bot.send_message(callback.message.chat.id, 'Выберите команду:', reply_markup=dashboard)
    elif callback.data == 'select_ps':
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=profile_select_board)
    elif callback.data[:4] == 'prof':
        first_player_number = int(callback.message.text.split()[0].split('.')[0])
        player_number = first_player_number + int(callback.data[4:]) - 1
        player_name = data[player_number][1].split()[0][2:]
        cntry = data[player_number][1][:2]
        country_place = int(countries[cntry].index(player_name)) + 1
        hardest = data[player_number][name][data[player_number][name].find('(') + 1:data[player_number][name].rfind(')')].split(',')[0]
        result = f'Игрок № {data[player_number][place]}: {data[player_number][name].split()[0]}' + '\n' + f'Хардест: {hardest}' + '\n' + f'{str(data[player_number][score])} очков' + '\n' + f'Место в стране: {country_place}' + '\n' + f'Пиковая позиция: {data[player_number][peak_pos]}'  + '\n' + f'Пиковые очки: {data[player_number][peak_score]}'
        bot.edit_message_text(result, callback.message.chat.id, callback.message.message_id, parse_mode='html', reply_markup=profile_board)
    elif callback.data == 'back_to_top':
        output = ''
        page_number = int(callback.message.text.split()[2][:-1]) // 10 + 1
        for i in range((page_number - 1) * 10 + 1, (page_number - 1) * 10 + 11):                    
            row = data[i]
            output += f'{row[place]}. {row[name]}<u>{row[score]}</u> очков ' + '\n'
        bot.edit_message_text(output, callback.message.chat.id, callback.message.message_id, parse_mode='html', reply_markup=callback.message.reply_markup)
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=top_board)
    elif callback.data == 'hide_pages':
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=top_board)
        
        




bot.infinity_polling()