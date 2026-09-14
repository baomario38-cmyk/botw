import telebot
from telebot import types

# Thay thế bằng Token của bạn và ID Telegram của Admin
TOKEN = "8669420885:AAH95FXO5CbGVvyApmui-8On0uoDw4WFmp0"
ADMIN_ID = 7550929812  # Điền ID Telegram chuẩn của bạn vào đây

bot = telebot.TeleBot(TOKEN)

# Thông tin Ngân hàng của bạn
BANK_ID = "MB"          
ACCOUNT_NO = "0862446911" 
ACCOUNT_NAME = "NGUYEN QUOC BAO"

# Hệ thống danh mục và sản phẩm chi tiết dạng phân cấp
shop_categories = {
    "aimlock": {
        "title": "🎯 **DANH MỤC SẢN PHẨM: AIMLOCK**",
        "items": [
            {"id": "aim_1", "name": "AimLock Sensi 1.0", "price": "50.000đ", "amount": 50000, "image": "https://via.placeholder.com/400"},
            {"id": "aim_2", "name": "AimLock Utral 2.0", "price": "100.000đ", "amount": 100000, "image": "https://via.placeholder.com/400"},
            {"id": "aim_3", "name": "AimLock Premium 3.0", "price": "150.000đ", "amount": 150000, "image": "https://via.placeholder.com/400"},
            {"id": "aim_4", "name": "AimLock LuxVip 4.0", "price": "200.000đ", "amount": 200000, "image": "https://via.placeholder.com/400"}
        ]
    },
    "aim_filza": {
        "title": "📂 **DANH MỤC SẢN PHẨM: AIM FILZA**",
        "items": [
            {"id": "filza_1", "name": "Filza V1 Basic", "price": "60.000đ", "amount": 60000, "image": "https://via.placeholder.com/400"},
            {"id": "filza_2", "name": "Filza V2 Pro", "price": "120.000đ", "amount": 120000, "image": "https://via.placeholder.com/400"}
        ]
    },
    "slotvip": {
        "title": "🎰 **DANH MỤC SẢN PHẨM: SLOTVIP**",
        "items": [
            {"id": "slot_1", "name": "SlotVip Hack 1 Ngày", "price": "30.000đ", "amount": 30000, "image": "https://via.placeholder.com/400"},
            {"id": "slot_2", "name": "SlotVip Hack 1 Tháng", "price": "250.000đ", "amount": 250000, "image": "https://via.placeholder.com/400"}
        ]
    },
    "proxy": {
        "title": "🌐 **DANH MỤC SẢN PHẨM: PROXY**",
        "items": [
            {"id": "proxy_1", "name": "Proxy Việt Nam Sạch", "price": "40.000đ", "amount": 40000, "image": "https://via.placeholder.com/400"}
        ]
    },
    "modskin": {
        "title": "👕 **DANH MỤC SẢN PHẨM: MODSKIN**",
        "items": [
            {"id": "mod_1", "name": "Modskin FF Full Hiệu Ứng", "price": "80.000đ", "amount": 80000, "image": "https://via.placeholder.com/400"}
        ]
    },
    "menu_item": {
        "title": "📜 **DANH MỤC SẢN PHẨM: MENU**",
        "items": [
            {"id": "menu_1", "name": "Menu VIP Tổng Hợp", "price": "100.000đ", "amount": 100000, "image": "https://via.placeholder.com/400"}
        ]
    }
}

# Các mức giá nạp tiền mẫu
deposit_packages = {
    "dep_50k": {"amount": 50000, "label": "Nạp 50.000đ"},
    "dep_100k": {"amount": 100000, "label": "Nạp 100.000đ"},
    "dep_200k": {"amount": 200000, "label": "Nạp 200.000đ"},
    "dep_500k": {"amount": 500000, "label": "Nạp 500.000đ"}
}

