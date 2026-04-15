import re
from pyrogram import Client, filters
from database.db_handler import get_user_config

@Client.on_message(filters.regex(r"https?://(terabox|nephobox).+"))
async def process_and_forward(client, message):
    user_id = message.from_user.id
    config = await get_user_config(user_id)
    
    # 1. Process Text (Replacement Logic)
    text = message.text
    if config.get("replace_hashtag"):
        text = re.sub(r'#\w+', config['new_hashtag'], text)
    
    if config.get("replace_url"):
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', config['new_url'], text)

    # 2. Add Branding
    header = config.get("header", "")
    footer = config.get("footer", "")
    final_post = f"{header}\n\n{text}\n\n{footer}"

    # 3. Execution (Direct Reply + Auto-Forward)
    await message.reply_text(f"✅ **Processed Content:**\n\n{final_post}")

    if config.get("auto_forward_on"):
        for cat, channels in config.get("categories", {}).items():
            for channel_id in channels:
                try:
                    await client.send_message(chat_id=channel_id, text=final_post)
                except Exception as e:
                    print(f"Forwarding failed for {channel_id}: {e}")
                  
