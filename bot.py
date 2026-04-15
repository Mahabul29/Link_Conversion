from utils.helper_func import extract_terabox_link, apply_custom_branding

@app.on_message(filters.text)
async def on_new_link(client, message):
    link = extract_terabox_link(message.text)
    if link:
        # Get user settings from DB
        user_config = await db.get_user_config(message.from_user.id)
        
        # Process the message using our helper
        final_output = apply_custom_branding(message.text, link, user_config)
        
        # Send & Forward
        await message.reply_text(final_output)
        # (Add your auto_forward logic here)
        
