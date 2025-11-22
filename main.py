import telebot
from telebot import types

from config import BOT_TOKEN, ADMINS
from menus import main_menu, social_inline, send_photo,donate_photo_coins,donate_photo_gems,donate_photo_season, stadium_kb, club_kb, sticker_kb
from donate import quick_donate
from admin_panel import admin_keyboard, list_orders, admin_update_from_callback


bot = telebot.TeleBot(BOT_TOKEN)

# /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    name = message.from_user.first_name or "User"
    bot.send_message(message.chat.id, f"Salom {name}! Mega DLS Botga xush kelibsiz 🎮", reply_markup=main_menu())

# Help yoki menu
@bot.message_handler(commands=["menu"])
def cmd_menu(message):
    bot.send_message(message.chat.id, "Asosiy menyu:", reply_markup=main_menu())

# Matnli menu handler
@bot.message_handler(func=lambda m: True)
def handler(message):
    text = message.text
    chat = message.chat.id

    # ORQAGA
    if text == "⬅️ Orqaga":
        bot.send_message(chat, "Asosiy menyu:", reply_markup=main_menu())
        return

    # IJTIMOIY TARMOQLAR
    if text == "🌐 Ijtimoiy tarmoqlar":
        bot.send_message(chat, "Ijtimoiy tarmoqlarimiz:", reply_markup=social_inline())
        return


    # DONAT SERVIS (foto menyu)
    if text == "🛍 Donat Servis":
        # 1️⃣ Coins bo‘limi
        kb_coins = types.InlineKeyboardMarkup(row_width=1)
        kb_coins.add(types.InlineKeyboardButton("💰 Coins Buyurtma", callback_data="donate_coins"))
        kb_coins.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

        caption_coins = (
            "💰 *Coins Buyurtma*\n\n"
            "🔹 1000 Coins – Narxi: 5$\n"
            "🔹 5000 Coins – Narxi: 20$\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ☑️\n"
        )
        send_photo(bot, chat, "coins.jpg", caption_coins, kb_coins)

        # 2️⃣ Gems bo‘limi
        kb_gems = types.InlineKeyboardMarkup(row_width=1)
        kb_gems.add(types.InlineKeyboardButton("💎 Gems Buyurtma", callback_data="donate_gems"))
        kb_gems.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

        caption_gems = (
            "💎 *Gems Buyurtma*\n\n"
            "🔹 100 Gems – Narxi: 10$\n"
            "🔹 500 Gems – Narxi: 45$\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ☑️\n"

        )
        send_photo(bot, chat, "gems.jpg", caption_gems, kb_gems)

        # 3️⃣ Season Pass bo‘limi
        kb_season = types.InlineKeyboardMarkup(row_width=1)
        kb_season.add(types.InlineKeyboardButton("💳 Season Pass", callback_data="donate_season"))
        kb_season.add(types.InlineKeyboardButton("⬅️ Orqaga", callback_data="back_main"))

        caption_season = (
            "💳 *Season Pass*\n\n"
            "🔹 1 oylik Pass – Narxi: 50.000 ✅\n"
            "🔹 3 oylik Pass – Narxi: 120.000 ✅\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ☑️\n"

        )
        send_photo(bot, chat, "season pass.jpg", caption_season, kb_season)

        return

    if text =="🧑‍💻 admin":
        bot.send_message(chat,"admin:https://t.me/toshmirzayevinomjon",)
        return
    # STADIUM
    if text == "🏟 Stadion":
        message_text = (
            "🏟 *Stadionlar ro'yxati*\n\n"
            "1️⃣ *CHAMPIONS ARENA* 💸\n"
            "   Narxi: 400.000 ✅\n\n"
            "2️⃣ *CENTURY PARK* 💸\n"
            "   Narxi: 300.000 ✅\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ☑️\n"
            "📢 Qo‘shimcha ma’lumot uchun murojaat qiling."
        )
        send_photo(bot, chat, "stadium.jpg", message_text, stadium_kb())
        return

    # CLUB
    if text == "⚡ Dream Club":
        message_text = (
            "⚡ *Dream Club a’zolik paketlari*\n\n"
            "🔋 *EPIC CLUB MEMBER* – 10 kunlik\n"
            "   Narxi: 280.000 ✅\n\n"
            "🔋 *LEGENDARNY CLUB MEMBER* – 30 kunlik\n"
            "   Narxi: 380.000 ✅\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ☑️\n"        )
        send_photo(bot, chat, "dream club.jpg", message_text, club_kb())
        return

    # STICKER
    if text == "🎟 Sitikerlar":
        message_text = (
            "🎟 *Stikerlar ro'yxati*\n\n"
            "💰 Narxi: 50.000\n"
            "😍 Barcha stikerlar bir xil narxda\n\n"
            "👨‍💻 Admin: @toshmirzayevinomjon ✅\n"
        )
        send_photo(bot, chat, "sitiker.jpg", message_text, sticker_kb())
        return

    # DLS MA'LUMOT
    if text == "📘 DLS Ma’lumotlari":
        bot.send_message(chat, "xozircha bu qisim haqida ishlar olib borilmoqda siz ungacha admin murojat qilsangiz buladi:")
        return

    # ADMIN PANEL (faqat adminlarga)
    if chat in ADMINS:
        if text == "Admin panel":
            bot.send_message(chat, "Admin menyu:", reply_markup=admin_keyboard())
            return
        if text == "📦 Barcha buyurtmalar":
            list_orders(bot, chat)
            return

# Callback handler (inline tugmalar)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    chat = call.message.chat.id

    # Asosiyga qaytish
    if data == "back_main":
        bot.send_message(chat, "Asosiy menyu:", reply_markup=main_menu())
        bot.answer_callback_query(call.id)
        return

    # Donat tugmalari
    if data == "donate_coins":
        quick_donate(bot, chat, "Coins")
        bot.answer_callback_query(call.id, "Coins buyurtmasi tanlandi")
        return
    if data == "donate_gems":
        quick_donate(bot, chat, "Gems")
        bot.answer_callback_query(call.id, "Gems buyurtmasi tanlandi")
        return
    if data == "donate_season":
        quick_donate(bot, chat, "Season Pass")
        bot.answer_callback_query(call.id, "Season Pass buyurtmasi tanlandi")
        return

    # Stadion / club / sticker
    if data == "stadium_buy":
        quick_donate(bot, chat, "Stadium Upgrade")
        bot.answer_callback_query(call.id, "Stadion buyurtmasi")
        return
    if data == "club_info":
        bot.send_message(chat, "Dream Club haqida: ...")
        bot.answer_callback_query(call.id)
        return
    if data == "stick_buy":
        quick_donate(bot, chat, "Sticker")
        bot.answer_callback_query(call.id)
        return

    # Admin callback prefiksi
    if data.startswith("admin_"):
        # format admin_accept|orderid
        res = admin_update_from_callback(bot, data, call.from_user.id)
        # agar natija matn bo'lsa uni yubor
        if res:
            bot.send_message(call.from_user.id, res)
        bot.answer_callback_query(call.id)
        return

    bot.answer_callback_query(call.id, "Noma'lum tugma.")

if __name__ == "__main__":
    print("Bot ishga tushmoqda...")
    bot.infinity_polling()
