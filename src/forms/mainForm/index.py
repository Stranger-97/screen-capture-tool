# -*- coding: utf-8 -*-
from .MainForm import Ui_MainForm
from ..screenCapForm.index import screenCapForm
from PyQt5.QtWidgets import QWidget, QSystemTrayIcon, QMenu, QAction, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtCore
import time
import cv2
import os


class mainForm(QWidget, Ui_MainForm):

    def __init__(self):
        super(mainForm, self).__init__()
        self.setupUi(self)

        # 隐藏任务栏显示，窗口置顶
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)

        # 固定大小
        self.setFixedSize(self.width(), self.height())

        # 设置系统托盘
        self.tp = QSystemTrayIcon(self)
        self.tp.setIcon(QIcon('./res/imgs/icon.jpg'))  # 托盘图标
        self.tp.setToolTip('截图工具')  # 提示语
        self.tp.activated.connect(self.tpActivated)  # 激活时调用函数
        # 操作actions
        self.action_always_top = QAction('始终置顶', self, triggered=self.setAlwaysTop, checkable=True)
        self.action_always_top.setChecked(True)
        self.action_quit = QAction('退出', self, triggered = self.quit)
        # 目录
        self.tpMenu = QMenu()
        # 绑定actions
        self.tpMenu.addAction(self.action_quit)
        # 设置目录
        self.tp.setContextMenu(self.tpMenu)
        self.tp.show()

        self.scene = None
        # 子窗口
        self.screenCapForm = None

        # 禁用滚动条
        self.gv_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gv_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def tpActivated(self, reason):
        if (reason == QSystemTrayIcon.DoubleClick):
            # TODO: 双击截图操作
            self.hide()
            time.sleep(0.2)
            self.screenCapForm = screenCapForm(self)
            self.screenCapForm.showFullScreen()


    def setAlwaysTop(self):
        self.action_always_top.setChecked(not self.action_always_top.isChecked())

    def quit(self):
        self.tp.hide()
        exit(0)

    # 关闭时隐藏托盘
    def closeEvent(self, QCloseEvent):
        self.tp.hide()

    # 设置大小
    def setSize(self, width, height):
        self.setFixedSize(width, height)
        self.gv_display.setFixedSize(width, height)