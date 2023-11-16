# ---encoding:utf-8---
# @Time    : 2023/7/18 00:13
# @Author  : caishengxiang
# @Email   : 383301857@qq.com
# @File    : gpt.py
# @Project : caishengxiang
# 导入revChatGPT.V1中的Chatbot类
# ppython -m pip install --upgrade revChatGPT
import json
from revChatGPT.V1 import Chatbot

# 创建Chatbot实例并传入config参数，包括登录OpenAI的账户信息
# json.load(open('./gpt.json')
chatbot = Chatbot(config={"email": "yickho13@gmail.com",
    "password": "Heyi198401"})
# 定义问题
question = """使用达芬奇16做专场视频剪辑
"""

# 输出问题
print(question)

# 输出ChatGPT的回答
print("ChatGPTBot: ")

# 定义prev_text变量，用于保存上一次对话的文本内容
prev_text = ""

# 通过ask方法向ChatGPT发送问题并获取回答
for data in chatbot.ask(question):
    # 从回答数据中提取ChatGPT的回答，并去除前面已经输出过的文本部分
    message = data["message"][len(prev_text):]

    # 输出ChatGPT的回答
    print(message, end="", flush=True)

    # 更新prev_text变量
    prev_text = data["message"]

# 输出空行，以便下一轮对话
print()
