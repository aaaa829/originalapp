import time


# stateの値をカラーコードに変換
def make_colorCode(state, inf, diff):
    red = diff * state[0] + inf
    green = diff * state[1] + inf
    blue = diff * state[2] + inf
    red = int(red)
    green = int(green)
    blue = int(blue)
    return f"\033[38;2;{red};{green};{blue}m", f"{red:02x}{green:02x}{blue:02x}"


# 色と順番の設定（上から順に表示される。最初と最後が一周する。）
state = [
    [1, 0, 0],  # 赤
    [1, 1, 0],  # 黄
    [0, 1, 0],  # 緑
    [0, 1, 1],  # 青緑
    [0, 0, 1],  # 青
    [1, 0, 1],
]  # 紫


state += state[0::-1]
sup = (1 << 8) - 1  # RGBの上限
inf = 50  # RGBの下限
diff = sup - inf
state_map = []
split_num = 50


# stateの値をsplit_numに応じて細かく分ける
for i in range(len(state) - 1):
    red_diff = (state[i + 1][0] - state[i][0]) / split_num
    green_diff = (state[i + 1][1] - state[i][1]) / split_num
    blue_diff = (state[i + 1][2] - state[i][2]) / split_num
    lst = [
        [
            red_diff * j + state[i][0],
            green_diff * j + state[i][1],
            blue_diff * j + state[i][2],
        ]
        for j in range(split_num)
    ]
    state_map += lst
state_map += state[0::-1]


state_length = len(state_map)
index = 0
print("\n\n")

# ゲーミングprint開始
while 1:
    try:
        color_code, to_hex = make_colorCode(state_map[index], inf, diff)
        print(f"\033[2A{color_code}!! rainbow !!\t( #{to_hex} )\033[0m\n")
        index = (index + 1) % state_length
        time.sleep(0.02)

    except KeyboardInterrupt:  # ctrl + C
        print(" exit")
        break
