import sqlite3
import bot_emoji
from difflib import SequenceMatcher
import operator

# data["directions"] = {}
# data["directions"]['математика'] = '1'
# data["directions"]['физика'] = '2'
# data["directions"]['информатика'] = '3'
# print(list(data['directions'].values()))
# print(data)
# data['directions'].clear()
# d = data['directions'].keys()
# print(data["directions"])


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

image_id = 'AgACAgIAAxkBAAICdWJ5KTlgkkImhkQAAXtaIuYjjlrxdAAC87kxG54uyEscb7vtO6KpbQEAAwIAA3MAAyQE'
user_id = 448207047
with connection:
    # #cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
    # #cursor.execute("UPDATE 'users' SET image_id = ?, status_reg = ? WHERE user_id = ? ", (image_id, 0, user_id,))
    # acc_info = cursor.execute("SELECT nickname,image_id FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()
    # # exist = cursor.execute("SELECT * FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()
    # directions = cursor.execute("SELECT direction_id FROM 'user_directions' WHERE user_id = ?",
    #                                  (user_id,)).fetchall()
    #
    # cursor.execute("INSERT INTO 'user_directions' ('user_id', 'direction_id') VALUES (?,?)",
    #                (user_id, '1',))
    user_heh = '448207047'
    # достаю все id со статус акк = 1
    user_list_BD = cursor.execute("SELECT user_id FROM 'users' WHERE status_acc = ? AND user_id != ?", (1, user_heh)).fetchall()
    user_list = []

    # распаковка  user_ID из БД в список
    for user_id in user_list_BD:
        user_list.append(user_id[0])

    moe_dir = [3]
    # создаю словарь направлений людей со статус акк = 1

    dir_dict = {}
    for user_id in user_list:
        user_dir_BD = cursor.execute("SELECT direction_id FROM 'user_directions' WHERE user_id = ?",
                                     (user_id,)).fetchall()
        # распаковка списка направлений с БД для добавления в словарь
        dir_list = []
        for direc in user_dir_BD:
            dir_list.append(direc[0])
        dir_list.sort()
        dir_dict[f'{user_id}'] = dir_list

    # составление словаря с процентным совпалением направлений
    a = {}
    for heh in dir_dict:
        a[f"{heh}"] = SequenceMatcher(None, moe_dir, dir_dict[f'{heh}']).ratio()

    # функция сортировки для процентов совпадений, от самых больших к самым маленьким.
    a_1 = {k: v for k, v in sorted(a.items(), key=operator.itemgetter(1))}

    print(a_1)
    print(dir_dict)

# heh = ''
# temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика'}
# for direc in directions:
#     heh += f'{temp[str(direc[0])]}, '


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# # @dp.message_handler()
# # async def send_welcome(message: Message):
# #     pass
#
#
# # db.set_nickname(message.from_user.id, nickname)
# # db.set_age(message.from_user.id, age)
#
#
# @dp.message_handler()
# async def bot_message(message: Message):
#     if message.text == 'Рассказать о себе':
#         await bot.send_photo(message.chat.id, "AgACAgIAAxkBAAN-Yne5sjM3gXECIqV8Ezn0tNcp1vMAAg25MRueLsBLTnpKg4sI1PUBAAMCAANtAAMkBA")


# @dp.message_handler(content_types=ContentType.PHOTO)
# async def photo_handler(message: Message):
#     photo = message.photo.pop()
#     await photo.download('C:/Users/lump3n/PycharmProjects/bot')

# @dp.message_handler(content_types=["photo"])
# async def get_photo(message):
#     global file_id
#     file_id = message.photo[0].file_id
#     print(type(file_id))
#     print(file_id)
#     # этот идентификатор нужно где-то сохранить


# print(bot_emoji.set_emoji(':like:'))
# d = {'1': 'хых',
#      '2':{'dir':'хех'}}
#
# a = ['1', '2', '3']
#
# d.clear()
# print(d)

# s = ','
# print(s.join(a))

# data = {'image':'123'}
#
