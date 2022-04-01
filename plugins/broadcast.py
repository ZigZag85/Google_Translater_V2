from pyrogram import Client ,filters
import os
from helper.database import getid
ADMIN = int(os.environ.get("ADMIN", 923943045))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Verilənlər bazasından bütün idlər alınır ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Yayım Başlayır  .... \n Mesaj Göndərilir  {tot} İstifadəçilərə")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass
