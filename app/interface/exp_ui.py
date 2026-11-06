# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exp.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1670, 932)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(12, 31, 1140, 792))
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget_2.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.widget_graph_3 = QWidget(self.tab_5)
        self.widget_graph_3.setObjectName(u"widget_graph_3")
        self.widget_graph_3.setGeometry(QRect(0, 0, 1140, 792))
        self.widget_graph_3.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.widget_5 = QWidget(self.widget_graph_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 1140, 360))
        self.widget_5.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.label_expense_record = QLabel(self.widget_5)
        self.label_expense_record.setObjectName(u"label_expense_record")
        self.label_expense_record.setGeometry(QRect(14, -4, 181, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_expense_record.setFont(font)
        self.label_expense_record.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_total_expense = QLabel(self.widget_5)
        self.label_total_expense.setObjectName(u"label_total_expense")
        self.label_total_expense.setGeometry(QRect(740, 325, 231, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_total_expense.setFont(font1)
        self.label_total_expense.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_total_spends = QLabel(self.widget_5)
        self.label_total_spends.setObjectName(u"label_total_spends")
        self.label_total_spends.setGeometry(QRect(972, 331, 151, 21))
        self.label_total_spends.setFont(font1)
        self.label_total_spends.setStyleSheet(u"color: rgb(255, 133, 192);")
        self.tableWidget_1 = QTableWidget(self.widget_5)
        if (self.tableWidget_1.columnCount() < 7):
            self.tableWidget_1.setColumnCount(7)
        font2 = QFont()
        font2.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
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
        self.tableWidget_1.setGeometry(QRect(10, 27, 1121, 301))
        self.tableWidget_1.setFont(font1)
        self.tableWidget_1.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"border-color: rgb(130, 255, 213);\n"
"\n"
"\n"
"selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(97, 46, 46);\n"
"color: rgb(255, 193, 106);")
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
        self.lineEdit_spend.setGeometry(QRect(12, 331, 121, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_spend.sizePolicy().hasHeightForWidth())
        self.lineEdit_spend.setSizePolicy(sizePolicy)
        self.lineEdit_spend.setMinimumSize(QSize(0, 0))
        self.lineEdit_spend.setMaximumSize(QSize(1920, 70))
        self.lineEdit_spend.setFont(font)
        self.lineEdit_spend.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_spend.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_spend.setMaxLength(1000)
        self.lineEdit_spend.setFrame(False)
        self.lineEdit_spend.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_spend.setCursorPosition(0)
        self.lineEdit_spend.setDragEnabled(True)
        self.lineEdit_spend.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_spend.setClearButtonEnabled(False)
        self.toolButton_save1 = QToolButton(self.widget_5)
        self.toolButton_save1.setObjectName(u"toolButton_save1")
        self.toolButton_save1.setGeometry(QRect(670, 329, 61, 26))
        font3 = QFont()
        font3.setPointSize(12)
        self.toolButton_save1.setFont(font3)
        self.toolButton_save1.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_item = QLineEdit(self.widget_5)
        self.lineEdit_item.setObjectName(u"lineEdit_item")
        self.lineEdit_item.setGeometry(QRect(137, 331, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_item.sizePolicy().hasHeightForWidth())
        self.lineEdit_item.setSizePolicy(sizePolicy)
        self.lineEdit_item.setMinimumSize(QSize(0, 0))
        self.lineEdit_item.setMaximumSize(QSize(1920, 70))
        self.lineEdit_item.setFont(font)
        self.lineEdit_item.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_item.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_item.setMaxLength(1000)
        self.lineEdit_item.setFrame(False)
        self.lineEdit_item.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_item.setCursorPosition(0)
        self.lineEdit_item.setDragEnabled(True)
        self.lineEdit_item.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_item.setClearButtonEnabled(False)
        self.lineEdit_reciepent = QLineEdit(self.widget_5)
        self.lineEdit_reciepent.setObjectName(u"lineEdit_reciepent")
        self.lineEdit_reciepent.setGeometry(QRect(253, 331, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_reciepent.sizePolicy().hasHeightForWidth())
        self.lineEdit_reciepent.setSizePolicy(sizePolicy)
        self.lineEdit_reciepent.setMinimumSize(QSize(0, 0))
        self.lineEdit_reciepent.setMaximumSize(QSize(1920, 70))
        self.lineEdit_reciepent.setFont(font)
        self.lineEdit_reciepent.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_reciepent.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_reciepent.setMaxLength(1000)
        self.lineEdit_reciepent.setFrame(False)
        self.lineEdit_reciepent.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_reciepent.setCursorPosition(0)
        self.lineEdit_reciepent.setDragEnabled(True)
        self.lineEdit_reciepent.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_reciepent.setClearButtonEnabled(False)
        self.toolButton_del_row = QToolButton(self.widget_5)
        self.toolButton_del_row.setObjectName(u"toolButton_del_row")
        self.toolButton_del_row.setGeometry(QRect(1100, 1, 31, 26))
        font4 = QFont()
        font4.setPointSize(20)
        self.toolButton_del_row.setFont(font4)
        self.toolButton_del_row.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 0, 0);")
        self.label_expense_record.raise_()
        self.label_total_expense.raise_()
        self.label_total_spends.raise_()
        self.lineEdit_spend.raise_()
        self.toolButton_save1.raise_()
        self.lineEdit_item.raise_()
        self.lineEdit_reciepent.raise_()
        self.toolButton_del_row.raise_()
        self.tableWidget_1.raise_()
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.widget_graph_2 = QWidget(self.tab_6)
        self.widget_graph_2.setObjectName(u"widget_graph_2")
        self.widget_graph_2.setGeometry(QRect(0, 0, 1140, 792))
        self.widget_graph_2.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.tabWidget_2.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1670, 33))
        self.menuasd = QMenu(self.menubar)
        self.menuasd.setObjectName(u"menuasd")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuasd.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_expense_record.setText(QCoreApplication.translate("MainWindow", u"Purchases :-", None))
        self.label_total_expense.setText(QCoreApplication.translate("MainWindow", u"Total monthly Spend = ", None))
        self.label_total_spends.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem = self.tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SPEND/-", None));
        ___qtablewidgetitem1 = self.tableWidget_1.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Item/Purpose", None));
        ___qtablewidgetitem2 = self.tableWidget_1.horizontalHeaderItem(4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Reciepent", None));
        ___qtablewidgetitem3 = self.tableWidget_1.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.lineEdit_spend.setText("")
        self.lineEdit_spend.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Spend/-", None))
        self.toolButton_save1.setText(QCoreApplication.translate("MainWindow", u"Entry", None))
        self.lineEdit_item.setText("")
        self.lineEdit_item.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item...", None))
        self.lineEdit_reciepent.setText("")
        self.lineEdit_reciepent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recipient..", None))
        self.toolButton_del_row.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Banking", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Extra Gains", None))
        self.menuasd.setTitle(QCoreApplication.translate("MainWindow", u"asd", None))
    # retranslateUi

