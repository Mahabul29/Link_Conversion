import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("TeraBoxBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Command: Trial Activation ---
@app.on_message(filters.command("activate_trial"))
async def start_trial(client, message: Message):
    # Logic: Check DB if user already used trial; if not, set expiry to 5 days.
    await message.reply_text("✅ **5-Day Premium Trial Activated!**\nYou now have access to Auto-Forwarding and Custom Headers.")

# --- Command: Setup Shortener ---
@app.on_message(filters.command("shortener_api"))
async def setup_api(client, message: Message):
    await message.reply_text("🔗 Send your Shortener API and Domain in this format:\n`DOMAIN | API_KEY`")

# --- Core: Link Processing & Auto-Forward ---
@app.on_message(filters.regex(r"https?://(terabox|nephobox).+"))
async def handle_links(client, message: Message):
    user_id = message.from_user.id
    original_link = message.text
    
    # 1. Convert/Process Link (Placeholder)
    converted_link = f"https://terabox.com/s/example_converted"
    
    # 2. Apply Custom Shortener
    # short_link = shorten_url(converted_link, user_api_key)
    
    # 3. Apply Custom Headers/Footers
    final_caption = f"🚀 **Your Converted Link:**\n\n{converted_link}\n\n🌟 Powered by TeraBox Ultra"
    
    await message.reply_text(final_caption)
    
    # 4. Trigger Auto-Forward Logic
    # await trigger_auto_forward(user_id, final_caption)

app.run()
