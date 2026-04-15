import os
from dotenv import load_dotenv

# Load local .env file if it exists (for local testing)
load_dotenv()

class Config:
    # --- Telegram API Credentials ---
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # --- Database Configuration ---
    # Defaulting to a local URI if MONGO_URI isn't provided
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "TeraBoxUltraBot")
    
    # --- Bot Ownership & Logging ---
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0")) # For tracking errors/new users
    
    # --- Feature Defaults ---
    MAX_CATEGORIES = 5
    MAX_CHANNELS_PER_CAT = 10
    
    # --- External Resources ---
    START_BANNER = os.getenv("START_BANNER", "https://telegra.ph/your-default-image.jpg")
    SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/YourSupport")
  
