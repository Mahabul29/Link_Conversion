from pyrogram import Client
from database.db import get_user_config

async def auto_forward_engine(client: Client, user_id: int, message_text: str):
    config = await get_user_config(user_id)
    
    # 1. Apply Customizations
    header = config.get("header", "🔥 **TeraBox Link** 🔥")
    footer = config.get("footer", "Join our channel for more!")
    
    # Replace Hashtags logic
    if config.get("replace_hashtag"):
        message_text = re.sub(r'#\w+', config['new_hashtag'], message_text)

    final_caption = f"{header}\n\n{message_text}\n\n{footer}"

    # 2. Forward to Categories
    if config.get("forwarding_enabled"):
        categories = config.get("categories", {}) # e.g., {"Movies": [ID1, ID2], "Apps": [ID3]}
        
        for category, channels in categories.items():
            for channel_id in channels:
                try:
                    await client.send_message(chat_id=channel_id, text=final_caption)
                except Exception as e:
                    print(f"Error forwarding to {category}: {e}")
                  
