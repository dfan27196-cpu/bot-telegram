from pyrogram import Client

API_ID = 31846368
API_HASH = "c02139db5e8bc7a6252b2375e4be6dac"
PHONE_NUMBER = "+6282143999212"

app = Client("my_account", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

async def main():
    async with app:
        print("\n" + "="*50)
        print("STRING SESSION KAMU:")
        print(await app.export_session_string())
        print("="*50 + "\n")

app.run(main())
