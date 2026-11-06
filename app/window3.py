# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form2_responsiveZUmmXf.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_form1(object):
    def setupUi(self, form1):
        if not form1.objectName():
            form1.setObjectName(u"form1")
        form1.resize(1170, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form1.sizePolicy().hasHeightForWidth())
        form1.setSizePolicy(sizePolicy)
        form1.setMinimumSize(QSize(1170, 30))
        form1.setMaximumSize(QSize(16777215, 16777215))
        form1.setStyleSheet(u"QMainWindow {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(196, 220, 255);\n"
"    color: #f8fafc;\n"
"    \n"
"}")
        form1.setDocumentMode(False)
        self.actionINR = QAction(form1)
        self.actionINR.setObjectName(u"actionINR")
        self.actionOpen = QAction(form1)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(form1)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(form1)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(form1)
        self.actionExit.setObjectName(u"actionExit")
        self.action_screenshot = QAction(form1)
        self.action_screenshot.setObjectName(u"action_screenshot")
        self.actionTable_Edit = QAction(form1)
        self.actionTable_Edit.setObjectName(u"actionTable_Edit")
        self.actionAs_CSV_Excel = QAction(form1)
        self.actionAs_CSV_Excel.setObjectName(u"actionAs_CSV_Excel")
        self.actionOpen_Directories = QAction(form1)
        self.actionOpen_Directories.setObjectName(u"actionOpen_Directories")
        self.actionLight = QAction(form1)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDakr = QAction(form1)
        self.actionDakr.setObjectName(u"actionDakr")
        self.actionUSD = QAction(form1)
        self.actionUSD.setObjectName(u"actionUSD")
        self.actionClear_Data = QAction(form1)
        self.actionClear_Data.setObjectName(u"actionClear_Data")
        self.actionRefresh = QAction(form1)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionInfo = QAction(form1)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionArrange = QAction(form1)
        self.actionArrange.setObjectName(u"actionArrange")
        self.centralwidget = QWidget(form1)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_50 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(6, 0, 0, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 25))
        self.label_13.setMaximumSize(QSize(120, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.lineEdit_income0 = QLineEdit(self.centralwidget)
        self.lineEdit_income0.setObjectName(u"lineEdit_income0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_income0.sizePolicy().hasHeightForWidth())
        self.lineEdit_income0.setSizePolicy(sizePolicy1)
        self.lineEdit_income0.setMinimumSize(QSize(50, 26))
        self.lineEdit_income0.setMaximumSize(QSize(1920, 26))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.lineEdit_income0.setFont(font1)
        self.lineEdit_income0.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_income0.setStyleSheet(u"#lineEdit_income0 {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_income0:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_income0:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_income0.setMaxLength(1000)
        self.lineEdit_income0.setFrame(False)
        self.lineEdit_income0.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_income0.setCursorPosition(1)
        self.lineEdit_income0.setDragEnabled(True)
        self.lineEdit_income0.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_income0.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_income0)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(114, 25))
        self.label_14.setMaximumSize(QSize(114, 25))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.lineEdit_income = QLineEdit(self.centralwidget)
        self.lineEdit_income.setObjectName(u"lineEdit_income")
        sizePolicy1.setHeightForWidth(self.lineEdit_income.sizePolicy().hasHeightForWidth())
        self.lineEdit_income.setSizePolicy(sizePolicy1)
        self.lineEdit_income.setMinimumSize(QSize(50, 26))
        self.lineEdit_income.setMaximumSize(QSize(1920, 26))
        self.lineEdit_income.setFont(font1)
        self.lineEdit_income.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_income.setStyleSheet(u"#lineEdit_income {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_income:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_income:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_income.setMaxLength(1000)
        self.lineEdit_income.setFrame(False)
        self.lineEdit_income.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_income.setCursorPosition(1)
        self.lineEdit_income.setDragEnabled(True)
        self.lineEdit_income.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_income.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_income)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(181, 26))
        self.comboBox_4.setMaximumSize(QSize(16777215, 26))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.comboBox_4.setFont(font2)
        self.comboBox_4.setStyleSheet(u"/* ==========================\n"
"   QComboBox - Professional Soft Blue Theme\n"
"   ========================== */\n"
"\n"
"QComboBox {\n"
"    background-color: #f4f6fb;\n"
"    color: #1f2937;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QComboBox:hover {\n"
"    background-color: #f0f4ff;\n"
"    border: 1px solid #5e85d7;\n"
"}\n"
"\n"
"/* Focus (active) effect */\n"
"QComboBox:focus {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #5e85d7;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;\n"
"    color: #7a7a7a;\n"
"    border: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"/* Drop-down arrow area */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px "
                        "solid #a7b4d0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #e8ecf9, stop:1 #cfd8f3);\n"
"}\n"
"\n"
"/* Arrow icon (uses system default if custom not available) */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down_arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* === Drop-down List Styling === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #f9faff;\n"
"    color: #1f2937;\n"
"    border: 1px solid #5e85d7;\n"
"    border-radius: 6px;\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: #ffffff;\n"
"    outline: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Hover over individual items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #dbe6ff; /* Soft blue hover */\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"/* Selected item (click or keyboard highlight) */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    bac"
                        "kground-color: #5e85d7;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.comboBox_4.setFrame(False)

        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(111, 26))
        self.comboBox_3.setMaximumSize(QSize(16777215, 26))
        self.comboBox_3.setFont(font2)
        self.comboBox_3.setStyleSheet(u"/* ==========================\n"
"   QComboBox - Professional Soft Blue Theme\n"
"   ========================== */\n"
"\n"
"QComboBox {\n"
"    background-color: #f4f6fb;\n"
"    color: #1f2937;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QComboBox:hover {\n"
"    background-color: #f0f4ff;\n"
"    border: 1px solid #5e85d7;\n"
"}\n"
"\n"
"/* Focus (active) effect */\n"
"QComboBox:focus {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #5e85d7;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;\n"
"    color: #7a7a7a;\n"
"    border: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"/* Drop-down arrow area */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px "
                        "solid #a7b4d0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #e8ecf9, stop:1 #cfd8f3);\n"
"}\n"
"\n"
"/* Arrow icon (uses system default if custom not available) */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down_arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* === Drop-down List Styling === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #f9faff;\n"
"    color: #1f2937;\n"
"    border: 1px solid #5e85d7;\n"
"    border-radius: 6px;\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: #ffffff;\n"
"    outline: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Hover over individual items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #dbe6ff; /* Soft blue hover */\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"/* Selected item (click or keyboard highlight) */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    bac"
                        "kground-color: #5e85d7;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.comboBox_3.setFrame(False)

        self.horizontalLayout_2.addWidget(self.comboBox_3)

        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMinimumSize(QSize(151, 26))
        self.label_date.setMaximumSize(QSize(16777215, 26))
        self.label_date.setFont(font)
        self.label_date.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")

        self.horizontalLayout_2.addWidget(self.label_date)

        self.label_calc = QLabel(self.centralwidget)
        self.label_calc.setObjectName(u"label_calc")
        self.label_calc.setMinimumSize(QSize(261, 25))
        self.label_calc.setMaximumSize(QSize(16777215, 25))
        self.label_calc.setFont(font)
        self.label_calc.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")
        self.label_calc.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_calc)

        self.lineEdit_calc = QLineEdit(self.centralwidget)
        self.lineEdit_calc.setObjectName(u"lineEdit_calc")
        sizePolicy1.setHeightForWidth(self.lineEdit_calc.sizePolicy().hasHeightForWidth())
        self.lineEdit_calc.setSizePolicy(sizePolicy1)
        self.lineEdit_calc.setMinimumSize(QSize(151, 25))
        self.lineEdit_calc.setMaximumSize(QSize(1920, 25))
        self.lineEdit_calc.setFont(font1)
        self.lineEdit_calc.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_calc.setStyleSheet(u"#lineEdit_calc {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_calc:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_calc:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_calc.setMaxLength(1000)
        self.lineEdit_calc.setFrame(False)
        self.lineEdit_calc.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_calc.setCursorPosition(0)
        self.lineEdit_calc.setDragEnabled(True)
        self.lineEdit_calc.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_calc.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_calc)


        self.verticalLayout_22.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, -1, -1, 6)
        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setMinimumSize(QSize(60, 600))
        font3 = QFont()
        font3.setPointSize(12)
        self.tabWidget_3.setFont(font3)
        self.tabWidget_3.setStyleSheet(u"/* Main Tab Widget */\n"
"#tabWidget_3::pane {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #edf2f7, stop:1 #dce4f2);\n"
"   \n"
"   \n"
"    \n"
"}\n"
"\n"
"/* Tabs - neutral background, rounded, soft hover */\n"
"#tabWidget_3 QTabBar::tab {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7287ca, stop:1 #5f71a8);\n"
"    color: white;\n"
"    padding: 4px 10px;\n"
"    margin-right: 6px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    \n"
"    min-width: 100px;\n"
"    border: 1px solid #7287ca;\n"
"    border-bottom: none;\n"
"\n"
"\n"
"   \n"
"}\n"
"\n"
"/* Selected tab - highlighted cleanly with shadow and bolder color */\n"
"#tabWidget_3 QTabBar::tab:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c8ff, stop:1 #94b2e3);\n"
"    color: #445178;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;"
                        ";\n"
"    font-weight: 600;\n"
"\n"
"   \n"
"}\n"
"\n"
"/* Hover (for non-selected tabs) - subtle lightening */\n"
"#tabWidget_3 QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7c9bf1, stop:1 #7c9bf1);\n"
"    color: white;\n"
"    border: 1px solid #7c9bf1;\n"
"}\n"
"\n"
"/* TabBar base */\n"
"#tabWidget_3 QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"  \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget_3.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_3.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_3.setDocumentMode(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_36 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_5 = QWidget(self.tab_7)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(800, 100))
        self.widget_5.setStyleSheet(u"\n"
"#widget_5 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #94b2e3;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_5:hover {\n"
"        background-color: #81a6e1;\n"
"    border: 1px solid #4e8df5;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_5:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"   border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
""
                        "    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_expense_record = QLabel(self.widget_5)
        self.label_expense_record.setObjectName(u"label_expense_record")
        self.label_expense_record.setMaximumSize(QSize(87, 16777215))
        self.label_expense_record.setFont(font2)
        self.label_expense_record.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_3.addWidget(self.label_expense_record)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.toolButton_del_row = QToolButton(self.widget_5)
        self.toolButton_del_row.setObjectName(u"toolButton_del_row")
        self.toolButton_del_row.setMinimumSize(QSize(60, 0))
        self.toolButton_del_row.setMaximumSize(QSize(61, 16777215))
        self.toolButton_del_row.setFont(font3)
        self.toolButton_del_row.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_3.addWidget(self.toolButton_del_row)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget_1 = QTableWidget(self.widget_5)
        if (self.tableWidget_1.columnCount() < 7):
            self.tableWidget_1.setColumnCount(7)
        font4 = QFont()
        font4.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget_1.rowCount() < 12):
            self.tableWidget_1.setRowCount(12)
        self.tableWidget_1.setObjectName(u"tableWidget_1")
        self.tableWidget_1.setFont(font2)
        self.tableWidget_1.setStyleSheet(u"/* ===== Table Widget Style (Light Blue Theme) ===== */\n"
"#tableWidget_1 {\n"
"    background-color: #f5f9ff; /* soft blue-white background */\n"
"    alternate-background-color: #e8f1ff;\n"
"    gridline-color: #b7c9f0;\n"
"  \n"
"    \n"
"    font: 11pt \"Segoe UI\";\n"
"    color: #2f3e55;\n"
"    selection-background-color: #6ea6f8;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ===== Header Styling ===== */\n"
"#tableWidget_1 QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #cbd9f6, stop:1 #a9c4f2);\n"
"    color: #1d2b4d;\n"
"    font-weight: 600;\n"
"    font-size: 11pt;\n"
"    border: 1px solid #9bb8ef;\n"
"    \n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_1 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* ===== Row Hover Highlight ===== */\n"
"#tableWidget_1::item:hover {\n"
"    background-color: #c8ddff;\n"
"    color: #12294d;\n"
"}\n"
"\n"
"/* ===== Selected Cell ===== */\n"
"#tableWidget_1::item:selected {\n"
"    background-color: #7aa3e6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ===== Vertical Scrollbar ===== */\n"
"#tableWidget_1 QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::add-line:vertical,\n"
"#tableWidget_1 QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* ===== Horizontal Scrollbar ===== */\n"
"#tableWidget_1 QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    height: 10px;\n"
"    margin:"
                        " 0 2px 0 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::handle:horizontal {\n"
"    background: #90b4ff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::handle:horizontal:hover {\n"
"    background: #6e9fff;\n"
"}\n"
"\n"
"#tableWidget_1 QScrollBar::add-line:horizontal,\n"
"#tableWidget_1 QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"/* This styles the empty area (the viewport) */\n"
"#tableWidget_1 QTableCornerButton::section,\n"
"#tableWidget_1 QTableView QTableCornerButton::section,\n"
"#tableWidget_1 QWidget {\n"
"    background-color: #94b2e3; /* soft blue empty area */\n"
"}\n"
"\n"
"/* The actual viewport region where no cells exist */\n"
"#tableWidget_1 QTableView {\n"
"    background-color: #94b2e3; /* fill the empty space blue */\n"
"}\n"
"\n"
"")
        self.tableWidget_1.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_1.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_1.setLineWidth(1)
        self.tableWidget_1.setMidLineWidth(0)
        self.tableWidget_1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget_1.setAlternatingRowColors(True)
        self.tableWidget_1.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget_1.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_1.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget_1.setShowGrid(True)
        self.tableWidget_1.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_1.setSortingEnabled(False)
        self.tableWidget_1.setRowCount(12)
        self.tableWidget_1.setColumnCount(7)
        self.tableWidget_1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_1.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_1.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_1.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget_1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_spend = QLineEdit(self.widget_5)
        self.lineEdit_spend.setObjectName(u"lineEdit_spend")
        sizePolicy1.setHeightForWidth(self.lineEdit_spend.sizePolicy().hasHeightForWidth())
        self.lineEdit_spend.setSizePolicy(sizePolicy1)
        self.lineEdit_spend.setMinimumSize(QSize(0, 0))
        self.lineEdit_spend.setMaximumSize(QSize(1920, 70))
        self.lineEdit_spend.setFont(font1)
        self.lineEdit_spend.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_spend.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_spend.setMaxLength(1000)
        self.lineEdit_spend.setFrame(False)
        self.lineEdit_spend.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_spend.setCursorPosition(0)
        self.lineEdit_spend.setDragEnabled(True)
        self.lineEdit_spend.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_spend.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_spend)

        self.lineEdit_item = QLineEdit(self.widget_5)
        self.lineEdit_item.setObjectName(u"lineEdit_item")
        sizePolicy1.setHeightForWidth(self.lineEdit_item.sizePolicy().hasHeightForWidth())
        self.lineEdit_item.setSizePolicy(sizePolicy1)
        self.lineEdit_item.setMinimumSize(QSize(0, 0))
        self.lineEdit_item.setMaximumSize(QSize(1920, 70))
        self.lineEdit_item.setFont(font1)
        self.lineEdit_item.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_item.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_item.setMaxLength(1000)
        self.lineEdit_item.setFrame(False)
        self.lineEdit_item.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_item.setCursorPosition(0)
        self.lineEdit_item.setDragEnabled(True)
        self.lineEdit_item.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_item.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_item)

        self.lineEdit_reciepent = QLineEdit(self.widget_5)
        self.lineEdit_reciepent.setObjectName(u"lineEdit_reciepent")
        sizePolicy1.setHeightForWidth(self.lineEdit_reciepent.sizePolicy().hasHeightForWidth())
        self.lineEdit_reciepent.setSizePolicy(sizePolicy1)
        self.lineEdit_reciepent.setMinimumSize(QSize(0, 0))
        self.lineEdit_reciepent.setMaximumSize(QSize(1920, 70))
        self.lineEdit_reciepent.setFont(font1)
        self.lineEdit_reciepent.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_reciepent.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_reciepent.setMaxLength(1000)
        self.lineEdit_reciepent.setFrame(False)
        self.lineEdit_reciepent.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_reciepent.setCursorPosition(0)
        self.lineEdit_reciepent.setDragEnabled(True)
        self.lineEdit_reciepent.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_reciepent.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_reciepent)

        self.toolButton_save1 = QToolButton(self.widget_5)
        self.toolButton_save1.setObjectName(u"toolButton_save1")
        self.toolButton_save1.setMinimumSize(QSize(70, 0))
        self.toolButton_save1.setFont(font3)
        self.toolButton_save1.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_4.addWidget(self.toolButton_save1)

        self.label_total_expense = QLabel(self.widget_5)
        self.label_total_expense.setObjectName(u"label_total_expense")
        self.label_total_expense.setMinimumSize(QSize(158, 26))
        self.label_total_expense.setMaximumSize(QSize(158, 26))
        self.label_total_expense.setFont(font2)
        self.label_total_expense.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_4.addWidget(self.label_total_expense)

        self.label_total_spends = QLabel(self.widget_5)
        self.label_total_spends.setObjectName(u"label_total_spends")
        self.label_total_spends.setMinimumSize(QSize(206, 26))
        self.label_total_spends.setFont(font2)
        self.label_total_spends.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_4.addWidget(self.label_total_spends)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.verticalLayout_16.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.tab_7)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(800, 0))
        self.widget_6.setStyleSheet(u"#widget_6 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #a5b7d9;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_6:hover {\n"
"    background-color: #81a6e1;\n"
"    border: 1px solid #4e8df5;\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_6:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_extra_gains = QLabel(self.widget_6)
        self.label_extra_gains.setObjectName(u"label_extra_gains")
        self.label_extra_gains.setMaximumSize(QSize(87, 16777215))
        self.label_extra_gains.setFont(font2)
        self.label_extra_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_6.addWidget(self.label_extra_gains)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.toolButton_del_row_2 = QToolButton(self.widget_6)
        self.toolButton_del_row_2.setObjectName(u"toolButton_del_row_2")
        self.toolButton_del_row_2.setMinimumSize(QSize(60, 0))
        self.toolButton_del_row_2.setMaximumSize(QSize(61, 16777215))
        self.toolButton_del_row_2.setFont(font3)
        self.toolButton_del_row_2.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_6.addWidget(self.toolButton_del_row_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tableWidget_2 = QTableWidget(self.widget_6)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        if (self.tableWidget_2.rowCount() < 12):
            self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font2)
        self.tableWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"/* ===== Table Widget Style (Light Blue Theme) ===== */\n"
"#tableWidget_2 {\n"
"    background-color: #f5f9ff; /* soft blue-white background */\n"
"    alternate-background-color: #e8f1ff;\n"
"    gridline-color: #b7c9f0;\n"
"  \n"
"    \n"
"    font: 11pt \"Segoe UI\";\n"
"    color: #2f3e55;\n"
"    selection-background-color: #6ea6f8;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ===== Header Styling ===== */\n"
"#tableWidget_2 QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #cbd9f6, stop:1 #a9c4f2);\n"
"    color: #1d2b4d;\n"
"    font-weight: 600;\n"
"    font-size: 11pt;\n"
"    border: 1px solid #9bb8ef;\n"
"  \n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_2 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ffffff;\n"
"}\n"
""
                        "\n"
"/* ===== Row Hover Highlight ===== */\n"
"#tableWidget_2::item:hover {\n"
"    background-color: #c8ddff;\n"
"    color: #12294d;\n"
"}\n"
"\n"
"/* ===== Selected Cell ===== */\n"
"#tableWidget_2::item:selected {\n"
"    background-color: #7aa3e6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ===== Vertical Scrollbar ===== */\n"
"#tableWidget_2 QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::add-line:vertical,\n"
"#tableWidget_2 QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* ===== Horizontal Scrollbar ===== */\n"
"#tableWidget_2 QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    height: 10px;\n"
"    margin:"
                        " 0 2px 0 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::handle:horizontal {\n"
"    background: #90b4ff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::handle:horizontal:hover {\n"
"    background: #6e9fff;\n"
"}\n"
"\n"
"#tableWidget_2 QScrollBar::add-line:horizontal,\n"
"#tableWidget_2 QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"/* This styles the empty area (the viewport) */\n"
"#tableWidget_2 QTableCornerButton::section,\n"
"#tableWidget_2 QTableView QTableCornerButton::section,\n"
"#tableWidget_2 QWidget {\n"
"    background-color: #94b2e3; /* soft blue empty area */\n"
"}\n"
"\n"
"/* The actual viewport region where no cells exist */\n"
"#tableWidget_2 QTableView {\n"
"    background-color: #94b2e3; /* fill the empty space blue */\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidget_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_get = QLineEdit(self.widget_6)
        self.lineEdit_get.setObjectName(u"lineEdit_get")
        sizePolicy1.setHeightForWidth(self.lineEdit_get.sizePolicy().hasHeightForWidth())
        self.lineEdit_get.setSizePolicy(sizePolicy1)
        self.lineEdit_get.setMinimumSize(QSize(0, 0))
        self.lineEdit_get.setMaximumSize(QSize(1920, 70))
        self.lineEdit_get.setFont(font1)
        self.lineEdit_get.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_get.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_get.setMaxLength(1000)
        self.lineEdit_get.setFrame(False)
        self.lineEdit_get.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_get.setCursorPosition(0)
        self.lineEdit_get.setDragEnabled(True)
        self.lineEdit_get.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_get.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_get)

        self.lineEdit_for_what = QLineEdit(self.widget_6)
        self.lineEdit_for_what.setObjectName(u"lineEdit_for_what")
        sizePolicy1.setHeightForWidth(self.lineEdit_for_what.sizePolicy().hasHeightForWidth())
        self.lineEdit_for_what.setSizePolicy(sizePolicy1)
        self.lineEdit_for_what.setMinimumSize(QSize(0, 0))
        self.lineEdit_for_what.setMaximumSize(QSize(1920, 70))
        self.lineEdit_for_what.setFont(font1)
        self.lineEdit_for_what.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_for_what.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_for_what.setMaxLength(1000)
        self.lineEdit_for_what.setFrame(False)
        self.lineEdit_for_what.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_for_what.setCursorPosition(0)
        self.lineEdit_for_what.setDragEnabled(True)
        self.lineEdit_for_what.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_for_what.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_for_what)

        self.lineEdit_giver = QLineEdit(self.widget_6)
        self.lineEdit_giver.setObjectName(u"lineEdit_giver")
        sizePolicy1.setHeightForWidth(self.lineEdit_giver.sizePolicy().hasHeightForWidth())
        self.lineEdit_giver.setSizePolicy(sizePolicy1)
        self.lineEdit_giver.setMinimumSize(QSize(0, 0))
        self.lineEdit_giver.setMaximumSize(QSize(1920, 70))
        self.lineEdit_giver.setFont(font1)
        self.lineEdit_giver.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_giver.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_giver.setMaxLength(1000)
        self.lineEdit_giver.setFrame(False)
        self.lineEdit_giver.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_giver.setCursorPosition(0)
        self.lineEdit_giver.setDragEnabled(True)
        self.lineEdit_giver.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_giver.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_giver)

        self.toolButton_save2 = QToolButton(self.widget_6)
        self.toolButton_save2.setObjectName(u"toolButton_save2")
        self.toolButton_save2.setMinimumSize(QSize(70, 0))
        self.toolButton_save2.setFont(font3)
        self.toolButton_save2.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_5.addWidget(self.toolButton_save2)

        self.label_monthly_gains = QLabel(self.widget_6)
        self.label_monthly_gains.setObjectName(u"label_monthly_gains")
        self.label_monthly_gains.setMinimumSize(QSize(158, 26))
        self.label_monthly_gains.setMaximumSize(QSize(158, 26))
        self.label_monthly_gains.setFont(font2)
        self.label_monthly_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_5.addWidget(self.label_monthly_gains)

        self.label_total_gains = QLabel(self.widget_6)
        self.label_total_gains.setObjectName(u"label_total_gains")
        self.label_total_gains.setMinimumSize(QSize(206, 26))
        self.label_total_gains.setFont(font2)
        self.label_total_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_5.addWidget(self.label_total_gains)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_16.addWidget(self.widget_6)


        self.horizontalLayout_36.addLayout(self.verticalLayout_16)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_45 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.tab_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(811, 400))
        self.widget_7.setStyleSheet(u"\n"
"#widget_7 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #94b2e3;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_7:hover {\n"
"    background-color: #81a6e1;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_7:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"   border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px"
                        "; /* Rounded */\n"
"}\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_extra_gains_2 = QLabel(self.widget_7)
        self.label_extra_gains_2.setObjectName(u"label_extra_gains_2")
        self.label_extra_gains_2.setMaximumSize(QSize(135, 26))
        self.label_extra_gains_2.setFont(font2)
        self.label_extra_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_9.addWidget(self.label_extra_gains_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.toolButton_del_row_3 = QToolButton(self.widget_7)
        self.toolButton_del_row_3.setObjectName(u"toolButton_del_row_3")
        self.toolButton_del_row_3.setMinimumSize(QSize(60, 26))
        self.toolButton_del_row_3.setMaximumSize(QSize(60, 26))
        self.toolButton_del_row_3.setFont(font3)
        self.toolButton_del_row_3.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_9.addWidget(self.toolButton_del_row_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.tableWidget_3 = QTableWidget(self.widget_7)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        if (self.tableWidget_3.rowCount() < 23):
            self.tableWidget_3.setRowCount(23)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font2)
        self.tableWidget_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_3.setStyleSheet(u"/* ===== Table Widget Style (Light Blue Theme) ===== */\n"
"#tableWidget_3 {\n"
"    background-color: #f5f9ff; /* soft blue-white background */\n"
"    alternate-background-color: #e8f1ff;\n"
"    gridline-color: #b7c9f0;\n"
"  \n"
"    \n"
"    font: 11pt \"Segoe UI\";\n"
"    color: #2f3e55;\n"
"    selection-background-color: #6ea6f8;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ===== Header Styling ===== */\n"
"#tableWidget_3 QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #cbd9f6, stop:1 #a9c4f2);\n"
"    color: #1d2b4d;\n"
"    font-weight: 600;\n"
"    font-size: 11pt;\n"
"    border: 1px solid #9bb8ef;\n"
"\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_3 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
""
                        "/* ===== Row Hover Highlight ===== */\n"
"#tableWidget_3::item:hover {\n"
"    background-color: #c8ddff;\n"
"    color: #12294d;\n"
"}\n"
"\n"
"/* ===== Selected Cell ===== */\n"
"#tableWidget_3::item:selected {\n"
"    background-color: #7aa3e6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ===== Vertical Scrollbar ===== */\n"
"#tableWidget_3 QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::add-line:vertical,\n"
"#tableWidget_3 QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* ===== Horizontal Scrollbar ===== */\n"
"#tableWidget_3 QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    height: 10px;\n"
"    margin: 0 2p"
                        "x 0 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::handle:horizontal {\n"
"    background: #90b4ff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::handle:horizontal:hover {\n"
"    background: #6e9fff;\n"
"}\n"
"\n"
"#tableWidget_3 QScrollBar::add-line:horizontal,\n"
"#tableWidget_3 QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"/* This styles the empty area (the viewport) */\n"
"#tableWidget_3 QTableCornerButton::section,\n"
"#tableWidget_3 QTableView QTableCornerButton::section,\n"
"#tableWidget_3 QWidget {\n"
"    background-color: #94b2e3; /* soft blue empty area */\n"
"}\n"
"\n"
"/* The actual viewport region where no cells exist */\n"
"#tableWidget_3 QTableView {\n"
"    background-color: #94b2e3; /* fill the empty space blue */\n"
"}\n"
"\n"
"")
        self.tableWidget_3.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_3.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setMidLineWidth(0)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setRowCount(23)
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tableWidget_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_get_2 = QLineEdit(self.widget_7)
        self.lineEdit_get_2.setObjectName(u"lineEdit_get_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_get_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_get_2.setSizePolicy(sizePolicy1)
        self.lineEdit_get_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_get_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_get_2.setFont(font1)
        self.lineEdit_get_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_get_2.setStyleSheet(u"#lineEdit_get_2 {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_get_2:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_get_2:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_get_2.setMaxLength(1000)
        self.lineEdit_get_2.setFrame(False)
        self.lineEdit_get_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_get_2.setCursorPosition(0)
        self.lineEdit_get_2.setDragEnabled(True)
        self.lineEdit_get_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_get_2.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_get_2)

        self.lineEdit_for_what_2 = QLineEdit(self.widget_7)
        self.lineEdit_for_what_2.setObjectName(u"lineEdit_for_what_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_for_what_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_for_what_2.setSizePolicy(sizePolicy1)
        self.lineEdit_for_what_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_for_what_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_for_what_2.setFont(font1)
        self.lineEdit_for_what_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_for_what_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_for_what_2.setMaxLength(1000)
        self.lineEdit_for_what_2.setFrame(False)
        self.lineEdit_for_what_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_for_what_2.setCursorPosition(0)
        self.lineEdit_for_what_2.setDragEnabled(True)
        self.lineEdit_for_what_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_for_what_2.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_for_what_2)

        self.lineEdit_giver_2 = QLineEdit(self.widget_7)
        self.lineEdit_giver_2.setObjectName(u"lineEdit_giver_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_giver_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_giver_2.setSizePolicy(sizePolicy1)
        self.lineEdit_giver_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_giver_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_giver_2.setFont(font1)
        self.lineEdit_giver_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_giver_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}")
        self.lineEdit_giver_2.setMaxLength(1000)
        self.lineEdit_giver_2.setFrame(False)
        self.lineEdit_giver_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_giver_2.setCursorPosition(0)
        self.lineEdit_giver_2.setDragEnabled(True)
        self.lineEdit_giver_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_giver_2.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_giver_2)

        self.toolButton_save2_2 = QToolButton(self.widget_7)
        self.toolButton_save2_2.setObjectName(u"toolButton_save2_2")
        self.toolButton_save2_2.setMinimumSize(QSize(70, 25))
        self.toolButton_save2_2.setFont(font3)
        self.toolButton_save2_2.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_10.addWidget(self.toolButton_save2_2)

        self.label_monthly_gains_2 = QLabel(self.widget_7)
        self.label_monthly_gains_2.setObjectName(u"label_monthly_gains_2")
        self.label_monthly_gains_2.setMaximumSize(QSize(150, 26))
        self.label_monthly_gains_2.setFont(font2)
        self.label_monthly_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_10.addWidget(self.label_monthly_gains_2)

        self.label_total_gains_2 = QLabel(self.widget_7)
        self.label_total_gains_2.setObjectName(u"label_total_gains_2")
        self.label_total_gains_2.setMaximumSize(QSize(212, 26))
        self.label_total_gains_2.setFont(font2)
        self.label_total_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_10.addWidget(self.label_total_gains_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)


        self.horizontalLayout_45.addWidget(self.widget_7)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_46 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.tab_10)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: #94b2e3;\n"
"\n"
"\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_extra_gains_3 = QLabel(self.widget_2)
        self.label_extra_gains_3.setObjectName(u"label_extra_gains_3")
        self.label_extra_gains_3.setMinimumSize(QSize(95, 26))
        self.label_extra_gains_3.setMaximumSize(QSize(95, 26))
        self.label_extra_gains_3.setFont(font2)
        self.label_extra_gains_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_12.addWidget(self.label_extra_gains_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.pushButton_save_button = QPushButton(self.widget_2)
        self.pushButton_save_button.setObjectName(u"pushButton_save_button")
        self.pushButton_save_button.setMinimumSize(QSize(60, 26))
        self.pushButton_save_button.setMaximumSize(QSize(60, 26))
        self.pushButton_save_button.setFont(font3)
        self.pushButton_save_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_save_button)

        self.pushButton_load_button = QPushButton(self.widget_2)
        self.pushButton_load_button.setObjectName(u"pushButton_load_button")
        self.pushButton_load_button.setMinimumSize(QSize(68, 26))
        self.pushButton_load_button.setMaximumSize(QSize(68, 26))
        self.pushButton_load_button.setFont(font3)
        self.pushButton_load_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_load_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: #eaf1fb;\n"
"color: rgb(0, 0, 0);\n"
" border-radius: 10px;")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(90, 30))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.lineEdit_stock_name_input = QLineEdit(self.widget_4)
        self.lineEdit_stock_name_input.setObjectName(u"lineEdit_stock_name_input")
        self.lineEdit_stock_name_input.setMinimumSize(QSize(250, 30))
        self.lineEdit_stock_name_input.setMaximumSize(QSize(250, 30))
        self.lineEdit_stock_name_input.setFont(font1)
        self.lineEdit_stock_name_input.setStyleSheet(u"#lineEdit_stock_name_input {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_stock_name_input:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_stock_name_input:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.lineEdit_stock_name_input)

        self.pushButton_add_stock_button = QPushButton(self.widget_4)
        self.pushButton_add_stock_button.setObjectName(u"pushButton_add_stock_button")
        self.pushButton_add_stock_button.setMinimumSize(QSize(90, 30))
        self.pushButton_add_stock_button.setMaximumSize(QSize(90, 16777215))
        self.pushButton_add_stock_button.setFont(font3)
        self.pushButton_add_stock_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_add_stock_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.comboBox_5 = QComboBox(self.widget_4)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(150, 30))
        self.comboBox_5.setMaximumSize(QSize(150, 30))
        self.comboBox_5.setFont(font2)
        self.comboBox_5.setStyleSheet(u"/* ==========================\n"
"   QComboBox - Professional Soft Blue Theme\n"
"   ========================== */\n"
"\n"
"QComboBox {\n"
"    background-color: #f4f6fb;\n"
"    color: #1f2937;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QComboBox:hover {\n"
"    background-color: #f0f4ff;\n"
"    border: 1px solid #5e85d7;\n"
"}\n"
"\n"
"/* Focus (active) effect */\n"
"QComboBox:focus {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #5e85d7;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;\n"
"    color: #7a7a7a;\n"
"    border: 1px solid #c0c0c0;\n"
"}\n"
"\n"
"/* Drop-down arrow area */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px "
                        "solid #a7b4d0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #e8ecf9, stop:1 #cfd8f3);\n"
"}\n"
"\n"
"/* Arrow icon (uses system default if custom not available) */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down_arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* === Drop-down List Styling === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #f9faff;\n"
"    color: #1f2937;\n"
"    border: 1px solid #5e85d7;\n"
"    border-radius: 6px;\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: #ffffff;\n"
"    outline: none;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Hover over individual items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #dbe6ff; /* Soft blue hover */\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"/* Selected item (click or keyboard highlight) */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    bac"
                        "kground-color: #5e85d7;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.comboBox_5.setFrame(False)

        self.horizontalLayout_13.addWidget(self.comboBox_5)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(100, 100))
        self.widget_3.setStyleSheet(u"#widget_3 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #a5b7d9;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_3:hover {\n"
"    background-color: #81a6e1;\n"
"    \n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_3:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(87, 26))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.lineEdit_search_stock_input = QLineEdit(self.widget_3)
        self.lineEdit_search_stock_input.setObjectName(u"lineEdit_search_stock_input")
        self.lineEdit_search_stock_input.setMinimumSize(QSize(0, 26))
        self.lineEdit_search_stock_input.setFont(font3)
        self.lineEdit_search_stock_input.setStyleSheet(u"#lineEdit_search_stock_input {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"  \n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_search_stock_input:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_search_stock_input:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.lineEdit_search_stock_input)

        self.pushButton_search_stock_button_ = QPushButton(self.widget_3)
        self.pushButton_search_stock_button_.setObjectName(u"pushButton_search_stock_button_")
        self.pushButton_search_stock_button_.setMinimumSize(QSize(60, 26))
        self.pushButton_search_stock_button_.setMaximumSize(QSize(76, 26))
        self.pushButton_search_stock_button_.setFont(font3)
        self.pushButton_search_stock_button_.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_search_stock_button_)

        self.pushButton_delete_stock_button = QPushButton(self.widget_3)
        self.pushButton_delete_stock_button.setObjectName(u"pushButton_delete_stock_button")
        self.pushButton_delete_stock_button.setMinimumSize(QSize(61, 26))
        self.pushButton_delete_stock_button.setMaximumSize(QSize(76, 26))
        self.pushButton_delete_stock_button.setFont(font3)
        self.pushButton_delete_stock_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_delete_stock_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.listWidget_stock_list = QListWidget(self.widget_3)
        self.listWidget_stock_list.setObjectName(u"listWidget_stock_list")
        self.listWidget_stock_list.setMinimumSize(QSize(40, 50))
        self.listWidget_stock_list.setFont(font3)
        self.listWidget_stock_list.setStyleSheet(u"#listWidget_stock_list {\n"
"    background-color: #eaf1fb;\n"
"    border: 1px solid #b0c4de;\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"  \n"
"    color: #1a1a1a;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Scrollbar styling */\n"
"#listWidget_stock_list QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #c4dcff;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#listWidget_stock_list QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#listWidget_stock_list QScrollBar::handle:vertical:hover {\n"
"    background: #486da8;\n"
"}\n"
"\n"
"#listWidget_stock_list QScrollBar::add-line:vertical,\n"
"#listWidget_stock_list QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* List item styling */\n"
"#listWidget_stock_list::item {\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#listWidget_stock_list::item:selected {\n"
"    background-color: #81a6e1;\n"
"    color: white;\n"
""
                        "}\n"
"\n"
"#listWidget_stock_list::item:hover {\n"
"    background-color: #c4dcff;\n"
"color: black;\n"
"}\n"
"")
        self.listWidget_stock_list.setSelectionRectVisible(True)

        self.verticalLayout_4.addWidget(self.listWidget_stock_list)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_17.addWidget(self.label_12)

        self.lineEdit_item_name_input = QLineEdit(self.widget_3)
        self.lineEdit_item_name_input.setObjectName(u"lineEdit_item_name_input")
        self.lineEdit_item_name_input.setMinimumSize(QSize(84, 30))
        self.lineEdit_item_name_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_item_name_input.setFont(font3)
        self.lineEdit_item_name_input.setStyleSheet(u"#lineEdit_item_name_input {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"  \n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_item_name_input:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_item_name_input:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.lineEdit_item_name_input)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_19.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 26))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_16.addWidget(self.label_24)

        self.lineEdit_search_item_lineedit = QLineEdit(self.widget_3)
        self.lineEdit_search_item_lineedit.setObjectName(u"lineEdit_search_item_lineedit")
        self.lineEdit_search_item_lineedit.setMaximumSize(QSize(16777215, 26))
        self.lineEdit_search_item_lineedit.setFont(font3)
        self.lineEdit_search_item_lineedit.setStyleSheet(u"#lineEdit_search_item_lineedit {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"  \n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_search_item_lineedit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_search_item_lineedit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.lineEdit_search_item_lineedit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.pushButton_search_item_button_ = QPushButton(self.widget_3)
        self.pushButton_search_item_button_.setObjectName(u"pushButton_search_item_button_")
        self.pushButton_search_item_button_.setMinimumSize(QSize(60, 26))
        self.pushButton_search_item_button_.setMaximumSize(QSize(76, 26))
        self.pushButton_search_item_button_.setFont(font3)
        self.pushButton_search_item_button_.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton_search_item_button_)

        self.pushButton_delete_item_button = QPushButton(self.widget_3)
        self.pushButton_delete_item_button.setObjectName(u"pushButton_delete_item_button")
        self.pushButton_delete_item_button.setMinimumSize(QSize(60, 26))
        self.pushButton_delete_item_button.setMaximumSize(QSize(70, 26))
        self.pushButton_delete_item_button.setFont(font3)
        self.pushButton_delete_item_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton_delete_item_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.tableWidget_item_table = QTableWidget(self.widget_3)
        if (self.tableWidget_item_table.columnCount() < 3):
            self.tableWidget_item_table.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_item_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_item_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_item_table.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        if (self.tableWidget_item_table.rowCount() < 18):
            self.tableWidget_item_table.setRowCount(18)
        self.tableWidget_item_table.setObjectName(u"tableWidget_item_table")
        self.tableWidget_item_table.setFont(font2)
        self.tableWidget_item_table.setStyleSheet(u"/* ===== Table Widget Style (Light Blue Theme) ===== */\n"
"#tableWidget_item_table {\n"
"    background-color: #f5f9ff; /* soft blue-white background */\n"
"    alternate-background-color: #e8f1ff;\n"
"    gridline-color: #b7c9f0;\n"
"  \n"
"    \n"
"    font: 11pt \"Segoe UI\";\n"
"    color: #2f3e55;\n"
"    selection-background-color: #6ea6f8;\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ===== Header Styling ===== */\n"
"#tableWidget_item_table QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #cbd9f6, stop:1 #a9c4f2);\n"
"    color: #1d2b4d;\n"
"    font-weight: 600;\n"
"    font-size: 11pt;\n"
"    border: 1px solid #9bb8ef;\n"
"  \n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_item_table QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"  "
                        "  color: #ffffff;\n"
"}\n"
"\n"
"/* ===== Row Hover Highlight ===== */\n"
"#tableWidget_item_table::item:hover {\n"
"    background-color: #c8ddff;\n"
"    color: #12294d;\n"
"}\n"
"\n"
"/* ===== Selected Cell ===== */\n"
"#tableWidget_item_table::item:selected {\n"
"    background-color: #7aa3e6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* ===== Vertical Scrollbar ===== */\n"
"#tableWidget_item_table QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::add-line:vertical,\n"
"#tableWidget_item_table QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* ===== Horizontal Scrollbar ===== */\n"
"#tableWidget_item_table QScrollBar:h"
                        "orizontal {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    height: 10px;\n"
"    margin: 0 2px 0 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::handle:horizontal {\n"
"    background: #90b4ff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::handle:horizontal:hover {\n"
"    background: #6e9fff;\n"
"}\n"
"\n"
"#tableWidget_item_table QScrollBar::add-line:horizontal,\n"
"#tableWidget_item_table QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"}\n"
"\n"
"\n"
"/* This styles the empty area (the viewport) */\n"
"#tableWidget_item_table QTableCornerButton::section,\n"
"#tableWidget_item_table QTableView QTableCornerButton::section,\n"
"#tableWidget_item_table QWidget {\n"
"    background-color: #94b2e3; /* soft blue empty area */\n"
"}\n"
"\n"
"/* The actual viewport region where no cells exist */\n"
"#tableWidget_item_table QTableView {\n"
"    background-color: #94b2e3; /* fill the empty space blue */\n"
"}\n"
"\n"
"")
        self.tableWidget_item_table.setRowCount(18)

        self.verticalLayout_5.addWidget(self.tableWidget_item_table)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.lineEdit_item_rate_input = QLineEdit(self.widget_3)
        self.lineEdit_item_rate_input.setObjectName(u"lineEdit_item_rate_input")
        self.lineEdit_item_rate_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_item_rate_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_item_rate_input.setFont(font3)
        self.lineEdit_item_rate_input.setStyleSheet(u"#lineEdit_item_rate_input {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"    \n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_item_rate_input:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_item_rate_input:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.lineEdit_item_rate_input)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.lineEdit_item_quantity_input = QLineEdit(self.widget_3)
        self.lineEdit_item_quantity_input.setObjectName(u"lineEdit_item_quantity_input")
        self.lineEdit_item_quantity_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_item_quantity_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_item_quantity_input.setFont(font3)
        self.lineEdit_item_quantity_input.setStyleSheet(u"#lineEdit_item_quantity_input {\n"
"    background-color: #f4f6fb;\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #a0aec0;\n"
"    border-radius: 6px;\n"
"    padding: 0px 10px;\n"
"  \n"
"    selection-background-color: #3a7bd5; /* Highlight text selection in blue */\n"
"\n"
"}\n"
"\n"
"#lineEdit_item_quantity_input:hover {\n"
"    border: 1px solid #3a7bd5;  /* Professional blue on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"#lineEdit_item_quantity_input:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green focus */\n"
"    background-color: #ffffff;  /* Crisp white for focus */\n"
"    color: #000000;\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.lineEdit_item_quantity_input)

        self.pushButton_add_item_button = QPushButton(self.widget_3)
        self.pushButton_add_item_button.setObjectName(u"pushButton_add_item_button")
        self.pushButton_add_item_button.setMinimumSize(QSize(84, 30))
        self.pushButton_add_item_button.setMaximumSize(QSize(16777215, 30))
        self.pushButton_add_item_button.setFont(font3)
        self.pushButton_add_item_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_18.addWidget(self.pushButton_add_item_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_19.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addWidget(self.widget_3)


        self.horizontalLayout_46.addWidget(self.widget_2)

        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_47 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.tab_11)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"\n"
"#widget_8 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #94b2e3;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_8:hover {\n"
"    background-color: #81a6e1;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_8:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"   border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px"
                        "; /* Rounded */\n"
"}\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.scrollArea_image_grid = QScrollArea(self.widget_8)
        self.scrollArea_image_grid.setObjectName(u"scrollArea_image_grid")
        self.scrollArea_image_grid.setMinimumSize(QSize(520, 200))
        self.scrollArea_image_grid.setStyleSheet(u"\n"
"\n"
"\n"
"#scrollArea_image_grid {\n"
"background-color: #6578b3;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 5px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"/* Scrollbar styling for a clean, modern look */\n"
"#scrollArea_image_grid QScrollBar:vertical {\n"
"    background: #a5bbe6;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::handle:vertical {\n"
"     background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::add-line:vertical,\n"
"#scrollArea_image_grid QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar:horizontal {\n"
"    background: #a5bbe6;\n"
"    height: 10px;\n"
"    margin: 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::handle:horizontal {\n"
"    background: #6c"
                        "7cb0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::handle:horizontal:hover {\n"
"    background: #4e5e9e;\n"
"}\n"
"\n"
"#scrollArea_image_grid QScrollBar::add-line:horizontal,\n"
"#scrollArea_image_grid QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea_image_grid.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 518, 636))
        self.scrollArea_image_grid.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea_image_grid)


        self.horizontalLayout_23.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_open_product_image = QPushButton(self.widget_8)
        self.pushButton_open_product_image.setObjectName(u"pushButton_open_product_image")
        self.pushButton_open_product_image.setMinimumSize(QSize(175, 30))
        self.pushButton_open_product_image.setMaximumSize(QSize(16777215, 30))
        self.pushButton_open_product_image.setFont(font3)
        self.pushButton_open_product_image.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_21.addWidget(self.pushButton_open_product_image)

        self.pushButton_refresh_image_grid = QPushButton(self.widget_8)
        self.pushButton_refresh_image_grid.setObjectName(u"pushButton_refresh_image_grid")
        self.pushButton_refresh_image_grid.setMinimumSize(QSize(0, 30))
        self.pushButton_refresh_image_grid.setMaximumSize(QSize(100, 30))
        self.pushButton_refresh_image_grid.setFont(font3)
        self.pushButton_refresh_image_grid.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_21.addWidget(self.pushButton_refresh_image_grid)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.label_image_show = QLabel(self.widget_8)
        self.label_image_show.setObjectName(u"label_image_show")
        self.label_image_show.setMinimumSize(QSize(100, 200))
        self.label_image_show.setMaximumSize(QSize(400, 16777215))
        self.label_image_show.setFont(font2)
        self.label_image_show.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_image_show.setAutoFillBackground(False)
        self.label_image_show.setStyleSheet(u"background-color: rgb(228, 235, 248);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.label_image_show.setFrameShape(QFrame.Shape.Box)
        self.label_image_show.setScaledContents(False)

        self.verticalLayout_8.addWidget(self.label_image_show)

        self.textEdit_image_description = QTextEdit(self.widget_8)
        self.textEdit_image_description.setObjectName(u"textEdit_image_description")
        self.textEdit_image_description.setMinimumSize(QSize(100, 200))
        self.textEdit_image_description.setMaximumSize(QSize(400, 300))
        self.textEdit_image_description.setFont(font3)
        self.textEdit_image_description.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_image_description.setFrameShape(QFrame.Shape.WinPanel)

        self.verticalLayout_8.addWidget(self.textEdit_image_description)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_show_product_folder = QPushButton(self.widget_8)
        self.pushButton_show_product_folder.setObjectName(u"pushButton_show_product_folder")
        self.pushButton_show_product_folder.setMinimumSize(QSize(0, 30))
        self.pushButton_show_product_folder.setMaximumSize(QSize(16777215, 30))
        self.pushButton_show_product_folder.setFont(font3)
        self.pushButton_show_product_folder.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_show_product_folder)

        self.pushButton_save_description = QPushButton(self.widget_8)
        self.pushButton_save_description.setObjectName(u"pushButton_save_description")
        self.pushButton_save_description.setMinimumSize(QSize(0, 30))
        self.pushButton_save_description.setMaximumSize(QSize(16777215, 30))
        self.pushButton_save_description.setFont(font3)
        self.pushButton_save_description.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_save_description)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_23.addLayout(self.verticalLayout_8)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_47.addWidget(self.widget_8)

        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_48 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.widget_graph_6 = QWidget(self.tab_4)
        self.widget_graph_6.setObjectName(u"widget_graph_6")
        self.widget_graph_6.setStyleSheet(u"background-color: #dcebff;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"\n"
"color: rgb(0, 0, 0);")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_graph_6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(20, -1, 9, -1)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.label_21 = QLabel(self.widget_graph_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(159, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.label_21)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_9)

        self.toolButton_save_button = QToolButton(self.widget_graph_6)
        self.toolButton_save_button.setObjectName(u"toolButton_save_button")
        self.toolButton_save_button.setMinimumSize(QSize(100, 30))
        self.toolButton_save_button.setMaximumSize(QSize(80, 30))
        self.toolButton_save_button.setFont(font3)
        self.toolButton_save_button.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout_25.addWidget(self.toolButton_save_button)


        self.verticalLayout_15.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_3 = QLabel(self.widget_graph_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_26.addWidget(self.label_3)

        self.lineEdit_shop_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_name.setObjectName(u"lineEdit_shop_name")
        self.lineEdit_shop_name.setMinimumSize(QSize(310, 25))
        self.lineEdit_shop_name.setFont(font3)
        self.lineEdit_shop_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_26.addWidget(self.lineEdit_shop_name)

        self.label_suggest_qty = QLabel(self.widget_graph_6)
        self.label_suggest_qty.setObjectName(u"label_suggest_qty")
        self.label_suggest_qty.setFont(font2)
        self.label_suggest_qty.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_26.addWidget(self.label_suggest_qty)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_13)


        self.verticalLayout_15.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_4 = QLabel(self.widget_graph_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.label_4)

        self.lineEdit_shop_address = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_address.setObjectName(u"lineEdit_shop_address")
        self.lineEdit_shop_address.setMinimumSize(QSize(450, 25))
        self.lineEdit_shop_address.setFont(font3)
        self.lineEdit_shop_address.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_27.addWidget(self.lineEdit_shop_address)

        self.lineEdit_suggest_item = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_item.setObjectName(u"lineEdit_suggest_item")
        self.lineEdit_suggest_item.setMinimumSize(QSize(100, 0))
        self.lineEdit_suggest_item.setFont(font3)
        self.lineEdit_suggest_item.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")

        self.horizontalLayout_27.addWidget(self.lineEdit_suggest_item)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_5 = QLabel(self.widget_graph_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.label_5)

        self.lineEdit_shop_gstin = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_gstin.setObjectName(u"lineEdit_shop_gstin")
        self.lineEdit_shop_gstin.setMinimumSize(QSize(0, 25))
        self.lineEdit_shop_gstin.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_shop_gstin.setFont(font3)
        self.lineEdit_shop_gstin.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_28.addWidget(self.lineEdit_shop_gstin)

        self.lineEdit_suggest_quantity = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_quantity.setObjectName(u"lineEdit_suggest_quantity")
        self.lineEdit_suggest_quantity.setFont(font3)
        self.lineEdit_suggest_quantity.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")

        self.horizontalLayout_28.addWidget(self.lineEdit_suggest_quantity)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_15)


        self.verticalLayout_15.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_6 = QLabel(self.widget_graph_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_29.addWidget(self.label_6)

        self.lineEdit_customer_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_name.setObjectName(u"lineEdit_customer_name")
        self.lineEdit_customer_name.setMinimumSize(QSize(100, 25))
        self.lineEdit_customer_name.setMaximumSize(QSize(350, 16777215))
        self.lineEdit_customer_name.setFont(font3)
        self.lineEdit_customer_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_29.addWidget(self.lineEdit_customer_name)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_16)


        self.verticalLayout_15.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_7 = QLabel(self.widget_graph_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_30.addWidget(self.label_7)

        self.lineEdit_customer_address = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_address.setObjectName(u"lineEdit_customer_address")
        self.lineEdit_customer_address.setMinimumSize(QSize(0, 25))
        self.lineEdit_customer_address.setFont(font3)
        self.lineEdit_customer_address.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_30.addWidget(self.lineEdit_customer_address)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_17)


        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_8 = QLabel(self.widget_graph_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.label_8)

        self.lineEdit_customer_gstin = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_gstin.setObjectName(u"lineEdit_customer_gstin")
        self.lineEdit_customer_gstin.setMinimumSize(QSize(0, 25))
        self.lineEdit_customer_gstin.setMaximumSize(QSize(250, 25))
        self.lineEdit_customer_gstin.setFont(font3)
        self.lineEdit_customer_gstin.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.horizontalLayout_31.addWidget(self.lineEdit_customer_gstin)

        self.lineEdit_suggest_rate = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_rate.setObjectName(u"lineEdit_suggest_rate")
        self.lineEdit_suggest_rate.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_suggest_rate.setFont(font3)
        self.lineEdit_suggest_rate.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")

        self.horizontalLayout_31.addWidget(self.lineEdit_suggest_rate)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_18)


        self.verticalLayout_15.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.table_item_table = QTableWidget(self.widget_graph_6)
        if (self.table_item_table.columnCount() < 8):
            self.table_item_table.setColumnCount(8)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setBackground(QColor(191, 191, 191));
        self.table_item_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setBackground(QColor(158, 158, 158));
        self.table_item_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setBackground(QColor(191, 191, 191));
        self.table_item_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setBackground(QColor(158, 158, 158));
        self.table_item_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setBackground(QColor(191, 191, 191));
        self.table_item_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setBackground(QColor(158, 158, 158));
        self.table_item_table.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setBackground(QColor(191, 191, 191));
        self.table_item_table.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setBackground(QColor(158, 158, 158));
        self.table_item_table.setHorizontalHeaderItem(7, __qtablewidgetitem31)
        if (self.table_item_table.rowCount() < 20):
            self.table_item_table.setRowCount(20)
        self.table_item_table.setObjectName(u"table_item_table")
        self.table_item_table.setMinimumSize(QSize(0, 274))
        self.table_item_table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.table_item_table.setStyleSheet(u"/* ===== Table Widget Style (Light Blue Theme) ===== */\n"
"#table_item_table {\n"
"    background-color: #f7f7f7; /* soft blue-white background */\n"
"    alternate-background-color: #e8f1ff;\n"
"    gridline-color: #b7c9f0;\n"
"  \n"
"    \n"
"    font: 10pt \"Segoe UI\";\n"
"    color: black;\n"
"    selection-background-color: #6ea6f8;\n"
"    selection-color: white;\n"
" border: 1px solid #e6e6e6;\n"
"   \n"
"}\n"
"\n"
"/* ===== Header Styling ===== */\n"
"#table_item_table QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: #1d2b4d;\n"
"    font-weight: 600;\n"
"    font-size: 10pt;\n"
"    border: 1px solid #9bb8ef;\n"
" \n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#table_item_table QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    co"
                        "lor: black;\n"
"}\n"
"\n"
"/* ===== Row Hover Highlight ===== */\n"
"#table_item_table::item:hover {\n"
"    background-color: #c8ddff;\n"
"    color: #12294d;\n"
"}\n"
"\n"
"/* ===== Selected Cell ===== */\n"
"#table_item_table::item:selected {\n"
"    background-color: #7aa3e6;\n"
"    color: black;\n"
"}\n"
"\n"
"/* ===== Vertical Scrollbar ===== */\n"
"#table_item_table QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ebf2ff;\n"
"    width: 10px;\n"
"    margin: 2px 0 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::handle:vertical {\n"
"    background: #5077ba;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::handle:vertical:hover {\n"
"    background: #496baa;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::add-line:vertical,\n"
"#table_item_table QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* ===== Horizontal Scrollbar ===== */\n"
"#table_item_table QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: "
                        "#ebf2ff;\n"
"    height: 10px;\n"
"    margin: 0 2px 0 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::handle:horizontal {\n"
"    background: #90b4ff;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::handle:horizontal:hover {\n"
"    background: #6e9fff;\n"
"}\n"
"\n"
"#table_item_table QScrollBar::add-line:horizontal,\n"
"#table_item_table QScrollBar::sub-line:horizontal {\n"
"    width: 0;\n"
"}\n"
"")
        self.table_item_table.setRowCount(20)
        self.table_item_table.setColumnCount(8)

        self.verticalLayout_15.addWidget(self.table_item_table)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.widget_graph_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 25))
        self.label_17.setMaximumSize(QSize(16777215, 25))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_17)

        self.lineEdit_bank_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_bank_name.setObjectName(u"lineEdit_bank_name")
        self.lineEdit_bank_name.setMinimumSize(QSize(200, 25))
        self.lineEdit_bank_name.setMaximumSize(QSize(500, 25))
        self.lineEdit_bank_name.setFont(font3)
        self.lineEdit_bank_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.verticalLayout_9.addWidget(self.lineEdit_bank_name)


        self.horizontalLayout_32.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_18 = QLabel(self.widget_graph_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 25))
        self.label_18.setMaximumSize(QSize(16777215, 25))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.label_18)

        self.lineEdit_account_number = QLineEdit(self.widget_graph_6)
        self.lineEdit_account_number.setObjectName(u"lineEdit_account_number")
        self.lineEdit_account_number.setMaximumSize(QSize(350, 30))
        self.lineEdit_account_number.setFont(font3)
        self.lineEdit_account_number.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.verticalLayout_10.addWidget(self.lineEdit_account_number)


        self.horizontalLayout_32.addLayout(self.verticalLayout_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_19 = QLabel(self.widget_graph_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 25))
        self.label_19.setMaximumSize(QSize(16777215, 25))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_19)

        self.lineEdit_ifsc_code = QLineEdit(self.widget_graph_6)
        self.lineEdit_ifsc_code.setObjectName(u"lineEdit_ifsc_code")
        self.lineEdit_ifsc_code.setMinimumSize(QSize(200, 25))
        self.lineEdit_ifsc_code.setMaximumSize(QSize(500, 25))
        self.lineEdit_ifsc_code.setFont(font3)
        self.lineEdit_ifsc_code.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.verticalLayout_11.addWidget(self.lineEdit_ifsc_code)


        self.horizontalLayout_33.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_20 = QLabel(self.widget_graph_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 25))
        self.label_20.setMaximumSize(QSize(16777215, 25))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.label_20)

        self.lineEdit_branch = QLineEdit(self.widget_graph_6)
        self.lineEdit_branch.setObjectName(u"lineEdit_branch")
        self.lineEdit_branch.setMinimumSize(QSize(200, 0))
        self.lineEdit_branch.setMaximumSize(QSize(350, 30))
        self.lineEdit_branch.setFont(font3)
        self.lineEdit_branch.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"     border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 0px; /* Rounded */")

        self.verticalLayout_12.addWidget(self.lineEdit_branch)


        self.horizontalLayout_33.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_34.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.toolButton_add_item_button = QToolButton(self.widget_graph_6)
        self.toolButton_add_item_button.setObjectName(u"toolButton_add_item_button")
        self.toolButton_add_item_button.setMinimumSize(QSize(100, 30))
        self.toolButton_add_item_button.setMaximumSize(QSize(16777215, 30))
        self.toolButton_add_item_button.setFont(font3)
        self.toolButton_add_item_button.setStyleSheet(u"QToolButton {\n"
"\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ebebeb, stop:1 #ffffff);\n"
"    color: black;\n"
"    border: none;\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 4px;\n"
"   \n"
"    \n"
"}\n"
"\n"
"QToolButton:hover {\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #ffffff, stop:1 #ffffff);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
" \n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f4f6fb, stop:1 #cbcbcb);\n"
"color: black;\n"
"  \n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.verticalLayout_14.addWidget(self.toolButton_add_item_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_14.addItem(self.verticalSpacer)


        self.horizontalLayout_34.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_35.addLayout(self.verticalLayout_15)


        self.horizontalLayout_48.addWidget(self.widget_graph_6)

        self.tabWidget_3.addTab(self.tab_4, "")

        self.horizontalLayout_49.addWidget(self.tabWidget_3)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, 6, -1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(331, 233))
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        self.tabWidget.setStyleSheet(u"/* Main Tab Widget */\n"
"#tabWidget::pane {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #edf2f7, stop:1 #dce4f2);\n"
"   \n"
"   \n"
"    \n"
"}\n"
"\n"
"/* Tabs - neutral background, rounded, soft hover */\n"
"#tabWidget QTabBar::tab {\n"
"    background-color: #5165a6; /* Dark Blue */\n"
"    color: white;\n"
"    padding: 2px 6px;\n"
"    margin-right: 6px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: 500;\n"
"    min-width: 100px;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-bottom: none;\n"
"   \n"
"}\n"
"\n"
"/* Selected tab - highlighted cleanly with shadow and bolder color */\n"
"#tabWidget QTabBar::tab:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c8ff, stop:1 #94b2e3);\n"
"    color: white;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;;\n"
"    font-weight: 600;\n"
" font: 11pt \"Segoe UI\";\n"
""
                        "   \n"
"}\n"
"\n"
"/* Hover (for non-selected tabs) - subtle lightening */\n"
"#tabWidget QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7c9bf1, stop:1 #7c9bf1);\n"
"    color: white;\n"
"    border: 1px solid #9fb0d6;\n"
"}\n"
"\n"
"/* TabBar base */\n"
"#tabWidget QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"  \n"
"}\n"
"\n"
"\n"
"#tabWidget QWidget {\n"
"    background-color: #c4dcff;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.tab)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(0, 0))
        self.calendarWidget.setStyleSheet(u"/* ==========================\n"
"   QCalendarWidget - Professional Soft Blue Theme\n"
"   ========================== */\n"
"\n"
"/* Overall calendar */\n"
"QCalendarWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f2f5fb, stop:1 #dce4f2);\n"
"    border: 1px solid #a7b4d0;\n"
"    \n"
"    font: 10pt \"Segoe UI\";\n"
"    color: #1f2937;\n"
"    selection-background-color: #5e85d7;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Navigation bar (Month & Year area) */\n"
"QCalendarWidget QToolButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #d4def3, stop:1 #b8c6e0);\n"
"    color: #1e2b4f;\n"
"    font: bold 10pt \"Segoe UI\";\n"
"    border: 1px solid #9eaed3;\n"
"    border-radius: 6px;\n"
"    \n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7ea2f7, stop:1 #5e85d7);\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Dropdown popup (month/year menu)"
                        " */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #f9fbff;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item {\n"
"\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: #8caefb;  /* Light blue highlight */\n"
"    color: white;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item:hover {\n"
"    background-color: #dbe6ff;  /* Soft hover blue */\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"/* Header row (days of the week) */\n"
"QCalendarWidget QHeaderView::section {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #b8c6e0, stop:1 #a7b4d0);\n"
"    color: #1f2937;\n"
"    font-weight: 600;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"/* Days grid */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background: #f7f9fc;\n"
"    alternate-background-color: #edf2f7;\n"
"    border: none;\n"
"    color: #1f2937;\n"
"    gridline-colo"
                        "r: #cfd9ec;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Day hover */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #dbe6ff;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Selected date */\n"
"QCalendarWidget QAbstractItemView::item:selected {\n"
"    background-color: #5e85d7;\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Highlight today\u2019s date */\n"
"QCalendarWidget QTableView::item:focus {\n"
"    border: 1px solid #5e85d7;\n"
"}\n"
"\n"
"/* Different color for weekends */\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item {\n"
"    \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item:enabled {\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item:enabled:!active {\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item:enabled:selected {\n"
"    color: whit"
                        "e;\n"
"}\n"
"\n"
"/* Spinbox (year selector) */\n"
"QCalendarWidget QSpinBox {\n"
"    background: #edf2f7;\n"
"    color: #1f2937;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
" \n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button,\n"
"QCalendarWidget QSpinBox::down-button {\n"
"    background: #c5d2ed;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button:hover,\n"
"QCalendarWidget QSpinBox::down-button:hover {\n"
"    background: #8caefb;\n"
"}\n"
"")
        self.calendarWidget.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)

        self.horizontalLayout.addWidget(self.calendarWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_51 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.textEdit_notes = QTextEdit(self.tab_2)
        self.textEdit_notes.setObjectName(u"textEdit_notes")
        self.textEdit_notes.setFont(font1)
        self.textEdit_notes.setAutoFillBackground(False)
        self.textEdit_notes.setStyleSheet(u"/* ===== QTextEdit - Professional Light Blue Theme ===== */\n"
"QTextEdit {\n"
"    background-color: #f4f6fb;   /* Soft blue-gray background */\n"
"    color: #1e1e1e;             /* Dark readable text */\n"
"    border: 1px solid #a0aec0;  /* Subtle neutral border */\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Blue highlight for selected text */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Hover Effect */\n"
"QTextEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Blue border on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"/* Focus Effect */\n"
"QTextEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green border when focused */\n"
"    background-color: #ffffff;  /* Clean white focus background */\n"
"    color: #000000;\n"
"}\n"
"")
        self.textEdit_notes.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_notes.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_notes.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_51.addWidget(self.textEdit_notes)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_21.addWidget(self.tabWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 215))
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.widget.setStyleSheet(u"#widget {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #a5b7d9;\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget:hover {\n"
"    background-color: #81a6e1;\n"
"    border: 1px solid #4e8df5;\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.horizontalLayout_42 = QHBoxLayout(self.widget)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_income_3 = QLabel(self.widget)
        self.label_income_3.setObjectName(u"label_income_3")
        self.label_income_3.setMaximumSize(QSize(16777215, 25))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(16)
        font6.setWeight(QFont.DemiBold)
        font6.setItalic(False)
        self.label_income_3.setFont(font6)
        self.label_income_3.setStyleSheet(u"color: #2d3e79;\n"
"font-weight: 600;")

        self.verticalLayout_20.addWidget(self.label_income_3)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_income_2 = QLabel(self.widget)
        self.label_income_2.setObjectName(u"label_income_2")
        self.label_income_2.setMaximumSize(QSize(16777215, 20))
        self.label_income_2.setFont(font2)

        self.horizontalLayout_37.addWidget(self.label_income_2)

        self.label_income = QLabel(self.widget)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setMaximumSize(QSize(16777215, 20))
        self.label_income.setFont(font2)

        self.horizontalLayout_37.addWidget(self.label_income)


        self.verticalLayout_18.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_expense_2 = QLabel(self.widget)
        self.label_expense_2.setObjectName(u"label_expense_2")
        self.label_expense_2.setMaximumSize(QSize(16777215, 20))
        self.label_expense_2.setFont(font2)

        self.horizontalLayout_38.addWidget(self.label_expense_2)

        self.label_expense = QLabel(self.widget)
        self.label_expense.setObjectName(u"label_expense")
        self.label_expense.setMaximumSize(QSize(16777215, 20))
        self.label_expense.setFont(font2)

        self.horizontalLayout_38.addWidget(self.label_expense)


        self.verticalLayout_18.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_savings_2 = QLabel(self.widget)
        self.label_savings_2.setObjectName(u"label_savings_2")
        self.label_savings_2.setMaximumSize(QSize(16777215, 20))
        self.label_savings_2.setFont(font2)
        self.label_savings_2.setStyleSheet(u"color: rgb(245, 249, 255);")

        self.horizontalLayout_39.addWidget(self.label_savings_2)

        self.label_savings = QLabel(self.widget)
        self.label_savings.setObjectName(u"label_savings")
        self.label_savings.setMaximumSize(QSize(16777215, 20))
        self.label_savings.setFont(font2)
        self.label_savings.setStyleSheet(u"color: rgb(245, 249, 255);")

        self.horizontalLayout_39.addWidget(self.label_savings)


        self.verticalLayout_18.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_gains_2 = QLabel(self.widget)
        self.label_gains_2.setObjectName(u"label_gains_2")
        self.label_gains_2.setMaximumSize(QSize(16777215, 20))
        self.label_gains_2.setFont(font2)
        self.label_gains_2.setStyleSheet(u"color: rgb(245, 249, 255);")

        self.horizontalLayout_40.addWidget(self.label_gains_2)

        self.label_gains = QLabel(self.widget)
        self.label_gains.setObjectName(u"label_gains")
        self.label_gains.setMaximumSize(QSize(16777215, 20))
        self.label_gains.setFont(font2)
        self.label_gains.setStyleSheet(u"color: rgb(245, 249, 255);")

        self.horizontalLayout_40.addWidget(self.label_gains)


        self.verticalLayout_18.addLayout(self.horizontalLayout_40)


        self.horizontalLayout_41.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_11)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setStyleSheet(u"background-color: rgb(196, 220, 255);")
        self.label_2.setPixmap(QPixmap(u"../../../../Users/Abhishek/.designer/template/pprofile2.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_2)

        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(16777215, 20))
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_name.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_name)


        self.horizontalLayout_41.addLayout(self.verticalLayout_17)


        self.verticalLayout_20.addLayout(self.horizontalLayout_41)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)

        self.label_gains_3 = QLabel(self.widget)
        self.label_gains_3.setObjectName(u"label_gains_3")
        self.label_gains_3.setMaximumSize(QSize(16777215, 20))
        self.label_gains_3.setFont(font2)
        self.label_gains_3.setStyleSheet(u"color: rgb(245, 249, 255);")

        self.verticalLayout_19.addWidget(self.label_gains_3)

        self.textEdit_notes_2 = QTextEdit(self.widget)
        self.textEdit_notes_2.setObjectName(u"textEdit_notes_2")
        self.textEdit_notes_2.setMinimumSize(QSize(0, 30))
        self.textEdit_notes_2.setFont(font1)
        self.textEdit_notes_2.setAutoFillBackground(False)
        self.textEdit_notes_2.setStyleSheet(u"/* ===== QTextEdit - Professional Light Blue Theme ===== */\n"
"QTextEdit {\n"
"    background-color: #f4f6fb;   /* Soft blue-gray background */\n"
"    color: #1e1e1e;             /* Dark readable text */\n"
"    border: 1px solid #a0aec0;  /* Subtle neutral border */\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    font: 14pt \"Cambria\";\n"
"    selection-background-color: #3a7bd5; /* Blue highlight for selected text */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Hover Effect */\n"
"QTextEdit:hover {\n"
"    border: 1px solid #3a7bd5;  /* Blue border on hover */\n"
"    background-color: #f0f4ff;  /* Slightly lighter background */\n"
"}\n"
"\n"
"/* Focus Effect */\n"
"QTextEdit:focus {\n"
"    border: 1px solid #2bb673;  /* Elegant green border when focused */\n"
"    background-color: #ffffff;  /* Clean white focus background */\n"
"    color: #000000;\n"
"}\n"
"")
        self.textEdit_notes_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_notes_2.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_notes_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_19.addWidget(self.textEdit_notes_2)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)


        self.horizontalLayout_42.addLayout(self.verticalLayout_20)


        self.verticalLayout_21.addWidget(self.widget)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(0, 235))
        self.tabWidget_2.setMaximumSize(QSize(400, 16777215))
        self.tabWidget_2.setStyleSheet(u"/* Main Tab Widget */\n"
"#tabWidget_2::pane {\n"
"    \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #edf2f7, stop:1 #dce4f2);\n"
"   \n"
"   \n"
"    \n"
"}\n"
"\n"
"/* Tabs - neutral background, rounded, soft hover */\n"
"#tabWidget_2 QTabBar::tab {\n"
"    background-color: #7287ca; /* Dark Blue */\n"
"    color: white;\n"
"    padding: 2px 6px;\n"
"    margin-right: 6px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: 500;\n"
"    min-width: 100px;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-bottom: none;\n"
"\n"
"\n"
"   \n"
"}\n"
"\n"
"/* Selected tab - highlighted cleanly with shadow and bolder color */\n"
"#tabWidget_2 QTabBar::tab:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c8ff, stop:1 #94b2e3);\n"
"    color: white;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;;\n"
"    font-weight: 600;\n"
" font: 12pt "
                        "\"Segoe UI\";\n"
"   \n"
"}\n"
"\n"
"/* Hover (for non-selected tabs) - subtle lightening */\n"
"#tabWidget_2 QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7c9bf1, stop:1 #7c9bf1);\n"
"    color: white;\n"
"    border: 1px solid #9fb0d6;\n"
"}\n"
"\n"
"/* TabBar base */\n"
"#tabWidget_2 QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"  \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_2.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_43 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_graph = QWidget(self.tab_5)
        self.widget_graph.setObjectName(u"widget_graph")
        self.widget_graph.setStyleSheet(u"#widget_graph {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #94b2e3;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_graph:hover {\n"
"    background-color: #81a6e1;\n"
"    border: 1px solid #4e8df5;\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_graph:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"}\n"
"")

        self.horizontalLayout_43.addWidget(self.widget_graph)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_44 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.widget_graph_2 = QWidget(self.tab_6)
        self.widget_graph_2.setObjectName(u"widget_graph_2")
        self.widget_graph_2.setStyleSheet(u"#widget_graph_2 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #94b2e3;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_graph_2:hover {\n"
"    background-color: #81a6e1;\n"
"    border: 1px solid #4e8df5;\n"
"}\n"
"\n"
"/* Optional focus / active effect */\n"
"#widget_graph_2:focus {\n"
"    border: 2px solid #2b6ef3;\n"
"    background-color: #ffffff;\n"
"}\n"
"")

        self.horizontalLayout_44.addWidget(self.widget_graph_2)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout_21.addWidget(self.tabWidget_2)


        self.horizontalLayout_49.addLayout(self.verticalLayout_21)


        self.verticalLayout_22.addLayout(self.horizontalLayout_49)


        self.horizontalLayout_50.addLayout(self.verticalLayout_22)

        form1.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(form1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1170, 33))
        self.menubar.setFont(font2)
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #7287ca;   /* Matches top frame */\n"
"    color: #ffffff;\n"
"    font: 11pt \"Segoe UI\";\n"
"    padding: 0px 4px;\n"
"    border-bottom: 1px solid #5d6b8d; /* Subtle divider */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 12px;\n"
"    margin: 2px;\n"
"    border-radius: 6px;\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #7c9bf1;   /* Light blue highlight */\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #e4ebf8;   /* Aqua click */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #e4ebf8;   /* Matches widget panels */\n"
"    color: #1e1e1e;\n"
"    border: 1px solid #7986ac;\n"
"    padding: 6px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 18px;\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #c6d4f5;  /* Soft selec"
                        "tion */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #a3b1d3;\n"
