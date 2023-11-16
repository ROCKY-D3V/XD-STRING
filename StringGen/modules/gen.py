import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Anony
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"𝘁𝗲𝗹𝗲𝘁𝗵𝗼𝗻"
    elif old_pyro:
        ty = f"ᴩ𝘆𝗿𝗼𝗴𝗿𝗮𝗺 v1"
    else:
        ty = f"ᴩ𝘆𝗿𝗼𝗴𝗿𝗮𝗺 v2"

    await message.reply_text(f"» 𝘁𝗿𝘆𝗶𝗻𝗴 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 {ty} 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿...")

    try:
        api_id = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝗽𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗮𝗽𝗶 𝗶𝗱 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝗲𝗱 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗶𝗺𝗲𝗱 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 5 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗵𝗲 𝗮𝗽𝗶 𝗶𝗱 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 𝗶𝗻𝘃𝗮𝗹𝗶𝗱.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝗽𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗮𝗽𝗶 𝗵𝗮𝘀𝗵 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝗲𝗱 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗶𝗺𝗲𝗱 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 5 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗵𝗲 𝗮𝗽𝗶 ʜᴀsʜ 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 𝗶𝗻𝘃𝗮𝗹𝗶𝗱.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text="» 𝗽𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗽𝗵𝗼𝗻𝗲 𝗻𝘂𝗺𝗯𝗲𝗿 𝘁𝗼 𝗽𝗿𝗼𝗰𝗲𝗲𝗱 :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗶𝗺𝗲𝗱 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 5 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Anony.send_message(user_id, "» 𝘁𝗿𝘆𝗶𝗻𝗴 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗼𝘁𝗽 𝗮𝘁 𝘁𝗵𝗲 𝗴𝗶𝘃𝗲𝗻 𝗻𝘂𝗺𝗯𝗲𝗿...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Anony.send_message(
            user_id,
            f"» 𝗳𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗰𝗼𝗱𝗲 𝗳𝗼𝗿 𝗹𝗼𝗴𝗶𝗻.\n\𝗻𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗳𝗼𝗿 {f.value or f.x} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀 𝗮𝗻𝗱 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Anony.send_message(
            user_id,
            "» 𝗮𝗽𝗶 𝗶𝗱 𝗼𝗿 𝗮𝗽𝗶 𝗵𝗮𝘀𝗵 𝗶𝘀 𝗶𝗻𝘃𝗮𝗹𝗶𝗱.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Anony.send_message(
            user_id,
            "» 𝗽𝗵𝗼𝗻𝗲 𝗻𝘂𝗺𝗯𝗲𝗿 𝗶𝗻𝘃𝗮𝗹𝗶𝗱.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    try:
        otp = await Anony.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"𝗽𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗼𝘁𝗽 𝘀𝗲𝗻𝘁 𝘁𝗼 {phone_number}.\n\n𝗶𝗳 𝗼𝘁𝗽 𝗶𝘀 <code>12345</code>, ᴩ𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗻𝗱 𝗶𝘁 𝗮𝘀 <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗶𝗺𝗲 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 10 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗵𝗲 𝗼𝘁𝗽 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 <b>𝘄𝗿𝗼𝗻𝗴.</b>\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Anony.send_message(
            user_id,
            "» 𝘁𝗵𝗲 𝗼𝘁𝗽 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 <b>ᴇxᴩɪʀᴇᴅ.</b>\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Anony.ask(
                identifier=(message.chat.id, user_id, None),
                text="» 𝗽𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝘁𝘄𝗼 𝘀𝘁𝗲𝗽 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘁𝗼 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲 :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Anony.send_message(
                user_id,
                "» 𝘁𝗶𝗺𝗲𝗱 𝗹𝗶𝗺𝗶𝘁 𝗿𝗲𝗮𝗰𝗵𝗲𝗱 𝗼𝗳 5 𝗺𝗶𝗻𝘂𝘁𝗲𝘀.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Anony.send_message(
                user_id,
                "» 𝘁𝗵𝗲 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘆𝗼𝘂'𝘃𝗲 𝘀𝗲𝗻𝘁 𝗶𝘀 𝘄𝗿𝗼𝗻𝗴.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝘀𝘁𝗮𝗿𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗮𝗴𝗮𝗶𝗻.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Anony.send_message(user_id, f"ᴇʀʀᴏʀ : <code>{str(ex)}</code>")

    try:
        txt = "𝗵𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 {0} 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻\n\n<code>{1}</code>\n\n𝗮 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗯𝗼𝘁 𝗯𝘆 <a href={2}>𝗫𝗗 𝗡𝗘𝗧𝗪𝗢𝗥𝗞</a>\n☠ <b>𝗻𝗼𝘁𝗲 :</b> 𝗱𝗼𝗻'𝘁 𝘀𝗵𝗮𝗿𝗲 𝗶𝘁 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂𝗿 𝗴𝗶𝗿𝗹𝗳𝗿𝗶𝗲𝗻𝗱."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@XD_N3TWORK"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("XD_N3TWORK")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Anony.send_message(
            chat_id=user_id,
            text=f"𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝘆𝗼𝘂𝗿 {ty} 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻.\n\n𝗽𝗹𝗲𝗮𝘀𝗲 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗮𝘃𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗳𝗼𝗿 𝗴𝗲𝘁𝘁𝗶𝗻𝗴 𝗶𝘁.\n\n𝗮 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗯𝗼𝘁 𝗯𝘆 <a href={SUPPORT_CHAT}>𝗫𝗗 𝗡𝗘𝗧𝗪𝗢𝗥𝗞</a>.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝘀𝗮𝘃𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» 𝗰𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱 𝘁𝗵𝗲 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗿𝗲𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» 𝗰𝗮𝗻𝗰𝗲𝗹𝗹𝗲𝗱 𝘁𝗵𝗲 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝘀𝘁𝗿𝗶𝗻𝗴 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀.", reply_markup=retry_key
        )
        return True
    else:
        return False
