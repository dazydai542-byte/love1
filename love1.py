import tkinter as tk
import random

# === 可调参数 ===
NUM_WINDOWS   = 300        # 一共弹出多少个小窗口
INTERVAL_MS   = 40      # 每隔多少毫秒弹出一个
LIFETIME_MS   = 0    # 每个窗口显示多久后自动关闭（毫秒）；设为 0 则不自动关闭
WINDOW_W      = 260      # 窗口宽度
WINDOW_H      = 70       # 窗口高度
TOPMOST       = True     # 是否总在最前

TIPS = [
    '我想你了','今天过得开心嘛','期待和你见面','顺顺利利','平平安安','早点休息',
    '天冷了，多穿衣服','今天有想我嘛','我喜欢你','要想我哦','今天也辛苦啦',
    '吃饭了嘛','每天都要喜欢我哦', '想你想你想你','开心每一天', '宝贝','想和你在一起','想抱抱你','想亲亲你',
    '你是我的小苹果','遇见你真好','你是最棒的','爱你哟','想你了，快回来','想听你的声音','想见你',
    '想念你的笑容','你是我的唯一','每天都在想你','我们去河边散步好不好','你是我的全世界','想和你手牵手',
    '你世界第一好','想和你一起看星星','你好可爱','想和你一起旅行','好幸运遇见你','想和你一起吃饭','想和你一起看电影',
    '想和你一起做饭','想和你一起睡觉','想和你一起逛街','想和你一起运动','想和你一起学习','想和你一起打游戏',
    '想和你一起听音乐','想和你一起看书','想和你一起做手工','想和你一起养一只小狗','I love you', 'I miss you'
]
BG_COLORS = [
    'pink','skyblue','green','lavender','lightyellow','plum',
    'coral','bisque','lavenderblush','oldlace'
]

def create_tip(root):
    """创建一个随机位置的提示小窗（使用 Toplevel，不再重复创建 Tk）。"""
    # 用屏幕尺寸计算随机位置
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    x = random.randrange(0, max(1, screen_w - WINDOW_W))
    y = random.randrange(0, max(1, screen_h - WINDOW_H))

    tip = random.choice(TIPS)
    bg  = random.choice(BG_COLORS)

    win = tk.Toplevel(root)
    win.title("宝宝")
    win.geometry(f"{WINDOW_W}x{WINDOW_H}+{x}+{y}")
    if TOPMOST:
        win.attributes('-topmost', True)

    # 纯展示：如果你想无边框更可爱，可以打开下一行（可选）
    # win.overrideredirect(True)

    # 字体在不同系统可能稍有差异，若微软雅黑不存在会自动回退
    label = tk.Label(
        win, text=tip, bg=bg,
        font=('微软雅黑', 16),
        width=30, height=3
    )
    label.pack(fill='both', expand=True)

    # 设定自动关闭
    if LIFETIME_MS > 0:
        win.after(LIFETIME_MS, win.destroy)

def schedule_many(root, n=NUM_WINDOWS, interval=INTERVAL_MS):
    """按固定间隔调度创建多个提示窗。"""
    for i in range(n):
        root.after(i * interval, lambda: create_tip(root))

def main():
    # 只创建一个 Tk 根窗口，并把它隐藏；后续窗口都用 Toplevel
    root = tk.Tk()
    root.withdraw()

    # 调度多个提示弹窗
    schedule_many(root)

    #如果你想无限循环每隔一段时间弹出一个，可以用下面这段替换上面的调度：
    #def loop():
         #create_tip(root)
         #root.after(2000, loop)   # 每 2 秒再来一个
    #loop()

    root.mainloop()

if __name__ == "__main__":
    main()
    
