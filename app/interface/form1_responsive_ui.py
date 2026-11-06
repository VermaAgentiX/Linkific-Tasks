# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form1_responsive.ui'
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
    QFrame, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolButton, QWidget)

class Ui_form1(object):
    def setupUi(self, form1):
        if not form1.objectName():
            form1.setObjectName(u"form1")
        form1.resize(1500, 1010)
        form1.setMinimumSize(QSize(1160, 432))
        form1.setMaximumSize(QSize(1920, 1080))
        form1.setStyleSheet(u"QMainWindow {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(196, 220, 255);\n"
"    color: #f8fafc;\n"
"    font-family: \"Segoe UI\", system-ui;\n"
"}")
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(1160, 39, 331, 261))
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
"\n"
"\n"
"   \n"
"}\n"
"\n"
"/* Selected tab - highlighted cleanly with shadow and bolder color */\n"
"#tabWidget QTabBar::tab:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c8ff, stop:1 #96b4e6);\n"
"    color: white;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;;\n"
"    font-weight: 600;\n"
"    box-shadow: 0 "
                        "2px 4px rgba(0, 0, 0, 0.25);\n"
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
"#tabWidget_2 QWidget {\n"
"    background-color: #c4dcff;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 371, 238))
        self.widget.setStyleSheet(u"background-color: rgb(149, 179, 228);")
        self.calendarWidget = QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 0, 331, 238))
        self.calendarWidget.setStyleSheet(u"/* ==========================\n"
"   QCalendarWidget - Professional Soft Blue Theme\n"
"   ========================== */\n"
"\n"
"/* Overall calendar */\n"
"QCalendarWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f2f5fb, stop:1 #dce4f2);\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 8px;\n"
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
"    padding: 4px 10px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7ea2f7, stop:1 #5e85d7);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Remov"
                        "e arrow indicator from dropdown */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Dropdown popup (month/year menu) */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #f9fbff;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: #1f2937;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item {\n"
"    padding: 6px 12px;\n"
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
"    padding: 6px 0;\n"
"}\n"
"\n"
""
                        "/* Days grid */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background: #f7f9fc;\n"
"    alternate-background-color: #edf2f7;\n"
"    border: none;\n"
"    color: #1f2937;\n"
"    gridline-color: #cfd9ec;\n"
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
"    margin: 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item:enabled {\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"QCalendarWidget QW"
                        "idget#qt_calendar_calendarview QTableView::item:enabled:!active {\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_calendarview QTableView::item:enabled:selected {\n"
"    color: white;\n"
"}\n"
"\n"
"/* Spinbox (year selector) */\n"
"QCalendarWidget QSpinBox {\n"
"    background: #edf2f7;\n"
"    color: #1f2937;\n"
"    border: 1px solid #a7b4d0;\n"
"    border-radius: 6px;\n"
"    padding: 2px 6px;\n"
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_notes = QTextEdit(self.tab_2)
        self.textEdit_notes.setObjectName(u"textEdit_notes")
        self.textEdit_notes.setGeometry(QRect(0, 0, 331, 238))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.textEdit_notes.setFont(font)
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
        self.tabWidget.addTab(self.tab_2, "")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(12, 4, 121, 25))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(1160, 309, 331, 251))
        self.textEdit.setStyleSheet(u"background-color: rgb(150, 180, 230);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(1360, 450, 131, 51))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_name.setWordWrap(True)
        self.label_income = QLabel(self.centralwidget)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setGeometry(QRect(1274, 356, 91, 20))
        self.label_income.setFont(font2)
        self.label_expense = QLabel(self.centralwidget)
        self.label_expense.setObjectName(u"label_expense")
        self.label_expense.setGeometry(QRect(1274, 376, 91, 20))
        self.label_expense.setFont(font2)
        self.label_savings = QLabel(self.centralwidget)
        self.label_savings.setObjectName(u"label_savings")
        self.label_savings.setGeometry(QRect(1274, 396, 91, 20))
        self.label_savings.setFont(font2)
        self.label_savings.setStyleSheet(u"color: rgb(245, 249, 255);")
        self.label_gains = QLabel(self.centralwidget)
        self.label_gains.setObjectName(u"label_gains")
        self.label_gains.setGeometry(QRect(1274, 416, 91, 20))
        self.label_gains.setFont(font2)
        self.label_gains.setStyleSheet(u"color: rgb(245, 249, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1379, 350, 91, 81))
        self.label_2.setStyleSheet(u"background-color: rgb(196, 220, 255);")
        self.label_2.setPixmap(QPixmap(u"../../../../Users/Abhishek/.designer/template/pprofile2.png"))
        self.label_2.setScaledContents(True)
        self.lineEdit_income = QLineEdit(self.centralwidget)
        self.lineEdit_income.setObjectName(u"lineEdit_income")
        self.lineEdit_income.setGeometry(QRect(432, 5, 171, 26))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_income.sizePolicy().hasHeightForWidth())
        self.lineEdit_income.setSizePolicy(sizePolicy)
        self.lineEdit_income.setMinimumSize(QSize(0, 0))
        self.lineEdit_income.setMaximumSize(QSize(1920, 70))
        self.lineEdit_income.setFont(font)
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
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(801, 5, 111, 26))
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
        self.lineEdit_calc = QLineEdit(self.centralwidget)
        self.lineEdit_calc.setObjectName(u"lineEdit_calc")
        self.lineEdit_calc.setGeometry(QRect(1340, 5, 151, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_calc.sizePolicy().hasHeightForWidth())
        self.lineEdit_calc.setSizePolicy(sizePolicy)
        self.lineEdit_calc.setMinimumSize(QSize(0, 0))
        self.lineEdit_calc.setMaximumSize(QSize(1920, 70))
        self.lineEdit_calc.setFont(font)
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
        self.label_calc = QLabel(self.centralwidget)
        self.label_calc.setObjectName(u"label_calc")
        self.label_calc.setGeometry(QRect(1077, 3, 261, 25))
        self.label_calc.setFont(font1)
        self.label_calc.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")
        self.label_calc.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(312, 4, 121, 25))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")
        self.lineEdit_income0 = QLineEdit(self.centralwidget)
        self.lineEdit_income0.setObjectName(u"lineEdit_income0")
        self.lineEdit_income0.setGeometry(QRect(136, 5, 167, 26))
        sizePolicy.setHeightForWidth(self.lineEdit_income0.sizePolicy().hasHeightForWidth())
        self.lineEdit_income0.setSizePolicy(sizePolicy)
        self.lineEdit_income0.setMinimumSize(QSize(0, 0))
        self.lineEdit_income0.setMaximumSize(QSize(1920, 70))
        self.lineEdit_income0.setFont(font)
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
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(1160, 567, 331, 238))
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
"\n"
"\n"
"   \n"
"}\n"
"\n"
"/* Selected tab - highlighted cleanly with shadow and bolder color */\n"
"#tabWidget_2 QTabBar::tab:selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c8ff, stop:1 #96b4e6);\n"
"    color: white;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;;\n"
"    font-weight: 600;\n"
"    box-shad"
                        "ow: 0 2px 4px rgba(0, 0, 0, 0.25);\n"
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
"#tabWidget_2 QWidget {\n"
"    background-color: #c4dcff;\n"
"}\n"
"")
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_2.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.widget_graph = QWidget(self.tab_5)
        self.widget_graph.setObjectName(u"widget_graph")
        self.widget_graph.setGeometry(QRect(0, -10, 331, 238))
        self.widget_graph.setStyleSheet(u"background-color: rgb(228, 235, 248);")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.widget_graph_2 = QWidget(self.tab_6)
        self.widget_graph_2.setObjectName(u"widget_graph_2")
        self.widget_graph_2.setGeometry(QRect(0, 0, 331, 221))
        self.widget_graph_2.setStyleSheet(u"background-color: rgb(228, 235, 248);")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(611, 5, 181, 26))
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
        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 40, 1140, 771))
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
"    background-color: #7287ca; /* Dark Blue */\n"
"    color: white;\n"
"    padding: 4px 10px;\n"
"    margin-right: 6px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    \n"
"    min-width: 100px;\n"
"    border: 1px solid #a7b4d0;\n"
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
"    color: white;\n"
"    border: 1px solid #96b4e6;\n"
"border-bottom: 1px solid #96b4e6;;\n"
"    font-weight: 600;\n"
" font: 12pt \"Segoe UI\";\n"
""
                        "   \n"
