import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
# Optional: comma-separated Telegram numeric user IDs, e.g. "123456789,987654321"
ALLOWED_USER_IDS = {
    int(value.strip())
    for value in os.environ.get("ALLOWED_USER_IDS", "").split(",")
    if value.strip().isdigit()
}

def is_allowed(user_id: int) -> bool:
    # Until you configure an allowlist, permit /start so you can test the bot.
    return not ALLOWED_USER_IDS or user_id in ALLOWED_USER_IDS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not update.message:
        return
    if not is_allowed(user.id):
        await update.message.reply_text("این ربات خصوصی است و شما مجاز نیستید.")
        return
    await update.message.reply_text(
        "ربات حضور و غیاب آمادهٔ آزمایش است.\n\n"
        "دستورها:\n"
        "/help — راهنما\n"
        "/id — نمایش شناسه عددی تلگرام شما\n\n"
        "اتصال به فایل HTML در مرحله بعد انجام می‌شود."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    user = update.effective_user
    if not user or not is_allowed(user.id):
        await update.message.reply_text("این ربات خصوصی است و شما مجاز نیستید.")
        return
    await update.message.reply_text(
        "راهنما:\n"
        "/start — شروع\n"
        "/help — نمایش راهنما\n"
        "/id — نمایش شناسه عددی تلگرام\n\n"
        "فعلاً این نسخه فقط برای آزمایش اتصال ربات است؛ "
        "هنوز به فایل Attendance codes.html متصل نشده است."
    )

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not update.message:
        return
    if not is_allowed(user.id):
        await update.message.reply_text("این ربات خصوصی است و شما مجاز نیستید.")
        return
    await update.message.reply_text(f"شناسه عددی تلگرام شما: {user.id}")

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN is missing. Set it as an environment variable; "
            "never hard-code or share your token."
        )
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", id_command))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
