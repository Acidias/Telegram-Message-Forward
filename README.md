# Telegram-Message-Forward

This Python script is connecting to your account with few details. 

It's not complated yet, but after giving the necessary information the script checking all notification. And if the sender is in = to your given senders ID, the script forwards the message to you.

Soon, I'll Update so you can just change every variable in the beginning of the code.


You can get the senders information with this code:

    sender = await event.get_sender()
    print("-------------------------------------------------------  Senders ID: ------------------------------------------------")
    print(sender.id)
    
    print("------------------------------------------------------  Senders Name: -----------------------------------------------")
    print(sender.username)

    print("----------------------------------------------------Detailed Information: --------------------------------------------")
    print(sender)
    

Detailed Information structure:
User(id=Int, is_self=False, contact=False, mutual_contact=False, deleted=False, bot=True, bot_chat_history=False, bot_nochats=False, verified=False, restricted=False, min=True, bot_inline_geo=False, support=False, scam=False, apply_min_photo=True, fake=False, bot_attach_menu=False, premium=False, attach_menu_enabled=False, access_hash=INT, first_name='String', last_name=None, username='STRING', phone=None, photo=, dc_id=4, has_video=False, stripped_thumb=b''), status=None, bot_info_version=1, restriction_reason=[], bot_inline_placeholder=None, lang_code=None, emoji_status=None, usernames=[])
