from nonebot import on_keyword, on_message
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import google.generativeai as genai
genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-pro')

chat = on_message(rule=to_me(), priority=5)
@chat.handle()
async def chat_handle(bot: Bot, event: Event, state: T_State):
    msg = str(event.message)
    response = model.generate_content(msg)

    msg_list =[]
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "1",
                "uin": event.self_id,
                "content": response.text
                }
            }
        )
    await bot.send_group_forward_msg(group_id = event.group_id, messages = msg_list)