"}\n"
"\n"
"/* Hover (for non-selected tabs) - subtle lightening */\n"
"#tabWidget_3 QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #7c9bf1, stop:1 #7c9bf1);\n"
"    color: white;\n"
"    border: 1px solid #9fb0d6;\n"
"}\n"
"\n"
"/* TabBar base */\n"
"#tabWidget_3 QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"  \n"
"}\n"
"\n"
"\n"
"#tabWidget_3 QWidget {\n"
"    background-color: #c4dcff;\n"
"}\n"
"")
        self.tabWidget_3.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget_3.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_3.setDocumentMode(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.widget_5 = QWidget(self.tab_7)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, -1, 1141, 364))
        self.widget_5.setStyleSheet(u"\n"
"#widget_5 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #a5b7d9;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"}\n"
"\n"
"/* Add subtle shadow feel */\n"
"#widget_5:hover {\n"
"    background-color: #81a6e1;\n"
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
"    border-bottom-right-radius: 8px"
                        "; /* Rounded */\n"
"}\n"
"")
        self.label_expense_record = QLabel(self.widget_5)
        self.label_expense_record.setObjectName(u"label_expense_record")
        self.label_expense_record.setGeometry(QRect(10, 3, 181, 25))
        self.label_expense_record.setFont(font2)
        self.label_expense_record.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_total_expense = QLabel(self.widget_5)
        self.label_total_expense.setObjectName(u"label_total_expense")
        self.label_total_expense.setGeometry(QRect(740, 330, 191, 31))
        self.label_total_expense.setFont(font2)
        self.label_total_expense.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_total_spends = QLabel(self.widget_5)
        self.label_total_spends.setObjectName(u"label_total_spends")
        self.label_total_spends.setGeometry(QRect(972, 333, 151, 21))
        self.label_total_spends.setFont(font2)
        self.label_total_spends.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
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
        if (self.tableWidget_1.rowCount() < 9):
            self.tableWidget_1.setRowCount(9)
        self.tableWidget_1.setObjectName(u"tableWidget_1")
        self.tableWidget_1.setGeometry(QRect(10, 40, 1121, 287))
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
"    padding: 6px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_1 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ff"
                        "ffff;\n"
"}\n"
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
"    height: 10px;"
                        "\n"
