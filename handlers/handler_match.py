from bot import bot, db
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from states import Match as fsm_match, Main as fsm_main, Profile as fsm_prof

from send_menu import get_data_profiles, send_self_profile
import markups as nav
from bot_emoji import set_emoji


async def check_buttons_match(message: types.Message, state: FSMContext):
    if message.text == 'Меню':
        await bot.send_message(message.from_user.id, "Меню: ", reply_markup=nav.MenuMain)
        await bot.send_message(message.from_user.id, nav.menu_main_text)
        state.finish()
        await fsm_main.menu.set()

    if message.text == 'Смотреть анкеты '+set_emoji(":eyes:"):
        state.finish()
        await fsm_match.match.set()
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
                                 caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}", reply_markup=nav.MenuMatch)

    if message.text == set_emoji(':+1:'):
        async with state.proxy() as data:
            #отправленное сообщение тому кого лайкнули
            await bot.send_message(data['id'], 'Этот человек сказал мне, что хочет с тобой пообщаться:')
            info = db.get_acc_info(message.from_user.id)
            # --- костыль для вывода названия направлений
            temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика', '4': 'Русский язык', '5': 'Химия',
                    '6': 'История', '7': 'Обществознание', '8': 'Биология', '9': 'Английский', '10': 'Литература',
                    '11': 'География'}
            temp_dir = []
            for direction in db.get_directions(message.from_user.id):
                temp_dir.append(temp[str(direction[0])])

            sep = ', '
            await bot.send_photo(data['id'], info[0],
                                 caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}")
            await bot.send_message(data['id'], 'Этот человек хотел бы с тобой пообщаться, отвитишь взаимностью ?', reply_markup=nav.MenuMatchReply)
            #добавление лайка в бд
            db.add_likes(message.from_user.id, data['id'])
            await bot.send_message(message.from_user.id, "Я рассказал о тебе, этому человеку")

        flag = 1
        async with state.proxy() as data:
            if data['sequence_dir_sort'] == {}:
                flag = 0

        if flag == 0:
            await bot.send_message(message.from_user.id, 'Анкеты закончились, попробуй посмотреть ещё раз',
                                   reply_markup=nav.MenuSee)
        else:
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

    if message.text == set_emoji(':-1:'):
        flag = 1
        async with state.proxy() as data:
            if data['sequence_dir_sort'] == {}:
                flag = 0

        if flag == 0:
            await bot.send_message(message.from_user.id, 'Анкеты закончились, попробуй посмотреть ещё раз',
                                   reply_markup=nav.MenuSee)

        else:
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


async def check_buttons_match_reply(callback_query: types.CallbackQuery, state: FSMContext):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    # Считывание нажатий клавиатуры и запись данных в state.proxy
    if code == 1:
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)

        id_ = db.get_likes(callback_query.from_user.id)[0]

        print(id_)
        info = db.get_acc_info(callback_query.from_user.id)
        # --- костыль для вывода названия направлений
        temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика', '4': 'Русский язык', '5': 'Химия',
                '6': 'История', '7': 'Обществознание', '8': 'Биология', '9': 'Английский', '10': 'Литература',
                '11': 'География'}
        temp_dir = []
        for direction in db.get_directions(callback_query.from_user.id):
            temp_dir.append(temp[str(direction[0])])

        sep = ', '
        await bot.send_message(id_, "Этот человек ответил взаимностью и хотел бы пообщаться:")
        await bot.send_photo(id_, info[0],
                             caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}")
        await bot.send_message(id_,
                               'Чтобы связаться с ним нажми ' + f'<a href="tg://user?id={callback_query.from_user.id}">СЮДА</a>',
                               parse_mode="HTML")
        await bot.send_message(callback_query.from_user.id,
                               'Чтобы связаться с ним нажми ' + f'<a href="tg://user?id={id_}">СЮДА</a>',
                               parse_mode="HTML")

        db.del_likes(id_ ,callback_query.from_user.id )
        print(callback_query.from_user.id, '   ', id_)

    if code == 2:
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, '')



def handler_menu_match(dp: Dispatcher):
    dp.register_message_handler(check_buttons_match, text='Меню', state=fsm_match.match)
    dp.register_message_handler(check_buttons_match, text=set_emoji(':+1:'), state=fsm_match.match)
    dp.register_message_handler(check_buttons_match, text=set_emoji(':-1:'), state=fsm_match.match)
    dp.register_message_handler(check_buttons_match, text='Смотреть анкеты '+set_emoji(":eyes:"), state=fsm_match.match)

    dp.register_callback_query_handler(check_buttons_match_reply,
                                       lambda c: c.data and c.data.startswith('match_rep'),
                                       state=fsm_prof.menu_profile)
