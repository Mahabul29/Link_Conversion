from pyrogram import Client, filters

@Client.on_message(filters.command("auto_forward"))
async def setup_forwarding(client, message):
    text = (
        "🚀 **AUTO FORWARD SETTINGS**\n\n"
        "📂 **Categories:** Create up to 5 categories.\n"
        "📺 **Channels:** Add up to 10 channels per category.\n\n"
        "Use `/add_cat [name]` to create a category.\n"
        "Use `/add_channel [cat_name] [channel_id]` to link a channel."
    )
    await message.reply_text(text)

@Client.on_message(filters.command("header"))
async def set_header(client, message):
    new_header = message.text.split(None, 1)[1]
    # Update DB logic here
    await message.reply_text(f"✅ **Header Updated:**\n`{new_header}`")
  
