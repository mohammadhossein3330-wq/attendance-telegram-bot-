# Attendance Telegram Bot — starter

This is a minimal Telegram bot starter for the Attendance codes project.

## Commands
- `/start`
- `/help`
- `/id`

**Important:** This starter is not yet connected to `Attendance codes.html` or a shared database. It does not validate attendance codes yet. That integration is the next step.

## Run locally
1. Install Python 3.10 or newer.
2. In this folder, install dependencies:
   `pip install -r requirements.txt`
3. Set the bot token as an environment variable (do not paste it into source code):
   - Windows PowerShell: `$env:BOT_TOKEN="YOUR_TOKEN"`
   - macOS/Linux: `export BOT_TOKEN="YOUR_TOKEN"`
4. Optional privacy allowlist:
   `ALLOWED_USER_IDS="123456789,987654321"`
5. Run:
   `python bot.py`

Start with an empty `ALLOWED_USER_IDS` only while testing. Once you know both Telegram numeric IDs, set the allowlist to those IDs.

## Security
- Never publish your bot token in GitHub or send it in chat.
- If the token is exposed, revoke it with BotFather and generate a new one.
