from pyrogram import Client

API_ID = 31846368
API_HASH = "c02139db5e8bc7a6252b2375e4be6dac"

with Client("generate_session", api_id=API_ID, api_hash=API_HASH) as app:
    print("\n" + "="*50)
    print("STRING SESSION KAMU:")
    print(app.export_session_string())
    print("="*50 + "\n")
  
