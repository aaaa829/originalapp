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


# def delete():
# 動かした図形が同色の図形と接触した場合消滅する関数


def main():
    global canvas1
    w = 1280
    h = 640
    root = tk.Tk()

    # キャンバス作成
    canvas1 = tk.Canvas(root, width=w, height=h, highlightthickness=0, bg="white")

    canvas1.grid(row=0, column=0)

    # 色を用意
    colors = ("red", "green", "yellow", "blue", "purple", "pink", "orange")

    # 色の数だけ適当に位置をずらしながら長方形（正方形）を描画
    for i, color in enumerate(colors):
        print(i)
        rect = canvas1.create_rectangle(i * 60 + 20, 20, i * 60 + 70, 70, fill=color)
        rect2 = canvas1.create_rectangle(i * 60 + 20, 570, i * 60 + 70, 510, fill=color)

        canvas1.tag_bind(rect, "<ButtonPress-1>", click)
        canvas1.tag_bind(rect, "<Button1-Motion>", drag)

    root.mainloop()


import random
import numpy as np

if __name__ == "__main__":
    main()
    # img = np.zeros((400, 600, 3), np.uint8)
    # for i in range(10):  # 以下のインデント行を10回繰り返す
    #     x = int(random.uniform(10, 590))  # 10以上590以下の乱数(浮動小数点型)を発生し、intで整数に変換、xとする
    #     y = int(random.uniform(10, 390))  # 10以上390以下の乱数(浮動小数点型)を発生し、intで整数に変換、yとする
    #     cv2.circle(img, (x, y), 10, (255, 255, 0), -1)  # 中心がx,y半径が10の水色の塗りつぶした円を描画

    # cv2.imshow("random_circle", img)  # 別ウィンドウを開き(ウィンドウ名 "random_circle")オブジェクトimgを表示
    # cv2.imwrite("random_circle.png", img)  # 画像をファイル名random_circle.pngで保存

    # cv2.waitKey(0)  # キー入力待ち
    # cv2.destroyAllWindows()  # ウインドウを閉じる
