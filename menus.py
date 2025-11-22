# menus.py
from telebot import types
from config import MEDIA_PATH

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🌐 Ijtimoiy tarmoqlar", "🛍 Donat Servis")
    keyboard.row("🏟 Stadion", "⚡ Dream Club")
    keyboard.row("🎟 Sitikerlar", "📘 DLS Ma’lumotlari","🧑‍💻 admin")
    keyboard.row("⬅️ Orqaga")
    return keyboard

def social_inline():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Telegram 📲", url="https://t.me/toshmirzayev_inomjon"))
    kb.add(types.InlineKeyboardButton("Instagram 📸", url="https://www.instagram.com/inomjon.lvl/"))
    kb.add(types.InlineKeyboardButton("YouTube ▶️", url="https://youtube.com/@new_rek_kanal?si=-Hbnk0V6yceqAX0p"))
    return kb

# ---------- DONAT BO‘LIMI ----------

def donate_service_menu(bot, chat_id):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("💰 Coins", callback_data="donate_coins"))
    kb.add(types.InlineKeyboardButton("💎 Gems", callback_data="donate_gems"))
    kb.add(types.InlineKeyboardButton("💳 Season Pass", callback_data="donate_season"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    bot.send_message(chat_id, "🛍 *Donat Servis* — bo‘limlardan birini tanlang:", reply_markup=kb, parse_mode="Markdown")

def donate_photo_coins(bot, chat_id):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("💰 Coins Buyurtma", callback_data="donate_coins"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

    caption = (
        "💰 *Coins Buyurtma*\n\n"
        "• Bundle : 35.000 ✅\n"
        "• Stack  : 70.000 ✅\n"
        "• Cup    : 115.000 ✅\n"
        "• Case   : 190.000 ✅\n"
        "• Locker : 330.000 ✅\n"
        "• Vault  : 700.000 ✅\n\n"
        "👨‍💻 Admin: @toshmirzayevinomjon ☑️"
    )

    send_photo(bot, chat_id, "coins.jpg", caption, kb)

def donate_photo_gems(bot, chat_id):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("💎 Gems Buyurtma", callback_data="donate_gems"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

    caption = (
        "💎 *Gems Buyurtma*\n\n"
        "💎 90 = 35.000 ✅\n"
        "💎 400 = 130.000 ✅\n"
        "💎 910 = 275.000 ✅\n"
        "💎 2.700 = 700.000 ✅\n"
        "💎 6.000 = 1.600.000 ✅\n\n"
        "👨‍💻 Admin: @toshmirzayevinomjon ☑️"
    )

    send_photo(bot, chat_id, "gems.jpg", caption, kb)


def donate_photo_season(bot, chat_id):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("💳 Season Pass", callback_data="donate_season"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

    caption = (
        "💳 *Season Pass*\n\n"
        "Sezon pass narxlari:\n"
        "• Aksiya kelgani: 25 000 soʻm 💵\n"
        "• Aksiya kelmagani: 38 000 soʻm 💵\n"
        "• Premium pass: 150 000 soʻm 💵\n\n"
        "👨‍💻 Admin: @toshmirzayevinomjon ☑️"
    )

    send_photo(bot, chat_id, "season_pass.jpg", caption, kb)

# ---------- STADION ----------

def stadium_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("🏟 Stadionni yaxshilash (buyurtma)", callback_data="stadium_buy"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

# ---------- DREAM CLUB ----------

def club_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("⚡ Dream Club info", callback_data="club_info"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

# ---------- STIKERLAR ----------

def sticker_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("🎟 Sticker buyurtma", callback_data="stick_buy"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

# ---------- SEND PHOTO FUNCTION ----------

def send_photo(bot, chat_id, filename, caption, inline_kb=None):
    path = f"{MEDIA_PATH}{filename}"
    try:
        with open(path, "rb") as ph:
            bot.send_photo(chat_id, ph, caption=caption, reply_markup=inline_kb, parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(chat_id, f"Rasm topilmadi: {filename}\n{caption}", reply_markup=inline_kb)
