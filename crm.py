# crm.py
from utils import load_orders, save_orders, new_order_id, now_str

def add_order(user_id, username, item, amount, payment_method, note=""):
    orders = load_orders()
    oid = new_order_id()
    orders[oid] = {
        "user_id": user_id,
        "username": username,
        "item": item,
        "amount": amount,
        "payment_method": payment_method,
        "note": note,
        "status": "kutilmoqda",
        "created_at": now_str(),
        "updated_at": now_str()
    }
    save_orders(orders)
    return oid

def update_order_status(order_id, status, admin_id=None):
    orders = load_orders()
    if order_id not in orders:
        return False
    orders[order_id]["status"] = status
    orders[order_id]["updated_at"] = now_str()
    if admin_id:
        orders[order_id]["admin"] = admin_id
    save_orders(orders)
    return True

def get_order(order_id):
    orders = load_orders()
    return orders.get(order_id)

def all_orders():
    return load_orders()
