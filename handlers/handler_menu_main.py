from bot import bot, db
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from states import Match as fsm_match, Main as fsm_main

from send_menu import send_self_profile, get_data_profiles
import markups as nav
from bot_emoji import set_emoji


async def check_buttons_main(message: types.Message, state: FSMContext):
    if message.text == set_emoji('Смотреть анкеты '+set_emoji(":eyes:")):
        await bot.send_message(message.from_user.id, "Удачи в поисках ", reply_markup=nav.MenuMatch)

        await fsm_match.match.set()
        # подтягивание данных и отправка анкеты по ним
        await get_data_profiles(message, state)
        async with state.proxy() as data:
            await bot.send_message(message.from_user.id, set_emoji(':mag:'))
            data['id'] = data['sequence_dir_sort'].popitem()[0]

            info = db.get_acc_info(data['id'])

            # --- костыль для вывода названия направлений
            temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика', '4': 'Русский язык', '5': 'Химия',
                    '6': 'История','7': 'Обществознание', '8': 'Биология', '9': 'Английский','10':'Литература','11':'География'}
            temp_dir = []
            for direction in db.get_directions(data['id']):
                temp_dir.append(temp[str(direction[0])])
            sep = ', '
            await bot.send_photo(message.from_user.id, info[0],
                                 caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}")

    if message.text == '1':
        await bot.send_message(message.from_user.id, "Вот твоя анкета:", reply_markup=nav.MenuProfile)
        await send_self_profile(message)

    if message.text == '2' or message.text =="Возобновить поиск":
        status = db.check_status_acc(message.from_user.id)[0]
        if status == 1:

            await bot.send_message(message.from_user.id, "Жалко, что ты уходишь, возвращайся", reply_markup=nav.MenuMain_1)
            db.set_status_acc(message.from_user.id, 0)
        else:
            await bot.send_message(message.from_user.id, "С возвращением"+set_emoji(':hand:'))
            await bot.send_message(message.from_user.id, nav.menu_main_text, reply_markup=nav.MenuMain)
            db.set_status_acc(message.from_user.id, 1)

    if message.text == '3':
        await bot.send_message(message.from_user.id,'Данный бот разработан при выполнении Выпускной квалификационной работы \n '
                                                    'Студент группы 4816, Ослаповский И. А.\n '
                                                    'Почта для отзывов и предложений: bul.reyn@mail.ru ')


# --- Функция регистрации обработчиков ---
def handler_menu_main(dp: Dispatcher):
    dp.register_message_handler(check_buttons_main, text='1', state=fsm_main.menu)
    dp.register_message_handler(check_buttons_main, text='2', state=fsm_main.menu)
    dp.register_message_handler(check_buttons_main, text='Возобновить поиск', state=fsm_main.menu)
    dp.register_message_handler(check_buttons_main, text='3', state=fsm_main.menu)
    dp.register_message_handler(check_buttons_main, text='Смотреть анкеты ' + set_emoji(":eyes:"), state=fsm_main.menu)