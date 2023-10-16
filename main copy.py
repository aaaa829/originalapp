import cv2
import tkinter as tk


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

    if canvas1.coords(rect["red"]) == canvas1.coords(rect2["red"]):
        canvas1.delete(rect["red"], rect2["red"])

    if canvas1.coords(rect["green"]) == canvas1.coords(rect2["green"]):
        canvas1.delete(rect["green"], rect2["green"])

    if canvas1.coords(rect["yellow"]) == canvas1.coords(rect2["yellow"]):
        canvas1.delete(rect["yellow"], rect2["yellow"])

    if canvas1.coords(rect["blue"]) == canvas1.coords(rect2["blue"]):
        canvas1.delete(rect["blue"], rect2["blue"])

    if canvas1.coords(rect["pink"]) == canvas1.coords(rect2["pink"]):
        canvas1.delete(rect["pink"], rect2["pink"])

    if canvas1.coords(rect["purple"]) == canvas1.coords(rect2["purple"]):
        canvas1.delete(rect["purple"], rect2["purple"])

    if canvas1.coords(rect["orange"]) == canvas1.coords(rect2["orange"]):
        canvas1.delete(rect["orange"], rect2["orange"])


def main():
    global canvas1
    w = 1280
    h = 640
    root = tk.Tk()

    # キャンバス作成
    canvas1 = tk.Canvas(root, width=w, height=h, highlightthickness=0, bg="white")

    canvas1.grid(row=0, column=0)

    # 色を用意
    global colors
    colors = ("red", "green", "yellow", "blue", "purple", "pink", "orange")

    global rect
    global rect2
    rect = {}
    rect2 = {}
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
    main()
