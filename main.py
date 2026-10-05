import asyncio
import os
from pyrogram import Client, filters

# Data resmi milik kamu
API_ID = 31846368
API_HASH = "c02139db5e8bc7a6252b2375e4be6dac"
BOT_TOKEN = "8812594031:AAGGP0V1-pYyNGfFLCAmuBc7Wcy5docGpDk"

bot = Client("saver_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("saver_user", api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.private & filters.text)
async def process_link(client, message):
    url = message.text.strip()
    if "t.me/" not in url:
        await message.reply_text("Silakan kirim tautan pesan Telegram yang valid.")
        return

    status = await message.reply_text("⏳ Memproses link...")

    try:
        parts = url.split("/")
        msg_id = int(parts[-1])
        
        if "c/" in url:
            chat_id = int("-100" + parts[-2])
        else:
            chat_id = parts[-2]

        await status.edit_text("📥 Mengunduh media...")
        target_msg = await user.get_messages(chat_id, msg_id)

        if not target_msg.media:
            await status.edit_text("Pesan ini tidak berisi media.")
            return

        file_path = await user.download_media(target_msg)

        await status.edit_text("📤 Mengirim file ke obrolan...")
        await bot.send_document(
            chat_id=message.chat.id,
            document=file_path,
            caption="File berhasil diunduh!"
        )
        
        if os.path.exists(file_path):
            os.remove(file_path)
            
        await status.delete()

    except Exception as err:
        await status.edit_text(f"Gagal mengunduh: {str(err)}")

async def start_all():
    print("Menyalakan sesi akun dan bot...")
    await user.start()
    await bot.start()
    print("Bot siap digunakan!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_all())
