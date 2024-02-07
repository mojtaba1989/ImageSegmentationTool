# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guide.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import cv2

class Ui_AssistApp(object):
    def setupUi(self, AssistApp, image=None, master_obj=None):
        AssistApp.setObjectName("AssistApp")
        AssistApp.resize(800, 679)
        self.centralwidget = QtWidgets.QWidget(AssistApp)
        self.centralwidget.setObjectName("centralwidget")
        self.image = image
        self.master_obj = master_obj
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(8, 4, 781, 431))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap(""))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 440, 781, 152))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.hue_min = QtWidgets.QSlider(self.widget)
        self.hue_min.setAcceptDrops(True)
        self.hue_min.setAutoFillBackground(True)
        self.hue_min.setMaximum(255)
        self.hue_min.setTracking(True)
        self.hue_min.setOrientation(QtCore.Qt.Horizontal)
        self.hue_min.setInvertedAppearance(False)
        self.hue_min.setInvertedControls(False)
        self.hue_min.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.hue_min.setTickInterval(5)
        self.hue_min.setObjectName("hue_min")
        self.gridLayout_2.addWidget(self.hue_min, 0, 1, 1, 1)
        self.hue_min_d = QtWidgets.QLabel(self.widget)
        self.hue_min_d.setObjectName("hue_min_d")
        self.gridLayout_2.addWidget(self.hue_min_d, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.hue_max = QtWidgets.QSlider(self.widget)
        self.hue_max.setAcceptDrops(True)
        self.hue_max.setAutoFillBackground(True)
        self.hue_max.setMaximum(255)
        self.hue_max.setTracking(True)
        self.hue_max.setOrientation(QtCore.Qt.Horizontal)
        self.hue_max.setInvertedAppearance(False)
        self.hue_max.setInvertedControls(False)
        self.hue_max.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.hue_max.setTickInterval(5)
        self.hue_max.setObjectName("hue_max")
        self.gridLayout_2.addWidget(self.hue_max, 1, 1, 1, 1)
        self.hue_max_d = QtWidgets.QLabel(self.widget)
        self.hue_max_d.setObjectName("hue_max_d")
        self.gridLayout_2.addWidget(self.hue_max_d, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.sat_min = QtWidgets.QSlider(self.widget)
        self.sat_min.setAcceptDrops(True)
        self.sat_min.setAutoFillBackground(True)
        self.sat_min.setMaximum(255)
        self.sat_min.setTracking(True)
        self.sat_min.setOrientation(QtCore.Qt.Horizontal)
        self.sat_min.setInvertedAppearance(False)
        self.sat_min.setInvertedControls(False)
        self.sat_min.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sat_min.setTickInterval(5)
        self.sat_min.setObjectName("sat_min")
        self.gridLayout_2.addWidget(self.sat_min, 2, 1, 1, 1)
        self.sat_min_d = QtWidgets.QLabel(self.widget)
        self.sat_min_d.setObjectName("sat_min_d")
        self.gridLayout_2.addWidget(self.sat_min_d, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.sat_max = QtWidgets.QSlider(self.widget)
        self.sat_max.setAcceptDrops(True)
        self.sat_max.setAutoFillBackground(True)
        self.sat_max.setMaximum(255)
        self.sat_max.setTracking(True)
        self.sat_max.setOrientation(QtCore.Qt.Horizontal)
        self.sat_max.setInvertedAppearance(False)
        self.sat_max.setInvertedControls(False)
        self.sat_max.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sat_max.setTickInterval(5)
        self.sat_max.setObjectName("sat_max")
        self.gridLayout_2.addWidget(self.sat_max, 3, 1, 1, 1)
        self.sat_max_d = QtWidgets.QLabel(self.widget)
        self.sat_max_d.setObjectName("sat_max_d")
        self.gridLayout_2.addWidget(self.sat_max_d, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.val_min = QtWidgets.QSlider(self.widget)
        self.val_min.setAcceptDrops(True)
        self.val_min.setAutoFillBackground(True)
        self.val_min.setMaximum(255)
        self.val_min.setTracking(True)
        self.val_min.setOrientation(QtCore.Qt.Horizontal)
        self.val_min.setInvertedAppearance(False)
        self.val_min.setInvertedControls(False)
        self.val_min.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.val_min.setTickInterval(5)
        self.val_min.setObjectName("val_min")
        self.gridLayout_2.addWidget(self.val_min, 4, 1, 1, 1)
        self.val_min_d = QtWidgets.QLabel(self.widget)
        self.val_min_d.setObjectName("val_min_d")
        self.gridLayout_2.addWidget(self.val_min_d, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.val_max = QtWidgets.QSlider(self.widget)
        self.val_max.setAcceptDrops(True)
        self.val_max.setAutoFillBackground(True)
        self.val_max.setMaximum(255)
        self.val_max.setTracking(True)
        self.val_max.setOrientation(QtCore.Qt.Horizontal)
        self.val_max.setInvertedAppearance(False)
        self.val_max.setInvertedControls(False)
        self.val_max.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.val_max.setTickInterval(5)
        self.val_max.setObjectName("val_max")
        self.gridLayout_2.addWidget(self.val_max, 5, 1, 1, 1)
        self.val_max_d = QtWidgets.QLabel(self.widget)
        self.val_max_d.setObjectName("val_max_d")
        self.gridLayout_2.addWidget(self.val_max_d, 5, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(270, 600, 250, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.target = QtWidgets.QComboBox(self.widget1)
        self.target.setDuplicatesEnabled(True)
        self.target.setObjectName("target")
        self.target.addItems(["None", "White", "Green", "Yellow"])
        self.horizontalLayout.addWidget(self.target)
        self.applyButton = QtWidgets.QPushButton(self.widget1)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout.addWidget(self.applyButton)
        AssistApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AssistApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        AssistApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AssistApp)
        self.statusbar.setObjectName("statusbar")
        AssistApp.setStatusBar(self.statusbar)

        img = cv2.imread(self.image)
        self.IMG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        self.RED = np.zeros_like(self.IMG, np.uint8)
        self.RED[:] = (255, 0, 0)

        self.WARN = True

        self.retranslateUi(AssistApp)
        QtCore.QMetaObject.connectSlotsByName(AssistApp)

        self.hue_min.valueChanged.connect(self.hueMinRead)
        self.hue_max.valueChanged.connect(self.hueMaxRead)
        self.sat_min.valueChanged.connect(self.satMinRead)
        self.sat_max.valueChanged.connect(self.satMaxRead)
        self.val_min.valueChanged.connect(self.valMinRead)
        self.val_max.valueChanged.connect(self.valMaxRead)

        self.applyButton.clicked.connect(self.send_command)

        self.update()

    def retranslateUi(self, AssistApp):
        _translate = QtCore.QCoreApplication.translate
        AssistApp.setWindowTitle(_translate("AssistApp", "HSV Assist"))
        self.label_2.setText(_translate("AssistApp", "HUE MIN"))
        self.hue_min_d.setText(_translate("AssistApp", "0"))
        self.label_3.setText(_translate("AssistApp", "HUE MAX"))
        self.hue_max_d.setText(_translate("AssistApp", "0"))
        self.label_4.setText(_translate("AssistApp", "SAT MIN"))
        self.sat_min_d.setText(_translate("AssistApp", "0"))
        self.label_5.setText(_translate("AssistApp", "SAT MAX"))
        self.sat_max_d.setText(_translate("AssistApp", "0"))
        self.label_6.setText(_translate("AssistApp", "VAL MIN"))
        self.val_min_d.setText(_translate("AssistApp", "0"))
        self.label_7.setText(_translate("AssistApp", "VAL MAX"))
        self.val_max_d.setText(_translate("AssistApp", "0"))
        self.label_8.setText(_translate("AssistApp", "Which color?"))
        self.applyButton.setText(_translate("AssistApp", "Send"))

    def hueMinRead(self):
        self.hue_min_d.setText(f"{self.hue_min.value()}")
        try:
            if self.hue_min.value() > self.hue_max.value():
                self.showWarning("Hue Min must be equal or less than Hue Max!")
                self.hue_min.setValue(self.hue_max.value())
            self.update()
        except:
            pass

    def hueMaxRead(self):
        self.hue_max_d.setText(f"{self.hue_max.value()}")
        try:
            if self.hue_min.value() > self.hue_max.value():
                self.showWarning("Hue Max must be equal or greater than Hue Min!")
                self.hue_max.setValue(self.hue_min.value())
            self.update()
        except:
            pass

    def satMinRead(self):
        self.sat_min_d.setText(f"{self.sat_min.value()}")
        try:
            if self.sat_min.value() > self.sat_max.value():
                self.showWarning("Sat Min must be equal or less than Sat Max!")
                self.sat_min.setValue(self.sat_max.value())
            self.update()
        except:
            pass

    def satMaxRead(self):
        self.sat_max_d.setText(f"{self.sat_max.value()}")
        try:
            if self.sat_min.value() > self.sat_max.value():
                self.showWarning("Sat Max must be equal or greater than Sat Min!")
                self.sat_max.setValue(self.sat_min.value())
            self.update()
        except:
            pass

    def valMinRead(self):
        self.val_min_d.setText(f"{self.val_min.value()}")
        try:
            if self.val_min.value() > self.val_max.value():
                self.showWarning("Val Min must be equal or less than Val Max!")
                self.val_min.setValue(self.val_max.value())
            self.update()
        except:
            pass

    def valMaxRead(self):
        self.val_max_d.setText(f"{self.val_max.value()}")
        try:
            if self.val_min.value() > self.val_max.value():
                self.showWarning("Val Max must be equal or greater than Val Min!")
                self.val_max.setValue(self.val_min.value())
            self.update()
        except:
            pass

    def showWarning(self, message):
        if self.WARN:
            msg = QMessageBox()
            msg.setWindowTitle("Bad Argument")
            msg.setText(message)
            msg.setIcon(QMessageBox.Critical)
            chk = QtWidgets.QCheckBox()
            chk.setText("Do show this again")
            msg.setCheckBox(chk)
            msg.exec_()
            if chk.isChecked():
                self.WARN = False
    
    def update(self):
        img = self.IMG.copy()
        height, width, channel = img.shape
        bytes_per_line = 3 * width
        hsv_min = np.array([self.hue_min.value(), self.sat_min.value(), self.val_min.value()])
        hsv_max = np.array([self.hue_max.value(), self.sat_max.value(), self.val_max.value()])
        mask = cv2.inRange(self.HSV, hsv_min, hsv_max)
        imask = mask > 0
        img[imask] = self.RED[imask]
        q_image = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_image)
        self.img.setPixmap(pixmap)

    def send_command(self):
        if self.target.currentText() == 'White':
            self.master_obj.hue_min_w.setText(str(self.hue_min.value()))
            self.master_obj.hue_max_w.setText(str(self.hue_max.value()))
            self.master_obj.sat_min_w.setText(str(self.sat_min.value()))
            self.master_obj.sat_max_w.setText(str(self.sat_max.value()))
            self.master_obj.val_min_w.setText(str(self.val_min.value()))
            self.master_obj.val_max_w.setText(str(self.val_max.value()))
        elif self.target.currentText() == 'Green':
            self.master_obj.hue_min_g.setText(str(self.hue_min.value()))
            self.master_obj.hue_max_g.setText(str(self.hue_max.value()))
            self.master_obj.sat_min_g.setText(str(self.sat_min.value()))
            self.master_obj.sat_max_g.setText(str(self.sat_max.value()))
            self.master_obj.val_min_g.setText(str(self.val_min.value()))
            self.master_obj.val_max_g.setText(str(self.val_max.value()))
        elif self.target.currentText() == 'Yellow':
            self.master_obj.hue_min_y.setText(str(self.hue_min.value()))
            self.master_obj.hue_max_y.setText(str(self.hue_max.value()))
            self.master_obj.sat_min_y.setText(str(self.sat_min.value()))
            self.master_obj.sat_max_y.setText(str(self.sat_max.value()))
            self.master_obj.val_min_y.setText(str(self.val_min.value()))
            self.master_obj.val_max_y.setText(str(self.val_max.value()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssistApp = QtWidgets.QMainWindow()
    ui = Ui_AssistApp()
    ui.setupUi(AssistApp, 'logo.jpg')
    AssistApp.show()
    sys.exit(app.exec_())

