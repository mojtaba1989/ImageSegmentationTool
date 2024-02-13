from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import cv2
import os

class Ui_PaintApp(object):
    def setupUi(self, PaintApp, image=None, master_obj=None):
        PaintApp.setObjectName("PaintApp")
        PaintApp.setWindowModality(QtCore.Qt.ApplicationModal)
        PaintApp.resize(830, 680)
        self.image = image
        self.master_obj = master_obj
        self.centralwidget = QtWidgets.QWidget(PaintApp)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(11, 11, 800, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.img = QtWidgets.QLabel()
        self.img.setMouseTracking(True)
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap(""))
        self.img.setScaledContents(False)
        self.img.setObjectName("img")
        self.scrollArea.setWidget(self.img)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(25, 620, 760, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.undo = QtWidgets.QPushButton(self.widget)
        self.undo.setObjectName("undo")
        self.undo.setToolTip("CTRL+Z")
        self.horizontalLayout.addWidget(self.undo)
        self.erase = QtWidgets.QPushButton(self.widget)
        self.erase.setObjectName("erase")
        self.erase.setToolTip("Eraser only works as brush\nPress ESC or click on Draw to change back to draw")
        self.horizontalLayout.addWidget(self.erase)
        self.tool = QtWidgets.QComboBox(self.widget)
        self.tool.setObjectName("tool")
        self.tool.addItems(["Brush", "Line"])
        self.tool.setToolTip("Brush: click to start, hold to draw and release to end\n----\nLine:click to start/add a point to polygon and press ESC to finish drawing")
        self.horizontalLayout.addWidget(self.tool)
        self.brushSize = QtWidgets.QSpinBox(self.widget)
        self.brushSize.setObjectName("brushSize")
        self.brushSize.setMinimum(1)
        self.brushSize.setMaximum(99)
        self.brushSize.setValue(11)
        self.horizontalLayout.addWidget(self.brushSize)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.target = QtWidgets.QComboBox(self.widget)
        self.target.setDuplicatesEnabled(True)
        self.target.setObjectName("target")
        self.target.addItems(["White", "Green", "Yellow"])
        self.horizontalLayout.addWidget(self.target)
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.zoomin = QtWidgets.QPushButton(self.widget)
        self.zoomin.setObjectName("zoomin")
        self.horizontalLayout.addWidget(self.zoomin)
        self.zoomout = QtWidgets.QPushButton(self.widget)
        self.zoomout.setObjectName("zoomout")
        self.horizontalLayout.addWidget(self.zoomout)
        self.fit = QtWidgets.QPushButton(self.widget)
        self.fit.setObjectName("fit")
        self.horizontalLayout.addWidget(self.fit)
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setToolTip("Saves modified image with same filename.\nCheck \"PATH_TO_FILE\"/_modified/ directory")
        self.horizontalLayout.addWidget(self.saveButton)
        PaintApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PaintApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 20))
        self.menubar.setObjectName("menubar")
        PaintApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PaintApp)
        self.statusbar.setObjectName("statusbar")
        PaintApp.setStatusBar(self.statusbar)

        img = cv2.imread(self.image)
        self.IMG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.MASK = np.zeros_like(self.IMG, np.uint8)
        self.LMASK = []
        self.LMASK.append(self.MASK)
        self.GREEN = (1, 255, 1)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 1)
        self.CLREAR = (0, 0, 0)

        self.WARN = True
        self.CLICKED = False
        self.ERASE = False
        self.SCALE = 1
        self.BRUSH = self.WHITE
        self.POLYGON = []
        self.PREVIOUS_TOOL = None
        self.SAVED_BEFORE_EXIT = True

        self.retranslateUi(PaintApp)
        QtCore.QMetaObject.connectSlotsByName(PaintApp)

        self.zoomin.clicked.connect(self.zoomin_command)
        self.zoomout.clicked.connect(self.zoomout_command)
        self.fit.clicked.connect(self.fit_command)
        self.erase.clicked.connect(self.erase_command)
        self.undo.clicked.connect(self.undo_command)
        self.saveButton.clicked.connect(lambda:self.save_command(PaintApp))

        self.target.currentTextChanged.connect(self.brush_color_change)

        self.img.mousePressEvent = self.on_mouse_click
        self.img.mouseMoveEvent = self.on_mouse_move
        self.img.mouseReleaseEvent = self.on_mouse_release
        PaintApp.closeEvent = self.closeEvent
        PaintApp.keyPressEvent = self.keyPressEvent

        self.update()
        self.history_check()

    def retranslateUi(self, PaintApp):
        _translate = QtCore.QCoreApplication.translate
        PaintApp.setWindowTitle(_translate("PaintApp", "Paint"))
        self.erase.setText(_translate("PaintApp", "Eraser"))
        self.undo.setText(_translate("PaintApp", "Undo"))
        self.undo.setShortcut(_translate("PaintApp", "Ctrl+z"))
        self.label_2.setText(_translate("PaintApp", "Color"))
        self.zoomin.setText(_translate("PaintApp", "Zoom In"))
        self.zoomout.setText(_translate("PaintApp", "Zoom Out"))
        self.fit.setText(_translate("PaintApp", "Fit Screen"))
        self.saveButton.setText(_translate("PaintApp", "Save"))

    def on_mouse_click(self, event):
        self.CLICKED = True
        self.LMASK.append(self.LMASK[-1].copy())
        pos = self.img.mapFromGlobal(self.scrollArea.mapToGlobal(event.pos()))
        h_scrollbar_value = self.scrollArea.horizontalScrollBar().value()
        v_scrollbar_value = self.scrollArea.verticalScrollBar().value()
        actual_pos_x = int((pos.x() - h_scrollbar_value) / self.SCALE)
        actual_pos_y = int((pos.y() - v_scrollbar_value) / self.SCALE)
        mask = self.LMASK[-1]
        sample_size = self.brushSize.value()
        half_sample_size = sample_size // 2
        cv2.circle(mask, (actual_pos_x, actual_pos_y), half_sample_size, self.BRUSH, -1)
        self.update(mask=mask)
        if self.tool.currentText()=='Line':
            self.POLYGON.append((actual_pos_x, actual_pos_y))
            if len(self.POLYGON) > 1:
                cv2.line(mask, self.POLYGON[-2], self.POLYGON[-1], self.BRUSH, sample_size)


    def on_mouse_move(self, event):
        if self.CLICKED and self.tool.currentText()=='Brush':
            pos = self.img.mapFromGlobal(self.scrollArea.mapToGlobal(event.pos()))
            h_scrollbar_value = self.scrollArea.horizontalScrollBar().value()
            v_scrollbar_value = self.scrollArea.verticalScrollBar().value()
            actual_pos_x = int((pos.x() - h_scrollbar_value) / self.SCALE)
            actual_pos_y = int((pos.y() - v_scrollbar_value) / self.SCALE)
            mask = self.LMASK[-1]
            sample_size = self.brushSize.value()
            half_sample_size = sample_size // 2
            cv2.circle(mask, (actual_pos_x, actual_pos_y), half_sample_size, self.BRUSH, -1)
            self.update(mask=mask)
        elif self.CLICKED and self.tool.currentText()=='Line':
            pos = self.img.mapFromGlobal(self.scrollArea.mapToGlobal(event.pos()))
            h_scrollbar_value = self.scrollArea.horizontalScrollBar().value()
            v_scrollbar_value = self.scrollArea.verticalScrollBar().value()
            actual_pos_x = int((pos.x() - h_scrollbar_value) / self.SCALE)
            actual_pos_y = int((pos.y() - v_scrollbar_value) / self.SCALE)
            mask = self.LMASK[-1].copy()
            sample_size = self.brushSize.value()
            cv2.line(mask, self.POLYGON[-1], (actual_pos_x, actual_pos_y), self.BRUSH, sample_size)
            self.update(mask=mask)

    def on_mouse_release(self, event):
        if self.tool.currentText() == 'Brush':
            self.CLICKED = False
        self.history_check()
    
    def erase_command(self):
        if not self.ERASE:
            self.ERASE = True
            self.erase.setText(QtCore.QCoreApplication.translate("PaintApp", "Draw"))
            self.BRUSH = self.CLREAR
            self.PREVIOUS_TOOL = self.tool.currentText()
            self.tool.setCurrentText("Brush")
        else:
            self.ERASE = False
            self.erase.setText(QtCore.QCoreApplication.translate("PaintApp", "Erase"))
            self.tool.setCurrentText(self.PREVIOUS_TOOL)
            self.brush_color_change()
            
    def brush_color_change(self):
        if self.target.currentText() == "White":
            self.BRUSH = self.WHITE
        elif self.target.currentText() == "Green":
            self.BRUSH = self.GREEN
        elif self.target.currentText() == "Yellow":
            self.BRUSH = self.YELLOW

    def update(self, mask=None):
        img = self.IMG.copy()
        try:
            img[mask > 0] = mask[mask > 0]
        except:
            pass
        height, width, channel = img.shape
        bytes_per_line = 3 * width
        q_image = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.pixmap = QtGui.QPixmap.fromImage(q_image)
        self.img.setPixmap(self.pixmap)
        self.resize_image()
        self.SAVED_BEFORE_EXIT = False

    def undo_command(self):
        if len(self.LMASK) > 1:
            self.LMASK.pop()
            self.update(self.LMASK[-1])
            self.history_check()

    def history_check(self):
        if len(self.LMASK) > 1:
            self.undo.setEnabled(True)
            while len(self.LMASK) > 20:
                self.LMASK.pop(1)
        else:
            self.undo.setEnabled(False)

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

    def save_command(self):
        dir = os.path.dirname(self.image) + '/_modified'
        filename = os.path.basename(self.image)
        if not os.path.exists(dir):
            os.mkdir(dir)        
        img = self.IMG.copy()
        try:
            img[self.LMASK[-1] > 0] = self.LMASK[-1][self.LMASK[-1] > 0]
        except:
            pass
        cv2.imwrite(os.path.join(dir, filename), cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        self.SAVED_BEFORE_EXIT = True
    
    def keyPressEvent(self, event):
        if event.key() == 16777216:  #ESC
            self.CLICKED = False
            self.POLYGON.clear()
            self.update(mask=self.LMASK[-1])
            self.ERASE = False
            self.erase.setText(QtCore.QCoreApplication.translate("PaintApp", "Erase"))
            self.tool.setCurrentText(self.PREVIOUS_TOOL)
            self.brush_color_change()

    def closeEvent(self, event):
        if self.SAVED_BEFORE_EXIT and self.master_obj:
            filename = os.path.basename(self.image)
            self.master_obj.reload(f"{filename} has been added to \"Modified\" list", filename)
        elif not self.SAVED_BEFORE_EXIT and self.master_obj:
            msg = QMessageBox()
            msg.setWindowTitle("Unsaved changes")
            msg.setText("Unsaved Changes will be discarded\nSave before proceed?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(msg.Save|msg.Ignore)
            msg.setDefaultButton(msg.Save)
            result = msg.exec_()
            if result == msg.Save:
                self.save_command()
                filename = os.path.basename(self.image)
                self.master_obj.reload(f"{filename} has been added to \"Modified\" list", filename)
        elif not self.SAVED_BEFORE_EXIT:
            msg = QMessageBox()
            msg.setWindowTitle("Unsaved changes")
            msg.setText("Unsaved Changes will be discarded\nSave before proceed?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(msg.Save|msg.Ignore)
            msg.setDefaultButton(msg.Save)
            result = msg.exec_()
            if result == msg.Save:
                self.save_command()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaintApp = QtWidgets.QMainWindow()
    ui = Ui_PaintApp()
    ui.setupUi(PaintApp, '/home/moji/python_devel/ImageSegmentationTool/normal.png')
    PaintApp.show()
    sys.exit(app.exec_())

