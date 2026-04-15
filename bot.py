from pyrogram import Client
from config import Config  # Importing the class we created

# Initialize the Client using variables from config.py
app = Client(
    "TeraBoxBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins") # This tells the bot to look in the /plugins folder for commands
)

if __name__ == "__main__":
    print("🚀 TeraBox Ultra Bot is Starting...")
    app.run()
    
