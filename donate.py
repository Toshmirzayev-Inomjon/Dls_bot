# donate.py
from telebot import types
from crm import add_order, get_order
from utils import save_orders, load_orders







def quick_donate(bot, chat_id, item_label):
    # tez buyurtma (masalan coins tugmasidan keladi)
    msg = bot.send_message(chat_id, f"siz buyurtma uchun adminga murojat qiling.")
