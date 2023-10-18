import pyautogui as pg
import numpy as np
import CaptureApp as ca


class Config:
    def __init__(self):
        # パラメーター管理
        self.start_flag = 0
        self.stop_flag = 0
        self.fps = 15
        self.m_time = 10  # s
        self.h, self.w = np.array(pg.screenshot()).shape[:2]
        self.img_list = []
