import win32api
import win32con
import win32gui
import time
from pathlib import Path
import random


def Windows_img(paperPath):
    # 读取注册表
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 在注册表中写入属性值
    win32api.RegSetValueEx(k, "wapaperStyle", 0, win32con.REG_SZ, "0")  # 0 代表桌面居中 2 代表拉伸桌面
    win32api.RegSetValueEx(k, "Tilewallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, paperPath, win32con.SPIF_SENDWININICHANGE)


def changeWallpaper():
    time_ = int(60)
    path = 'D:\桌面\python\wallpaper_change\壁纸更换库'
    # D:\桌面\python\wallpaper_change\wallpaper
    p = Path(r'{}'.format(path))
    imgs = list(p.glob('**/*.jpg'))
    wall_papers = []
    for img in imgs:
        wall_papers.append(str(img))
    # 随机打乱顺序
    random.shuffle(wall_papers)
    # print(wall_papers)
    num = 0
    while True:
        Windows_img(wall_papers[num])
        time.sleep(time_)  # 设置壁纸更换间隔，这里为3秒，根据用户自身需要自己设置秒数
        num += 1
        if num == len(wall_papers):  # 如果到了最后一张图片，则重新回到第一张
            num = 0


if __name__ == '__main__':
    changeWallpaper()
