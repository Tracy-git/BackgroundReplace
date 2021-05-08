from pymatting import cutout
import inference
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from test import Gradient_color
import os

desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\'

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def mian(file_path):
    inference.main(file_path)
    try:
        cutout(
            file_path,
            "trimap.png",
            "test.png")
        print('='*40 + '>Successfully!')
        os.remove('trimap.png')
        os.remove('pha.png')
    except:
        print('Erro')
if __name__ == '__main__':
    mian(file_path)
    img = Image.open('test.png')
    w,h = img.size
    a = int(input('选择背景颜色数字(1:红;2:蓝;3:白;4:深蓝;5:深蓝渐变；6:灰渐变)：'))
    r,g,b = (0,0,0)
    if a == 1:
        r,g,b = (211,25,26)
    elif a == 2:
        r,g,b = (75,151,226)
    elif a == 3:
        r, g, b = (255, 255, 255)
    elif a == 4:
        r, g, b = (46, 85, 124)
    elif a == 5:
        bg_1 = (46, 85, 124)
        bg_2 = (70, 141, 212)
        size = (w,h)
        bg1 = Gradient_color(bg_1,bg_2,size)
        bg1.paste(img, (0, 0), mask=img.split()[3])
        bg1.save(desk+'//results.png')
    elif a == 6:
        bg_1 = (56, 60, 64)
        bg_2 = (144, 153, 158)
        size = (w,h)
        bg1 = Gradient_color(bg_1,bg_2,size)
        bg1.paste(img, (0, 0), mask=img.split()[3])
        bg1.save(desk+'//results.png')
    if a in range(1,5):
        bg = Image.new("RGB", (w,h), (r,g,b))
        bg.paste(img,(0,0),mask=img.split()[3])
        bg.save(desk+'//results.png')

    print('完成，文件保存在桌面')
    os.remove('test.png')








