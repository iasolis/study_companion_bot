from aiogram.dispatcher.filters.state import StatesGroup, State


# --- Registration ---
class Registration(StatesGroup):
    set_nickname = State()
    set_age = State()
    set_summary = State()
    set_image = State()
    set_directions = State()


# --- Profile ---
class Profile(StatesGroup):
    menu_profile = State()


class ChangeProfile(StatesGroup):
    nickname = State()
    age = State()
    summary = State()
    image = State()
    directions = State()


# --- Match ---
class Match(StatesGroup):
    match = State()


# --- Main menu ---
class Main(StatesGroup):
    menu = State()
