from src.bot import bot, db
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from src.states import Profile as fsm_prof, ChangeProfile as fsm_change, Registration as fsm_reg, Match as fsm_match

from src import markups as nav
from src.bot_emoji import set_emoji
from src.send_menu import send_self_profile, get_data_profiles


async def check_buttons_menu_profile(message: types.Message, state: FSMContext):
    if message.text == '1':
        await bot.send_message(message.from_user.id, "Как тебя зовут ?")
        await fsm_change.nickname.set()

    if message.text == '2':
        await bot.send_message(message.from_user.id, "Отправь свое фото")
        await fsm_change.image.set()

    if message.text == '3':
        await bot.send_message(message.from_user.id, "Отправь сообщение о себе")
        await fsm_change.summary.set()

    if message.text == '4':
        await bot.send_message(message.from_user.id, 'Выбери направления', reply_markup=nav.MenuDirectionSelection)
        db.del_directions(message.from_user.id)
        async with state.proxy() as data:
            data["directions"] = {}
        await fsm_change.directions.set()

    if message.text == '5':
        await bot.send_message(message.from_user.id, "Как тебя зовут ?")
        db.del_directions(message.from_user.id)
        await fsm_reg.set_nickname.set()


    if message.text == 'Смотреть анкеты ' + set_emoji(":eyes:"):
        await bot.send_message(message.from_user.id, "Удачи в поисках", reply_markup=nav.MenuMatch)

        await fsm_match.match.set()
        # подтягивание данных и отправка анкет по ним
        await get_data_profiles(message, state)
        async with state.proxy() as data:
            await bot.send_message(message.from_user.id, set_emoji(':mag:'))
            data['id'] = data['sequence_dir_sort'].popitem()[0]
            info = db.get_acc_info(data['id'])

            # --- костыль для вывода названия направлений
            temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика', '4': 'Русский язык', '5': 'Химия',
                    '6': 'История', '7': 'Обществознание', '8': 'Биология', '9': 'Английский', '10': 'Литература',
                    '11': 'География'}
            temp_dir = []
            for direction in db.get_directions(data['id']):
                temp_dir.append(temp[str(direction[0])])
            sep = ', '
            await bot.send_photo(message.from_user.id, info[0],
                                 caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}")


async def change_name(message: types.Message):
    db.set_nickname(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, "А теперь отправь свой возраст")
    await fsm_change.age.set()


async def change_age(message: types.Message):
    db.set_age(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, "Вот твоя анкета:")
    await send_self_profile(message)


async def change_image(message: types.Message):
    db.set_acc_image(message.from_user.id, message.photo[0].file_id)
    await bot.send_message(message.from_user.id, "Вот твоя анкета:")
    await send_self_profile(message)


async def change_summary(message: types.Message):
    db.set_summary(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, "Вот твоя анкета:")
    await send_self_profile(message)


async def change_directions(callback_query: types.CallbackQuery, state: FSMContext):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)

    # Считывание нажатий клавиатуры и запись данных в state.proxy
    if code == 1:
        await bot.answer_callback_query(callback_query.id, text='Выбрана Математика')
        async with state.proxy() as data:
            data["directions"]['Математика'] = '1'
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Выбрана Физика')
        async with state.proxy() as data:
            data["directions"]['Физика'] = '2'
    if code == 3:
        await bot.answer_callback_query(callback_query.id, text='Выбрана Информатика')
        async with state.proxy() as data:
            data["directions"]['Информатика'] = '3'

    if code == 5:
        await bot.answer_callback_query(callback_query.id, text='Выбрана Химия')
        async with state.proxy() as data:
            data["directions"]['Химия'] = '5'
    if code == 8:
        await bot.answer_callback_query(callback_query.id, text='Выбрана Биология')
        async with state.proxy() as data:
            data["directions"]['Биология'] = '8'
    if code == 'A':
        await bot.answer_callback_query(callback_query.id, text='Выбрана География')
        async with state.proxy() as data:
            data["directions"]['География'] = '11'

    if code == 6:
        await bot.answer_callback_query(callback_query.id, text='Выбрана История')
        async with state.proxy() as data:
            data["directions"]['История'] = '6'
    if code == 7:
        await bot.answer_callback_query(callback_query.id, text='Выбрано Обществознание')
        async with state.proxy() as data:
            data["directions"]['Обществознание'] = '7'
    if code == 'E':
        await bot.answer_callback_query(callback_query.id, text='Выбрана Литература')
        async with state.proxy() as data:
            data["directions"]['Литература'] = '10'

    if code == 4:
        await bot.answer_callback_query(callback_query.id, text='Выбран Русский язык')
        async with state.proxy() as data:
            data["directions"]['Русский язык'] = '4'
    if code == 9:
        await bot.answer_callback_query(callback_query.id, text='Выбран Англ. язык')
        async with state.proxy() as data:
            data["directions"]['Английский'] = '9'

    if code == 'B':
        async with state.proxy() as data:
            sep = ', '
            await bot.answer_callback_query(callback_query.id, text=f"{sep.join(data['directions'].keys())}",
                                            show_alert=True)
    if code == 'C':
        async with state.proxy() as data:
            data["directions"].clear()
        await bot.answer_callback_query(callback_query.id, text='Очищены')

    if code == 'D':
        await bot.answer_callback_query(callback_query.id, text='Сохранено')
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        async with state.proxy() as data:
            for direction in list(data["directions"].values()):
                db.add_direction(callback_query.from_user.id, int(direction))

        await bot.send_message(callback_query.from_user.id, "Вот твоя анкета:")
        await send_self_profile(callback_query)


# --- Функция регистрации обработчиков ---
def handler_menu_profile(dp: Dispatcher):
    dp.register_message_handler(check_buttons_menu_profile, text='1', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='2', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='3', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='4', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='5', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='6', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='7', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='8', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='9', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='E', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='A', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='B', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='C', state=fsm_prof.menu_profile)
    dp.register_message_handler(check_buttons_menu_profile, text='D', state=fsm_prof.menu_profile)

    dp.register_message_handler(check_buttons_menu_profile, text='Смотреть анкеты ' + set_emoji(":eyes:"), state=fsm_prof.menu_profile)

    dp.register_message_handler(change_name, state=fsm_change.nickname)
    dp.register_message_handler(change_age, state=fsm_change.age)
    dp.register_message_handler(change_image, content_types=["photo"], state=fsm_change.image)
    dp.register_message_handler(change_summary, state=fsm_change.summary)

    dp.register_callback_query_handler(change_directions, lambda c: c.data and c.data.startswith('btn'),
                                       state=fsm_change.directions)

