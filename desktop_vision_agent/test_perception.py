from perception.screenshot import capture_screen, save_screenshot
from perception.vlm_client import analyze_screen

print("📸 正在截图...")
img = capture_screen()
save_screenshot(img, "test_perception")
print("✅ 截图完成，已保存到 logs/screenshots/test_perception.png")

print("\n🤖 正在调用 Gemini-2.5 分析屏幕...")
instruction = "帮我了解当前屏幕上有什么"
result = analyze_screen(img, instruction)

print("\n" + "="*50)
print("Gemini-2.5 分析结果：")
print("="*50)
print(result)