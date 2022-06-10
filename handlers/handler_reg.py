from bot import bot, db
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from states import Registration as fsm_reg, Profile as fsm_prof

from send_menu import send_self_profile
import markups as nav
from bot_emoji import set_emoji


# --- Обработчик команды /start ---
# Ветвление событий в зависимости от наличия анкеты в БД:
# Если анкета имеется в БД, то она вывыдится пользователю и передает меню управления
# Если анкеты нет, то пользователь переходит в состояние регистрации
async def send_welcome(message: types.Message):
    if db.check_acc_exist(message.from_user.id) is None:
        await bot.send_message(message.from_user.id, "Здравствуй дружище!" + set_emoji(":hand:") +
                               "\nДля начала стоит заполнить свою анкету ")
        await bot.send_message(message.from_user.id, set_emoji(":point_down:"))

        await bot.send_message(message.from_user.id, "Напиши как тебя зовут ?")
        db.add_acc(message.from_user.id)
        await fsm_reg.set_nickname.set()
    else:
        await bot.send_message(message.from_user.id, "Тю, так мы знакомы, вот твоя анкета")
        await send_self_profile(message)


# --- Обработчик сохранения имени/никнейма ---
async def set_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text
    await bot.send_message(message.from_user.id, "А сколько тебе лет ?")
    await fsm_reg.next()


# --- Обработчик сохранения возраста ---
async def set_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
    await bot.send_message(message.from_user.id, "А теперь отправь сообщение о себе")
    await fsm_reg.next()


# ---Обработчик сохранения сообщения о себе ---
async def set_summary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["summary"] = message.text
    await bot.send_message(message.from_user.id, "А теперь отправь свое фото")
    await fsm_reg.next()


# ---Обработчик сохранения фото анкеты---
async def set_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["image"] = message.photo[0].file_id
    await bot.send_message(message.from_user.id, 'Выбери направления', reply_markup=nav.MenuDirectionSelection)
    async with state.proxy() as data:
        data["directions"] = {}
    await fsm_reg.next()


# Функция обработки inline клавиатуры
async def handling_choice(callback_query: types.CallbackQuery, state: FSMContext):
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
            await bot.answer_callback_query(callback_query.id, text=f"{sep.join(data['directions'].keys())}", show_alert=True)
    if code == 'C':
        async with state.proxy() as data:
            data['directions'].clear()
        await bot.answer_callback_query(callback_query.id, text='Очищены')

    if code == 'D':
        await bot.answer_callback_query(callback_query.id, text='Сохранено')
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        # Запись данных анкеты в БД
        async with state.proxy() as data:
            db.set_nickname(callback_query.from_user.id, data['nickname'])
            db.set_age(callback_query.from_user.id, data['age'])
            db.set_summary(callback_query.from_user.id, data['summary'])
            db.set_acc_image(callback_query.from_user.id, data['image'])
            for direction in list(data['directions'].values()):
                db.add_direction(callback_query.from_user.id, int(direction))
        # Отображение анкеты и вывод сообщения, описывающее меню
        await bot.send_message(callback_query.from_user.id, "Вот такая у тебя получилась анкета:", reply_markup=nav.MenuProfile)
        await send_self_profile(callback_query)
        await state.finish()
        await fsm_prof.menu_profile.set()


# --- Функция регистрации обработчиков ---
def handler_register(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'], state=None)
    dp.register_message_handler(set_nickname, state=fsm_reg.set_nickname)
    dp.register_message_handler(set_age, state=fsm_reg.set_age)
    dp.register_message_handler(set_summary, state=fsm_reg.set_summary)
    dp.register_message_handler(set_image, content_types=["photo"], state=fsm_reg.set_image)
    dp.register_callback_query_handler(handling_choice, lambda c: c.data and c.data.startswith('btn'),
                                       state=fsm_reg.set_directions)
