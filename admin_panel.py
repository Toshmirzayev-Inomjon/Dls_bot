# admin_panel.py
from telebot import types

from config import ADMINS
from crm import all_orders, get_order, update_order_status

def admin_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📦 Barcha buyurtmalar", "✅ Buyurtma holatini yangilash")
    kb.row("🧾 Statistikalar", "⬅️ Orqaga")
    return kb


def list_orders(bot, chat_id):
    orders = all_orders()
    if not orders:
        bot.send_message(chat_id, "Hozircha buyurtma yo‘q.")
        return

    for oid, data in orders.items():
        text = (
            f"ID: `{oid}`\n"
            f"User: @{data.get('username')} ({data.get('user_id')})\n"
            f"Item: {data.get('item')}\n"
            f"Amount: {data.get('amount')}\n"
            f"Payment: {data.get('payment_method')}\n"
            f"Status: {data.get('status')}\n"
            f"Created: {data.get('created_at')}"
        )

        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("✅ Tasdiqlash", callback_data=f"admin_accept|{oid}"))
        kb.add(types.InlineKeyboardButton("❌ Bekor qilish", callback_data=f"admin_reject|{oid}"))
        kb.add(types.InlineKeyboardButton("✳ Qo'shimcha ma'lumot", callback_data=f"admin_info|{oid}"))

        bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=kb)


def admin_update_from_callback(bot, callback_data, admin_id):
    # callback_data format: action|orderid
    try:
        action, oid = callback_data.split("|", 1)
    except Exception:
        return "xato"

    if action == "admin_accept":
        update_order_status(oid, "tasdiqlandi", admin_id)
        return f"Buyurtma {oid} tasdiqlandi."

    if action == "admin_reject":
        update_order_status(oid, "bekor qilindi", admin_id)
        return f"Buyurtma {oid} bekor qilindi."

    if action == "admin_info":
        order = get_order(oid)
        if not order:
            return "Buyurtma topilmadi."

        return (
            f"ID: `{oid}`\n"
            f"User: @{order.get('username')} ({order.get('user_id')})\n"
            f"Item: {order.get('item')}\n"
            f"Amount: {order.get('amount')}\n"
            f"Payment: {order.get('payment_method')}\n"
            f"Status: {order.get('status')}\n"
            f"Note: {order.get('note')}"
        )

    return "Noma'lum harakat."
