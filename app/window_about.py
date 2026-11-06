# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutzxFBaC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,
    QWidget)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(670, 500)
        about.setMinimumSize(QSize(670, 500))
        about.setMaximumSize(QSize(670, 500))
        about.setStyleSheet(u"background-color: rgb(165, 187, 230);")
        self.textEdit_about = QTextEdit(about)
        self.textEdit_about.setObjectName(u"textEdit_about")
        self.textEdit_about.setGeometry(QRect(10, 0, 650, 503))
        self.textEdit_about.setStyleSheet(u"background-color: rgb(212, 219, 231);")
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About", None))
        self.textEdit_about.setHtml(QCoreApplication.translate("about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700; color:#828fb9;\">About Finance Flow</span></h1>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#8390ba;\">Overview</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">Welcome to </span><span style=\" font-size:11pt; font-weight:700; color:#8390ba;\">Finance Flow</span><span style=\" font-size:11pt; color:#000000;\"> \u2013 your ultimate companion for managing and tracking personal expenses effortlessly. Designed with simplicity and functionality in mind, Finance Flow helps you keep a detailed record of your spending, visualize your financial health, and make informed decisions about your money.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#8390ba;\">Features</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; "
                        "font-weight:700; color:#8390ba;\">Expense Tracking</span><span style=\" font-size:11pt; color:#000000;\">: Easily enter and categorize your expenses. Record details about the purpose, recipient, and amount spent.</span></li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#8390ba;\">Notes and Data Entry</span><span style=\" color:#8390ba;\">:</span> Add insightful notes to each entry for better tracking and future reference.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#8390ba;\">Data Visualization</span><span style=\" color:#8390ba;\">:</span> Visualize your financial data with interactive bar plots using pyqtgraph, helping you understand your remaining income and overall spending patterns.<"
                        "/li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#8390ba;\">Customizable Tables</span><span style=\" color:#8390ba;\">:</span> Manage and review your data with user-friendly tables that adapt to your needs.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#828fb9;\">Why Choose Finance Flow?</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#8390ba;\">Intuitive Interface</span><span style=\" font-size:11pt; color:#8390ba;\">:</span><span style=\" font-size:"
                        "11pt; color:#000000;\"> Designed with user experience in mind, Finance Flow makes it easy to navigate and manage your finances without hassle.</span></li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#8390ba;\">Comprehensive Tracking</span><span style=\" color:#8390ba;\">:</span> From daily expenses to long-term spending habits, Finance Flow gives you a complete overview of your financial situation.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#828fb9;\">Visual Insights</span><span style=\" color:#828fb9;\">:</span> Leverage powerful visualizations to quickly grasp your financial status and make proactive decisions.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#8390ba;\">Version</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#8390ba;\">Current Version</span><span style=\" font-size:11pt; color:#8390ba;\">: 1.1</span></li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#8390ba;\">Developer Information</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#8390ba;\">Finance Flow</span><span style=\" font-size:11pt; c"
                        "olor:#000000;\"> is developed by </span><span style=\" font-size:11pt; font-weight:700; color:#828fb9;\">Abhishek Verma</span><span style=\" font-size:11pt; color:#828fb9;\">,</span><span style=\" font-size:11pt; color:#000000;\"> a Btech graduate and software engineer currently working in the field of Software development and Machine learning. He is dedicated to creating practical solutions that simplify everyday tasks and enhance user experience.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#8390ba;\">How It Works</span></h2>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#8390ba;\">Data Entry</span><span style=\" fon"
                        "t-size:11pt; color:#8390ba;\">:</span><span style=\" font-size:11pt; color:#000000;\"> Input your expense data including categories, purposes, and recipients.</span></li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7986ac;\">Organize &amp; Analyze</span><span style=\" color:#7986ac;\">:</span> Use the built-in tables to organize your entries and add notes for better tracking.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7986ac;\">Visualize</span><span style=\" color:#7986ac;\">:</span> Review your remaining income and spending patterns through interactive graphs.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7885ab;\">Manage</span><span style=\" color:#7885ab;\">:</span> Edit, update, or delete entries as needed to keep your records accurate and up-to-date.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7986ac;\">Calculator</span><span style=\" color:#7986ac;\">:</span> calculate datas easily using keyboard input, just type expressions.</li>\n"
"<li style=\" font-size:11pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7986ac;\">Calender</span><span style=\" color:#7986ac;\">:</span> calender is present in the same window.</li></ol>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#828fb9;\">Support</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">If you have any questions or need assistance with Finance Flow, please reach out to our support team at support at abhishek639679@gmail.com . We're here to help!</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#828fb9;\">Feedback</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">We value your feedback! Share your thoughts or suggestions with us at abhishek639679@gmail.com to help us improve and enhance your experience.</span></p>\n"
"<h2 style=\" margin-t"
                        "op:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#808db6;\">Connect with Us</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">Follow us on social media to stay updated on the latest news, updates, and tips related to Finance Flow:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#828fb9;\">https://abhi639679.wixsite.com/abhishek</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:11pt; color:#828fb9;\" style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://www.instagram.com/abhiiverma007/</li></ul>\n"
"<li style=\" font-size:11pt; color:#828fb9;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://www.linkedin.com/in/abhishek-verma-11729123a/</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">Thank you for choosing Finance Flow. We hope it makes managing your finances as smooth and stress-free as possible!</span></p></body></html>", None))
    # retranslateUi

