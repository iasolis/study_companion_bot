from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot_emoji import set_emoji

# --- Profile Menu ---
btnChangeNameAge = KeyboardButton('1')
btnChangeImg = KeyboardButton('2')
btnChangeSummary = KeyboardButton('3')
btnChangeEdu = KeyboardButton('4')
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
btn_dir_sel_1 = InlineKeyboardButton('Математика', callback_data='btn1') #
btn_dir_sel_2 = InlineKeyboardButton('Физика', callback_data='btn2')#
btn_dir_sel_3 = InlineKeyboardButton('Информатика', callback_data='btn3') #

btn_dir_sel_4 = InlineKeyboardButton('Русский язык', callback_data='btn4')#
btn_dir_sel_5 = InlineKeyboardButton('Химия', callback_data='btn5') #
btn_dir_sel_6 = InlineKeyboardButton('История', callback_data='btn6') #

btn_dir_sel_7 = InlineKeyboardButton('Обществознание', callback_data='btn7')#
btn_dir_sel_8 = InlineKeyboardButton('Биология', callback_data='btn8')#
btn_dir_sel_9 = InlineKeyboardButton('Английский', callback_data='btn9')

btn_dir_sel_E = InlineKeyboardButton('Литература', callback_data='btnE')
btn_dir_sel_A = InlineKeyboardButton('География', callback_data='btnA') #

btn_dir_sel_B = InlineKeyboardButton('Проверить', callback_data='btnB')
btn_dir_sel_C = InlineKeyboardButton('Удалить', callback_data='btnC')
btn_dir_sel_D = InlineKeyboardButton('Сохранить', callback_data='btnD')

MenuDirectionSelection = InlineKeyboardMarkup().row(btn_dir_sel_1, btn_dir_sel_2,
                                                    btn_dir_sel_3).row(btn_dir_sel_5, btn_dir_sel_8,
                                                    btn_dir_sel_A).row(btn_dir_sel_6, btn_dir_sel_7,
                                                    btn_dir_sel_E).row(btn_dir_sel_4,
                                                    btn_dir_sel_9).row(btn_dir_sel_B, btn_dir_sel_C, btn_dir_sel_D)

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