user_cart = {}
user_balances = {}  # Lưu số dư của khách hàng

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Các nút menu chính
    btn1 = types.InlineKeyboardButton("AIMLOCK", callback_data="cat_aimlock")
    btn2 = types.InlineKeyboardButton("AIM FILZA", callback_data="cat_aim_filza")
    btn3 = types.InlineKeyboardButton("SLOTVIP", callback_data="cat_slotvip")
    btn4 = types.InlineKeyboardButton("PROXY", callback_data="cat_proxy")
    btn5 = types.InlineKeyboardButton("MODSKIN", callback_data="cat_modskin")
    btn6 = types.InlineKeyboardButton("MENU", callback_data="cat_menu_item")
    
    btn_deposit = types.InlineKeyboardButton("💳 Nạp Tiền Vào Ví", callback_data="menu_deposit")
    btn_support = types.InlineKeyboardButton("Liên Hệ Admin", url="https://t.me/username_cua_ban")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn_deposit, btn_support)
    
    current_bal = user_balances.get(message.chat.id, 0)
    
    welcome_text = (
        "👑 **WhitzStore - Bot Bán Hàng** 👑\n"
        "--------------------------------------------------\n"
        "✅ *Nơi Cung cấp các Hack - Cheat FF*\n"
        "✅ *Sản Phẩm Uy tín - Chất Lượng - An Toàn*\n"
        "⚡ *Giao Dịch Nhanh Chóng - Tiện Lợi - 24/7*\n"
        "🛒 *Đầy Đủ Các Mặt Hàng Bạn Cần*\n"
        "--------------------------------------------------\n"
        f"💰 **Số dư ví của bạn:** `{current_bal:,}đ`\n"
        "--------------------------------------------------\n"
        "🏆 **WHITZ STORE** 🏆\n"
        "🔥 *uy tín tạo nên thương hiệu* 🔥\n\n"
        "👇 **Vui lòng chọn danh mục dịch vụ bên dưới:**"
    )
    
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

# ==================== CÁC LỆNH ADMIN ====================

