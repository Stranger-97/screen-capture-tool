# -*- coding:utf-8 -*-
from .ScreenCapForm import Ui_screenCapForm
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt5.Qt import QPoint
import time
import cv2


class screenCapForm(QWidget, Ui_screenCapForm):
    def __init__(self, father):
        super(screenCapForm, self).__init__()
        self.setupUi(self)

        # 设置格式
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint)
        # 改变窗口大小
        self.screenRect = QApplication.desktop().screenGeometry()
        self.setFixedSize(self.screenRect.width(), self.screenRect.height())
        self.gv_fullscreen.setFixedSize(self.screenRect.width(), self.screenRect.height())
        self.l_rec.setFixedSize(self.screenRect.width(), self.screenRect.height())

        # 禁用滚动条
        self.gv_fullscreen.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gv_fullscreen.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # 获取桌面截图
        self.screenPixmap = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        self.scene = QGraphicsScene()
        self.scene.addItem(QGraphicsPixmapItem(self.screenPixmap))
        self.gv_fullscreen.setScene(self.scene)

        # 是否截图状态，选取过程中为pending，结束时或者截图前为done
        self.status = 'done'
        self.father = father
        # 画板，画笔
        self.board = QPixmap(self.screenRect.width(), self.screenRect.height())
        self.board.fill(QtCore.Qt.transparent)
        self.painter = QPainter()
        self.from_point = [0, 0]
        self.to_point = [0, 0]
        self.l_rec.setPixmap(self.board)

    def keyPressEvent(self, QKeyEvent):
        if (QKeyEvent.key() == QtCore.Qt.Key_Escape):
            self.close()

    def paintEvent(self, QPaintEvent):
        if (self.status == 'pending'):
            self.painter.begin(self)
            self.drawRec()
            self.l_rec.setPixmap(self.board)
            self.painter.end()

    def closeEvent(self, QCloseEvent):
        self.father.show()

    def mousePressEvent(self, QMouseEvent):
        self.status = 'pending'
        self.from_point = [QMouseEvent.pos().x(), QMouseEvent.pos().y()]

    def mouseMoveEvent(self, QMouseEvent):
        if (self.status == 'pending'):
            self.to_point = [QMouseEvent.pos().x(), QMouseEvent.pos().y()]
            self.update()
            time.sleep(0.1)

    def mouseReleaseEvent(self, QMouseEvent):
        self.status = 'done'
        self.setParentImg()
        self.close()

    def drawRec(self):
        # 填充为透明
        # self.board.fill(QtCore.Qt.red)
        # 设置画笔
        self.painter.setPen(QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
        # 绘制矩形
        self.painter.drawRect(self.from_point[0], self.from_point[1], self.to_point[0] - self.from_point[0],
                              self.to_point[1] - self.from_point[1])

    def setParentImg(self):
        qimg = self.screenPixmap.toImage()
        cut_qimg = qimg.copy(self.from_point[0], self.from_point[1], self.to_point[0] - self.from_point[0],
                             self.to_point[1] - self.from_point[1])
        cut_pixmap = QPixmap.fromImage(cut_qimg)
        self.father.scene = QGraphicsScene()
        self.father.scene.addItem(QGraphicsPixmapItem(cut_pixmap))
        self.father.gv_display.setScene(self.father.scene)
        self.father.setSize(self.to_point[0] - self.from_point[0], self.to_point[1] - self.from_point[1])
