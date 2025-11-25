# menus.py
from telebot import types
from config import MEDIA_PATH

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🌐 Ijtimoiy tarmoqlar", "🛍 Donat Servis")
    keyboard.row("🏟 Stadion", "⚡ Dream Club")
    keyboard.row("🎟 Sitikerlar", "📘 DLS Ma’lumotlari", "🧑‍💻 admin")
    keyboard.row("⬅️ Orqaga")
    return keyboard

def social_inline():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("Telegram 📲", url="https://t.me/toshmirzay_inomjon"))
    kb.add(types.InlineKeyboardButton("Instagram 📸", url="https://www.instagram.com/inomjon.lvl/"))
    kb.add(types.InlineKeyboardButton("YouTube ▶️", url="https://youtube.com/@new_rek_kanal"))
    return kb

# Donat bo'limlari uchun ichki inline menyular (variantlar)
def coins_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("Bundle — 35.000", callback_data="item|coins_bundle"))
    kb.add(types.InlineKeyboardButton("Stack  — 70.000", callback_data="item|coins_stack"))
    kb.add(types.InlineKeyboardButton("Cup    — 115.000", callback_data="item|coins_cup"))
    kb.add(types.InlineKeyboardButton("Case   — 190.000", callback_data="item|coins_case"))
    kb.add(types.InlineKeyboardButton("Locker — 330.000", callback_data="item|coins_locker"))
    kb.add(types.InlineKeyboardButton("Vault  — 700.000", callback_data="item|coins_vault"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def gems_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("90 — 35.000", callback_data="item|gems_90"))
    kb.add(types.InlineKeyboardButton("400 — 130.000", callback_data="item|gems_400"))
    kb.add(types.InlineKeyboardButton("910 — 275.000", callback_data="item|gems_910"))
    kb.add(types.InlineKeyboardButton("2700 — 700.000", callback_data="item|gems_2700"))
    kb.add(types.InlineKeyboardButton("6000 — 1.600.000", callback_data="item|gems_6000"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def season_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("Aksiya: 25.000", callback_data="item|season_sale"))
    kb.add(types.InlineKeyboardButton("Normal: 38.000", callback_data="item|season_normal"))
    kb.add(types.InlineKeyboardButton("Premium: 150.000", callback_data="item|season_premium"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def stadium_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("🏟 Stadionni yaxshilash (buyurtma)", callback_data="item|stadium_upgrade"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def club_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("⚡ Dream Club info", callback_data="item|club_info"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def sticker_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton("🎟 Sticker buyurtma", callback_data="item|sticker_buy"))
    kb.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))
    return kb

def send_photo(bot, chat_id, filename, caption, inline_kb=None):
    path = f"{MEDIA_PATH}{filename}"
    try:
        with open(path, "rb") as ph:
            bot.send_photo(chat_id, ph, caption=caption, reply_markup=inline_kb, parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(chat_id, f"Rasm topilmadi: {filename}\n{caption}", reply_markup=inline_kb)
