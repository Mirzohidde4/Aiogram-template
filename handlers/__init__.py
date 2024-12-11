from aiogram import Router
from filters.private_chat import ChatPrivateFilter
from filters.group import GroupFilter
from filters.admin import IsBotAdminFilter
from data.config import ADMINS


def setup_routers() -> Router:
    from .users import admin, start, help
    from .groups import group_start
    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(is_private=True))
    group_start.router.message.filter(GroupFilter())
    admin.router.message.filter(IsBotAdminFilter(user_ids=ADMINS))

    router.include_routers(admin.router, start.router, help.router, group_start.router)
    return router