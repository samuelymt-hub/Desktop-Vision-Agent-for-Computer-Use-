import mss
import cv2
import pyautogui
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

with mss.mss() as sct:
    screenshot = sct.grab(sct.monitors[1])
    img = np.array(screenshot)
    cv2.imwrite("test_screenshot.png", img)
    print("✅ 截图成功，已保存为 test_screenshot.png")

size = pyautogui.size()
print(f"✅ 屏幕分辨率：{size.width} x {size.height}")

api_key = os.getenv("OPENAI_API_KEY")
print(f"✅ API Key 已读取：{api_key[:8]}..." if api_key else "❌ 未找到 API Key，请检查 .env 文件")