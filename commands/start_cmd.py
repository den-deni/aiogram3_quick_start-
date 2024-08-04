from aiogram.filters import Command
from aiogram import F, Router, html
from aiogram.types import Message


start_router = Router()


@start_router.message(Command('start'))
async def command_start(mess: Message):
    await mess.answer(f'Hello, {html.bold(mess.from_user.full_name)}!')

