import re

def extract_terabox_link(text):
    """ Extracts the first TeraBox link found in a message """
    pattern = r"https?://(?:www\.)?(?:terabox|nephobox|teraboxapp|4shared)\.com/s/\S+"
    match = re.search(pattern, text)
    return match.group(0) if match else None

def apply_custom_branding(text, link, config):
    """
    Applies all user settings: Headers, Footers, 
    Hashtag replacement, and Link Hiding.
    """
    processed_text = text

    # 1. Replace Hashtags
    if config.get("replace_hashtag") and config.get("new_hashtag"):
        processed_text = re.sub(r'#\w+', config['new_hashtag'], processed_text)

    # 2. Replace URLs (if user wants to swap other links)
    if config.get("replace_url") and config.get("new_url"):
        processed_text = re.sub(r'http[s]?://(?:(?![terabox]).)\S+', config['new_url'], processed_text)

    # 3. Handle Link Visibility
    if config.get("hide_tera_link"):
        # Remove raw link from text and create a hyperlinked version
        processed_text = processed_text.replace(link, "").strip()
        final_body = f"{processed_text}\n\n🔗 [Click to View Content]({link})"
    elif config.get("only_links"):
        final_body = link
    else:
        final_body = processed_text

    # 4. Wrap with Header and Footer
    header = config.get("header", "")
    footer = config.get("footer", "")
    
    return f"{header}\n\n{final_body}\n\n{footer}".strip()

def get_readable_time(seconds: int) -> str:
    """ Helper to show how long a session has been active """
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and result == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time
  
