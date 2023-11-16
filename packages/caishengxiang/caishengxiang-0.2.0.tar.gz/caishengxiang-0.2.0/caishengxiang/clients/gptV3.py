# ---encoding:utf-8---
# @Time    : 2023/7/18 00:31
# @Author  : caishengxiang
# @Email   : 383301857@qq.com
# @File    : gptV3.py
# @Project : caishengxiang
api_key = "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"

from revChatGPT.V3 import Chatbot

chatbot = Chatbot(api_key=api_key)
for data in chatbot.ask_stream("如何使用达芬奇17做专场视频剪辑？"):
    print(data, end="", flush=True)
