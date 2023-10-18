import cv2
import pyautogui as pg
import numpy as np
import time
import Config as con


class RecordThread:
    def __init__(self, con):
        super().__init__()
        self.con = con

    def loop(self):
        self.con.img_list = []
        while self.con.stop_flag != 1:
            time.sleep(0.01)
            img = pg.screenshot()
            img = np.array(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            self.con.img_list.append(img)
