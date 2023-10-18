import cv2
from PyQt5 import QtWidgets
import threading
import Config as con
import screencapture as sc


class CaptureApp(QtWidgets.QWidget):
    def __init__(self):
        super(CaptureApp, self).__init__()
        self.con = con.Config()

        # layout
        self.hbox_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.hbox_layout)

        # widgetの配置
        self.createWidget()

    def closeEvent(self, event):
        if self.con.start_flag == 1:
            self.con.stop_flag = 1
            self.record_thread.join()

    def createWidget(self):
        # button
        self.start_button = QtWidgets.QPushButton("start")
        self.stop_button = QtWidgets.QPushButton("stop")
        self.label = QtWidgets.QLabel("please start")
        self.hbox_layout.addWidget(self.start_button)
        self.hbox_layout.addWidget(self.stop_button)
        self.hbox_layout.addWidget(self.label)

        # function
        self.start_button.clicked.connect(self.recordStart)
        self.stop_button.clicked.connect(self.recordStop)

    def updateLabel(self):
        if self.con.stop_flag == 0:
            self.label.setText("rec now")
        elif self.con.stop_flag == 1:
            self.label.setText("please start")

    def recordStart(self):
        self.con.start_flag = 1
        self.record_thread = threading.Thread(
            target=sc.record_control, args=(self.con,)
        )
        self.record_thread.start()

        # label表示名の更新
        self.updateLabel()

    def recordStop(self):
        # start flagが1の場合
        if self.con.start_flag == 1:
            # stop flagを1にする
            self.con.stop_flag = 1
            # thread処理解除
            self.record_thread.join()
            # 画面録画を保存
            self.recordSave()
            # label表示名の更新
            self.updateLabel()

            # stop flagを0にする
            self.con.stop_flag = 0
            # start flagを0にする
            self.con.start_flag = 0
        else:
            print("please rec start")

    def recordSave(self):
        self.save_path = QtWidgets.QFileDialog.getSaveFileName(
            self, "save file", filter="*.mp4"
        )[0]

        if self.save_path == "":
            return
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        video = cv2.VideoWriter(
            self.save_path, fourcc, self.con.fps, (self.con.w, self.con.h)
        )
        for img in self.con.img_list:
            video.write(img)
        video.release()
