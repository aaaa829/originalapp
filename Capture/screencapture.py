import cv2
import pyautogui as pg
import numpy as np
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import threading
import time
import Config as con
import CaptureApp as ca
import RecordThread as rt


def record_control(con):
    rec = rt.RecordThread(con)
    rec.loop()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = ca.CaptureApp()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
