import mss
import numpy as np
import cv2
import base64
from pathlib import Path

SCREENSHOT_DIR = Path("logs/screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

def capture_screen() -> np.ndarray:
    """截取屏幕，返回 numpy 数组"""
    with mss.MSS() as sct:
        monitor = sct.monitors[1]  # 主显示器
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

def save_screenshot(img: np.ndarray, name: str = "screen") -> Path:
    """保存截图到 logs/screenshots/"""
    path = SCREENSHOT_DIR / f"{name}.png"
    cv2.imwrite(str(path), img)
    return path

def image_to_base64(img: np.ndarray) -> str:
    """将图像转为 base64 字符串，用于传给 API"""
    # 压缩到 1280 宽，节省 token
    h, w = img.shape[:2]
    if w > 1280:
        scale = 1280 / w
        img = cv2.resize(img, (1280, int(h * scale)))
    
    _, buffer = cv2.imencode(".png", img)
    return base64.b64encode(buffer).decode("utf-8")