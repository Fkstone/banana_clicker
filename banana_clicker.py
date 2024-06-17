import pyautogui
import time
import keyboard
import pygetwindow as gw

# 目标窗口标题
target_title = "Banana"

# 获取所有窗口
all_windows = gw.getAllWindows()

# 查找匹配的窗口
window = None
for win in all_windows:
    if win.title == target_title:
        window = win
        break

if window is None:
    print(f"没有找到名为 {target_title} 的窗口")
    print("按下 'Esc' 键退出程序")
    keyboard.wait('esc')  # 等待用户按下 'Esc' 键
    exit()
else:
    # 激活窗口
    window.activate()
    time.sleep(0.5)  # 等待窗口激活

    # 获取窗口的左上角坐标和宽高
    window_left = window.left
    window_top = window.top
    window_width = window.width
    window_height = window.height
    
    # 计算窗口中心位置
    center_x = window_left + window_width // 2
    center_y = window_top + window_height // 2

# 保持鼠标在窗口中心并点击
pyautogui.FAILSAFE = False  # 关闭FailSafe功能，防止鼠标移动到屏幕角落时抛出异常
print("按下 'Esc' 键以停止程序")

# 全局变量用于控制主循环
running = True

# 停止程序的函数
def stop_program():
    global running
    running = False
    print("检测到 'Esc' 键，程序停止")

# 添加热键监听
keyboard.add_hotkey('esc', stop_program)

try:
    while running:
        # 移动鼠标到窗口中心
        pyautogui.moveTo(center_x, center_y)
        # 每秒点击20次
        for _ in range(20):
            if not running:
                break
            pyautogui.click()
            time.sleep(0.05)  # 0.05秒的间隔使得每秒20次点击

except KeyboardInterrupt:
    print("程序已停止")
finally:
    # 移除 'Esc' 热键
    keyboard.remove_hotkey('esc')