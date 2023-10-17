import tkinter as tk
from pygame.locals import *
import pygame

rect = {}
rect2 = {}


def click(event):
    global figure
    global before_x, before_y

    x = event.x
    y = event.y

    # クリックされた位置に一番近い図形のID取得
    figure = canvas1.find_closest(x, y)

    # マウスの座標を記憶
    before_x = x
    before_y = y


def drag(event):
    global before_x, before_y
    x = event.x
    y = event.y

    # 前回からのマウスの移動量の分だけ図形も移動
    canvas1.move(figure, x - before_x, y - before_y)
    # マウスの座標を記憶
    before_x = x
    before_y = y

    # 座標の中心 canvas1.coords(figure)
    # 座標の左上隅、右下隅　canvas1.bbox(figure)
    # canvas1.coords(figure)[0] <= x <= canvas1.coords(figure)[2]
    # and canvas1.coords(figure)[1] <= y <= canvas1.coords(figure)[3]
    for i in colors:
        if canvas1.coords(rect[i]) == canvas1.coords(rect2[i]):
            canvas1.delete(rect[i], rect2[i])
            del rect[i]
            se.play()
            if len(rect) == 0:
                quit()


def quit():
    root.quit()
    root.destroy()


def main():
    global root
    global canvas1
    w = 1280
    h = 640
    root = tk.Tk()

    # キャンバス作成
    canvas1 = tk.Canvas(root, width=w, height=h, highlightthickness=0, bg="white")

    canvas1.grid(row=0, column=0)

    # 色を用意
    global colors
    colors = (
        "red",
        "green",
        "yellow",
        "blue",
        "purple",
        "pink",
        "orange",
        "black",
        "skyblue",
    )

    global rect
    global rect2
    # 色の数だけ適当に位置をずらしながら長方形（正方形）を描画
    for i, color in enumerate(colors):
        rect[color] = canvas1.create_rectangle(
            i * 60 + 20, 20, i * 60 + 70, 70, fill=color
        )
        rect2[color] = canvas1.create_rectangle(
            (w - (i * 60 + 20)), h - 20, (w - (i * 60 + 70)), h - 70, fill=color
        )
        canvas1.tag_bind(rect[color], "<ButtonPress-1>", click)
        canvas1.tag_bind(rect[color], "<Button1-Motion>", drag)

    root.mainloop()


if __name__ == "__main__":
    pygame.init()
    se = pygame.mixer.Sound("originalapp/img/expl.mp3")
    main()
