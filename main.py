import asyncio
from colorama import Fore

from aiogram import Bot

from bot import dp
from settings import settings


async def start() -> None:
    bot = Bot(token=settings.api_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print(f"{Fore.YELLOW}[LOG] Систему LTM запущено!{Fore.RESET}")
    asyncio.run(start())
