import datetime

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import ctx_data
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards import nav_btns
    # test_keyboards
from tgbot.services.repository import Repo

opts = {"hey": ('Привет', 'Здравствуйте', 'Доброе утро', 'Добрый день', 'Добрый вечер', 'Доброй ночи')}


async def greeting(user_id):
    data = ctx_data.get()
    repo = data.get("repo")
    name = await repo.get_user_name(user_id)
    now = datetime.datetime.now()
    now += datetime.timedelta(hours=1)
    if 4 < now.hour <= 12:
        greet = opts["hey"][2]
    if 12 < now.hour <= 16:
        greet = opts["hey"][3]
    if 16 < now.hour <= 24:
        greet = opts["hey"][4]
    if 0 <= now.hour <= 4:
        greet = opts["hey"][5]

    text = f'{greet}, {name}🖤'
    return text


async def main_menu_admin(c: CallbackQuery, state: FSMContext):
    await state.reset_state()
    await c.answer()
    await c.message.edit_text(f'<b>Главное меню</b>\n{await greeting(c.from_user.id)}',
                              reply_markup=nav_btns.admin_main_menu, parse_mode='HTML')


async def get_user_list(c: CallbackQuery, repo: Repo):
    await c.answer()
    await c.message.edit_text(await repo.list_all_users(), reply_markup=nav_btns.admin_users_list)


async def get_today_user_list(c: CallbackQuery, repo: Repo):
    await c.message.edit_text(await repo.list_all_today_users(), reply_markup=nav_btns.back_to_mm)


async def get_user_info(message: types.message, repo: Repo):
    info = message.get_args()
    try:
        await message.answer(await repo.user_info(info), parse_mode='HTML', reply_markup=nav_btns.back_to_mm)
    except:
        await message.answer('Ошибка')


async def add_vip_user(m: Message, repo: Repo):
    info = m.get_args()
    await m.answer(f"Статус обновлен. Текущий статус - {await repo.add_vip_user(int(info))}")


async def admin_panel_switch(m: Message, repo: Repo):
    await repo.admin_switch(int(m.from_user.id))
    await m.delete()
    await m.answer(f'<a href="tg://user?id={m.from_user.id}">Успешно</a>', parse_mode='HTML')


# async def admin_test(m: Message):
#     await m.answer('TEST', reply_markup=test_keyboards.fruits_kbd)


def register_admin(dp: Dispatcher):
    dp.register_callback_query_handler(get_user_list, text=['admin_all_users'], is_admin=True,
                                       state='*')
    dp.register_message_handler(get_user_info, commands=['i'], state='*', is_admin=True)
    dp.register_message_handler(add_vip_user, commands=['vip'], state='*', is_admin=True)
    dp.register_callback_query_handler(get_today_user_list, text=['admin_today_all_users'], state='*', is_admin=True)
    dp.register_message_handler(admin_panel_switch, commands='a', commands_prefix='!', state='*')
    # dp.register_message_handler(admin_test, commands='tt', state='*')
