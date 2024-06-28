from nonebot import on_keyword, on_message
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import google.generativeai as genai
genai.configure(api_key="AIzaSyCzTgoCUzbJ60sVEYCgDG1QlUaKxCov-vg")

model = genai.GenerativeModel('gemini-1.5-pro')
chatnew = model.start_chat(history=[])


chat = on_message(rule=to_me(), priority=5)
@chat.handle()
async def chat_handle(bot: Bot, event: Event, state: T_State):
    msg = str(event.message)
    try:
        response1 = chatnew.send_message(msg)
        response = response1.text
    except Exception as e:
        response = "抱歉，我无法回答这个问题。"
        print(f"Error in send_message: {e}")
    msg_list =[]
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "1",
                "uin": event.self_id,
                "content": response
                }
            }
        )
    await bot.send_group_forward_msg(group_id = event.group_id, messages = msg_list)