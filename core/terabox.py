import re
import aiohttp

async def get_terabox_data(url: str):
    # Regex to ensure it's a valid TeraBox link
    pattern = r"https?://(terabox|nephobox|teraboxapp)\.com/s/(\w+)"
    match = re.search(pattern, url)
    if not match:
        return None
    
    # Logic to return the standardized link
    # (Optional: Add scraping logic here if you need to fetch file titles)
    return url 