@bot.message_handler(commands=['congti'])
def add_balance_to_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts = message.text.replace("/congti", "").strip().split()
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ Sai cú pháp! Dùng: `/congti ID_Khách Số_tiền`", parse_mode="Markdown")
            return
        
        target_chat_id = int(parts[0])
        amount = int(parts[1])
        
        current = user_balances.get(target_chat_id, 0)
        user_balances[target_chat_id] = current + amount
        
        bot.reply_to(message, f"✅ Đã cộng `{amount:,}đ` cho ID: `{target_chat_id}`.\nVí hiện tại của khách: `{user_balances[target_chat_id]:,}đ`", parse_mode="Markdown")
        bot.send_message(target_chat_id, f"🎉 **NẠP TIỀN THÀNH CÔNG!**\nTài khoản được cộng thêm: **{amount:,}đ**\n💰 Số dư ví: **{user_balances[target_chat_id]:,}đ**", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {str(e)}")

# ==================== XỬ LÝ GIAO DIỆN KHÁCH HÀNG ====================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    
    # 1. Hiển thị danh sách sản phẩm trong danh mục con (dạng dọc kèm nút mua từng món)
    if call.data.startswith("cat_"):
        cat_key = call.data.replace("cat_", "")
        category = shop_categories.get(cat_key)
        
        if not category:
            bot.answer_callback_query(call.id, "Danh mục không tồn tại!")
            return
            
        text = f"{category['title']}\n\n📋 **Danh sách sản phẩm chi tiết:**\n"
        for idx, item in enumerate(category['items'], 1):
            text += f"{idx}. **{item['name']}** — `{item['price']}`\n"
            
        markup = types.InlineKeyboardMarkup(row_width=1)
        # Tạo nút bấm mua cho từng mặt hàng
        for item in category['items']:
            markup.add(types.InlineKeyboardButton(f"🛒 Mua {item['name']} ({item['price']})", callback_data=f"buy_{cat_key}_{item['id']}"))
            
        markup.add(types.InlineKeyboardButton("⬅️ Quay lại Menu Chính", callback_data="back_home"))
        
        bot.edit_message_text(text, chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    # 2. Xử lý khi khách bấm nút mua một sản phẩm cụ thể
    elif call.data.startswith("buy_"):
        parts = call.data.split("_")
        if len(parts) >= 3:
            cat_key = parts[1]
            item_id = "_".join(parts[2:])
            
            category = shop_categories.get(cat_key)
            selected_item = None
            if category:
                for itm in category['items']:
                    if itm['id'] == item_id:
                        selected_item = itm
                        break
                        
            if not selected_item:
                bot.answer_callback_query(call.id, "Sản phẩm không tồn tại!")
                return
                
            user_cart[chat_id] = {"name": selected_item['name'], "price": selected_item['price']}
            
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("❌ Hủy bỏ", callback_data=f"cat_{cat_key}"))
            
            try:
                bot.delete_message(chat_id, call.message.message_id)
                bot.send_photo(
                    chat_id, photo=selected_item['image'], 
                    caption=f"🛒 Bạn đã chọn mua: **{selected_item['name']}**\n💰 Giá: **{selected_item['price']}**\n\nVui lòng nhập **Họ tên và Số điện thoại** của bạn để hoàn tất đơn hàng:",
                    parse_mode="Markdown", reply_markup=markup
                )
            except:
                bot.edit_message_text(
                    f"🛒 Bạn đã chọn mua: **{selected_item['name']}** (Giá: **{selected_item['price']}**)\n\nVui lòng nhập **Họ tên và Số điện thoại** của bạn:",
                    chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup
                )
            bot.register_next_step_handler_by_chat_id(chat_id, process_order)

    # 3. Giao diện nạp tiền
    elif call.data == "menu_deposit":
        markup = types.InlineKeyboardMarkup(row_width=2)
        for key, dep in deposit_packages.items():
            markup.add(types.InlineKeyboardButton(dep['label'], callback_data=f"dep_{key}"))
        markup.add(types.InlineKeyboardButton("⬅️ Quay lại Menu Chính", callback_data="back_home"))
        
        bot.edit_message_text(
            "💳 **CHỌN MỨC GIÁ NẠP TIỀN:**\nVui lòng chọn số tiền bạn muốn nạp vào ví:",
            chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup
        )

    elif call.data.startswith("dep_dep_"):
        pkg_key = call.data.replace("dep_", "")
        dep_info = deposit_packages.get(pkg_key)
        if not dep_info:
            return
            
        amount = dep_info['amount']
        user_cart[chat_id] = {"type": "deposit", "amount": amount}
        
        add_info = f"NAP {chat_id}"
        qr_url = f"https://img.vietqr.io/image/{BANK_ID}-{ACCOUNT_NO}-compact2.png?amount={amount}&addInfo={add_info}&accountName={ACCOUNT_NAME}"
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ Đã Chuyển Khoản Xong", callback_data="confirm_deposit"))
        markup.add(types.InlineKeyboardButton("⬅️ Chọn lại mệnh giá", callback_data="menu_deposit"))
        
        caption_text = (
            "🏦 **MÃ QR QUÉT NHANH CHUYỂN KHOẢN**\n"
            "--------------------------------------------------\n"
            f"🔹 Ngân hàng: **MB Bank**\n"
            f"🔹 Số tài khoản: `{ACCOUNT_NO}`\n"
            f"🔹 Chủ tài khoản: **{ACCOUNT_NAME}**\n"
            f"🔹 Số tiền: **{amount:,}đ**\n"
            f"🔹 Nội dung chuyển: `{add_info}`\n"
            "--------------------------------------------------\n"
            "💡 *Mở app ngân hàng quét mã QR bên trên để tự động điền thông tin và số tiền chính xác!*"
        )
        
        try:
            bot.delete_message(chat_id, call.message.message_id)
            bot.send_photo(chat_id, photo=qr_url, caption=caption_text, parse_mode="Markdown", reply_markup=markup)
        except Exception as e:
            bot.send_message(chat_id, caption_text, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "confirm_deposit":
        dep_data = user_cart.get(chat_id)
        if not dep_data or dep_data.get("type") != "deposit":
            bot.answer_callback_query(call.id, "Phiên giao dịch hết hạn!", show_alert=True)
            return
            
        amount = dep_data["amount"]
        
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
            
        bot.send_message(
            chat_id,
            "⏳ **ĐÃ GỬI YÊU CẦU XÁC NHẬN!**\n"
            "Hệ thống đã gửi thông tin chuyển khoản của bạn đến Admin. Số dư sẽ được cộng vào tài khoản ngay khi Admin kiểm tra xong.",
            parse_mode="Markdown"
        )
        
        admin_notification = (
            f"🔔 **CÓ YÊU CẦU NẠP TIỀN MỚI!**\n\n"
            f"👤 Khách: {call.from_user.first_name} (@{call.from_user.username or 'Không có'})\n"
            f"🆔 ID Khách: `{chat_id}`\n"
            f"💰 Số tiền yêu cầu nạp: **{amount:,}đ**\n\n"
            f"👉 *Lệnh cộng tiền nhanh:*\n"
            f"`/congti {chat_id} {amount}`"
        )
        bot.send_message(ADMIN_ID, admin_notification, parse_mode="Markdown")

    elif call.data == "back_home":
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
        send_welcome(call.message)

def process_order(message):
    chat_id = message.chat.id
    customer_info = message.text
    product_info = user_cart.get(chat_id)
    
    if not product_info or "name" not in product_info:
        return
        
    product_name = product_info["name"]
    
    bot.send_message(chat_id, "✅ **Đặt hàng thành công!** Đơn hàng đã được gửi về hệ thống.")
    
    admin_text = (
        f"🚨 **CÓ ĐƠN HÀNG MỚI!**\n\n"
        f"🛍️ Sản phẩm: **{product_name}**\n"
        f"👤 Khách hàng: {message.from_user.first_name} (ID: `{chat_id}`)\n"
        f"📝 Thông tin liên hệ: {customer_info}"
    )
    bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")

print("Bot bán hàng đang chạy...")
bot.infinity_polling()
