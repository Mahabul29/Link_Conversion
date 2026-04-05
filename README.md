# 🚀 TeraBox Link Converter & Media Forwarder

A professional Telegram bot designed to convert TeraBox links into your personal affiliate links. This bot allows you to manage your earnings directly through Telegram without needing the TeraBox app.

---

## 🌟 Key Features

### 🔗 1. Intelligent Link Conversion
- Automatically detects TeraBox, NephoBox, and alternate domain links.
- Converts links instantly using your connected account credentials.
- Supports single links or links embedded within long text.

### 🖼️ 2. Media & Caption Support (Unique!)
- **Photo + Link:** Send a photo with a TeraBox link in the caption. The bot will return the **same photo** but with your **new converted link** attached.
- Preserves original formatting and emojis from the source post.

### 🔑 3. Session Connection
- No password required! Connect securely using your **NDUS Cookie**.
- Persistent sessions: The bot remembers your account via a built-in database (`database/`).
- Use `/session` to link or update your account anytime.

---

## 📂 Repository Structure

Based on professional deployment standards:

- `main.py`: The entry point for the Telegram bot.
- `config.py`: Configuration for API ID, HASH, and BOT TOKEN.
- `helper_func.py`: Logic for link extraction and TeraBox API interactions.
- `database/`: Stores user sessions and preferences (SQLite/MongoDB).
- `plugins/`: Modular handlers for commands and link processing.
- `requirements.txt`: List of Python dependencies.

---

## 🛠️ Quick Setup Guide

### 1. Installation
```bash
git clone [https://github.com/yourusername/terabox-bot.git](https://github.com/yourusername/terabox-bot.git)
cd terabox-bot
pip install -r requirements.txt