"    margin: 0 2px 0 2px;\n"
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
        self.tableWidget_1.setRowCount(9)
        self.tableWidget_1.setColumnCount(7)
        self.tableWidget_1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_1.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_1.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_1.verticalHeader().setStretchLastSection(False)
        self.lineEdit_spend = QLineEdit(self.widget_5)
        self.lineEdit_spend.setObjectName(u"lineEdit_spend")
        self.lineEdit_spend.setGeometry(QRect(10, 333, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_spend.sizePolicy().hasHeightForWidth())
        self.lineEdit_spend.setSizePolicy(sizePolicy)
        self.lineEdit_spend.setMinimumSize(QSize(0, 0))
        self.lineEdit_spend.setMaximumSize(QSize(1920, 70))
        self.lineEdit_spend.setFont(font)
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
        self.toolButton_save1 = QToolButton(self.widget_5)
        self.toolButton_save1.setObjectName(u"toolButton_save1")
        self.toolButton_save1.setGeometry(QRect(670, 333, 61, 26))
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
        self.lineEdit_item = QLineEdit(self.widget_5)
        self.lineEdit_item.setObjectName(u"lineEdit_item")
        self.lineEdit_item.setGeometry(QRect(137, 333, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_item.sizePolicy().hasHeightForWidth())
        self.lineEdit_item.setSizePolicy(sizePolicy)
        self.lineEdit_item.setMinimumSize(QSize(0, 0))
        self.lineEdit_item.setMaximumSize(QSize(1920, 70))
        self.lineEdit_item.setFont(font)
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
        self.lineEdit_reciepent = QLineEdit(self.widget_5)
        self.lineEdit_reciepent.setObjectName(u"lineEdit_reciepent")
        self.lineEdit_reciepent.setGeometry(QRect(253, 333, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_reciepent.sizePolicy().hasHeightForWidth())
        self.lineEdit_reciepent.setSizePolicy(sizePolicy)
        self.lineEdit_reciepent.setMinimumSize(QSize(0, 0))
        self.lineEdit_reciepent.setMaximumSize(QSize(1920, 70))
        self.lineEdit_reciepent.setFont(font)
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
        self.toolButton_del_row = QToolButton(self.widget_5)
        self.toolButton_del_row.setObjectName(u"toolButton_del_row")
        self.toolButton_del_row.setGeometry(QRect(1072, 7, 60, 26))
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
        self.label_expense_record.raise_()
        self.label_total_expense.raise_()
        self.label_total_spends.raise_()
        self.lineEdit_spend.raise_()
        self.toolButton_save1.raise_()
        self.lineEdit_item.raise_()
        self.lineEdit_reciepent.raise_()
        self.toolButton_del_row.raise_()
        self.tableWidget_1.raise_()
        self.widget_6 = QWidget(self.tab_7)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 370, 1140, 371))
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
        self.label_extra_gains = QLabel(self.widget_6)
        self.label_extra_gains.setObjectName(u"label_extra_gains")
        self.label_extra_gains.setGeometry(QRect(14, 4, 111, 19))
        self.label_extra_gains.setFont(font2)
        self.label_extra_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_monthly_gains = QLabel(self.widget_6)
        self.label_monthly_gains.setObjectName(u"label_monthly_gains")
        self.label_monthly_gains.setGeometry(QRect(740, 334, 201, 31))
        self.label_monthly_gains.setFont(font2)
        self.label_monthly_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_total_gains = QLabel(self.widget_6)
        self.label_total_gains.setObjectName(u"label_total_gains")
        self.label_total_gains.setGeometry(QRect(950, 339, 171, 21))
        self.label_total_gains.setFont(font2)
        self.label_total_gains.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
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
        self.tableWidget_2.setGeometry(QRect(10, 40, 1121, 293))
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
"    padding: 6px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_2 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ff"
                        "ffff;\n"
"}\n"
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
"    height: 10px;"
                        "\n"
"    margin: 0 2px 0 2px;\n"
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
        self.lineEdit_get = QLineEdit(self.widget_6)
        self.lineEdit_get.setObjectName(u"lineEdit_get")
        self.lineEdit_get.setGeometry(QRect(10, 339, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_get.sizePolicy().hasHeightForWidth())
        self.lineEdit_get.setSizePolicy(sizePolicy)
        self.lineEdit_get.setMinimumSize(QSize(0, 0))
        self.lineEdit_get.setMaximumSize(QSize(1920, 70))
        self.lineEdit_get.setFont(font)
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
        self.toolButton_save2 = QToolButton(self.widget_6)
        self.toolButton_save2.setObjectName(u"toolButton_save2")
        self.toolButton_save2.setGeometry(QRect(670, 339, 61, 26))
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
        self.lineEdit_for_what = QLineEdit(self.widget_6)
        self.lineEdit_for_what.setObjectName(u"lineEdit_for_what")
        self.lineEdit_for_what.setGeometry(QRect(137, 339, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_for_what.sizePolicy().hasHeightForWidth())
        self.lineEdit_for_what.setSizePolicy(sizePolicy)
        self.lineEdit_for_what.setMinimumSize(QSize(0, 0))
        self.lineEdit_for_what.setMaximumSize(QSize(1920, 70))
        self.lineEdit_for_what.setFont(font)
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
        self.lineEdit_giver = QLineEdit(self.widget_6)
        self.lineEdit_giver.setObjectName(u"lineEdit_giver")
        self.lineEdit_giver.setGeometry(QRect(253, 339, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_giver.sizePolicy().hasHeightForWidth())
        self.lineEdit_giver.setSizePolicy(sizePolicy)
        self.lineEdit_giver.setMinimumSize(QSize(0, 0))
        self.lineEdit_giver.setMaximumSize(QSize(1920, 70))
        self.lineEdit_giver.setFont(font)
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
        self.toolButton_del_row_2 = QToolButton(self.widget_6)
        self.toolButton_del_row_2.setObjectName(u"toolButton_del_row_2")
        self.toolButton_del_row_2.setGeometry(QRect(1072, 7, 60, 26))
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
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.widget_7 = QWidget(self.tab_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, -1, 1140, 741))
        self.widget_7.setStyleSheet(u"\n"
"#widget_7 {\n"
"    \n"
"	background-color: rgb(148, 178, 227);\n"
"    border: 1px solid #a5b7d9;\n"
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
        self.label_extra_gains_2 = QLabel(self.widget_7)
        self.label_extra_gains_2.setObjectName(u"label_extra_gains_2")
        self.label_extra_gains_2.setGeometry(QRect(10, 3, 181, 25))
        self.label_extra_gains_2.setFont(font2)
        self.label_extra_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_monthly_gains_2 = QLabel(self.widget_7)
        self.label_monthly_gains_2.setObjectName(u"label_monthly_gains_2")
        self.label_monthly_gains_2.setGeometry(QRect(740, 705, 201, 31))
        self.label_monthly_gains_2.setFont(font2)
        self.label_monthly_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_total_gains_2 = QLabel(self.widget_7)
        self.label_total_gains_2.setObjectName(u"label_total_gains_2")
        self.label_total_gains_2.setGeometry(QRect(950, 710, 171, 21))
        self.label_total_gains_2.setFont(font2)
        self.label_total_gains_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
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
        self.tableWidget_3.setGeometry(QRect(10, 40, 1121, 664))
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
"    padding: 6px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_3 QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
"    color: #ff"
                        "ffff;\n"
"}\n"
"\n"
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
"    height: 10px;"
                        "\n"
"    margin: 0 2px 0 2px;\n"
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
        self.lineEdit_get_2 = QLineEdit(self.widget_7)
        self.lineEdit_get_2.setObjectName(u"lineEdit_get_2")
        self.lineEdit_get_2.setGeometry(QRect(10, 710, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_get_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_get_2.setSizePolicy(sizePolicy)
        self.lineEdit_get_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_get_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_get_2.setFont(font)
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
        self.toolButton_save2_2 = QToolButton(self.widget_7)
        self.toolButton_save2_2.setObjectName(u"toolButton_save2_2")
        self.toolButton_save2_2.setGeometry(QRect(670, 710, 61, 26))
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
        self.lineEdit_for_what_2 = QLineEdit(self.widget_7)
        self.lineEdit_for_what_2.setObjectName(u"lineEdit_for_what_2")
        self.lineEdit_for_what_2.setGeometry(QRect(137, 710, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_for_what_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_for_what_2.setSizePolicy(sizePolicy)
        self.lineEdit_for_what_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_for_what_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_for_what_2.setFont(font)
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
        self.lineEdit_giver_2 = QLineEdit(self.widget_7)
        self.lineEdit_giver_2.setObjectName(u"lineEdit_giver_2")
        self.lineEdit_giver_2.setGeometry(QRect(253, 710, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_giver_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_giver_2.setSizePolicy(sizePolicy)
        self.lineEdit_giver_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_giver_2.setMaximumSize(QSize(1920, 70))
        self.lineEdit_giver_2.setFont(font)
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
        self.toolButton_del_row_3 = QToolButton(self.widget_7)
        self.toolButton_del_row_3.setObjectName(u"toolButton_del_row_3")
        self.toolButton_del_row_3.setGeometry(QRect(1072, 7, 60, 26))
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
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.widget_2 = QWidget(self.tab_10)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1140, 740))
        self.widget_2.setStyleSheet(u"background-color: #96b4e6;\n"
"\n"
"\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 110, 1120, 622))
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
        self.listWidget_stock_list = QListWidget(self.widget_3)
        self.listWidget_stock_list.setObjectName(u"listWidget_stock_list")
        self.listWidget_stock_list.setGeometry(QRect(10, 40, 435, 541))
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
        self.tableWidget_item_table.setGeometry(QRect(454, 40, 661, 541))
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
"    \n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"/* ===== Hover effect on header ===== */\n"
"#tableWidget_item_table QHeaderView::section:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #a6c5ff, stop:1 #8db4ff);\n"
""
                        "    color: #ffffff;\n"
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
"    background: #c4dcff;\n"
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
"#tableWidget_item_table QScrollBar"
                        ":horizontal {\n"
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
"")
        self.tableWidget_item_table.setRowCount(18)
        self.pushButton_search_item_button_ = QPushButton(self.widget_3)
        self.pushButton_search_item_button_.setObjectName(u"pushButton_search_item_button_")
        self.pushButton_search_item_button_.setGeometry(QRect(776, 7, 61, 26))
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
        self.lineEdit_search_item_lineedit = QLineEdit(self.widget_3)
        self.lineEdit_search_item_lineedit.setObjectName(u"lineEdit_search_item_lineedit")
        self.lineEdit_search_item_lineedit.setGeometry(QRect(544, 7, 225, 26))
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
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(448, 9, 91, 21))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.lineEdit_search_stock_input = QLineEdit(self.widget_3)
        self.lineEdit_search_stock_input.setObjectName(u"lineEdit_search_stock_input")
        self.lineEdit_search_stock_input.setGeometry(QRect(101, 7, 206, 26))
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
        self.pushButton_search_stock_button_ = QPushButton(self.widget_3)
        self.pushButton_search_stock_button_.setObjectName(u"pushButton_search_stock_button_")
        self.pushButton_search_stock_button_.setGeometry(QRect(313, 7, 61, 26))
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
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(6, 9, 92, 21))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.pushButton_delete_item_button = QPushButton(self.widget_3)
        self.pushButton_delete_item_button.setObjectName(u"pushButton_delete_item_button")
        self.pushButton_delete_item_button.setGeometry(QRect(1053, 7, 60, 26))
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
        self.pushButton_delete_stock_button = QPushButton(self.widget_3)
        self.pushButton_delete_stock_button.setObjectName(u"pushButton_delete_stock_button")
        self.pushButton_delete_stock_button.setGeometry(QRect(380, 7, 60, 26))
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
        self.pushButton_add_item_button = QPushButton(self.widget_3)
        self.pushButton_add_item_button.setObjectName(u"pushButton_add_item_button")
        self.pushButton_add_item_button.setGeometry(QRect(984, 588, 131, 26))
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
        self.lineEdit_item_rate_input = QLineEdit(self.widget_3)
        self.lineEdit_item_rate_input.setObjectName(u"lineEdit_item_rate_input")
        self.lineEdit_item_rate_input.setGeometry(QRect(490, 588, 181, 26))
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
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 590, 81, 21))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.lineEdit_item_quantity_input = QLineEdit(self.widget_3)
        self.lineEdit_item_quantity_input.setObjectName(u"lineEdit_item_quantity_input")
        self.lineEdit_item_quantity_input.setGeometry(QRect(746, 588, 227, 26))
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
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(680, 592, 71, 21))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(450, 592, 41, 21))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.lineEdit_item_name_input = QLineEdit(self.widget_3)
        self.lineEdit_item_name_input.setObjectName(u"lineEdit_item_name_input")
        self.lineEdit_item_name_input.setGeometry(QRect(94, 588, 349, 26))
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
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 40, 1120, 51))
        self.widget_4.setStyleSheet(u"background-color: #eaf1fb;\n"
"color: rgb(0, 0, 0);\n"
" border-radius: 10px;")
        self.pushButton_add_stock_button = QPushButton(self.widget_4)
        self.pushButton_add_stock_button.setObjectName(u"pushButton_add_stock_button")
        self.pushButton_add_stock_button.setGeometry(QRect(510, 10, 121, 31))
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
        self.lineEdit_stock_name_input = QLineEdit(self.widget_4)
        self.lineEdit_stock_name_input.setObjectName(u"lineEdit_stock_name_input")
        self.lineEdit_stock_name_input.setGeometry(QRect(118, 13, 381, 26))
        self.lineEdit_stock_name_input.setFont(font)
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
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(18, 16, 91, 21))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comboBox_5 = QComboBox(self.widget_4)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(890, 10, 221, 30))
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
        self.label_extra_gains_3 = QLabel(self.widget_2)
        self.label_extra_gains_3.setObjectName(u"label_extra_gains_3")
        self.label_extra_gains_3.setGeometry(QRect(10, 3, 181, 25))
        self.label_extra_gains_3.setFont(font2)
        self.label_extra_gains_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(740, 92, 101, 16))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(190, 92, 71, 16))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(37, 56, 86,0);")
        self.pushButton_load_button = QPushButton(self.widget_2)
        self.pushButton_load_button.setObjectName(u"pushButton_load_button")
        self.pushButton_load_button.setGeometry(QRect(1060, 7, 71, 28))
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
        self.pushButton_save_button = QPushButton(self.widget_2)
        self.pushButton_save_button.setObjectName(u"pushButton_save_button")
        self.pushButton_save_button.setGeometry(QRect(980, 7, 71, 28))
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
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.widget_8 = QWidget(self.tab_11)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1141, 751))
        self.widget_8.setStyleSheet(u"background-color: #96b4e6;\n"
"")
        self.scrollArea_image_grid = QScrollArea(self.widget_8)
        self.scrollArea_image_grid.setObjectName(u"scrollArea_image_grid")
        self.scrollArea_image_grid.setGeometry(QRect(10, 40, 801, 691))
        self.scrollArea_image_grid.setStyleSheet(u"\n"
"background-color: rgb(165, 187, 230);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;")
        self.scrollArea_image_grid.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 799, 689))
        self.scrollArea_image_grid.setWidget(self.scrollAreaWidgetContents)
        self.label_image_show = QLabel(self.widget_8)
        self.label_image_show.setObjectName(u"label_image_show")
        self.label_image_show.setGeometry(QRect(820, 40, 310, 371))
        self.label_image_show.setFont(font2)
        self.label_image_show.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_image_show.setAutoFillBackground(False)
        self.label_image_show.setStyleSheet(u"background-color: rgb(228, 235, 248);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;\n"
"color: rgb(0, 0, 0);")
        self.label_image_show.setFrameShape(QFrame.Shape.Box)
        self.label_image_show.setScaledContents(False)
        self.textEdit_image_description = QTextEdit(self.widget_8)
        self.textEdit_image_description.setObjectName(u"textEdit_image_description")
        self.textEdit_image_description.setGeometry(QRect(819, 422, 311, 271))
        font5 = QFont()
        font5.setPointSize(14)
        self.textEdit_image_description.setFont(font5)
        self.textEdit_image_description.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"        border: 1px solid #7986ac;\n"
