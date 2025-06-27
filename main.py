from telethon import TelegramClient, events
from flask import Flask
import threading
import os

# Prendi i valori API_ID e API_HASH dalle variabili d'ambiente (le imposti su Railway)
api_id = int(os.environ.get("22413168"))
api_hash = os.environ.get("b7eac7c88749e112d062c0bdd1fdb1ab")
session_name = "userbot"

# Mini server web per tenere Railway attivo
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Userbot attivo su Railway"

def run():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run).start()

# Avvio del bot Telegram
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(pattern=r'^\.ping$'))
async def handler(event):
    await event.respond("🏓 Pong! (il bot è attivo)")

client.start()
client.run_until_disconnected()
git add .
git commit -m "Aggiunto codice Telethon userbot"
git push origin main  # o il branch che stai usando

