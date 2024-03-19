import contextlib
import asyncio

from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging

TOKEN = "6418642371:AAGmw6lsieRscKjeKxb1QGK3K_88rTyS9M8"
CHANNEL_ID = -1001761164730
ADMIN_ID = 1975980836

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = (f'👋 HOLA, AMIGO \n\n'
           f'TE LO ADVIERTO POR ULTIMA VEZ 🕢\n\n'
           f'🤔 Aún no me has escrito y estás esperando tu oportunidad?\n\n'
           f'💕Hoy me quedan 2 plazas en mi equipo.\n'
           f'No desperdicies la oportunidad, no habrá otra\n\n'
           f'👇ESCRIBEME AHORA MISMO\n\n'
           f'💎 @silvia_invers 💎\n\n'
           f'💎 @silvia_invers 💎\n\n'
           f'💎 @silvia_invers 💎\n\n')
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot: Bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id==CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f"[Exception] - {ex}", exc_info=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())