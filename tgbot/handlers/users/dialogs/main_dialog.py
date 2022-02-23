from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Start, Button
from aiogram_dialog.widgets.text import Const, Format

from tgbot.handlers.users.dialogs.getters import Getter
from tgbot.handlers.users.dialogs.registration import name_handler
from tgbot.states.states import MainSG, RegSG, Timetablenew, FastTimetable

dialog_main = Dialog(
    Window(
        Format('Привет!'),
        Button(Const('➡️ Вперед'), id='main_menu', on_click=name_handler),
        state=MainSG.greeting,
    ),
    Window(
        Format('<b>Главное меню</b>\n{name}', when='registered'),
        Group(
            Start(Const('Расписание'), id='utimetable', state=Timetablenew.choose_class),
            Button(Format('Настройки'), id='settings', ),
            Start(Format('Сегодня [{date}]'), id='now', data={'date': 'now'}, state=FastTimetable.main),  # TODO :
            Start(Format('Завтра [{next_date}]'), id='next_day', data={'date': 'next_day'}, state=FastTimetable.main),
            when='registered'
        ),
        Format('Необходима регистрация', when='not_registered'),
        Group(
            Start(Const('Регистрация'), id='register', state=RegSG.school, when='not_registered'),
        ),
        state=MainSG.main_menu,
        getter=Getter.check_exists,
    ),
)


async def start(c: CallbackQuery, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    await dialog_manager.start(MainSG.greeting, mode=StartMode.RESET_STACK)


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