"    margin: 4px 10px;\n"
"}\n"
"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuSnap = QMenu(self.menubar)
        self.menuSnap.setObjectName(u"menuSnap")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setGeometry(QRect(486, 154, 150, 113))
        self.menuAbout.setFont(font3)
        form1.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuSnap.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionTable_Edit)
        self.menuEdit.addAction(self.actionClear_Data)
        self.menuEdit.addAction(self.actionArrange)
        self.menuExport.addAction(self.actionAs_CSV_Excel)
        self.menuSnap.addSeparator()
        self.menuSnap.addAction(self.action_screenshot)
        self.menuSnap.addAction(self.actionOpen_Directories)
        self.menuAbout.addAction(self.actionInfo)

        self.retranslateUi(form1)

        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form1)
    # setupUi

    def retranslateUi(self, form1):
        form1.setWindowTitle(QCoreApplication.translate("form1", u"Finance Flow v1.1", None))
        self.actionINR.setText(QCoreApplication.translate("form1", u"INR", None))
        self.actionOpen.setText(QCoreApplication.translate("form1", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("form1", u"Save Settings", None))
        self.actionSave_As.setText(QCoreApplication.translate("form1", u"Save Notes", None))
        self.actionExit.setText(QCoreApplication.translate("form1", u"Exit", None))
        self.action_screenshot.setText(QCoreApplication.translate("form1", u"ScreenShot", None))
        self.actionTable_Edit.setText(QCoreApplication.translate("form1", u"Table Edit", None))
        self.actionAs_CSV_Excel.setText(QCoreApplication.translate("form1", u"As CSV/Excel", None))
        self.actionOpen_Directories.setText(QCoreApplication.translate("form1", u"Open Directory", None))
        self.actionLight.setText(QCoreApplication.translate("form1", u"Light", None))
        self.actionDakr.setText(QCoreApplication.translate("form1", u"Dark", None))
        self.actionUSD.setText(QCoreApplication.translate("form1", u"USD", None))
        self.actionClear_Data.setText(QCoreApplication.translate("form1", u"Reset Data", None))
        self.actionRefresh.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.actionInfo.setText(QCoreApplication.translate("form1", u"Info", None))
        self.actionArrange.setText(QCoreApplication.translate("form1", u"Arrange", None))
        self.label_13.setText(QCoreApplication.translate("form1", u"Monthly Income:", None))
        self.lineEdit_income0.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income0.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.label_14.setText(QCoreApplication.translate("form1", u"Current Income:", None))
        self.lineEdit_income.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("form1", u"Default WorkSpace", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("form1", u"Sales", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("form1", u"Purchase", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("form1", u"Stock", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("form1", u"Banking Transactions", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("form1", u"GST-Auto", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("form1", u"0% GST", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("form1", u"5% GST", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("form1", u"12% GST", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("form1", u"18% GST", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("form1", u"28% GST", None))

        self.label_date.setText(QCoreApplication.translate("form1", u"Date:- 26/01/2001", None))
        self.label_calc.setText(QCoreApplication.translate("form1", u"Calc :", None))
        self.lineEdit_calc.setText("")
        self.lineEdit_calc.setPlaceholderText(QCoreApplication.translate("form1", u"Use Numkeys...", None))
        self.label_expense_record.setText(QCoreApplication.translate("form1", u"Purchases :-", None))
        self.toolButton_del_row.setText(QCoreApplication.translate("form1", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("form1", u"SPEND/-", None));
        ___qtablewidgetitem1 = self.tableWidget_1.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("form1", u"Item/Purpose", None));
        ___qtablewidgetitem2 = self.tableWidget_1.horizontalHeaderItem(4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("form1", u"Reciepent", None));
        ___qtablewidgetitem3 = self.tableWidget_1.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("form1", u"Time", None));
        self.lineEdit_spend.setText("")
        self.lineEdit_spend.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.lineEdit_item.setText("")
        self.lineEdit_item.setPlaceholderText(QCoreApplication.translate("form1", u"Item...", None))
        self.lineEdit_reciepent.setText("")
        self.lineEdit_reciepent.setPlaceholderText(QCoreApplication.translate("form1", u"Recipient..", None))
        self.toolButton_save1.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.label_total_expense.setText(QCoreApplication.translate("form1", u"Total monthly Spend = ", None))
        self.label_total_spends.setText(QCoreApplication.translate("form1", u"0", None))
        self.label_extra_gains.setText(QCoreApplication.translate("form1", u"Sales:-", None))
        self.toolButton_del_row_2.setText(QCoreApplication.translate("form1", u"Delete", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("form1", u"RECIEVED/-", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("form1", u"Item/N/A", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("form1", u"Payer/Giver", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("form1", u"Time", None));
        self.lineEdit_get.setText("")
        self.lineEdit_get.setPlaceholderText(QCoreApplication.translate("form1", u"Get/-", None))
        self.lineEdit_for_what.setText("")
        self.lineEdit_for_what.setPlaceholderText(QCoreApplication.translate("form1", u"for what...", None))
        self.lineEdit_giver.setText("")
        self.lineEdit_giver.setPlaceholderText(QCoreApplication.translate("form1", u"Giver...", None))
        self.toolButton_save2.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.label_monthly_gains.setText(QCoreApplication.translate("form1", u"Total monthly Sales = ", None))
        self.label_total_gains.setText(QCoreApplication.translate("form1", u"1600/-", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("form1", u"Sales and Purchases", None))
        self.label_extra_gains_2.setText(QCoreApplication.translate("form1", u"Transaction Record:-", None))
        self.toolButton_del_row_3.setText(QCoreApplication.translate("form1", u"Delete", None))
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("form1", u"RECIEVED/-", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("form1", u"Item/N/A", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("form1", u"Payer/Giver", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("form1", u"Time", None));
        self.lineEdit_get_2.setText("")
        self.lineEdit_get_2.setPlaceholderText(QCoreApplication.translate("form1", u"Get/-", None))
        self.lineEdit_for_what_2.setText("")
        self.lineEdit_for_what_2.setPlaceholderText(QCoreApplication.translate("form1", u"for what...", None))
        self.lineEdit_giver_2.setText("")
        self.lineEdit_giver_2.setPlaceholderText(QCoreApplication.translate("form1", u"Giver...", None))
        self.toolButton_save2_2.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.label_monthly_gains_2.setText(QCoreApplication.translate("form1", u"Total monthly Sales = ", None))
        self.label_total_gains_2.setText(QCoreApplication.translate("form1", u"1600/-", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("form1", u"Banking", None))
        self.label_extra_gains_3.setText(QCoreApplication.translate("form1", u"Stock Details:-", None))
        self.pushButton_save_button.setText(QCoreApplication.translate("form1", u"Save", None))
        self.pushButton_load_button.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.label_9.setText(QCoreApplication.translate("form1", u"Stock Name:", None))
        self.lineEdit_stock_name_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Stock Name", None))
        self.pushButton_add_stock_button.setText(QCoreApplication.translate("form1", u"Add Stock", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("form1", u"Per Day", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("form1", u"Per Week", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("form1", u"Per Month", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("form1", u"Per Year", None))

        self.label_10.setText(QCoreApplication.translate("form1", u"Search Stock:", None))
        self.lineEdit_search_stock_input.setPlaceholderText(QCoreApplication.translate("form1", u"Search Stock", None))
        self.pushButton_search_stock_button_.setText(QCoreApplication.translate("form1", u"Search", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete_stock_button.setToolTip(QCoreApplication.translate("form1", u"<html><head/><body><p>Shortcut: Ctrl+Del</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_stock_button.setText(QCoreApplication.translate("form1", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.pushButton_delete_stock_button.setShortcut(QCoreApplication.translate("form1", u"Ctrl+Del", None))
#endif // QT_CONFIG(shortcut)
        self.label_12.setText(QCoreApplication.translate("form1", u"Item Name:", None))
        self.lineEdit_item_name_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Item Name", None))
        self.label_24.setText(QCoreApplication.translate("form1", u"Search Items:", None))
        self.lineEdit_search_item_lineedit.setPlaceholderText(QCoreApplication.translate("form1", u"Search Items", None))
        self.pushButton_search_item_button_.setText(QCoreApplication.translate("form1", u"Search", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete_item_button.setToolTip(QCoreApplication.translate("form1", u"<html><head/><body><p>Shortcut: Del</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_item_button.setText(QCoreApplication.translate("form1", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.pushButton_delete_item_button.setShortcut(QCoreApplication.translate("form1", u"Del", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem12 = self.tableWidget_item_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("form1", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_item_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("form1", u"Rate (in Rs)", None));
        ___qtablewidgetitem14 = self.tableWidget_item_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("form1", u"Quantity", None));
        self.label_15.setText(QCoreApplication.translate("form1", u"Rate:", None))
        self.lineEdit_item_rate_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Item Rate (Rs/-)", None))
        self.label_16.setText(QCoreApplication.translate("form1", u"Quantity:", None))
        self.lineEdit_item_quantity_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Quantity (Default:1)", None))
        self.pushButton_add_item_button.setText(QCoreApplication.translate("form1", u"Add Item", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("form1", u"Stock Details", None))
        self.label_25.setText(QCoreApplication.translate("form1", u"Products with Description", None))
        self.pushButton_open_product_image.setText(QCoreApplication.translate("form1", u"Open Product Image", None))
#if QT_CONFIG(shortcut)
        self.pushButton_open_product_image.setShortcut(QCoreApplication.translate("form1", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_refresh_image_grid.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.label_image_show.setText(QCoreApplication.translate("form1", u"                 Product Image", None))
        self.textEdit_image_description.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Product Description here...", None))
        self.pushButton_show_product_folder.setText(QCoreApplication.translate("form1", u"Show Folder", None))
        self.pushButton_save_description.setText(QCoreApplication.translate("form1", u"Save in Products", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("form1", u"Products", None))
        self.label_21.setText(QCoreApplication.translate("form1", u"IINVOICE RECIEPT", None))
        self.toolButton_save_button.setText(QCoreApplication.translate("form1", u"Export", None))
        self.label_3.setText(QCoreApplication.translate("form1", u"Your Shop Name:   ", None))
        self.lineEdit_shop_name.setPlaceholderText("")
        self.label_suggest_qty.setText(QCoreApplication.translate("form1", u"#Testing Total Quantity", None))
        self.label_4.setText(QCoreApplication.translate("form1", u"Your Shop Address:", None))
        self.lineEdit_suggest_item.setPlaceholderText(QCoreApplication.translate("form1", u"Type Item", None))
        self.label_5.setText(QCoreApplication.translate("form1", u"Your Shop GSTIN:   ", None))
        self.lineEdit_suggest_quantity.setPlaceholderText(QCoreApplication.translate("form1", u"Qty", None))
        self.label_6.setText(QCoreApplication.translate("form1", u"Customer Name:    ", None))
        self.label_7.setText(QCoreApplication.translate("form1", u"Customer Address: ", None))
        self.label_8.setText(QCoreApplication.translate("form1", u"Customer GSTIN:    ", None))
        self.lineEdit_suggest_rate.setPlaceholderText(QCoreApplication.translate("form1", u"Rate", None))
        ___qtablewidgetitem15 = self.table_item_table.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("form1", u"Description", None));
        ___qtablewidgetitem16 = self.table_item_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("form1", u"HSN Code", None));
        ___qtablewidgetitem17 = self.table_item_table.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("form1", u"Quantity", None));
        ___qtablewidgetitem18 = self.table_item_table.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("form1", u"Rate", None));
        ___qtablewidgetitem19 = self.table_item_table.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("form1", u"GST Rate (%)", None));
        ___qtablewidgetitem20 = self.table_item_table.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("form1", u"CGST", None));
        ___qtablewidgetitem21 = self.table_item_table.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("form1", u"SGST", None));
        ___qtablewidgetitem22 = self.table_item_table.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("form1", u"Total", None));
        self.label_17.setText(QCoreApplication.translate("form1", u"Bank Name:", None))
        self.label_18.setText(QCoreApplication.translate("form1", u"Account Number:", None))
        self.label_19.setText(QCoreApplication.translate("form1", u"IFSC Code:", None))
        self.label_20.setText(QCoreApplication.translate("form1", u"Branch:", None))
        self.toolButton_add_item_button.setText(QCoreApplication.translate("form1", u"Add Item", None))
#if QT_CONFIG(shortcut)
        self.toolButton_add_item_button.setShortcut(QCoreApplication.translate("form1", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("form1", u"Sale Bill", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("form1", u"Calender", None))
        self.textEdit_notes.setHtml(QCoreApplication.translate("form1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p></body></html>", None))
        self.textEdit_notes.setPlaceholderText(QCoreApplication.translate("form1", u"Notes...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("form1", u"Notes", None))
        self.label_income_3.setText(QCoreApplication.translate("form1", u"# Current Summary Report", None))
        self.label_income_2.setText(QCoreApplication.translate("form1", u"1. Total Income", None))
        self.label_income.setText(QCoreApplication.translate("form1", u"64000/-", None))
        self.label_expense_2.setText(QCoreApplication.translate("form1", u"2. Total Expense", None))
        self.label_expense.setText(QCoreApplication.translate("form1", u"45000", None))
        self.label_savings_2.setText(QCoreApplication.translate("form1", u"3. Net Savings", None))
        self.label_savings.setText(QCoreApplication.translate("form1", u"15000", None))
        self.label_gains_2.setText(QCoreApplication.translate("form1", u"4. Extra Gains", None))
        self.label_gains.setText(QCoreApplication.translate("form1", u"4000", None))
        self.label_2.setText("")
        self.label_name.setText(QCoreApplication.translate("form1", u"Abhishek Verma", None))
        self.label_gains_3.setText(QCoreApplication.translate("form1", u"5. Miscellaneous Expenses", None))
        self.textEdit_notes_2.setHtml(QCoreApplication.translate("form1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p></body></html>", None))
        self.textEdit_notes_2.setPlaceholderText(QCoreApplication.translate("form1", u"Notes...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("form1", u"Remaining income", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("form1", u"Extra Gains", None))
        self.menuFile.setTitle(QCoreApplication.translate("form1", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("form1", u"Edit", None))
        self.menuExport.setTitle(QCoreApplication.translate("form1", u"Export", None))
        self.menuSnap.setTitle(QCoreApplication.translate("form1", u"Snap", None))
        self.menuAbout.setStyleSheet(QCoreApplication.translate("form1", u"background-color: rgb(232, 232, 232);\n"
"color: rgb(0, 0, 0);", None))
        self.menuAbout.setTitle(QCoreApplication.translate("form1", u"About", None))
    # retranslateUi