"    border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_image_description.setFrameShape(QFrame.Shape.WinPanel)
        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(440, 3, 281, 25))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_refresh_image_grid = QPushButton(self.widget_8)
        self.pushButton_refresh_image_grid.setObjectName(u"pushButton_refresh_image_grid")
        self.pushButton_refresh_image_grid.setGeometry(QRect(982, 6, 151, 28))
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
        self.pushButton_save_description = QPushButton(self.widget_8)
        self.pushButton_save_description.setObjectName(u"pushButton_save_description")
        self.pushButton_save_description.setGeometry(QRect(982, 702, 150, 28))
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
        self.pushButton_open_product_image = QPushButton(self.widget_8)
        self.pushButton_open_product_image.setObjectName(u"pushButton_open_product_image")
        self.pushButton_open_product_image.setGeometry(QRect(820, 6, 161, 28))
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
        self.pushButton_show_product_folder = QPushButton(self.widget_8)
        self.pushButton_show_product_folder.setObjectName(u"pushButton_show_product_folder")
        self.pushButton_show_product_folder.setGeometry(QRect(818, 702, 160, 28))
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
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_graph_6 = QWidget(self.tab_4)
        self.widget_graph_6.setObjectName(u"widget_graph_6")
        self.widget_graph_6.setGeometry(QRect(0, 0, 1140, 737))
        self.widget_graph_6.setStyleSheet(u"background-color: #dcebff;\n"
"       border-top-left-radius: 0px;   /* No radius on top-left */\n"
"    border-top-right-radius: 8px;  /* Rounded */\n"
"    border-bottom-left-radius: 8px; /* Rounded */\n"
"    border-bottom-right-radius: 8px; /* Rounded */\n"
"\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_shop_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_name.setObjectName(u"lineEdit_shop_name")
        self.lineEdit_shop_name.setGeometry(QRect(212, 50, 361, 24))
        self.lineEdit_shop_name.setFont(font3)
        self.lineEdit_shop_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_shop_address = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_address.setObjectName(u"lineEdit_shop_address")
        self.lineEdit_shop_address.setGeometry(QRect(212, 80, 581, 24))
        self.lineEdit_shop_address.setFont(font3)
        self.lineEdit_shop_address.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_shop_gstin = QLineEdit(self.widget_graph_6)
        self.lineEdit_shop_gstin.setObjectName(u"lineEdit_shop_gstin")
        self.lineEdit_shop_gstin.setGeometry(QRect(212, 109, 201, 24))
        self.lineEdit_shop_gstin.setFont(font3)
        self.lineEdit_shop_gstin.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_customer_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_name.setObjectName(u"lineEdit_customer_name")
        self.lineEdit_customer_name.setGeometry(QRect(212, 140, 311, 24))
        self.lineEdit_customer_name.setFont(font3)
        self.lineEdit_customer_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_customer_address = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_address.setObjectName(u"lineEdit_customer_address")
        self.lineEdit_customer_address.setGeometry(QRect(212, 170, 581, 24))
        self.lineEdit_customer_address.setFont(font3)
        self.lineEdit_customer_address.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_customer_gstin = QLineEdit(self.widget_graph_6)
        self.lineEdit_customer_gstin.setObjectName(u"lineEdit_customer_gstin")
        self.lineEdit_customer_gstin.setGeometry(QRect(212, 200, 261, 24))
        self.lineEdit_customer_gstin.setFont(font3)
        self.lineEdit_customer_gstin.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.label_3 = QLabel(self.widget_graph_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 50, 131, 21))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.widget_graph_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 80, 141, 21))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.widget_graph_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 110, 131, 21))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6 = QLabel(self.widget_graph_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 140, 121, 21))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_7 = QLabel(self.widget_graph_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 170, 131, 21))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_8 = QLabel(self.widget_graph_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 200, 121, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
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
        if (self.table_item_table.rowCount() < 12):
            self.table_item_table.setRowCount(12)
        self.table_item_table.setObjectName(u"table_item_table")
        self.table_item_table.setGeometry(QRect(70, 240, 1001, 381))
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
                        "lor: #black;\n"
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
"    background:"
                        " #ebf2ff;\n"
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
        self.table_item_table.setRowCount(12)
        self.table_item_table.setColumnCount(8)
        self.toolButton_save_button = QToolButton(self.widget_graph_6)
        self.toolButton_save_button.setObjectName(u"toolButton_save_button")
        self.toolButton_save_button.setGeometry(QRect(1042, 7, 91, 26))
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
        self.toolButton_add_item_button = QToolButton(self.widget_graph_6)
        self.toolButton_add_item_button.setObjectName(u"toolButton_add_item_button")
        self.toolButton_add_item_button.setGeometry(QRect(962, 630, 111, 31))
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
        self.lineEdit_bank_name = QLineEdit(self.widget_graph_6)
        self.lineEdit_bank_name.setObjectName(u"lineEdit_bank_name")
        self.lineEdit_bank_name.setGeometry(QRect(70, 656, 346, 24))
        self.lineEdit_bank_name.setFont(font3)
        self.lineEdit_bank_name.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_account_number = QLineEdit(self.widget_graph_6)
        self.lineEdit_account_number.setObjectName(u"lineEdit_account_number")
        self.lineEdit_account_number.setGeometry(QRect(427, 656, 346, 24))
        self.lineEdit_account_number.setFont(font3)
        self.lineEdit_account_number.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_ifsc_code = QLineEdit(self.widget_graph_6)
        self.lineEdit_ifsc_code.setObjectName(u"lineEdit_ifsc_code")
        self.lineEdit_ifsc_code.setGeometry(QRect(70, 703, 346, 24))
        self.lineEdit_ifsc_code.setFont(font3)
        self.lineEdit_ifsc_code.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_branch = QLineEdit(self.widget_graph_6)
        self.lineEdit_branch.setObjectName(u"lineEdit_branch")
        self.lineEdit_branch.setGeometry(QRect(430, 703, 346, 24))
        self.lineEdit_branch.setFont(font3)
        self.lineEdit_branch.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.label_17 = QLabel(self.widget_graph_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(70, 634, 121, 21))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_18 = QLabel(self.widget_graph_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(430, 630, 121, 21))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_19 = QLabel(self.widget_graph_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 680, 121, 21))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_20 = QLabel(self.widget_graph_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(430, 680, 121, 21))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_21 = QLabel(self.widget_graph_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(500, 6, 181, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_suggest_item = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_item.setObjectName(u"lineEdit_suggest_item")
        self.lineEdit_suggest_item.setGeometry(QRect(960, 90, 113, 31))
        self.lineEdit_suggest_item.setFont(font3)
        self.lineEdit_suggest_item.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_suggest_quantity = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_quantity.setObjectName(u"lineEdit_suggest_quantity")
        self.lineEdit_suggest_quantity.setGeometry(QRect(960, 130, 113, 31))
        self.lineEdit_suggest_quantity.setFont(font3)
        self.lineEdit_suggest_quantity.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.lineEdit_suggest_rate = QLineEdit(self.widget_graph_6)
        self.lineEdit_suggest_rate.setObjectName(u"lineEdit_suggest_rate")
        self.lineEdit_suggest_rate.setGeometry(QRect(960, 170, 113, 31))
        self.lineEdit_suggest_rate.setFont(font3)
        self.lineEdit_suggest_rate.setStyleSheet(u"background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #9d9d9d;\n"
"color: rgb(157, 157, 157);")
        self.label_suggest_qty = QLabel(self.widget_graph_6)
        self.label_suggest_qty.setObjectName(u"label_suggest_qty")
        self.label_suggest_qty.setGeometry(QRect(960, 50, 161, 31))
        self.label_suggest_qty.setFont(font2)
        self.label_suggest_qty.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(920, 4, 151, 25))
        self.label_date.setFont(font1)
        self.label_date.setStyleSheet(u"background-color: rgb(196, 220, 255);\n"
"color: rgb(47, 56, 83);")
        form1.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.textEdit.raise_()
        self.label_name.raise_()
        self.label_income.raise_()
        self.label_expense.raise_()
        self.label_savings.raise_()
        self.label_gains.raise_()
        self.label_2.raise_()
        self.comboBox_3.raise_()
        self.tabWidget_2.raise_()
        self.label_13.raise_()
        self.lineEdit_income0.raise_()
        self.label_14.raise_()
        self.lineEdit_income.raise_()
        self.comboBox_4.raise_()
        self.tabWidget_3.raise_()
        self.lineEdit_calc.raise_()
        self.label_calc.raise_()
        self.label_date.raise_()
        self.menubar = QMenuBar(form1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 33))
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
        self.menuAbout.setGeometry(QRect(691, 153, 150, 113))
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

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(4)


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
        self.label_13.setText(QCoreApplication.translate("form1", u"Monthly Income:", None))
        self.textEdit.setHtml(QCoreApplication.translate("form1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#000000;\"># Current Summary Report</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-size:11pt; color:#000000;\">1. Total Income</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">2. Total Expense</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">3. Net Savings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">4. Extra Gains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">5. Miscellaneous Expense</span></p></body></html>", None))
        self.label_name.setText(QCoreApplication.translate("form1", u"Abhishek Verma", None))
        self.label_income.setText(QCoreApplication.translate("form1", u"64000/-", None))
        self.label_expense.setText(QCoreApplication.translate("form1", u"45000", None))
        self.label_savings.setText(QCoreApplication.translate("form1", u"15000", None))
        self.label_gains.setText(QCoreApplication.translate("form1", u"4000", None))
        self.label_2.setText("")
        self.lineEdit_income.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("form1", u"GST-Auto", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("form1", u"0% GST", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("form1", u"5% GST", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("form1", u"12% GST", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("form1", u"18% GST", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("form1", u"28% GST", None))

        self.lineEdit_calc.setText("")
        self.lineEdit_calc.setPlaceholderText(QCoreApplication.translate("form1", u"Use Numkeys...", None))
        self.label_calc.setText(QCoreApplication.translate("form1", u"Calc :", None))
        self.label_14.setText(QCoreApplication.translate("form1", u"Current Income:", None))
        self.lineEdit_income0.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income0.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("form1", u"Remaining income", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("form1", u"Extra Gains", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("form1", u"Default WorkSpace", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("form1", u"Sales", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("form1", u"Purchase", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("form1", u"Stock", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("form1", u"Banking Transactions", None))

        self.label_expense_record.setText(QCoreApplication.translate("form1", u"Purchases :-", None))
        self.label_total_expense.setText(QCoreApplication.translate("form1", u"Total monthly Spend = ", None))
        self.label_total_spends.setText(QCoreApplication.translate("form1", u"0", None))
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
        self.toolButton_save1.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.lineEdit_item.setText("")
        self.lineEdit_item.setPlaceholderText(QCoreApplication.translate("form1", u"Item...", None))
        self.lineEdit_reciepent.setText("")
        self.lineEdit_reciepent.setPlaceholderText(QCoreApplication.translate("form1", u"Recipient..", None))
        self.toolButton_del_row.setText(QCoreApplication.translate("form1", u"Delete", None))
        self.label_extra_gains.setText(QCoreApplication.translate("form1", u"Sales:-", None))
        self.label_monthly_gains.setText(QCoreApplication.translate("form1", u"Total monthly Sales = ", None))
        self.label_total_gains.setText(QCoreApplication.translate("form1", u"1600/-", None))
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
        self.toolButton_save2.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.lineEdit_for_what.setText("")
        self.lineEdit_for_what.setPlaceholderText(QCoreApplication.translate("form1", u"for what...", None))
        self.lineEdit_giver.setText("")
        self.lineEdit_giver.setPlaceholderText(QCoreApplication.translate("form1", u"Giver...", None))
        self.toolButton_del_row_2.setText(QCoreApplication.translate("form1", u"Delete", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("form1", u"Sales and Purchases", None))
        self.label_extra_gains_2.setText(QCoreApplication.translate("form1", u"Transaction Record:-", None))
        self.label_monthly_gains_2.setText(QCoreApplication.translate("form1", u"Total monthly Sales = ", None))
        self.label_total_gains_2.setText(QCoreApplication.translate("form1", u"1600/-", None))
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
        self.toolButton_save2_2.setText(QCoreApplication.translate("form1", u"Entry", None))
        self.lineEdit_for_what_2.setText("")
        self.lineEdit_for_what_2.setPlaceholderText(QCoreApplication.translate("form1", u"for what...", None))
        self.lineEdit_giver_2.setText("")
        self.lineEdit_giver_2.setPlaceholderText(QCoreApplication.translate("form1", u"Giver...", None))
        self.toolButton_del_row_3.setText(QCoreApplication.translate("form1", u"Delete", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("form1", u"Banking", None))
        ___qtablewidgetitem12 = self.tableWidget_item_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("form1", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_item_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("form1", u"Rate (in Rs)", None));
        ___qtablewidgetitem14 = self.tableWidget_item_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("form1", u"Quantity", None));
        self.pushButton_search_item_button_.setText(QCoreApplication.translate("form1", u"Search", None))
        self.lineEdit_search_item_lineedit.setPlaceholderText(QCoreApplication.translate("form1", u"Search Items", None))
        self.label_24.setText(QCoreApplication.translate("form1", u"Search Items:", None))
        self.lineEdit_search_stock_input.setPlaceholderText(QCoreApplication.translate("form1", u"Search Stock", None))
        self.pushButton_search_stock_button_.setText(QCoreApplication.translate("form1", u"Search", None))
        self.label_10.setText(QCoreApplication.translate("form1", u"Search Stock:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete_item_button.setToolTip(QCoreApplication.translate("form1", u"<html><head/><body><p>Shortcut: Del</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_item_button.setText(QCoreApplication.translate("form1", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.pushButton_delete_item_button.setShortcut(QCoreApplication.translate("form1", u"Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_delete_stock_button.setToolTip(QCoreApplication.translate("form1", u"<html><head/><body><p>Shortcut: Ctrl+Del</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_stock_button.setText(QCoreApplication.translate("form1", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.pushButton_delete_stock_button.setShortcut(QCoreApplication.translate("form1", u"Ctrl+Del", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_add_item_button.setText(QCoreApplication.translate("form1", u"Add Item", None))
        self.lineEdit_item_rate_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Item Rate (Rs/-)", None))
        self.label_12.setText(QCoreApplication.translate("form1", u"Item Name:", None))
        self.lineEdit_item_quantity_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Quantity (Default:1)", None))
        self.label_16.setText(QCoreApplication.translate("form1", u"Quantity:", None))
        self.label_15.setText(QCoreApplication.translate("form1", u"Rate:", None))
        self.lineEdit_item_name_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Item Name", None))
        self.pushButton_add_stock_button.setText(QCoreApplication.translate("form1", u"Add Stock", None))
        self.lineEdit_stock_name_input.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Stock Name", None))
        self.label_9.setText(QCoreApplication.translate("form1", u"Stock Name:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("form1", u"Per Day", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("form1", u"Per Week", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("form1", u"Per Month", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("form1", u"Per Year", None))

        self.label_extra_gains_3.setText(QCoreApplication.translate("form1", u"Stock Details:-", None))
        self.label_23.setText(QCoreApplication.translate("form1", u"Stock Items", None))
        self.label_22.setText(QCoreApplication.translate("form1", u"Stocks", None))
        self.pushButton_load_button.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.pushButton_save_button.setText(QCoreApplication.translate("form1", u"Save", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("form1", u"Stock Details", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("form1", u"Company and Customer", None))
        self.label_image_show.setText(QCoreApplication.translate("form1", u"                 Product Image", None))
        self.textEdit_image_description.setPlaceholderText(QCoreApplication.translate("form1", u"Enter Product Description here...", None))
        self.label_25.setText(QCoreApplication.translate("form1", u"Products with Description", None))
        self.pushButton_refresh_image_grid.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.pushButton_save_description.setText(QCoreApplication.translate("form1", u"Save in Products", None))
        self.pushButton_open_product_image.setText(QCoreApplication.translate("form1", u"Open Product Image", None))
#if QT_CONFIG(shortcut)
        self.pushButton_open_product_image.setShortcut(QCoreApplication.translate("form1", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_show_product_folder.setText(QCoreApplication.translate("form1", u"Show Folder", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("form1", u"Products", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("form1", u"Purchase Bill", None))
        self.lineEdit_shop_name.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("form1", u"Your Shop Name:", None))
        self.label_4.setText(QCoreApplication.translate("form1", u"Your Shop Address:", None))
        self.label_5.setText(QCoreApplication.translate("form1", u"Your Shop GSTIN:", None))
        self.label_6.setText(QCoreApplication.translate("form1", u"Customer Name:", None))
        self.label_7.setText(QCoreApplication.translate("form1", u"Customer Address:", None))
        self.label_8.setText(QCoreApplication.translate("form1", u"Customer GSTIN:", None))
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
        self.toolButton_save_button.setText(QCoreApplication.translate("form1", u"Export", None))
        self.toolButton_add_item_button.setText(QCoreApplication.translate("form1", u"Add Item", None))
#if QT_CONFIG(shortcut)
        self.toolButton_add_item_button.setShortcut(QCoreApplication.translate("form1", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_17.setText(QCoreApplication.translate("form1", u"Bank Name:", None))
        self.label_18.setText(QCoreApplication.translate("form1", u"Account Number:", None))
        self.label_19.setText(QCoreApplication.translate("form1", u"IFSC Code:", None))
        self.label_20.setText(QCoreApplication.translate("form1", u"Branch:", None))
        self.label_21.setText(QCoreApplication.translate("form1", u"IINVOICE RECIEPT", None))
        self.lineEdit_suggest_item.setPlaceholderText(QCoreApplication.translate("form1", u"Type Item", None))
        self.lineEdit_suggest_quantity.setPlaceholderText(QCoreApplication.translate("form1", u"Qty", None))
        self.lineEdit_suggest_rate.setPlaceholderText(QCoreApplication.translate("form1", u"Rate", None))
        self.label_suggest_qty.setText(QCoreApplication.translate("form1", u"#Testing Total Quantity", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("form1", u"Sale Bill", None))
        self.label_date.setText(QCoreApplication.translate("form1", u"Date:- 26/01/2001", None))
        self.menuFile.setTitle(QCoreApplication.translate("form1", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("form1", u"Edit", None))
        self.menuExport.setTitle(QCoreApplication.translate("form1", u"Export", None))
        self.menuSnap.setTitle(QCoreApplication.translate("form1", u"Snap", None))
        self.menuAbout.setStyleSheet(QCoreApplication.translate("form1", u"background-color: rgb(232, 232, 232);\n"
"color: rgb(0, 0, 0);", None))
        self.menuAbout.setTitle(QCoreApplication.translate("form1", u"About", None))
    # retranslateUi

