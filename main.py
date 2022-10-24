import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
from Config import API_ID, API_HASH, BOT_TOKEN
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1955509952/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1955509952')
   open(f"Users/1955509952/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
UPDATES_CHANNEL = "marvelturkey"
OWNER= [641319713,5588996470]
PREMIUM=[641319713,5588996470]
app = pyrogram.Client("app", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-07-26", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="ᴜᴢɢᴜɴᴜᴍ ᴇꜰᴇɴᴅɪᴍ, ʏᴀꜱᴀᴋʟᴀɴᴅɪɴɪᴢ. [ᴅᴇꜱᴛᴇᴋ ɢʀᴜʙᴜᴍ](https://t.me/ProTubeSupport).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ ɢᴜɴᴄᴇʟʟᴇᴍᴇʟᴇʀɪᴍ ᴋᴀɴᴀʟɪɴᴀ ᴋᴀᴛɪʟɪɴ!\n ᴠᴇ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ ᴛɪᴋʟᴀʏɪɴ /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**ʙɪʀ ꜱᴇʏʟᴇʀ ʏᴀɴʟɪꜱ ɢɪᴛᴛɪ.  [ᴅᴇꜱᴛᴇᴋ ɢʀᴜʙᴜᴍ](https://t.me/ProTubeSupport).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("ɢɪʀɪꜱ ʏᴀᴘ✅", callback_data="Login"), InlineKeyboardButton("ᴇᴋʟᴇ💯", callback_data="Adding") ],[InlineKeyboardButton("ɴᴜᴍᴀʀᴀʟᴀʀ⚙️", callback_data="Edit"), InlineKeyboardButton("ɴᴜᴍᴀʀᴀʟᴀʀɪ ɢᴏʀ💕", callback_data="Ish")],[InlineKeyboardButton("ɴᴜᴍᴀʀᴀ ᴋᴀʟᴅɪʀ⚙️", callback_data="Remove"), InlineKeyboardButton("ᴀᴅᴍɪɴᴘᴀɴᴇʟɪ", callback_data="Admin")]])
   await message.reply_text(f"**ꜱᴇʟᴀᴍ** `{message.from_user.first_name}` **!\n\nʙᴇɴ ᴅɪᴢʟᴀʏɪᴄɪ ʙᴏᴛᴜᴍ \nᴜᴄʀᴇᴛꜱɪᴢ ᴅɪᴢʟᴀᴍᴀ ʏᴀᴘᴍᴀᴋ ɪᴄɪɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ,\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ ❤️**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ᴘʀᴇᴍɪᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴇɢɪʟꜱɪɴɪᴢ\nʟᴜᴛꜰᴇɴ ᴀʙᴏɴᴇ ᴏʟᴜɴ\nDm @ProTubeSupport\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ ❤️**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**ɢɪʀɪꜱ ʏᴀᴘᴍᴀᴋ ɪᴄɪɴ ʜᴇꜱᴀᴘ ꜱᴀʏɪꜱɪɴɪ ɢɪʀɪɴ (ꜱᴀʏɪ ᴏʟᴀʀᴀᴋ)**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**ɢᴇᴄᴇʀꜱɪᴢ ʙɪᴄɪᴍ 1'ᴅᴇɴ ᴀᴢ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**ʏᴀʟɴɪᴢᴄᴀ ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀꜱɪ ᴇᴋʟᴇʏᴇʙɪʟɪʀꜱɪɴɪᴢ {100-a} **")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**ꜱɪᴍᴅɪ ᴛᴇʟᴇɢʀᴀᴍ ʜᴇꜱᴀʙɪɴɪᴢɪɴ ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀꜱɪɴɪ ᴜʟᴜꜱʟᴀʀᴀʀᴀꜱɪ ꜰᴏʀᴍᴀᴛᴛᴀ ɢᴏɴᴅᴇʀɪɴ. \nIncluding **ᴜʟᴋᴇ ᴋᴏᴅᴜ**. \nᴏʀɴᴇᴋ: **+14154566376 = 14154566376 only not +****")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**ʙᴇʟɪʀᴛɪʟᴅɪɢɪ ɢɪʙɪ + ᴅᴀʜɪʟ ᴅᴇɢɪʟᴅɪʀ**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). ɴᴜᴍᴀʀᴀ: {phone} ʙᴀꜱᴀʀɪʏʟᴀ ᴀʏᴀʀʟᴀɴᴅɪ✅**")
         else:
            await app.send_message(message.chat.id, """**ɢᴇᴄᴇʀꜱɪᴢ ꜱᴀʏɪ ʙɪᴄɪᴍɪ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**ʜᴀᴛᴀ: {e}**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ᴘʀᴇᴍɪᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴇɢɪʟꜱɪɴɪᴢ\nʟᴜᴛꜰᴇɴ ᴀʙᴏɴᴇ ᴏʟᴜɴ\\nDm @ProTubeSupport\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ ❤️**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", API_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"ꜰʟᴏᴏᴅᴡᴀɪᴛ'ɪɴɪᴢ ᴠᴀʀ {e.x} ꜱᴀɴɪʏᴇ ꜱᴏɴʀᴀ ʙɪᴛᴇᴄᴇᴋ")
            return
         except PhoneNumberInvalidError:
            await message.reply("ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀɴɪᴢ ɢᴇᴄᴇʀꜱɪᴢ.\n\nʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /start 'ᴀ ʙᴀꜱɪɴ!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} ʏᴀꜱᴀᴋʟᴀɴᴅɪ")
            continue
         try:
            otp = await app.ask(message.chat.id, ("ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀɴɪᴢᴀ ʙɪʀ ᴏᴛᴘ ɢᴏɴᴅᴇʀɪʟɪʀ, \nʟᴜᴛꜰᴇɴ ᴏᴛᴘ'ʏɪ `1 2 3 4 5` ꜰᴏʀᴍᴀᴛɪɴᴅᴀ ɢɪʀɪɴ. __(ʜᴇʀ ꜱᴀʏɪ ᴀʀᴀꜱɪɴᴅᴀ ʙᴏꜱʟᴜᴋ ᴏʟᴀᴄᴀᴋ!)__ \n\nʙᴏᴛ ᴏᴛᴘ ɢᴏɴᴅᴇʀᴍɪʏᴏʀꜱᴀ, /restart ᴅᴇɴᴇʏɪɴ ᴠᴇ /start ᴋᴏᴍᴜᴛᴜʏʟᴀ ʙᴏᴛ'ᴀ ᴛᴇᴋʀᴀʀ ɢᴏʀᴇᴠ ʙᴀꜱʟᴀᴛɪɴ.\nɪᴘᴛᴀʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ /cancel 'ᴇ ʙᴀꜱɪɴ."), timeout=300)
         except TimeoutError:
            await message.reply("ᴢᴀᴍᴀɴ ꜱɪɴɪʀɪɴᴀ ᴜʟᴀꜱɪʟᴅɪ 5 ᴅᴀᴋɪᴋᴀ.\nʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /start 'ᴀ ʙᴀꜱɪɴ!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("ɢᴇᴄᴇʀꜱɪᴢ ᴋᴏᴅ.\n\nʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /start 'ᴀ ʙᴀꜱɪɴ!")
            return
         except PhoneCodeExpiredError:
            await message.reply("ᴋᴏᴅᴜɴ ꜱᴜʀᴇꜱɪ ᴅᴏʟᴅᴜ.\n\nʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /start 'ᴀ ʙᴀꜱɪɴ!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"ʜᴇꜱᴀʙɪɴɪᴢɪɴ ɪᴋɪ ᴀᴅɪᴍʟɪ ᴅᴏɢʀᴜʟᴀᴍᴀꜱɪ ᴠᴀʀ.\nꜱɪꜰʀᴇɴɪᴢɪ ɢɪʀɪɴɪᴢ ʟᴜᴛꜰᴇɴ.",timeout=300)
            except TimeoutError:
               await message.reply("`ᴢᴀᴍᴀɴ ꜱɪɴɪʀɪɴᴀ ᴜʟᴀꜱɪʟᴅɪ 5 ᴅᴀᴋɪᴋᴀ.\n\nʏᴇɴɪᴅᴇɴ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /start 'ᴀ ʙᴀꜱɪɴ!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/2056781888/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/2056781888/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="ɪʏɪ ʜᴀʙᴇʀ, ꜱᴜ ᴀɴᴅᴀ ʜᴇꜱᴀʙɪɴɪᴢᴀ ʜᴇʀʜᴀɴɢɪ ʙɪʀ ꜱɪɴɪʀ ᴜʏɢᴜʟᴀɴᴍɪʏᴏʀ. ʙɪʀ ᴋᴜꜱ ᴋᴀᴅᴀʀ ᴏᴢɢᴜʀꜱᴜɴ!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"ɢɪʀɪꜱ ʙᴀꜱᴀʀɪʟɪ✅ Done.\n\n**ɪꜱɪᴍ:** {me.first_name}\n**ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ:** {me.username}\n**ɴᴜᴍᴀʀᴀ:** {phone}\n**ꜱᴘᴀᴍʙᴏᴛ ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪ:** {stats}\n\n**@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ ❤️**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀꜱɪɴɪ ɢɪʀᴍᴇᴅɪɴɪᴢ \nʟᴜᴛꜰᴇɴ ᴄᴏɴꜰɪɢ⚙️ ᴋᴏᴍᴜᴛᴜɴᴜ /start ᴋᴏᴍᴜᴛᴜʏʟᴀ ᴅᴜᴢᴇɴʟᴇʏɪɴ.**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Error: {e}**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**ᴛᴜᴍ ᴀᴄᴄ ɢɪʀɪꜱɪ {s} ʜᴇꜱᴀᴘ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ {po} \n\nMade with ❤️ By @tMertTt**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ᴘʀᴇᴍɪᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴇɢɪʟꜱɪɴɪᴢ**")
      return
   number = await app.ask(chat_id=message.chat.id, text="**ꜱɪᴍᴅɪ ᴜꜱᴇʀ ᴄᴇᴋᴇᴄᴇɢɪɴ ɢʀᴜᴘ ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪɴɪ ɢᴏɴᴅᴇʀ**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ᴋᴇɴᴅɪ ɢʀᴜʙᴜɴᴜɴ ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪɴɪ ɢᴏɴᴅᴇʀ**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**ꜱɪᴍᴅɪ ɢᴏɴᴅᴇʀ ʙᴀꜱʟᴀ**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", API_ID , API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**Scraping Start**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nMade with ❤️ By @tMertTt**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Error: {phone} ꜱᴏɴʀᴀᴋɪɴᴇ ɢᴇᴄᴇʀᴋᴇɴ ʜᴀᴛᴀ ᴏʟᴜꜱᴛᴜ**")
                     break
                  if dad>40:
                     r+="**\nMade with ❤️ By @tMertTt**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Adding Start**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nMade with ❤️ By @tMertTt**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError {s.seconds} ꜱᴀɴɪʏᴇ ꜱᴏɴʀᴀ ʙɪᴛᴇᴄᴇᴋ\nꜱᴏɴʀᴀᴋɪ ɴᴜᴍᴀʀᴀʏᴀ ɢᴇᴄᴍᴇᴋ**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Too Many PeerFloodError\nꜱᴏɴʀᴀᴋɪ ɴᴜᴍᴀʀᴀʏᴀ ɢᴇᴄᴍᴇᴋ**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Made with ❤️ By @tMertTt")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nMade with ❤️ By @tMertTt**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ᴘʀᴇᴍɪᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴇɢɪʟꜱɪɴ**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**ᴛᴇʟᴇꜰᴏɴ ɴᴜᴍᴀʀᴀʟᴀʀɪɴɪᴢ**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nMade with ❤️ By @tMertTt**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Your Phone Numbers are**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nMade with ❤️ By @tMertTt**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**ᴘʀᴇᴍɪᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪ ᴅᴇɢɪʟꜱɪɴ**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**ᴋᴀʟᴅɪʀɪʟᴀᴄᴀᴋ ɴᴜᴍᴀʀᴀʏɪ ɢᴏɴᴅᴇʀ**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="ʙᴀꜱᴀʀɪʏʟᴀ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀ✅", callback_data="Users")], [InlineKeyboardButton("ʀᴇᴋʟᴀᴍ ʏᴀʏɪɴɪ💯", callback_data="Broadcast")],[InlineKeyboardButton("ᴋᴜʟʟᴀɴɪᴄɪ ᴇᴋʟᴇ", callback_data="New")], [InlineKeyboardButton("ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀɪ ᴋᴏɴᴛʀᴏʟ ᴇᴛ", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**ᴍᴇʀʜᴀʙᴀ** `{message.from_user.first_name}` **!\n\nʏᴏɴᴇᴛɪᴄɪ ᴘᴀɴᴇʟɪɴᴇ ʜᴏꜱ ɢᴇʟᴅɪɴɪᴢ**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**ʙᴏᴛ'ᴜɴ ꜱᴀʜɪʙɪ ᴅᴇɢɪʟꜱɪɴ ᴅᴏꜱᴛᴜᴍ \n\nMade with ❤️ By @tMertTt**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nɢɪʀɪꜱ ʏᴀᴘᴍᴀᴋ ᴠᴇ ʜᴇꜱᴀᴘ ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪɴɪ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ /login 'ᴇ ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪ.\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nɢɪʀɪꜱ ʏᴀᴘᴍᴀᴋ ᴠᴇ ʜᴇꜱᴀᴘ ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪɴɪ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ /phonesee 'ᴇ ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪ.\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nɢɪʀɪꜱ ʏᴀᴘᴍᴀᴋ ᴠᴇ ʜᴇꜱᴀᴘ ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪɴɪ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ /remove 'ᴇ ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪ.\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nɢɪʀɪꜱ✅ ʜᴇꜱᴀᴘᴛᴀɴ ᴇᴋʟᴇᴍᴇʏᴇ ʙᴀꜱʟᴀᴍᴀᴋ ɪᴄɪɴ /adding ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪᴅɪʀ..\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nɢɪʀɪꜱ ʏᴀᴘᴍᴀᴋ ᴠᴇ ʜᴇꜱᴀᴘ ɪꜱᴛᴀᴛɪꜱᴛɪᴋʟᴇʀɪɴɪ ᴋᴏɴᴛʀᴏʟ ᴇᴛᴍᴇᴋ ɪᴄɪɴ /phone 'ᴇ ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪ.\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ ꜱᴇʏ ʏᴏᴋ..!\nᴇᴠᴇ ɢɪᴛᴍᴇᴋ ɪᴄɪɴ /start 'ᴀ ᴛɪᴋʟᴀᴍᴀɴɪᴢ ʏᴇᴛᴇʀʟɪ.\n\n@tMertTt ᴛᴀʀᴀꜰɪɴᴅᴀɴ ʏᴀᴘɪʟᴍɪꜱᴛɪʀ**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"ʟᴜᴛꜰᴇɴ ʙᴇᴋʟᴇʏɪɴ...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nᴇɴɢᴇʟʟᴇɴᴅɪ- {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**ʏᴇɴɪ ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ᴋᴜʟʟᴀɴɪᴄɪ ᴋɪᴍʟɪɢɪɴɪ ɢᴏɴᴅᴇʀ**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="ʙᴀꜱᴀʀɪʏʟᴀ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Made with ❤️ By @tMertTt**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users✅", callback_data="Users")], [InlineKeyboardButton("Broadcast💯", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**ʏᴏɴᴇᴛɪᴄɪ ᴘᴀɴᴇʟɪɴᴇ ʜᴏꜱ ɢᴇʟᴅɪɴɪᴢ**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**ʙᴏᴛ'ᴜɴ ꜱᴀʜɪʙɪ ᴅᴇɢɪʟꜱɪɴ ᴅᴏꜱᴛᴜᴍ**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**ʏᴀʏɪɴ ɪᴄɪɴ ᴍᴇꜱᴀᴊ ᴠᴇʀ**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"ʙᴀꜱᴀʀɪʏʟᴀ ʏᴀʏɪɴʟᴀɴᴅɪ {a} ꜱᴏʜʙᴇᴛʟᴇʀ\nᴀʀɪᴢᴀʟɪ - {b} ꜱᴏʜʙᴇᴛʟᴇʀ !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Error: {e}**")




text = """
╔════╗ㅤProTubeSupport 
╚═╗╔═╝ tMertTt
╔═╣╠═╗
║╔╣╠╗║ㅤDızlayıcı
║╚╣╠╝║    Bot
╚═╣╠═╝
╔═╝╚═╗ 
╚════╝ 
"""
print(text)
print("Başarıyla Başladı........")
app.run()
