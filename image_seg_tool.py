import cv2
import os
import copy
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import PyQt5

import xml.etree.ElementTree as ET
from xml.dom import minidom
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.White = QtWidgets.QGroupBox(self.centralwidget)
        self.White.setGeometry(QtCore.QRect(20, 580, 191, 211))
        self.White.setCheckable(True)
        self.White.setChecked(True)
        self.White.setObjectName("White")
        self.threshold_w = QtWidgets.QSlider(self.White)
        self.threshold_w.setGeometry(QtCore.QRect(84, 159, 41, 16))
        self.threshold_w.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_w.setObjectName("threshold_w")
        self.threshold_w.setMaximum(255)
        self.threshold_w.setValue(50)
        self.label_8 = QtWidgets.QLabel(self.White)
        self.label_8.setGeometry(QtCore.QRect(12, 130, 80, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.White)
        self.label_7.setGeometry(QtCore.QRect(12, 43, 63, 16))
        self.label_7.setObjectName("label_7")
        self.sat_max_w = QtWidgets.QLineEdit(self.White)
        self.sat_max_w.setGeometry(QtCore.QRect(140, 72, 41, 23))
        self.sat_max_w.setObjectName("sat_max_w")
        self.sat_max_w.setText('255')
        self.val_max_w = QtWidgets.QLineEdit(self.White)
        self.val_max_w.setGeometry(QtCore.QRect(140, 101, 41, 23))
        self.val_max_w.setObjectName("val_max_w")
        self.val_max_w.setText('255')
        self.smooth_size_w = QtWidgets.QComboBox(self.White)
        self.smooth_size_w.setGeometry(QtCore.QRect(140, 130, 41, 23))
        self.smooth_size_w.setObjectName("smooth_size_w")
        self.smooth_size_w.addItems(['1', '3', '5', '7', '9'])
        self.label_4 = QtWidgets.QLabel(self.White)
        self.label_4.setGeometry(QtCore.QRect(84, 22, 22, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.White)
        self.label_5.setGeometry(QtCore.QRect(140, 22, 25, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.White)
        self.label_3.setGeometry(QtCore.QRect(12, 101, 33, 16))
        self.label_3.setObjectName("label_3")
        self.sat_min_w = QtWidgets.QLineEdit(self.White)
        self.sat_min_w.setGeometry(QtCore.QRect(84, 72, 41, 23))
        self.sat_min_w.setObjectName("sat_min_w")
        self.sat_min_w.setText('0')
        self.label_6 = QtWidgets.QLabel(self.White)
        self.label_6.setGeometry(QtCore.QRect(12, 72, 61, 16))
        self.label_6.setObjectName("label_6")
        self.hue_max_w = QtWidgets.QLineEdit(self.White)
        self.hue_max_w.setGeometry(QtCore.QRect(140, 43, 41, 23))
        self.hue_max_w.setObjectName("hue_max_w")
        self.hue_max_w.setText('255')
        self.val_min_w = QtWidgets.QLineEdit(self.White)
        self.val_min_w.setGeometry(QtCore.QRect(84, 101, 41, 23))
        self.val_min_w.setObjectName("val_min_w")
        self.val_min_w.setText('0')
        self.label_9 = QtWidgets.QLabel(self.White)
        self.label_9.setGeometry(QtCore.QRect(12, 159, 60, 16))
        self.label_9.setObjectName("label_9")
        self.hue_min_w = QtWidgets.QLineEdit(self.White)
        self.hue_min_w.setGeometry(QtCore.QRect(84, 43, 41, 23))
        self.hue_min_w.setObjectName("hue_min_w")
        self.hue_min_w.setText('0')
        self.label = QtWidgets.QLabel(self.White)
        self.label.setGeometry(QtCore.QRect(12, 180, 33, 16))
        self.label.setObjectName("label")
        self.mask_val_w = QtWidgets.QLineEdit(self.White)
        self.mask_val_w.setGeometry(QtCore.QRect(84, 180, 41, 23))
        self.mask_val_w.setObjectName("mask_val_w")
        self.mask_val_w.setText('255')
        self.threshold_w_d = QtWidgets.QLabel(self.White)
        self.threshold_w_d.setGeometry(QtCore.QRect(140, 160, 31, 16))
        self.threshold_w_d.setObjectName("threshold_w_d")
        self.Green = QtWidgets.QGroupBox(self.centralwidget)
        self.Green.setGeometry(QtCore.QRect(220, 580, 191, 211))
        self.Green.setCheckable(True)
        self.Green.setChecked(True)
        self.Green.setObjectName("Green")
        self.threshold_g = QtWidgets.QSlider(self.Green)
        self.threshold_g.setGeometry(QtCore.QRect(84, 159, 41, 16))
        self.threshold_g.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_g.setObjectName("threshold_g")
        self.threshold_g.setMaximum(255)
        self.threshold_g.setValue(50)
        self.label_10 = QtWidgets.QLabel(self.Green)
        self.label_10.setGeometry(QtCore.QRect(12, 130, 80, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Green)
        self.label_11.setGeometry(QtCore.QRect(12, 72, 63, 16))
        self.label_11.setObjectName("label_11")
        self.hue_max_g = QtWidgets.QLineEdit(self.Green)
        self.hue_max_g.setGeometry(QtCore.QRect(140, 43, 41, 23))
        self.hue_max_g.setObjectName("hue_max_g")
        self.hue_max_g.setText('255')
        self.val_max_g = QtWidgets.QLineEdit(self.Green)
        self.val_max_g.setGeometry(QtCore.QRect(140, 101, 41, 23))
        self.val_max_g.setObjectName("val_max_g")
        self.val_max_g.setText('255')
        self.smooth_size_g = QtWidgets.QComboBox(self.Green)
        self.smooth_size_g.setGeometry(QtCore.QRect(140, 130, 41, 23))
        self.smooth_size_g.setObjectName("smooth_size_g")
        self.smooth_size_g.addItems(['1', '3', '5', '7', '9'])
        self.label_12 = QtWidgets.QLabel(self.Green)
        self.label_12.setGeometry(QtCore.QRect(84, 22, 22, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Green)
        self.label_13.setGeometry(QtCore.QRect(140, 22, 25, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Green)
        self.label_14.setGeometry(QtCore.QRect(12, 101, 33, 16))
        self.label_14.setObjectName("label_14")
        self.hue_min_g = QtWidgets.QLineEdit(self.Green)
        self.hue_min_g.setGeometry(QtCore.QRect(84, 43, 41, 23))
        self.hue_min_g.setObjectName("hue_min_g")
        self.hue_min_g.setText('0')
        self.label_15 = QtWidgets.QLabel(self.Green)
        self.label_15.setGeometry(QtCore.QRect(12, 43, 24, 16))
        self.label_15.setObjectName("label_15")
        self.sat_max_g = QtWidgets.QLineEdit(self.Green)
        self.sat_max_g.setGeometry(QtCore.QRect(140, 72, 41, 23))
        self.sat_max_g.setObjectName("sat_max_g")
        self.sat_max_g.setText('255')
        self.val_min_g = QtWidgets.QLineEdit(self.Green)
        self.val_min_g.setGeometry(QtCore.QRect(84, 101, 41, 23))
        self.val_min_g.setObjectName("val_min_g")
        self.val_min_g.setText('0')
        self.label_16 = QtWidgets.QLabel(self.Green)
        self.label_16.setGeometry(QtCore.QRect(12, 159, 60, 16))
        self.label_16.setObjectName("label_16")
        self.sat_min_g = QtWidgets.QLineEdit(self.Green)
        self.sat_min_g.setGeometry(QtCore.QRect(84, 72, 41, 23))
        self.sat_min_g.setObjectName("sat_min_g")
        self.sat_min_g.setText('0')
        self.label_2 = QtWidgets.QLabel(self.Green)
        self.label_2.setGeometry(QtCore.QRect(12, 180, 33, 16))
        self.label_2.setObjectName("label_2")
        self.mask_val_g = QtWidgets.QLineEdit(self.Green)
        self.mask_val_g.setGeometry(QtCore.QRect(84, 180, 41, 23))
        self.mask_val_g.setObjectName("mask_val_g")
        self.mask_val_g.setText('80')
        self.threshold_g_d = QtWidgets.QLabel(self.Green)
        self.threshold_g_d.setGeometry(QtCore.QRect(140, 160, 31, 16))
        self.threshold_g_d.setObjectName("threshold_g_d")
        self.Yellow = QtWidgets.QGroupBox(self.centralwidget)
        self.Yellow.setGeometry(QtCore.QRect(420, 580, 191, 211))
        self.Yellow.setCheckable(True)
        self.Yellow.setChecked(True)
        self.Yellow.setObjectName("Yellow")
        self.threshold_y = QtWidgets.QSlider(self.Yellow)
        self.threshold_y.setGeometry(QtCore.QRect(84, 159, 41, 16))
        self.threshold_y.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_y.setObjectName("threshold_y")
        self.threshold_y.setMaximum(255)
        self.threshold_y.setValue(50)
        self.label_17 = QtWidgets.QLabel(self.Yellow)
        self.label_17.setGeometry(QtCore.QRect(12, 130, 80, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Yellow)
        self.label_18.setGeometry(QtCore.QRect(12, 72, 63, 16))
        self.label_18.setObjectName("label_18")
        self.hue_max_y = QtWidgets.QLineEdit(self.Yellow)
        self.hue_max_y.setGeometry(QtCore.QRect(140, 43, 41, 23))
        self.hue_max_y.setObjectName("hue_max_y")
        self.hue_max_y.setText('255')
        self.val_max_y = QtWidgets.QLineEdit(self.Yellow)
        self.val_max_y.setGeometry(QtCore.QRect(140, 101, 41, 23))
        self.val_max_y.setObjectName("val_max_y")
        self.val_max_y.setText('255')
        self.smooth_size_y = QtWidgets.QComboBox(self.Yellow)
        self.smooth_size_y.setGeometry(QtCore.QRect(140, 130, 41, 23))
        self.smooth_size_y.setObjectName("smooth_size_y")
        self.smooth_size_y.addItems(['1', '3', '5', '7', '9'])
        self.label_19 = QtWidgets.QLabel(self.Yellow)
        self.label_19.setGeometry(QtCore.QRect(84, 22, 22, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Yellow)
        self.label_20.setGeometry(QtCore.QRect(140, 22, 25, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Yellow)
        self.label_21.setGeometry(QtCore.QRect(12, 101, 33, 16))
        self.label_21.setObjectName("label_21")
        self.hue_min_y = QtWidgets.QLineEdit(self.Yellow)
        self.hue_min_y.setGeometry(QtCore.QRect(84, 43, 41, 23))
        self.hue_min_y.setObjectName("hue_min_y")
        self.hue_min_y.setText('0')
        self.label_22 = QtWidgets.QLabel(self.Yellow)
        self.label_22.setGeometry(QtCore.QRect(12, 43, 24, 16))
        self.label_22.setObjectName("label_22")
        self.sat_max_y = QtWidgets.QLineEdit(self.Yellow)
        self.sat_max_y.setGeometry(QtCore.QRect(140, 72, 41, 23))
        self.sat_max_y.setObjectName("sat_max_y")
        self.sat_max_y.setText('255')
        self.val_min_y = QtWidgets.QLineEdit(self.Yellow)
        self.val_min_y.setGeometry(QtCore.QRect(84, 101, 41, 23))
        self.val_min_y.setObjectName("val_min_y")
        self.val_min_y.setText('0')
        self.label_23 = QtWidgets.QLabel(self.Yellow)
        self.label_23.setGeometry(QtCore.QRect(12, 159, 60, 16))
        self.label_23.setObjectName("label_23")
        self.sat_min_y = QtWidgets.QLineEdit(self.Yellow)
        self.sat_min_y.setGeometry(QtCore.QRect(84, 72, 41, 23))
        self.sat_min_y.setObjectName("sat_min_y")
        self.sat_min_y.setText('0')
        self.label_24 = QtWidgets.QLabel(self.Yellow)
        self.label_24.setGeometry(QtCore.QRect(12, 180, 33, 16))
        self.label_24.setObjectName("label_24")
        self.mask_val_y = QtWidgets.QLineEdit(self.Yellow)
        self.mask_val_y.setGeometry(QtCore.QRect(84, 180, 41, 23))
        self.mask_val_y.setObjectName("mask_val_y")
        self.mask_val_y.setText('170')
        self.threshold_y_d = QtWidgets.QLabel(self.Yellow)
        self.threshold_y_d.setGeometry(QtCore.QRect(140, 160, 31, 16))
        self.threshold_y_d.setObjectName("threshold_y_d")
        self.Img = QtWidgets.QLabel(self.centralwidget)
        self.Img.setGeometry(QtCore.QRect(136, 70, 667, 500))
        self.Img.setMouseTracking(True)
        self.Img.setTabletTracking(True)
        self.Img.setAutoFillBackground(True)
        self.Img.setText("")
        self.Img.setPixmap(QtGui.QPixmap(""))
        self.Img.setScaledContents(True)
        self.Img.setObjectName("Img")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 0, 601, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.file_selector = QtWidgets.QComboBox(self.frame)
        self.file_selector.setGeometry(QtCore.QRect(120, 30, 381, 23))
        self.file_selector.setObjectName("file_selector")
        self.list_selector = QtWidgets.QComboBox(self.frame)
        self.list_selector.setGeometry(QtCore.QRect(20, 30, 91, 23))
        self.list_selector.setObjectName("list_selector")
        self.list_selector.addItems(['All', 'Not Processed', 'Prossed and flagged', 'Processed'])
        self.auto_load_xml = QtWidgets.QCheckBox(self.frame)
        self.auto_load_xml.setGeometry(QtCore.QRect(520, 10, 51, 21))
        self.auto_load_xml.setObjectName("auto_load_xml")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(120, 10, 91, 16))
        self.label_26.setObjectName("label_26")
        self.load_xml = QtWidgets.QPushButton(self.frame)
        self.load_xml.setGeometry(QtCore.QRect(510, 30, 80, 23))
        self.load_xml.setObjectName("load_xml")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(630, 0, 281, 61))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.sky_filter = QtWidgets.QGroupBox(self.centralwidget)
        self.sky_filter.setGeometry(QtCore.QRect(620, 580, 211, 61))
        self.sky_filter.setCheckable(True)
        self.sky_filter.setObjectName("sky_filter")
        self.sky_val = QtWidgets.QSlider(self.sky_filter)
        self.sky_val.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.sky_val.setMouseTracking(True)
        self.sky_val.setTabletTracking(False)
        self.sky_val.setOrientation(QtCore.Qt.Horizontal)
        self.sky_val.setObjectName("sky_val")
        self.sky_val_d = QtWidgets.QLabel(self.sky_filter)
        self.sky_val_d.setGeometry(QtCore.QRect(170, 30, 31, 16))
        self.sky_val_d.setObjectName("sky_val_d")
        self.prob = QtWidgets.QGroupBox(self.centralwidget)
        self.prob.setGeometry(QtCore.QRect(620, 650, 291, 61))
        self.prob.setCheckable(True)
        self.prob.setChecked(False)
        self.prob.setObjectName("prob")
        self.prob_out = QtWidgets.QLabel(self.prob)
        self.prob_out.setGeometry(QtCore.QRect(110, 29, 171, 21))
        self.prob_out.setAutoFillBackground(True)
        self.prob_out.setObjectName("prob_out")
        self.label_28 = QtWidgets.QLabel(self.prob)
        self.label_28.setGeometry(QtCore.QRect(10, 24, 41, 31))
        self.label_28.setObjectName("label_28")
        self.brush_size = QtWidgets.QSpinBox(self.prob)
        self.brush_size.setGeometry(QtCore.QRect(50, 30, 47, 24))
        self.brush_size.setObjectName("brush_size")
        self.brush_size.setMinimum(3)
        self.brush_size.setMaximum(99)
        self.brush_size.setSingleStep(2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(620, 720, 291, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.previous = QtWidgets.QPushButton(self.frame_2)
        self.previous.setObjectName("previous")
        self.gridLayout.addWidget(self.previous, 0, 0, 1, 1)
        self.next = QtWidgets.QPushButton(self.frame_2)
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 0, 1, 1, 1)
        self.saveNnext = QtWidgets.QPushButton(self.frame_2)
        self.saveNnext.setObjectName("saveNnext")
        self.gridLayout.addWidget(self.saveNnext, 0, 2, 1, 1)
        self.save = QtWidgets.QPushButton(self.frame_2)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 1, 2, 1, 1)
        self.mask = QtWidgets.QPushButton(self.frame_2)
        self.mask.setObjectName("mask")
        self.gridLayout.addWidget(self.mask, 1, 1, 1, 1)
        self.xml_enb = QtWidgets.QCheckBox(self.frame_2)
        self.xml_enb.setObjectName("xml_enb")
        self.gridLayout.addWidget(self.xml_enb, 1, 0, 1, 1)
        self.flagged = QtWidgets.QCheckBox(self.centralwidget)
        self.flagged.setGeometry(QtCore.QRect(840, 610, 71, 21))
        self.flagged.setObjectName("flagged")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuProcess = QtWidgets.QMenu(self.menubar)
        self.menuProcess.setObjectName("menuProcess")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionShow_Mask = QtWidgets.QAction(MainWindow)
        self.actionShow_Mask.setObjectName("actionShow_Mask")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuProcess.addAction(self.actionUpdate)
        self.menuProcess.addAction(self.actionShow_Mask)
        self.menuControl.addAction(self.actionNext)
        self.menuControl.addAction(self.actionPrevious)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # global variables:
        self.DIRECTORY = ""
        self.IMG_LIST = []
        self.INDEX = -1
        self.IDXNP = []
        self.IDXP = []
        self.IDXPnF = []
        self.DICT = []
        self.LIST_DICT = {'P': self.IDXP, 'NP': self.IDXNP, 'PnF': self.IDXPnF}
        self.MASK = None
        self.IMG = None
        self.HSV = None
        self.MASK_IS_SHOWN = False
        self.UNSAVED = False
        self.ASKTOSAVE = True
        

        # button action connections
        self.actionOpen_Folder.triggered.connect(self.actionOpen_Folder_command)
        self.actionUpdate.triggered.connect(self.applyAll)
        self.actionNext.triggered.connect(self.next_command)
        self.actionPrevious.triggered.connect(self.previous_command)
        self.actionShow_Mask.triggered.connect(self.actionShow_Mask_command)
        self.actionHelp.triggered.connect(self.showHelpDialog)
        self.actionAbout.triggered.connect(self.showAboutDialog)

        self.mask.clicked.connect(self.mask_command)
        self.next.clicked.connect(self.next_command)
        self.previous.clicked.connect(self.previous_command)
        self.save.clicked.connect(self.save_command)
        self.load_xml.clicked.connect(self.load_xml_command)
        self.saveNnext.clicked.connect(self.saveNnext_command)

        self.file_selector.currentIndexChanged.connect(self.file_selector_command)
        self.list_selector.currentIndexChanged.connect(self.list_selector_command)

        self.Img.mousePressEvent = self.on_mouse_click

        # Show slider values
        self.sky_val.valueChanged.connect(self.sky_val_read)
        self.threshold_g.valueChanged.connect(self.threshold_g_read)
        self.threshold_w.valueChanged.connect(self.threshold_w_read)
        self.threshold_y.valueChanged.connect(self.threshold_y_read)

        # Auto update on check uncheck
        self.White.toggled.connect(self.applyAll)
        self.Green.toggled.connect(self.applyAll)
        self.Yellow.toggled.connect(self.applyAll)
        self.sky_filter.toggled.connect(self.applyAll)

        # Check Insert Box Values
        self.sat_min_w.textChanged.connect(lambda: self.check_input_val(self.sat_min_w))
        self.sat_max_w.textChanged.connect(lambda: self.check_input_val(self.sat_max_w))
        self.hue_min_w.textChanged.connect(lambda: self.check_input_val(self.hue_min_w))
        self.hue_max_w.textChanged.connect(lambda: self.check_input_val(self.hue_max_w))
        self.val_min_w.textChanged.connect(lambda: self.check_input_val(self.val_min_w))
        self.val_max_w.textChanged.connect(lambda: self.check_input_val(self.val_max_w))
        self.mask_val_w.textChanged.connect(lambda: self.check_input_val(self.mask_val_w))
        self.sat_min_g.textChanged.connect(lambda: self.check_input_val(self.sat_min_g))
        self.sat_max_g.textChanged.connect(lambda: self.check_input_val(self.sat_max_g))
        self.hue_min_g.textChanged.connect(lambda: self.check_input_val(self.hue_min_g))
        self.hue_max_g.textChanged.connect(lambda: self.check_input_val(self.hue_max_g))
        self.val_min_g.textChanged.connect(lambda: self.check_input_val(self.val_min_g))
        self.val_max_g.textChanged.connect(lambda: self.check_input_val(self.val_max_g))
        self.mask_val_g.textChanged.connect(lambda: self.check_input_val(self.mask_val_g))
        self.sat_min_y.textChanged.connect(lambda: self.check_input_val(self.sat_min_y))
        self.sat_max_y.textChanged.connect(lambda: self.check_input_val(self.sat_max_y))
        self.hue_min_y.textChanged.connect(lambda: self.check_input_val(self.hue_min_y))
        self.hue_max_y.textChanged.connect(lambda: self.check_input_val(self.hue_max_y))
        self.val_min_y.textChanged.connect(lambda: self.check_input_val(self.val_min_y))
        self.val_max_y.textChanged.connect(lambda: self.check_input_val(self.val_max_y))
        self.mask_val_y.textChanged.connect(lambda: self.check_input_val(self.mask_val_y))

        # Exit
        app.aboutToQuit.connect(self.beforeClose_command)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Segmentation Tool"))
        self.White.setTitle(_translate("MainWindow", "White"))
        self.label_8.setText(_translate("MainWindow", "Smooth Filter"))
        self.label_7.setText(_translate("MainWindow", "Hue"))
        self.label_4.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Max"))
        self.label_3.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Saturation"))
        self.label_9.setText(_translate("MainWindow", "Threshold"))
        self.label.setText(_translate("MainWindow", "Label"))
        self.Green.setTitle(_translate("MainWindow", "Green"))
        self.label_10.setText(_translate("MainWindow", "Smooth Filter"))
        self.label_11.setText(_translate("MainWindow", "Saturation"))
        self.label_12.setText(_translate("MainWindow", "Min"))
        self.label_13.setText(_translate("MainWindow", "Max"))
        self.label_14.setText(_translate("MainWindow", "Value"))
        self.label_15.setText(_translate("MainWindow", "Hue"))
        self.label_16.setText(_translate("MainWindow", "Threshold"))
        self.label_2.setText(_translate("MainWindow", "Label"))
        self.Yellow.setTitle(_translate("MainWindow", "Yellow"))
        self.label_17.setText(_translate("MainWindow", "Smooth Filter"))
        self.label_18.setText(_translate("MainWindow", "Saturation"))
        self.label_19.setText(_translate("MainWindow", "Min"))
        self.label_20.setText(_translate("MainWindow", "Max"))
        self.label_21.setText(_translate("MainWindow", "Value"))
        self.label_22.setText(_translate("MainWindow", "Hue"))
        self.label_23.setText(_translate("MainWindow", "Threshold"))
        self.label_24.setText(_translate("MainWindow", "Label"))
        self.auto_load_xml.setText(_translate("MainWindow", "Auto"))
        self.label_25.setText(_translate("MainWindow", "Select List"))
        self.label_26.setText(_translate("MainWindow", "Select Image"))
        self.load_xml.setText(_translate("MainWindow", "Load XML"))
        self.sky_filter.setTitle(_translate("MainWindow", "Filter Sky"))
        self.prob.setTitle(_translate("MainWindow", "Prob"))
        self.prob_out.setText(_translate("MainWindow", ""))
        self.label_28.setText(_translate("MainWindow", "Brush\nSize"))
        self.previous.setText(_translate("MainWindow", "Previous"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.saveNnext.setText(_translate("MainWindow", "Save && Next"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.mask.setText(_translate("MainWindow", "Show Mask"))
        self.xml_enb.setText(_translate("MainWindow", "Save XML"))
        self.flagged.setText(_translate("MainWindow", "Flag it"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuProcess.setTitle(_translate("MainWindow", "Process"))
        self.menuControl.setTitle(_translate("MainWindow", "Navigate"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionOpen_Folder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update Mask"))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Shift+Return"))
        self.actionShow_Mask.setText(_translate("MainWindow", "Show Mask"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionNext.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionPrevious.setText(_translate("MainWindow", "Previous"))
        self.actionPrevious.setShortcut(_translate("MainWindow", "Ctrl+P"))

    def prob_out_command(self, hsv_values=None):
        if hsv_values is not None:
            hsv_integers = hsv_values.astype(int)
            self.prob_out.setText(f"H:{hsv_integers[0]}, S:{hsv_integers[1]}, V:{hsv_integers[2]}")

    def on_mouse_click(self, event):
        if self.prob.isChecked():
            x = event.pos().x()
            y = event.pos().y()
            hsv = cv2.resize(self.HSV, (667,500))
            sample_size = int(float(self.brush_size.value())/2)
            sampled_region = hsv[y - sample_size:y + sample_size, x - sample_size:x + sample_size]
            hsv_values = np.mean(sampled_region, axis=(0, 1))
            self.prob_out_command(hsv_values)


    def actionOpen_Folder_command(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        if temp:
            self.DIRECTORY = temp
            image_files = [f for f in os.listdir(self.DIRECTORY) if f.lower().endswith(("png", "jpg"))]
            self.IMG_LIST =  sorted([os.path.join(self.DIRECTORY, file) for file in image_files])
            if not self.IMG_LIST:
                msg = QMessageBox()
                msg.setWindowTitle("Image Not Found")
                msg.setText("No JPG/PNG file found!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Image Found")
                msg.setText(f"{len(self.IMG_LIST)} images found!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.DICT = []
                state_extract(self)
                main_list = [os.path.basename(f) for f in self.IMG_LIST]
                self.file_selector.clear()
                self.file_selector.addItems(main_list)
                self.INDEX = 0
                self.load_img()
                self.load_settings(not self.auto_load_xml.isChecked())
                self.show()
                self.load_default_xml()
    
    def file_selector_command(self):
        try:
            full_name = os.path.join(self.DIRECTORY, self.file_selector.currentText())
            self.INDEX = self.IMG_LIST.index(full_name)
            self.mask.setText(QtCore.QCoreApplication.translate("MainWindow", "Show Mask"))
            self.MASK_IS_SHOWN = False
            self.load_img()
            self.load_settings()
            self.show()
        except:
            pass
    
    def list_selector_command(self):
        print(self.LIST_DICT)
        if self.list_selector.currentText() == 'All':
            self.INDEX = 0
            self.file_selector.clear()
            self.file_selector.addItems([os.path.basename(f) for f in self.IMG_LIST])
        
        elif self.list_selector.currentText() == 'Not Processed':
            if self.IDXNP:
                self.INDEX = self.IDXNP[0]
                self.file_selector.clear()
                self.file_selector.addItems([os.path.basename(f) for f in [self.IMG_LIST[idx] for idx in self.IDXNP]])
            else:
                self.list_selector.setCurrentIndex(0)
                msg = QMessageBox()
                msg.setWindowTitle("Empty")
                msg.setText("List is Empty!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()   

        elif self.list_selector.currentText() == 'Prossed and flagged':
            if self.IDXPnF:
                self.INDEX = self.IDXPnF[0]
                self.file_selector.clear()
                self.file_selector.addItems([os.path.basename(f) for f in [self.IMG_LIST[idx] for idx in self.IDXPnF]])
            else:
                self.list_selector.setCurrentIndex(0)
                msg = QMessageBox()
                msg.setWindowTitle("Empty")
                msg.setText("List is Empty!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

        elif self.list_selector.currentText() == 'Processed':
            if self.IDXP:
                self.INDEX = self.IDXP[0]
                self.file_selector.clear()
                self.file_selector.addItems([os.path.basename(f) for f in [self.IMG_LIST[idx] for idx in self.IDXP]])
            else:
                self.list_selector.setCurrentIndex(0)
                msg = QMessageBox()
                msg.setWindowTitle("Empty")
                msg.setText("List is Empty!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
    
    def actionShow_Mask_command(self):
        self.MASK_IS_SHOWN = True
        _translate = QtCore.QCoreApplication.translate
        self.mask.setText(_translate("MainWindow", "Show Orig"))
        self.applyAll()
        self.show()
              
    def mask_command(self):
        if not self.MASK_IS_SHOWN:
            self.MASK_IS_SHOWN = True
            _translate = QtCore.QCoreApplication.translate
            self.mask.setText(_translate("MainWindow", "Show Orig"))
            self.applyAll()
            self.show()
        else:
            self.MASK_IS_SHOWN = False
            _translate = QtCore.QCoreApplication.translate
            self.mask.setText(_translate("MainWindow", "Show Mask"))
            self.show()
    
    def next_command(self):
        if self.ASKTOSAVE and self.UNSAVED:
            msg = QMessageBox()
            msg.setWindowTitle("Unsaved changes")
            msg.setText("Unsaved Changes will be discarded\nSave before proceed?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(msg.Save|msg.Ignore)
            msg.setDefaultButton(msg.Save)
            chk = QtWidgets.QCheckBox()
            chk.setText("Do not ask me again")
            msg.setCheckBox(chk)
            result = msg.exec_()
            if result == msg.Save:
                self.save_command()
            if chk.isChecked():
                self.ASKTOSAVE = False
        try:
            if self.list_selector.currentIndex() == 0: 
                self.INDEX = self.DICT[self.INDEX]['membership']['gNext']
            else:
                self.INDEX = self.DICT[self.INDEX]['membership']['Next']
            self.load_img()
            self.load_settings(not self.auto_load_xml.isChecked())
            self.show()
            self.file_selector.setCurrentText(os.path.basename(self.IMG_LIST[self.INDEX]))

        except IndexError:
            msg = QMessageBox()
            msg.setWindowTitle("Image Not Found")
            msg.setText("No JPG/PNG file found!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    
    def load_xml_command(self):
        xml_file = self.DICT[self.INDEX]['xml_file']
        try:
            with xml_parse_value(xml_file) as parser:
                self.flagged.setChecked(True if parser.get('flagged')=='True' else False)
                
                self.White.setChecked(True if parser.get('filters/White/active')=='True' else False)
                if self.White.isChecked():
                    self.mask_val_w.setText(parser.get('filters/White/label'))
                    self.sat_min_w.setText(parser.get('filters/White/sat/min'))
                    self.sat_max_w.setText(parser.get('filters/White/sat/max'))
                    self.hue_min_w.setText(parser.get('filters/White/hue/min'))
                    self.hue_max_w.setText(parser.get('filters/White/hue/max'))
                    self.val_min_w.setText(parser.get('filters/White/val/min'))
                    self.val_max_w.setText(parser.get('filters/White/val/max'))
                    self.smooth_size_w.setCurrentText(parser.get('filters/White/smooth/size'))
                    self.threshold_w.setValue(int(parser.get('filters/White/smooth/thresh')))

                self.Green.setChecked(True if parser.get('filters/Green/active')=='True' else False)
                if self.Green.isChecked():
                    self.mask_val_g.setText(parser.get('filters/Green/label'))
                    self.sat_min_g.setText(parser.get('filters/Green/sat/min'))
                    self.sat_max_g.setText(parser.get('filters/Green/sat/max'))
                    self.hue_min_g.setText(parser.get('filters/Green/hue/min'))
                    self.hue_max_g.setText(parser.get('filters/Green/hue/max'))
                    self.val_min_g.setText(parser.get('filters/Green/val/min'))
                    self.val_max_g.setText(parser.get('filters/Green/val/max'))
                    self.smooth_size_g.setCurrentText(parser.get('filters/Green/smooth/size'))
                    self.threshold_g.setValue(int(parser.get('filters/Green/smooth/thresh')))

                self.Yellow.setChecked(True if parser.get('filters/Yellow/active')=='True' else False)
                if self.Yellow.isChecked():
                    self.mask_val_y.setText(parser.get('filters/Yellow/label'))
                    self.sat_min_y.setText(parser.get('filters/Yellow/sat/min'))
                    self.sat_max_y.setText(parser.get('filters/Yellow/sat/max'))
                    self.hue_min_y.setText(parser.get('filters/Yellow/hue/min'))
                    self.hue_max_y.setText(parser.get('filters/Yellow/hue/max'))
                    self.val_min_y.setText(parser.get('filters/Yellow/val/min'))
                    self.val_max_y.setText(parser.get('filters/Yellow/val/max'))
                    self.smooth_size_y.setCurrentText(parser.get('filters/Yellow/smooth/size'))
                    self.threshold_y.setValue(int(parser.get('filters/Yellow/smooth/thresh')))

                self.sky_filter.setChecked(True if parser.get('filters/Sky/enable')=='True' else False)
                if self.sky_filter.isChecked():
                    self.sky_val.setValue(int(parser.get('filters/Sky/value')))

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Loading Failed")
            msg.setText("XML format is not compatible")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.load_xml.setEnabled(False)
    
    def load_default_xml(self):
        msg = QMessageBox()
        msg.setWindowTitle("Loat Preset")
        msg.setText("Would you like to load preset?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        result = msg.exec_()

        if result == QMessageBox.Yes:
            msg = QMessageBox()
            msg.setWindowTitle("Loat Preset")
            msg.setText("Which preset to load?")
            msg.setIcon(QMessageBox.Question)
            default_button = QtWidgets.QPushButton("Default XML")
            msg.addButton(default_button, QMessageBox.AcceptRole)
            select_button = QtWidgets.QPushButton("Select XML")
            msg.addButton(select_button, QMessageBox.AcceptRole)
            msg.setDefaultButton(default_button)
            msg.exec_()
            if msg.clickedButton() == default_button:
                default = True
            else: 
                default = False
        else:
            return

        if not default:
            qfd = QtWidgets.QFileDialog()
            path = self.DIRECTORY
            filter = "xml(*.xml)"
            title = "Select XML"
            xml_file, _ = QtWidgets.QFileDialog.getOpenFileName(qfd, title, path, filter)
            if not xml_file:
                msg = QMessageBox()
                msg.setWindowTitle("Loading Failed")
                msg.setText("No file selected")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
        else:
            xml_file = 'default_parameters.xml'
        try:
            with xml_parse_value(xml_file) as parser:                
                self.White.setChecked(True if parser.get('filters/White/active')=='True' else False)
                if self.White.isChecked():
                    self.mask_val_w.setText(parser.get('filters/White/label'))
                    self.sat_min_w.setText(parser.get('filters/White/sat/min'))
                    self.sat_max_w.setText(parser.get('filters/White/sat/max'))
                    self.hue_min_w.setText(parser.get('filters/White/hue/min'))
                    self.hue_max_w.setText(parser.get('filters/White/hue/max'))
                    self.val_min_w.setText(parser.get('filters/White/val/min'))
                    self.val_max_w.setText(parser.get('filters/White/val/max'))
                    self.smooth_size_w.setCurrentText(parser.get('filters/White/smooth/size'))
                    self.threshold_w.setValue(int(parser.get('filters/White/smooth/thresh')))

                self.Green.setChecked(True if parser.get('filters/Green/active')=='True' else False)
                if self.Green.isChecked():
                    self.mask_val_g.setText(parser.get('filters/Green/label'))
                    self.sat_min_g.setText(parser.get('filters/Green/sat/min'))
                    self.sat_max_g.setText(parser.get('filters/Green/sat/max'))
                    self.hue_min_g.setText(parser.get('filters/Green/hue/min'))
                    self.hue_max_g.setText(parser.get('filters/Green/hue/max'))
                    self.val_min_g.setText(parser.get('filters/Green/val/min'))
                    self.val_max_g.setText(parser.get('filters/Green/val/max'))
                    self.smooth_size_g.setCurrentText(parser.get('filters/Green/smooth/size'))
                    self.threshold_g.setValue(int(parser.get('filters/Green/smooth/thresh')))

                self.Yellow.setChecked(True if parser.get('filters/Yellow/active')=='True' else False)
                if self.Yellow.isChecked():
                    self.mask_val_y.setText(parser.get('filters/Yellow/label'))
                    self.sat_min_y.setText(parser.get('filters/Yellow/sat/min'))
                    self.sat_max_y.setText(parser.get('filters/Yellow/sat/max'))
                    self.hue_min_y.setText(parser.get('filters/Yellow/hue/min'))
                    self.hue_max_y.setText(parser.get('filters/Yellow/hue/max'))
                    self.val_min_y.setText(parser.get('filters/Yellow/val/min'))
                    self.val_max_y.setText(parser.get('filters/Yellow/val/max'))
                    self.smooth_size_y.setCurrentText(parser.get('filters/Yellow/smooth/size'))
                    self.threshold_y.setValue(int(parser.get('filters/Yellow/smooth/thresh')))

                self.sky_filter.setChecked(True if parser.get('filters/Sky/enable')=='True' else False)
                if self.sky_filter.isChecked():
                    self.sky_val.setValue(int(parser.get('filters/Sky/value')))
        except FileNotFoundError:
            msg = QMessageBox()
            msg.setWindowTitle("Loading Failed")
            msg.setText("XML not found")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Loading Failed")
            msg.setText("XML format is not compatible")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    
    def previous_command(self):
        if self.ASKTOSAVE and self.UNSAVED:
            msg = QMessageBox()
            msg.setWindowTitle("Unsaved changes")
            msg.setText("Unsaved Changes will be discarded\nSave before proceed?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(msg.Save|msg.Ignore)
            msg.setDefaultButton(msg.Save)
            chk = QtWidgets.QCheckBox()
            chk.setText("Do not ask me again")
            msg.setCheckBox(chk)
            result = msg.exec_()
            if result == msg.Save:
                self.save_command()
            if chk.isChecked():
                self.ASKTOSAVE = False
        try:
            if self.list_selector.currentIndex() == 0: 
                self.INDEX = self.DICT[self.INDEX]['membership']['gPrevious']
            else:
                self.INDEX = self.DICT[self.INDEX]['membership']['Previous']
            self.load_img()
            self.load_settings(not self.auto_load_xml.isChecked())
            self.show()
            self.file_selector.setCurrentText(os.path.basename(self.IMG_LIST[self.INDEX]))
        except IndexError:
            msg = QMessageBox()
            msg.setWindowTitle("Image Not Found")
            msg.setText("No JPG/PNG file found!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    
    def save_command(self):
        self.applyAll()
        dest_directory = os.path.join(self.DIRECTORY, 'labels')
        filename = os.path.basename(self.IMG_LIST[self.INDEX])
        mask_name = 'mask_' + os.path.splitext(filename)[0] + '.png' 
        if not os.path.exists(dest_directory):
            os.makedirs(dest_directory)
        
        gray_mask = cv2.cvtColor(self.MASK, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(os.path.join(dest_directory, mask_name), gray_mask)
        self.DICT[self.INDEX]['mask_file'] = os.path.join(dest_directory, mask_name)
        if self.xml_enb.isChecked():
            report = ET.Element("report")
            eFileName = ET.SubElement(report, "file")
            eFileName.text = filename
            eMaskName = ET.SubElement(report, "mask")
            eMaskName.text = mask_name
            eMaskName = ET.SubElement(report, "flagged")
            eMaskName.text = str(self.flagged.isChecked())
            eFilters = ET.SubElement(report, "filters")
            eSky = ET.SubElement(eFilters, 'Sky')
            eSkyVal = ET.SubElement(eSky, "enable"); eSkyVal.text =  str(self.sky_filter.isChecked())
            if self.sky_filter.isChecked():
                eSkyVal = ET.SubElement(eSky, "value"); eSkyVal.text =  str(self.sky_val.value())
            else:
                eSkyVal = ET.SubElement(eSky, "value"); eSkyVal.text =  ""

            efilter = ET.SubElement(eFilters, "White")
            eActive = ET.SubElement(efilter, 'active')
            eActive.text = str(self.White.isChecked())
            if self.White.isChecked():
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = self.mask_val_w.text()
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = self.hue_min_w.text()
                epars   = ET.SubElement(eHue, 'max'); epars.text = self.hue_max_w.text()
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = self.sat_min_w.text()
                epars   = ET.SubElement(eSat, 'max'); epars.text = self.sat_max_w.text()
                eVal    = ET.SubElement(efilter, 'val')             
                epars   = ET.SubElement(eVal, 'min'); epars.text = self.val_min_w.text()
                epars   = ET.SubElement(eVal, 'max'); epars.text = self.val_max_w.text()
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = str(self.smooth_size_w.currentText())
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = str(self.threshold_w.value())
            else:
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = ""
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = ""
                epars   = ET.SubElement(eHue, 'max'); epars.text = ""
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = ""
                epars   = ET.SubElement(eSat, 'max'); epars.text = ""
                eVal    = ET.SubElement(efilter, 'val')              
                epars   = ET.SubElement(eVal, 'min'); epars.text = ""
                epars   = ET.SubElement(eVal, 'max'); epars.text = ""
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = ""
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = ""

            efilter = ET.SubElement(eFilters, "Green")
            eActive = ET.SubElement(efilter, 'active')
            eActive.text = str(self.Green.isChecked())
            if self.Green.isChecked():
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = self.mask_val_g.text()
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = self.hue_min_g.text()
                epars   = ET.SubElement(eHue, 'max'); epars.text = self.hue_max_g.text()
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = self.sat_min_g.text()
                epars   = ET.SubElement(eSat, 'max'); epars.text = self.sat_max_g.text()
                eVal    = ET.SubElement(efilter, 'val')             
                epars   = ET.SubElement(eVal, 'min'); epars.text = self.val_min_g.text()
                epars   = ET.SubElement(eVal, 'max'); epars.text = self.val_max_g.text()
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = str(self.smooth_size_g.currentText())
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = str(self.threshold_g.value())
            else:
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = ""
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = ""
                epars   = ET.SubElement(eHue, 'max'); epars.text = ""
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = ""
                epars   = ET.SubElement(eSat, 'max'); epars.text = ""
                eVal    = ET.SubElement(efilter, 'val')              
                epars   = ET.SubElement(eVal, 'min'); epars.text = ""
                epars   = ET.SubElement(eVal, 'max'); epars.text = ""
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = ""
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = ""

            efilter = ET.SubElement(eFilters, "Yellow")
            eActive = ET.SubElement(efilter, 'active')
            eActive.text = str(self.Yellow.isChecked())
            if self.Yellow.isChecked():
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = self.mask_val_y.text()
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = self.hue_min_y.text()
                epars   = ET.SubElement(eHue, 'max'); epars.text = self.hue_max_y.text()
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = self.sat_min_y.text()
                epars   = ET.SubElement(eSat, 'max'); epars.text = self.sat_max_y.text()
                eVal    = ET.SubElement(efilter, 'val')             
                epars   = ET.SubElement(eVal, 'min'); epars.text = self.val_min_y.text()
                epars   = ET.SubElement(eVal, 'max'); epars.text = self.val_max_y.text()
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = str(self.smooth_size_y.currentText())
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = str(self.threshold_y.value())
            else:
                eLabel  = ET.SubElement(efilter, 'label'); eLabel.text = ""
                eHue    = ET.SubElement(efilter, 'hue')              
                epars   = ET.SubElement(eHue, 'min'); epars.text = ""
                epars   = ET.SubElement(eHue, 'max'); epars.text = ""
                eSat    = ET.SubElement(efilter, 'sat')              
                epars   = ET.SubElement(eSat, 'min'); epars.text = ""
                epars   = ET.SubElement(eSat, 'max'); epars.text = ""
                eVal    = ET.SubElement(efilter, 'val')              
                epars   = ET.SubElement(eVal, 'min'); epars.text = ""
                epars   = ET.SubElement(eVal, 'max'); epars.text = ""
                eFil    = ET.SubElement(efilter, 'smooth')
                epars   = ET.SubElement(eFil, 'size'); epars.text = ""
                epars   = ET.SubElement(eFil, 'thresh'); epars.text = ""

            xml_string = ET.tostring(report, encoding="utf-8").decode()
            xml_pretty_string = minidom.parseString(xml_string).toprettyxml(indent="    ")
            xml_filename = os.path.join(dest_directory, os.path.splitext(filename)[0] + ".xml")
            with open(xml_filename, "w", encoding="utf-8") as file:
                file.write(xml_pretty_string)
            self.DICT[self.INDEX]['xml_file'] = xml_filename
            self.load_settings()
        
        if self.flagged.isChecked():
            move(self, self.DICT[self.INDEX], 'PnF')
        else:
            move(self, self.DICT[self.INDEX], 'P')
        self.UNSAVED = False

    def saveNnext_command(self):
        self.save_command()
        self.next_command()

    def show(self):
        if self.INDEX != -1 and not self.MASK_IS_SHOWN:
            self.Img.setPixmap(display_prep(self.IMG))

        elif self.INDEX != -1 and self.MASK_IS_SHOWN:
            self.Img.setPixmap(display_prep(self.MASK))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Bad Argument")
            msg.setText("No Image to Dsiplay!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def load_settings(self, image_only=True):
        self.sky_val.setMaximum(self.IMG.shape[0])
        if self.DICT[self.INDEX]['xml_file']:
            self.load_xml.setEnabled(True)
            if not image_only:
                self.load_xml_command()
        else:
            self.load_xml.setEnabled(False)
        

    def load_img(self):
        self.MASK_IS_SHOWN = False
        img = cv2.imread(self.IMG_LIST[self.INDEX])
        self.IMG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

    def sky_val_read(self):
        self.sky_val_d.setText(f"{self.sky_val.value()}")
    
    def threshold_g_read(self):
        self.threshold_g_d.setText(f"{self.threshold_g.value()}")

    def threshold_w_read(self):
        self.threshold_w_d.setText(f"{self.threshold_w.value()}")

    def threshold_y_read(self):
        self.threshold_y_d.setText(f"{self.threshold_y.value()}")

    def check_input_val(self, obj):
        try:
            if int(obj.text()) < 0 or int(obj.text())>255:
                msg = QMessageBox()
                msg.setWindowTitle("Bad Argument")
                msg.setText("Please choose a number between 0 and 255!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        except:
            pass

    def applyWhite(self):
        if self.White.isChecked():
            hsv_min = np.array([int(self.hue_min_w.text()), int(self.sat_min_w.text()), int(self.val_min_w.text())])
            hsv_max = np.array([int(self.hue_max_w.text()), int(self.sat_max_w.text()), int(self.val_max_w.text())])
            tmp = cv2.inRange(self.HSV, hsv_min, hsv_max)
            kernel = np.ones((int(self.smooth_size_w.currentText()), int(self.smooth_size_w.currentText())))
            tmp = cv2.filter2D(tmp,-1,kernel)
            roi = tmp > int(self.threshold_w.value())
            self.MASK[roi] = int(self.mask_val_w.text())
    
    def applyGreen(self):
        if self.Green.isChecked():
            hsv_min = np.array([int(self.hue_min_g.text()), int(self.sat_min_g.text()), int(self.val_min_g.text())])
            hsv_max = np.array([int(self.hue_max_g.text()), int(self.sat_max_g.text()), int(self.val_max_g.text())])
            tmp = cv2.inRange(self.HSV, hsv_min, hsv_max)
            kernel = np.ones((int(self.smooth_size_g.currentText()), int(self.smooth_size_g.currentText())))
            tmp = cv2.filter2D(tmp,-1,kernel)
            roi = tmp > int(self.threshold_g.value())
            self.MASK[roi] = int(self.mask_val_g.text())
    
    def applyYellow(self):
        if self.Yellow.isChecked():
            hsv_min = np.array([int(self.hue_min_y.text()), int(self.sat_min_y.text()), int(self.val_min_y.text())])
            hsv_max = np.array([int(self.hue_max_y.text()), int(self.sat_max_y.text()), int(self.val_max_y.text())])
            tmp = cv2.inRange(self.HSV, hsv_min, hsv_max)
            kernel = np.ones((int(self.smooth_size_y.currentText()), int(self.smooth_size_y.currentText())))
            tmp = cv2.filter2D(tmp,-1,kernel)
            roi = tmp > int(self.threshold_y.value())
            self.MASK[roi] = int(self.mask_val_y.text())
    
    def applySkyFilter(self):
        if self.sky_filter.isChecked():
            self.MASK[0:int(self.sky_val.value()),:,:] = 0
    
    def applyAll(self):
        self.UNSAVED = True
        if self.INDEX != -1:
            self.MASK = np.zeros_like(self.IMG, np.uint8)
            self.applyWhite()
            self.applyGreen()
            self.applyYellow()
            self.applySkyFilter()
            self.show()
    
    def beforeClose_command(self):
        if self.UNSAVED:
            msg = QMessageBox()
            msg.setWindowTitle("Unsaved changes")
            msg.setText("Unsaved Changes will be discarded\nSave before Exit?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(msg.Save|msg.Close)
            msg.setDefaultButton(msg.Save)
            result = msg.exec_()
            if result == msg.Save:
                self.save_command()
        
        if self.DICT:
            msg = QMessageBox()
            msg.setWindowTitle("Exit")
            msg.setText("Would you like to save report before closing?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(msg.Save|msg.Close)
            msg.setDefaultButton(msg.Save)
            result = msg.exec_()
            if result == msg.Save:
                json_data = json.dumps(self.DICT, indent=4)
                with open(os.path.join(self.DIRECTORY, 'labels/report.json'), 'w') as f:
                    f.write(json_data)
    
    def showHelpDialog(self):
        help_dialog = HelpDialog()
        help_dialog.exec_()

    def showAboutDialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Help')
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        try:
            with open('README.md', 'r', encoding='utf-8') as file:
                readme_content = file.read()
        except FileNotFoundError:
            readme_content = 'README.md not found.'
        help_label = QtWidgets.QLabel(readme_content)
        ok_button = QtWidgets.QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(help_label)
        layout.addWidget(ok_button)

        self.setLayout(layout)

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('About')
        self.setGeometry(100, 100, 386, 292)

        self.initUI()

    def initUI(self):
        label = QtWidgets.QLabel()
        label.setGeometry(QtCore.QRect(70, 20, 251, 61))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("logo.jpg"))
        label.setObjectName("label")
        about_label = QtWidgets.QLabel("Image Segmantation Tool\n"
                                        "Version: 1.0.0\n"
                                        "\n"
                                        "Description:\n"
                                        "HSV filter-based image labeling tool.\n"
                                        "\n"
                                        "Author: Mojtaba Bahramgiri\n"
                                        "Copyright: © 2024 MTU-APSRC\n"
                                        "\n"
                                        "Follow us at https://www.linkedin.com/company/apslabs\n"
                                        "\n"
                                        "Thank you for using Image Segmantation Tool!")
        ok_button = QtWidgets.QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(about_label)
        layout.addWidget(ok_button)

        self.setLayout(layout)

class xml_parse_value:
    def __init__(self, file):
        tree = ET.parse(file)
        self.root = tree.getroot()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
        
    def get(self, element_path):
        current_element = self.root
        tags = element_path.split('/')
        for tag in tags:
            current_element = current_element.find(tag)
        if current_element is not None:
            return current_element.text
        else:
            return False
        
def display_prep(image):
    img = image.copy()
    img = cv2.resize(img, (800,600))
    height, width, channel = img.shape
    bytes_per_line = 3 * width
    q_image = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(q_image)
    return pixmap

def state_extract(obj):
    label_directory = os.path.join(obj.DIRECTORY, 'labels')
    if os.path.exists(label_directory):
        xml_list = [os.path.splitext(f)[0] for f in os.listdir(label_directory) if f.lower().endswith(('xml'))]
        mask_list = [os.path.splitext(f)[0] for f in os.listdir(label_directory) if f.lower().endswith(('png'))]
    image_list = [os.path.splitext(os.path.basename(f))[0] for f in obj.IMG_LIST]
    ext_list = [os.path.splitext(os.path.basename(f))[1] for f in obj.IMG_LIST]
    index = 0
    membership = {'lname':'NP', 'Next':-1, 'Previous': -1, 'gNext': -1, 'gPrevious': -1} # P/NP/PnF
    for img in image_list:
        entry = {'index':index, 'img_file':'', 'mask_file':None, 'xml_file':None,
                  'flagged': False, 'membership': copy.deepcopy(membership)}
        entry['img_file'] = os.path.join(obj.DIRECTORY, img + ext_list[index])
        index += 1
        if os.path.exists(label_directory) and img in xml_list:
            entry['xml_file'] = os.path.join(label_directory, img + '.xml')
            with xml_parse_value(entry['xml_file']) as f:
                entry['flagged'] = True if f.get('flagged') == 'True' else False
        if os.path.exists(label_directory) and 'mask_' + img in mask_list:
            entry['mask_file'] = os.path.join(label_directory, 'mask_' + img + '.png')
        obj.DICT.append(entry)

    obj.IDXNP.clear()
    obj.IDXPnF.clear()
    obj.IDXP.clear()
    for item in obj.DICT:
        if item['mask_file']:
            if item['flagged']:
                item['membership']['lname'] = 'PnF'
                obj.IDXPnF.append(item['index'])
            else:
                item['membership']['lname'] = 'P'
                obj.IDXP.append(item['index'])
        else:
            item['membership']['lname'] = 'NP'
            obj.IDXNP.append(item['index'])
    major_len = len(obj.IMG_LIST)
    for lst in obj.LIST_DICT.keys():
        minor_len = len(obj.LIST_DICT[lst])
        for idx in range(minor_len):
            item_idx = obj.LIST_DICT[lst][idx]
            if obj.DICT[item_idx]['index'] != item_idx or obj.DICT[item_idx]['membership']['lname'] != lst:
                print('Indexing Error')
                return False
            obj.DICT[item_idx]['membership']['gNext'] = (item_idx + 1) % major_len 
            obj.DICT[item_idx]['membership']['gPrevious'] = (item_idx - 1) % major_len 
            obj.DICT[item_idx]['membership']['Next'] = obj.LIST_DICT[lst][(idx + 1) % minor_len] 
            obj.DICT[item_idx]['membership']['Previous'] = obj.LIST_DICT[lst][(idx - 1) % minor_len]

def move(master, item, dest):
    if item['membership']['lname'] != dest:
        master.LIST_DICT[item['membership']['lname']].remove(item['index'])
        master.DICT[item['membership']['Previous']]['membership']['Next'] = item['membership']['Next']
        master.DICT[item['membership']['Next']]['membership']['Previous'] = item['membership']['Previous']
        item['membership']['lname'] = dest
        master.LIST_DICT[dest].append(item['index'])
        master.LIST_DICT[dest].sort()
        insert_idx = master.LIST_DICT[dest].index(item['index'])
        next_item = master.LIST_DICT[dest][(insert_idx+1)%len(master.LIST_DICT[dest])]
        prev_item = master.LIST_DICT[dest][(insert_idx-1)%len(master.LIST_DICT[dest])]
        master.DICT[next_item]['membership']['Previous'] = item['index']
        master.DICT[prev_item]['membership']['Next'] = item['index']
        item['membership']['Previous'] = prev_item
        item['membership']['Next'] = next_item   

         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
