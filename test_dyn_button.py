import telebot
from telebot import types
import sqlite3

# Токен, полученный от BotFather
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Файл базы данных
DATABASE = 'options.db'

def create_connection():
    """ Создать подключение к базе данных SQLite """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return conn

def create_tables():
    """ Создать таблицы в базе данных, если они не существуют """
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS options (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS suboptions (
                    id INTEGER PRIMARY KEY,
                    parent_id INTEGER,
                    name TEXT NOT NULL,
                    FOREIGN KEY (parent_id) REFERENCES options(id)
                );
            """)
            conn.commit()
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")
        finally:
            conn.close()

def read_options():
    """ Прочитать опции из базы данных """
    conn = create_connection()
    options = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT name FROM options")
            rows = cur.fetchall()
            options = [row[0] for row in rows]
        finally:
            conn.close()
    return options

def read_suboptions(parent_id):
    """ Прочитать подкатегории из базы данных на основе родительской категории """
    conn = create_connection()
    suboptions = []
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT name FROM suboptions WHERE parent_id=?", (parent_id,))
            rows = cur.fetchall()
            suboptions = [row[0] for row in rows]
        finally:
            conn.close()
    return suboptions

def get_id_by_name(name):
    """ Получить ID по имени категории """
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT id FROM options WHERE name=?", (name,))
            id = cur.fetchone()
            return id[0] if id else None
        finally:
            conn.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    options = read_options()
    markup = types.InlineKeyboardMarkup()
    for option in options:
        button = types.InlineKeyboardButton(text=option, callback_data='cat_' + option)
        markup.add(button)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    data = call.data
    if data == 'return':
        # Пользователь выбрал возврат к основным категориям
        options = read_options()
        markup = types.InlineKeyboardMarkup()
        for option in options:
            button = types.InlineKeyboardButton(text=option, callback_data='cat_' + option)
            markup.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию:", reply_markup=markup)
    elif data.startswith('cat_'):
        category = data[4:]
        category_id = get_id_by_name(category)
        suboptions = read_suboptions(category_id)
        markup = types.InlineKeyboardMarkup()
        for suboption in suboptions:
            button = types.InlineKeyboardButton(text=suboption, callback_data='sub_' + suboption)
            markup.add(button)
        markup.add(types.InlineKeyboardButton(text="⬅️ Вернуться", callback_data="return"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите подкатегорию:", reply_markup=markup)
    elif data.startswith('sub_'):
        subcategory = data[4:]
        bot.answer_callback_query(call.id, f"Вы выбрали {subcategory}")
        # Добавить дополнительные действия здесь, если нужно



def insert_initial_data():
    """ Вставить начальные данные в таблицы """
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Добавляем категории
            categories = ['Книги', 'Музыка', 'Технологии']
            for category in categories:
                cur.execute("INSERT INTO options (name) VALUES (?)", (category,))

            # Добавляем подкатегории, предполагаем, что ID категорий начинаются с 1 и инкрементируются
            subcategories = [
                (1, 'Фантастика'), (1, 'Научная литература'),
                (2, 'Классика'), (2, 'Рок'),
                (3, 'Компьютеры'), (3, 'Гаджеты')
            ]
            for parent_id, name in subcategories:
                cur.execute("INSERT INTO suboptions (parent_id, name) VALUES (?, ?)", (parent_id, name))

            conn.commit()
        except Exception as e:
            print(f"Ошибка при вставке данных: {e}")
        finally:
            conn.close()


create_tables()  # Убедитесь, что таблицы созданы
insert_initial_data()  # Заполняем таблицы начальными данными
bot.polling(none_stop=True)

