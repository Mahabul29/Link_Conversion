from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
🔥 **ADVANCED TERABOX CONVERTER & AUTO FORWARDER** 🔥

I am the most powerful TeraBox utility bot on Telegram. Send me any TeraBox link, and I will process it with your custom branding and forward it to your channels instantly!

🚀 **CORE FEATURES:**
🎯 **Convert:** TeraBox links to high-speed TeraBox links
📤 **Auto-Forward:** Multiple channels & 5 Categories
📝 **Branding:** Custom Headers, Footers & Banners
#️⃣ **Replacement:** Auto-replace hashtags & URLs
🔒 **Stealth:** Hide TeraBox links behind text

📊 **Earning Potential:** Optimized for high CPM... better than mdisk!
"""

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    # Using a professional button layout
    buttons = [
        [
            InlineKeyboardButton("📢 Setup Auto-Forward", callback_data="setup_forward"),
            InlineKeyboardButton("⚙️ Settings", callback_data="user_settings")
        ],
        [
            InlineKeyboardButton("🔗 Shortener Setup", callback_data="setup_shortener"),
            InlineKeyboardButton("🛠 Help & Commands", callback_data="help_cmds")
        ],
        [
            InlineKeyboardButton("👑 Support Group", url="https://t.me/YourSupportGroup")
        ]
    ]
    
    await message.reply_photo(
        photo="https://telegra.ph/your-banner-url.jpg", # Optional Banner Image
        caption=START_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
  
