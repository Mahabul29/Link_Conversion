# Function to apply "Only Links" or "Hide Link" modes
def apply_visibility_settings(text, link, settings):
    # Only Links Mode: Removes all text, only keeps the URL
    if settings.get("only_links_mode"):
        return link

    # Hide Tera Link: Turns the URL into a hyperlinked word
    if settings.get("hide_tera_link"):
        clean_text = text.replace(link, "")
        return f"{clean_text}\n\n🔗 [Click to View Content]({link})"
    
    return text
  
