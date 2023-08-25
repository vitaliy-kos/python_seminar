import telebot
from telebot import types
import sqlite3 as database

API_TOKEN = '6442564465:AAFj8JEpg_p-7_oNjXpOBPAPSeRhdLKvcnk'
bot = telebot.TeleBot(API_TOKEN)


con = database.connect("phone_book_bot.db", check_same_thread = False)
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    phone TEXT,
    type INT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(type) REFERENCES phone_types(id)
)""")
            
cur.execute("""CREATE TABLE IF NOT EXISTS phone_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT
)""")

ph_type = 0
contact_id = 0
fn = ''
ln = ''
cur.execute("""SELECT * FROM phone_types """)
phone_types = dict(cur.fetchall())

def create_user(fn, ln):
    cur.execute("""INSERT INTO users (first_name, last_name) VALUES (?, ?)""", (fn.lower(), ln.lower()))
    return cur.lastrowid

def get_user_by_id(id):
    cur.execute("SELECT * FROM users WHERE id=?", (id, ))
    return cur.fetchall()

def get_numbers_by_user_id(id):
    cur.execute("SELECT * FROM phones WHERE user_id=?", (id, ))
    return cur.fetchall()

def delete_user_by_id(id):
    cur.execute("DELETE FROM phones WHERE user_id=?", (id, ))
    cur.execute("DELETE FROM users WHERE id=?", (id, ))
    return

def update_last_name_in_base(id, ln):
    cur.execute("UPDATE users SET last_name=? WHERE id=?", (ln.lower(), id))
    return

def update_first_name_in_base(id, fn):
    cur.execute("UPDATE users SET first_name=? WHERE id=?", (fn.lower(), id))
    return

def add_number_to_base(contact_id, new_number, type):
    cur.execute("""INSERT OR IGNORE INTO phones (user_id, phone, type) VALUES (?, ?, ?)""", (contact_id, new_number, type))
    return

def edit_number_to_base(new_number, req_id):
    cur.execute("""UPDATE phones SET phone=? WHERE id=?""", (new_number, req_id))
    return

def delete_number_from_base(req_id):
    cur.execute("""DELETE FROM phones WHERE id=?""", (req_id))
    return

def get_users():
    cur.execute("SELECT * FROM users LIMIT 10")
    return cur.fetchall()

def search_contact_by_query(que):
    str_que = "%" + que + "%"
    print(str_que)
    cur.execute("SELECT users.id FROM phones FULL JOIN users ON phones.user_id = users.id WHERE phones.phone LIKE ? OR LOWER(users.first_name) LIKE LOWER(?) OR LOWER(users.last_name) LIKE LOWER(?) GROUP BY users.id", (str_que, str_que, str_que) )
    # print(cur)
    return cur.fetchall()

@bot.message_handler(commands=['start'])
def start_message(message):
    start_keyboard = types.InlineKeyboardMarkup()
    key_start = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
    start_keyboard.add(key_start)
    bot.send_message(message.chat.id, text='Добро пожаловать в телефонный справочник, Вы можете найти нужный контакт и просмотреть, добавить контакты, удалить или отредактировать.', reply_markup = start_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global contact_id
    global ph_type
    call_str = call.data.split('|')
    if (len(call_str) > 0): action = call_str[0]
    if (len(call_str) > 1): user_id = call_str[1]
    if (len(call_str) > 2): phone_type = call_str[2]
    
    
    if action == "help_info":
        help_keyboard = types.InlineKeyboardMarkup()
        key_main = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')
        help_keyboard.add(key_main)
        bot.send_message(call.message.chat.id, text='1. Чтобы найти нужный контакт, необходимо нажать на кнопку "Поиск контакта" и ввести имя или номер телефона\n2. Для добавления контакта нужно нажать на кнопку "Добавить контакт" и ввести необходимые данные\n3. Для обновления контакта нужно его найти и нажать на кнопку "Обновить"\n4. Чтобы удалить контакт нужно его найти и в меню контакта нажать на конпку "Удалить"', reply_markup = help_keyboard)

    elif action == "main_menu":
        keyboard = types.InlineKeyboardMarkup()
        key_watch = types.InlineKeyboardButton(text='Посмотреть контакты', callback_data='watch_contacts')
        keyboard.add(key_watch)
        key_search = types.InlineKeyboardButton(text='Поиск контакта', callback_data='search_contact')
        keyboard.add(key_search)
        key_add = types.InlineKeyboardButton(text='Добавить контакт', callback_data='add_contact')
        keyboard.add(key_add)
        key_help = types.InlineKeyboardButton(text='Справка', callback_data='help_info')
        keyboard.add(key_help)

        bot.send_message(call.message.chat.id, text="Выберите действие:", reply_markup=keyboard)

    elif action == "watch_contacts":
        users = get_users()
        users_keyboard = types.InlineKeyboardMarkup()
        for i in users:
            user_info = get_user_by_id(i[0])
            text = user_info[0][2].title() +  ' ' + user_info[0][1].title()
            key_user = types.InlineKeyboardButton(text, callback_data='get_user|' + str(i[0]))
            users_keyboard.add(key_user)
        bot.send_message(call.message.chat.id, "Контакты: ", reply_markup = users_keyboard)

    elif action == "search_contact":
        bot.send_message(call.message.chat.id, text="Введите номер, имя или фамилию:")
        bot.register_next_step_handler(call.message, search_contact)

    elif action == "add_contact":
        bot.send_message(call.message.chat.id, text="Введите имя:")
        bot.register_next_step_handler(call.message, get_user_first_name)

    elif action == "delete_contact":
        delete_user_by_id(user_id)
        delete_keyboard = types.InlineKeyboardMarkup()
        key_main = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')
        delete_keyboard.add(key_main)
        bot.send_message(call.message.chat.id, text="Контакт удален", reply_markup = delete_keyboard)

    elif action == "choose_number_to_edit":
        user_numbers = get_numbers_by_user_id(user_id)
        numbers_keyboard = types.InlineKeyboardMarkup()
        for number in user_numbers:
            key_number = types.InlineKeyboardButton(number[2], callback_data='edit_number|' + str(user_id) + '|' + str(number[0]))
            numbers_keyboard.add(key_number)
        bot.send_message(call.message.chat.id, "Выберите номер, который хотите изменить: ", reply_markup = numbers_keyboard)

    elif action == "edit_number":
        contact_id = user_id
        ph_type = phone_type
        bot.send_message(call.message.chat.id, text="Введите новый номер:")
        bot.register_next_step_handler(call.message, ask_number_to_edit)

    elif action == "choose_number_to_delete":
        user_numbers = get_numbers_by_user_id(user_id)
        numbers_keyboard = types.InlineKeyboardMarkup()
        for number in user_numbers:
            key_number = types.InlineKeyboardButton(number[2], callback_data='delete_number|' + str(user_id) + '|' + str(number[0]))
            numbers_keyboard.add(key_number)
        bot.send_message(call.message.chat.id, "Выберите номер, который хотите удалить: ", reply_markup = numbers_keyboard)

    elif action == "delete_number":
        contact_id = user_id
        ph_type = phone_type
        delete_number_from_base(phone_type)
        user_menu(contact_id, call.message.chat.id)
        contact_id = 0

    elif action == "choose_type_number":
        type_nembers_keyboard = types.InlineKeyboardMarkup()
        for id in phone_types:
            key_type = types.InlineKeyboardButton(phone_types.get(id), callback_data='add_number|' + str(user_id) + '|' + str(id))
            type_nembers_keyboard.add(key_type)
        bot.send_message(call.message.chat.id, "Выберите тип номера: ", reply_markup = type_nembers_keyboard)
    
    elif action == "add_number":
        contact_id = user_id
        ph_type = phone_type
        bot.send_message(call.message.chat.id, text="Введите номер:")
        bot.register_next_step_handler(call.message, ask_number_to_add)
    
    elif action == "edit_firstname":
        contact_id = user_id
        bot.send_message(call.message.chat.id, text="Введите имя:")
        bot.register_next_step_handler(call.message, update_user_first_name)

    elif action == "edit_lastname":
        contact_id = user_id
        bot.send_message(call.message.chat.id, text="Введите фамилию:")
        bot.register_next_step_handler(call.message, update_user_last_name)

    elif action == "get_user":
        user_menu(user_id, call.message.chat.id)

def ask_number_to_add(message):
    global contact_id
    global ph_type
    new_number = message.text
    add_number_to_base(contact_id, new_number, ph_type)
    user_menu(contact_id, message.chat.id)
    contact_id = 0
    ph_type = 0   

def ask_number_to_edit(message):
    global contact_id
    global ph_type
    new_number = message.text
    edit_number_to_base(new_number, ph_type)
    user_menu(contact_id, message.chat.id)
    contact_id = 0
    ph_type = 0

def update_user_first_name(message):
    global contact_id
    new_fn = message.text
    update_first_name_in_base(contact_id, new_fn)
    user_menu(contact_id, message.chat.id)
    contact_id = 0    

def update_user_last_name(message):
    global contact_id
    new_ln = message.text
    update_last_name_in_base(contact_id, new_ln)
    user_menu(contact_id, message.chat.id)
    contact_id = 0

def get_user_first_name(message):
    global fn
    fn = message.text
    bot.send_message(message.chat.id, text="Введите фамилию:")
    bot.register_next_step_handler(message, get_user_last_name)

def get_user_last_name(message):
    global ln
    ln = message.text
    user_id = create_user(fn, ln)
    user_menu(user_id, message.chat.id)

def search_contact(message):
    query = message.text
    user_id = search_contact_by_query(query)
    
    if (len(user_id) > 0):
        if (len(user_id) == 1):
            user_menu(user_id[0][0], message.chat.id)
        elif (len(user_id) > 1):
            users_keyboard = types.InlineKeyboardMarkup()
            for i in user_id:
                user_info = get_user_by_id(i[0])
                text = user_info[0][2].title() +  ' ' + user_info[0][1].title()
                key_user = types.InlineKeyboardButton(text, callback_data='get_user|' + str(i[0]))
                users_keyboard.add(key_user)
            bot.send_message(message.chat.id, "Найдены пользователи: ", reply_markup = users_keyboard)
    else:
        user_keyboard = types.InlineKeyboardMarkup()
        key_main_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')
        user_keyboard.add(key_main_menu)
        bot.send_message(message.chat.id, "Контакты или номера не найдены.", reply_markup = user_keyboard)

def user_menu(user_id, chat_id):
    global phone_types
    user_info = get_user_by_id(user_id)
    user_numbers = get_numbers_by_user_id(user_id)

    user_keyboard = types.InlineKeyboardMarkup()
    key_add = types.InlineKeyboardButton(text='Добавить номер', callback_data='choose_type_number|' + str(user_id))
    user_keyboard.add(key_add)
    key_edit_num = types.InlineKeyboardButton(text='Изменить номер', callback_data='choose_number_to_edit|' + str(user_id))
    user_keyboard.add(key_edit_num)

    if (len(user_numbers) > 0):
        key_delete_num = types.InlineKeyboardButton(text='Удалить номер', callback_data='choose_number_to_delete|' + str(user_id))
        user_keyboard.add(key_delete_num)

    key_edit_firstname = types.InlineKeyboardButton(text='Изменить имя', callback_data='edit_firstname|' + str(user_id))
    user_keyboard.add(key_edit_firstname)
    key_edit_lastname = types.InlineKeyboardButton(text='Изменить фамилию', callback_data='edit_lastname|' + str(user_id))
    user_keyboard.add(key_edit_lastname)
    key_delete_user = types.InlineKeyboardButton(text='Удалить контакт', callback_data='delete_contact|' + str(user_id))
    user_keyboard.add(key_delete_user)
    key_main_menu = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')
    user_keyboard.add(key_main_menu)

    if (len(user_numbers) > 0):
        phones = '\n\nТелефоны:'
        for i in user_numbers:
            phones = phones + '\n' + str(phone_types.get(i[3])) + ': ' + str(i[2])
    else:
        phones = ''

    text = "Пользователь ID-" + str(user_info[0][0]) + "\nИмя: " + str(user_info[0][1].title()) + "\nФамилия: " + str(user_info[0][2].title()) + phones

    bot.send_message(chat_id, text, reply_markup = user_keyboard)

bot.polling()