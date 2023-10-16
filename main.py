import cv2
import tkinter as tk
import random as rand

Xx = 720
Yy = 480


def click(event):
    global figure
    global before_x, before_y

    x = event.x
    y = event.y

    # クリックされた位置に一番近い図形のID取得
    figure = canvas.find_closest(x, y)

    # マウスの座標を記憶
    before_x = x
    before_y = y


def drag(event):
    global before_x, before_y

    x = event.x
    y = event.y

    # 前回からのマウスの移動量の分だけ図形も移動
    canvas.move(figure, x - before_x, y - before_y)
    # マウスの座標を記憶
    before_x = x
    before_y = y


def main():
    global canvas

    app = tk.Tk()
    app.geometry(f"{Xx}x{Yy}")

    # キャンバス作成
    canvas = tk.Canvas(app, width=Xx, height=Yy, highlightthickness=0, bg="white")

    canvas.grid(row=0, column=0)

    # 色を用意
    numlist = rand.sample((range(1, 14)), k=10)
    print(numlist)
    print(type(numlist))
    print(len(numlist))
    imglist = []
    for n in range(len(numlist)):
        i = f"originalapp/img/{numlist[n]}.png"
        img = tk.PhotoImage(file=f"originalapp/img/{numlist[n]}.png").subsample(5)
        imglist.append(img)
    print(imglist)

    for n in range(len(imglist)):
        rect = tk.Label(canvas, image=imglist[n])
        rect.grid(row=0, column=f"{n}")

    app.mainloop()


if __name__ == "__main__":
    main()
