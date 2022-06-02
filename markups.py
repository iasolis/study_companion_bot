from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot_emoji import set_emoji

# --- Profile Menu ---
btnChangeNameAge = KeyboardButton('1')
btnChangeImg = KeyboardButton('2')
btnChangeSummary = KeyboardButton('3')
#
btnChangeEdu = KeyboardButton('4')
#
btnChangeProfile = KeyboardButton('5')

btnStartMatching = KeyboardButton('Смотреть анкеты '+set_emoji(":eyes:"))
MenuProfile = ReplyKeyboardMarkup(resize_keyboard=True).row(btnChangeNameAge,btnChangeImg,
                                                            btnChangeSummary, btnChangeEdu,btnChangeProfile).add(btnStartMatching)

menu_profile_text = "1. Изменить имя/никнейм и возраст. \n"+\
        "2. Изменить фото. \n"+\
        "3. Изменить текст анкеты.  \n"+\
        "4. Изменить направления. \n"+\
        "5. Заполнить анкету заново. "

menu_main_text = "1. Профиль. \n"+\
        "2. Остановить поиск. \n"+\
        "3. Информация. \n"

menu_main_text1 = "1. Профиль. \n"+\
        "2. Возобновить поиск. \n"+\
        "3. Информация. \n"


# --- Direction Selection Menu ---
btn_dir_sel_1 = InlineKeyboardButton('Матем', callback_data='btn1')
btn_dir_sel_2 = InlineKeyboardButton('Физика', callback_data='btn2')
btn_dir_sel_3 = InlineKeyboardButton('Инфо', callback_data='btn3')
btn_dir_sel_4 = InlineKeyboardButton('Проверить', callback_data='btn4')
btn_dir_sel_5 = InlineKeyboardButton('Удалить', callback_data='btn5')
btn_dir_sel_6 = InlineKeyboardButton('Сохранить', callback_data='btn6')
MenuDirectionSelection = InlineKeyboardMarkup().row(btn_dir_sel_1, btn_dir_sel_2,
                                                    btn_dir_sel_3).row(btn_dir_sel_4, btn_dir_sel_5, btn_dir_sel_6)

# --- Match Menu ---
btnLike = KeyboardButton(set_emoji(":+1:"))
btnDislike = KeyboardButton(set_emoji(":-1:"))
btnMenu = KeyboardButton('Меню')
MenuMatch = ReplyKeyboardMarkup(resize_keyboard=True ).row(btnLike, btnDislike, btnMenu)

# --- Main Menu ---
btnProfileMenu = KeyboardButton('1')
btnFinishMatch = KeyboardButton('2')
btnInfo = KeyboardButton('3')
btnMatchMenu = KeyboardButton('Смотреть анкеты '+set_emoji(":eyes:"))
MenuMain = ReplyKeyboardMarkup(resize_keyboard=True).row(btnProfileMenu, btnFinishMatch, btnInfo).add(btnMatchMenu)

# --- Reply match menu ---
match_rep1 = InlineKeyboardButton('Да', callback_data='match_rep1')
match_rep2 = InlineKeyboardButton('Нет', callback_data='match_rep2')
MenuMatchReply = InlineKeyboardMarkup().row(match_rep1, match_rep2)

# -------------------------
MenuSee = ReplyKeyboardMarkup(resize_keyboard=True).row(btnMatchMenu, btnMenu)
MenuMain_1 = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('Возобновить поиск'))













