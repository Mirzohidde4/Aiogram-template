from aiogram import Router
from filters.private_chat import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import admin, start, help
    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))

    router.include_routers(admin.router, start.router, help.router)

    return router