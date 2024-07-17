from src.bot import bot, db
from states import Profile as fsm_prof
from src import markups as nav
from difflib import SequenceMatcher
import operator


async def send_self_profile(query):
    info = db.get_acc_info(query.from_user.id)
    # --- костыль для вывода названия направлений
    temp = {'1': 'Математика', '2': 'Физика', '3': 'Информатика', '4': 'Русский язык', '5': 'Химия',
            '6': 'История', '7': 'Обществознание', '8': 'Биология', '9': 'Английский', '10': 'Литература',
            '11': 'География'}
    temp_dir = []
    for direction in db.get_directions(query.from_user.id):
        temp_dir.append(temp[str(direction[0])])
    sep = ', '
    await bot.send_photo(query.from_user.id, info[0],
                         caption=f"{info[1]}, {info[2]} — {info[3]}\n{sep.join(temp_dir)}")
    await bot.send_message(query.from_user.id, nav.menu_profile_text, reply_markup=nav.MenuProfile)
    await fsm_prof.menu_profile.set()


async def get_data_profiles(message, state, ):
    async with state.proxy() as data:
        # получение списка активных пользователей
        user_list = []
        for user_id in db.get_active_user_id():
            user_list.append(user_id[0])
        data['active_user_id'] = user_list
        # получение словаря списка пользователй с их направлениями
        data['users_dirs'] = {}

        for user_id in user_list:
            # распаковка списка направлений с БД для добавления в словарь
            dir_list = []
            for direc in db.get_directions(user_id):
                dir_list.append(direc[0])
            dir_list.sort()
            data['users_dirs'][f'{user_id}'] = dir_list

        user_self_dir = data['users_dirs'].pop(f'{message.from_user.id}')

        # получение соотношения совпадений с направлениями пользователя и добавления этих значений в словарь
        sequence_dir = {}
        for sequence in data['users_dirs']:
            sequence_dir[f"{sequence}"] = SequenceMatcher(None, user_self_dir,
                                                          data['users_dirs'][f'{sequence}']).ratio()

        # функция соотношений совпадений, от самых больших к самым маленьким
        data['sequence_dir_sort'] = {k: v for k, v in sorted(sequence_dir.items(), key=operator.itemgetter(1))}





