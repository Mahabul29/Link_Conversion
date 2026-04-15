# 🔥 ADVANCED TERABOX CONVERTER & AUTO FORWARDER 🔥

A high-performance Telegram Bot built with **Python** and **Pyrogram**. This bot is designed for content creators who need to convert TeraBox links at scale and distribute them across multiple channels with custom branding.

---

## 🚀 Key Features

* 🎯 **Advanced TeraBox Conversion:** Instantly process TeraBox links for your audience.
* 📤 **Multi-Category Auto-Forwarder:**
    * Create up to **5 custom categories**.
    * Add up to **10 channels** per category.
    * Toggle between **Auto** and **Manual** forwarding modes.
* 🎨 **Full Customization:**
    * Set custom **Headers** and **Footers**.
    * Attach custom **Banners** to every post.
    * **Hide Tera Links:** Clean look using hyperlinked text.
* ⚙️ **Smart Filters:**
    * `Only Links Mode`: Removes all text, leaving only the URL.
    * `Hashtag Replacer`: Automatically swaps existing tags for your own.
    * `URL Replacer`: Replaces third-party links with your target URL.

---

## 🛠️ Commands

| Command | Description |
| :--- | :--- |
| `/start` | Start the bot and view the interactive menu |
| `/auto_forward` | Setup and manage your channel categories |
| `/header` | Set a custom header for your posts |
| `/footer` | Set a custom footer for your posts |
| `/replace_hashtag` | Replace all incoming hashtags with your own |
| `/only_links` | Toggle mode to strip text and only keep links |
| `/hide_tera_link` | Toggle hyperlinked text (Hide raw URL) |
| `/session` | Connect your session for restricted content |

---

## 🏗️ Quick Deployment

### 1. Requirements
* Python 3.9 or higher
* Telegram `API_ID` and `API_HASH` (get them from [my.telegram.org](https://my.telegram.org))
* A Bot Token from [@BotFather](https://t.me/BotFather)
* MongoDB Cluster (Free tier works perfectly)

### 2. Environment Variables
Create a `.env` file in the root directory:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_URI=your_mongodb_connection_string
