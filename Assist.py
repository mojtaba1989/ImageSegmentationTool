from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import cv2

class Ui_AssistApp(object):
    def setupUi(self, AssistApp, image=None, master_obj=None):
        AssistApp.setObjectName("AssistApp")
        AssistApp.setWindowModality(QtCore.Qt.ApplicationModal)
        AssistApp.resize(825, 830)
        self.image = image
        self.master_obj = master_obj
        self.centralwidget = QtWidgets.QWidget(AssistApp)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 620, 781, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.hue_min = QtWidgets.QSlider(self.layoutWidget)
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
        self.hue_min_d = QtWidgets.QLabel(self.layoutWidget)
        self.hue_min_d.setObjectName("hue_min_d")
        self.gridLayout_2.addWidget(self.hue_min_d, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.hue_max = QtWidgets.QSlider(self.layoutWidget)
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
        self.hue_max_d = QtWidgets.QLabel(self.layoutWidget)
        self.hue_max_d.setObjectName("hue_max_d")
        self.gridLayout_2.addWidget(self.hue_max_d, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.sat_min = QtWidgets.QSlider(self.layoutWidget)
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
        self.sat_min_d = QtWidgets.QLabel(self.layoutWidget)
        self.sat_min_d.setObjectName("sat_min_d")
        self.gridLayout_2.addWidget(self.sat_min_d, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.sat_max = QtWidgets.QSlider(self.layoutWidget)
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
        self.sat_max_d = QtWidgets.QLabel(self.layoutWidget)
        self.sat_max_d.setObjectName("sat_max_d")
        self.gridLayout_2.addWidget(self.sat_max_d, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.val_min = QtWidgets.QSlider(self.layoutWidget)
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
        self.val_min_d = QtWidgets.QLabel(self.layoutWidget)
        self.val_min_d.setObjectName("val_min_d")
        self.gridLayout_2.addWidget(self.val_min_d, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.val_max = QtWidgets.QSlider(self.layoutWidget)
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
        self.val_max_d = QtWidgets.QLabel(self.layoutWidget)
        self.val_max_d.setObjectName("val_max_d")
        self.gridLayout_2.addWidget(self.val_max_d, 5, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 780, 715, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.brushSize = QtWidgets.QSpinBox(self.layoutWidget1)
        self.brushSize.setObjectName("brushSize")
        self.brushSize.setMinimum(1)
        self.brushSize.setMaximum(51)
        self.brushSize.setSingleStep(2)
        self.horizontalLayout.addWidget(self.brushSize)
        self.sample = QtWidgets.QPushButton(self.layoutWidget1)
        self.sample.setObjectName("sample")
        self.horizontalLayout.addWidget(self.sample)
        self.zoomin = QtWidgets.QPushButton(self.layoutWidget1)
        self.zoomin.setObjectName("zoomin")
        self.horizontalLayout.addWidget(self.zoomin)
        self.zoomout = QtWidgets.QPushButton(self.layoutWidget1)
        self.zoomout.setObjectName("zoomout")
        self.horizontalLayout.addWidget(self.zoomout)
        self.fit = QtWidgets.QPushButton(self.layoutWidget1)
        self.fit.setObjectName("fit")
        self.horizontalLayout.addWidget(self.fit)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.target = QtWidgets.QComboBox(self.layoutWidget1)
        self.target.setDuplicatesEnabled(True)
        self.target.setObjectName("target")
        self.target.addItems(["None", "White", "Green", "Yellow"])
        self.horizontalLayout.addWidget(self.target)
        self.applyButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout.addWidget(self.applyButton)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 800, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.img = QtWidgets.QLabel()
        self.img.setMouseTracking(True)
        self.img.setPixmap(QtGui.QPixmap(""))
        self.img.setScaledContents(False)
        self.img.setObjectName("img")
        self.scrollArea.setWidget(self.img)
        AssistApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AssistApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 20))
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
        self.SCALE = 1

        self.retranslateUi(AssistApp)
        QtCore.QMetaObject.connectSlotsByName(AssistApp)

        self.hue_min.valueChanged.connect(self.hueMinRead)
        self.hue_max.valueChanged.connect(self.hueMaxRead)
        self.sat_min.valueChanged.connect(self.satMinRead)
        self.sat_max.valueChanged.connect(self.satMaxRead)
        self.val_min.valueChanged.connect(self.valMinRead)
        self.val_max.valueChanged.connect(self.valMaxRead)

        self.applyButton.clicked.connect(self.send_command)
        self.zoomin.clicked.connect(self.zoomin_command)
        self.zoomout.clicked.connect(self.zoomout_command)
        self.fit.clicked.connect(self.fit_command)

        self.img.mousePressEvent = self.on_mouse_click
        self.img.mouseMoveEvent = self.on_mouse_move
        self.sample.clicked.connect(self.sample_command)

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
        self.label.setText(_translate("AssistApp", "Brush size"))
        self.sample.setText(_translate("AssistApp", "Sample"))
        self.zoomin.setText(_translate("AssistApp", "Zoom In"))
        self.zoomout.setText(_translate("AssistApp", "Zoom Out"))
        self.fit.setText(_translate("AssistApp", "Fit Screen"))
        self.label_8.setText(_translate("AssistApp", "Which color?"))
        self.applyButton.setText(_translate("AssistApp", "Send"))

    def sample_command(self):
        if self.sample.isEnabled():
            self.sample.setEnabled(False)

    def on_mouse_click(self, event):
        if not self.sample.isEnabled():
            pos = self.img.mapFromGlobal(self.scrollArea.mapToGlobal(event.pos()))
            h_scrollbar_value = self.scrollArea.horizontalScrollBar().value()
            v_scrollbar_value = self.scrollArea.verticalScrollBar().value()
            actual_pos_x = int((pos.x() - h_scrollbar_value) / self.SCALE)
            actual_pos_y = int((pos.y() - v_scrollbar_value) / self.SCALE)            
            image_width = self.pixmap.width()
            image_height = self.pixmap.height()
            sample_size = self.brushSize.value()
            half_sample_size = sample_size // 2
            start_x = max(0, actual_pos_x - half_sample_size)
            start_y = max(0, actual_pos_y - half_sample_size)
            end_x = min(image_width, actual_pos_x + half_sample_size)
            end_y = min(image_height, actual_pos_y + half_sample_size)
            if half_sample_size == 0:
                sample_hsv = self.HSV[start_y, start_x, :]
                hue_min = sample_hsv[0]
                hue_max = sample_hsv[0]
                sat_min = sample_hsv[1]
                sat_max = sample_hsv[1]
                val_min = sample_hsv[2]
                val_max = sample_hsv[2]
            else:
                sample_hsv = self.HSV[start_y:end_y, start_x:end_x, :]
                hue_min = int(sample_hsv[:, :, 0].min())
                hue_max = int(sample_hsv[:, :, 0].max())
                sat_min = int(sample_hsv[:, :, 1].min())
                sat_max = int(sample_hsv[:, :, 1].max())
                val_min = int(sample_hsv[:, :, 2].min())
                val_max = int(sample_hsv[:, :, 2].max())
                
            self.hue_min.setValue(0)
            self.hue_max.setValue(255)
            self.sat_min.setValue(0)
            self.sat_max.setValue(255)
            self.val_min.setValue(0)
            self.val_max.setValue(255)
            self.hue_min.setValue(np.max([hue_min - 15, 0]))
            self.hue_max.setValue(np.min([hue_max + 15, 255]))
            self.sat_min.setValue(np.max([sat_min - 15, 0]))
            self.sat_max.setValue(np.min([sat_max + 15, 255]))
            self.val_min.setValue(np.max([val_min - 30, 0]))
            self.val_max.setValue(np.min([val_max + 30, 255]))
            self.sample.setEnabled(True)
    
    def on_mouse_move(self, event):
        if not self.sample.isEnabled():
            pos = self.img.mapFromGlobal(self.scrollArea.mapToGlobal(event.pos()))
            h_scrollbar_value = self.scrollArea.horizontalScrollBar().value()
            v_scrollbar_value = self.scrollArea.verticalScrollBar().value()
            actual_pos_x = int((pos.x() - h_scrollbar_value) / self.SCALE)
            actual_pos_y = int((pos.y() - v_scrollbar_value) / self.SCALE)
            img = self.IMG.copy()
            sample_size = self.brushSize.value()
            half_sample_size = sample_size // 2
            cv2.circle(img, (actual_pos_x, actual_pos_y), half_sample_size, (0, 0, 255), -1)
            height, width, channel = img.shape
            bytes_per_line = 3 * width
            q_image = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            self.pixmap = QtGui.QPixmap.fromImage(q_image)
            self.img.setPixmap(self.pixmap)
            self.resize_image()


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
        self.pixmap = QtGui.QPixmap.fromImage(q_image)
        self.img.setPixmap(self.pixmap)
        self.resize_image()

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

    def zoomin_command(self, event):
        self.img.setScaledContents(False)
        self.SCALE *= 1.25
        self.resize_image()

    def zoomout_command(self, event):
        self.img.setScaledContents(False)
        self.SCALE *= .8
        self.resize_image()

    def fit_command(self, event):
        self.SCALE = 1/1.2
        self.resize_image()
        self.img.setScaledContents(True)

    def resize_image(self):
        size = self.pixmap.size()
        scaled_pixmap = self.pixmap.scaled(self.SCALE * size)
        self.img.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssistApp = QtWidgets.QMainWindow()
    ui = Ui_AssistApp()
    ui.setupUi(AssistApp, 'normal.png')
    AssistApp.show()
    sys.exit(app.exec_())

