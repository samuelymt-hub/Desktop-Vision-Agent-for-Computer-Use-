import os
import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types
from perception.screenshot import image_to_base64
import base64

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """你是一个桌面操作助手，负责分析屏幕截图。
请用以下格式回答：

【当前界面】
简要描述当前屏幕显示的是什么程序/页面

【可交互元素】
列出所有可点击的按钮、输入框、菜单等，格式：
- 元素名称：大致位置（左上/中间/右上等）

【建议操作】
根据用户指令，下一步应该做什么
"""

def analyze_screen(img: np.ndarray, instruction: str) -> str:
    """
    将截图发给 Gemini 2.5 Flash，返回界面分析结果
    img: 屏幕截图（numpy 数组）
    instruction: 用户指令
    """
    img_base64 = image_to_base64(img)
    img_bytes = base64.b64decode(img_base64)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
            types.Part.from_text(text=f"{SYSTEM_PROMPT}\n\n用户指令：{instruction}\n请分析当前屏幕。")
        ]
    )

    return response.text