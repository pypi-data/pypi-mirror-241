from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.enums import MessageEntityType
from pyrogram.errors import RPCError

from .base import Monitor


class PornembyDoubleMonitor(Monitor):
    name = "Pornemby 怪兽自动翻倍"
    chat_user = "PronembyTGBot2_bot"
    chat_name = "Pornemby"
    chat_keyword = "击杀者\s+(.*)\s+是否要奖励翻倍"
    additional_auth = ["pornemby_pack"]

    async def on_trigger(self, message: Message, key, reply):
        for me in message.entities:
            if me.type == MessageEntityType.TEXT_MENTION:
                if me.user.id == self.client.me.id:
                    if isinstance(message.reply_markup, InlineKeyboardMarkup):
                        try:
                            await message.click("🎲开始翻倍游戏")
                        except RPCError:
                            pass
                        else:
                            self.log.info("检测到 Pornemby 怪兽击败, 已点击翻倍.")
                            return
