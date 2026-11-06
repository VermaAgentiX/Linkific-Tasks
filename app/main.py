from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint
import shutil
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QCompleter
)
from PySide6.QtCore import Qt
import sys
from PySide6.QtCore import QStringListModel

from PySide6.QtWidgets import (QLabel,
    QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QWidget, QSpinBox, QComboBox,QCompleter,
)
from PySide6.QtGui import QDoubleValidator

from fpdf import FPDF
from datetime import datetime

import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QGridLayout, QLabel, QPushButton, QFileDialog, QDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt






from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from random import randint



theme = 'dark'
class ToggleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initial state
        self.setCheckable(True)
        self.setFixedSize(54, 27)
        self.setStyleSheet(self.get_stylesheet(False))

        # Create the sliding circle
        self.circle = QPushButton(self)
        
        
        self.circle.setFixedSize(18, 18)
        self.circle.move(4, 4)
        self.circle.setStyleSheet("border-radius: 9px; background-color: white;")
        self.circle.setEnabled(False)

        # Animation for circle movement
        self.animation = QPropertyAnimation(self.circle, b"pos", self)

        # Connect the toggle state to the animation and style updates
        self.toggled.connect(self.animate)
        self.toggled.connect(self.print_state)  # Connect to print_state method

    def animate(self, checked):
        start_pos = self.circle.pos()
        end_pos = QPoint(32, 4) if checked else QPoint(4, 4)

        # Configure the animation
        self.animation.setDuration(200)
        self.animation.setStartValue(start_pos)
        self.animation.setEndValue(end_pos)
        self.animation.start()

        # Update the background style
        self.setStyleSheet(self.get_stylesheet(checked))

    def print_state(self, checked):
        global theme
        if checked:
            widget1.theme_light()
            theme = 'light'
        else:
            widget1.theme_dark()
            theme = 'dark'

    def get_stylesheet(self, checked):
        if checked:
            return (
                "background-color: rgb(0, 200, 100); border-radius: 13px;"
                "border: 2px solid rgb(80, 180, 80);"
            )
        else:
            return (
                "background-color: rgb(40, 40, 40); border-radius: 13px;"
                "border: 2px solid rgb(180, 180, 180);"
            )





# This Python file uses the following encoding: utf-8
print('Starting...')
import sys,os
import csv
try:

    import numpy as np
except:
    os.system('pip install numpy')
try:

    import pandas as pd
except:
    os.system('pip install pandas')

try:

    from pyautogui import screenshot as script
except:
    os.system('pip install pyautogui')
try:

    import pyqtgraph as pg
except:
    os.system('pip install pyqtgraph')

from datetime import datetime
try:

    from PySide6.QtGui import QColor
    from PySide6.QtCore import Qt, QPropertyAnimation, QRect

    from PySide6.QtWidgets import QApplication,QVBoxLayout, QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox,QFileDialog
    # Important:
    # You need to run the following command to generate the ui_form.py file
    #     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
except:
    os.system('pip install PySide6')



    



import json

import numpy as np
import pandas as pd
from pyautogui import screenshot as script
import pyqtgraph as pg
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QApplication,QVBoxLayout, QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox,QFileDialog

current_date = datetime.now()

# Format the date as "Aug2024_spends"
#file_name = current_date.strftime("%b%Y") + "_spends.csv"


k0 = 0
l0 = 0
y1_income = []

win_width = 1160
win_height = 435


filename = current_date.strftime("%b%Y") + "_spends.csv"

file_exists = os.path.isfile(filename)
if not file_exists:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['spend','for','item','to','reciepent','in','datetime','curr_income'])
else:
    pass

filename2 = current_date.strftime("%b%Y") + "_gains.csv"
file_exists2 = os.path.isfile(filename2)
if not file_exists2:
    with open(filename2, mode='w', newline='') as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(['gains','for','item','to','payer','in','datetime','curr_gain'])
else:
    pass









filename1 = "settings.json" 
file_exists1 = os.path.isfile(filename1)



admin_name=''
gmail=''
contact_no=''
company_name=''
shop_name = ''
monthly_income = ''
current_income = ''

            

intro_show = False
if not file_exists1:
    intro_show = True
    
    
    data1 = {
        
            "admin_name":'admin',
            "gmail":'',
            "contact_no":'',
            "company_name":'',
            "shop_name":'',
            "current_income": '0',
            "total_spends":'0',
            "monthly_income":'0',
            "previous_note": "",
            "total_gains": "0",
            "screen_width":"850",
            "screen_height":"435",
            "others_show":False,
            "others_hide":True,
            "admin_name":'Admin',
            "theme":'dark'
        }
        
    with open(filename1, "w") as json_file1:
        json.dump(data1, json_file1, indent=4)
else:
    pass


def spend_save(data1):
    global total_spends
   
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
      
            
        writer.writerow(data1)

    df = pd.read_csv(filename)
    total_spends = df['spend'].sum()
    widget1.form.label_total_spends.setText(str(total_spends))

def gain_save(data2):
    global total_gains
    
    file_exists2 = os.path.isfile(filename2)

    with open(filename2, mode='a', newline='') as file2:
        writer2 = csv.writer(file2)
      
            
        writer2.writerow(data2)

    df2 = pd.read_csv(filename2)
    total_gains = df2['gains'].sum()
    widget1.form.label_total_gains.setText(str(total_gains))


with open("settings.json", "r") as json_file:
    data_json7 = json.load(json_file)




        

from PySide6.QtGui import QPixmap, QMouseEvent


from window_intro import Ui_Dialog
class window_name_intro(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_Dialog()
        self.form.setupUi(self)
        self.form.toolButton_Create.clicked.connect(self.validate_inputs)
        self.form.toolButton_set_image.clicked.connect(self.open_file_dialog)
        
        
    def open_file_dialog(self):
        """
        Opens a file dialog to select an image and updates the label background.
        """
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:  # If user selects an image
            self.set_label_image(file_path)

        
        
        
        
        
    def validate_inputs(self):
        """Validate all line edits, and highlight empty fields."""
        inputs = [
            self.form.lineEdit_company_name,
            self.form.lineEdit_show_name,
            self.form.lineEdit_monthly_income,
            self.form.lineEdit_current_income
        ]

        all_valid = True 

        for line_edit in inputs:
            if not line_edit.text():  
                self.set_lineedit_red(line_edit)
                line_edit.setPlaceholderText("Required")
                all_valid = False
            else:
                self.clear_lineedit_style(line_edit)

        if all_valid:
            print("All fields are filled successfully!")
            self.show_window()
        else:
            print("Please fill in all required fields.")

    def set_lineedit_red(self, line_edit):
        """Set the line edit background to light red."""
        line_edit.setStyleSheet("border: 1px solid red;background-color: rgb(240, 240, 240);selection-background-color: rgb(137, 143, 255);selection-color: rgb(0, 0, 0);color: rgb(83, 248, 195);")

    def clear_lineedit_style(self, line_edit):
        """Clear the line edit styling."""
        
        line_edit.setStyleSheet("")
        
    def show_window(self):
        global widget1
        global gmail,contact_no,company_name,shop_name,admin_name,monthly_income,current_income
        


        admin_name = self.form.lineEdit_admin_name.text()
        gmail= self.form.lineEdit_gmail.text()
        contact_no = self.form.lineEdit_contact_no.text()
        company_name=self.form.lineEdit_company_name.text()
        shop_name = self.form.lineEdit_show_name.text()
        monthly_income = self.form.lineEdit_monthly_income.text()
        current_income = self.form.lineEdit_current_income.text()
        
        self.create_data()
        
        
        
        
        
        
    def create_data(self):

        data = {
            
            "admin_name":admin_name,
            "gmail":gmail,
            "contact_no":contact_no,
            "company_name":company_name,
            "shop_name":shop_name,
            
            "current_income": current_income,
            "total_spends": '0',
            "monthly_income":monthly_income,
            "previous_note": '',
            "total_gains": '0',
            "screen_width": win_width,
            "screen_height": win_height,
            "others_show":True,
            "others_hide":False,
            "admin_name":admin_name,
            "theme":'dark'
           
        }
        
        # Saving the dictionary as a JSON file
        with open("settings.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data saved to data.json")
        
       
        
        
        
        
        
        
        widget1 = window_main()
        widget1.show()
        widget1.hider()
        


    def set_label_image(self, file_path):
        """
        Sets the selected image as the background of the label.
        """
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(
            self.form.label_profile.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.form.label_profile.setPixmap(scaled_pixmap)
        
  
  
  
  
    def __init__(self):
        super().__init__()
        from PySide6.QtWidgets import QLabel

  
  
from window1 import Ui_form1

class window_main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_form1()
        self.form.setupUi(self)
        #---------------------------------for hiding iinvoice test objects------------------------\
        self.form.lineEdit_suggest_item.setVisible(False)
        self.form.lineEdit_suggest_quantity.setVisible(False)
        self.form.lineEdit_suggest_rate.setVisible(False)
        self.form.label_suggest_qty.setVisible(False)
        #---------------------------------for hiding test objects------------------------/
        
        
        
        self.resize(int(data_json7['screen_width']),int(data_json7["screen_height"]))
        print('Welcome to the Finance Flow ~')
        
        
        self.stocks = {
            
        }
        
        #-----------------------------------------Status_label---------------------------------\
            
        self.widget_status = QWidget(self)
        self.widget_status.setGeometry(530,5,450,22)
        self.widget_status.setStyleSheet('background-color: rgb(65, 75, 119); border-radius: 10px;')
        #when hover it shows status bar        
        
        from PySide6.QtGui import QFont
        self.label_status = QLabel('Label Text', self)
        #set geometry in main windows
        #self.label.setGeometry(20,20,200,50)
        self.label_status.setStyleSheet('color:rgb(255, 255, 255);')
        #label_status.setStyleSheet('font-weight: bold;')
        self.font = QFont()
        self.font.setFamily('Arial')
        self.font.setPointSize(12)
        #self.font.setBold(True)
        self.label_status.setGeometry(530,5,450,20)
        self.label_status.setFont(self.font)
        self.label_status.setAlignment(Qt.AlignCenter)
        self.label_status.setText("Welcome to the Project  v1.1")
        #-----------------------------------------End------------------------------------------/
        
        
        
        
        
        
        
        
        self.label1 = QLabel('Dark Theme', self)
        #set geometry in main windows
        #self.label.setGeometry(20,20,200,50)
        self.label1.setStyleSheet('color:black;')
        #label.setStyleSheet('font-weight: bold;')
        self.font = QFont()
        self.font.setFamily('Arial')
        self.font.setPointSize(12)
        self.label1.setFont(self.font)
        self.label1.move(1340,3)
        

        # Add the toggle button
        self.toggle = ToggleButton(self)
        self.toggle.move(1440, 3)
        self.form.table_item_table.setColumnWidth(0, 270)
        
        
        
        
        self.form.tableWidget_item_table.setColumnWidth(0,350)
        self.form.tableWidget_item_table.setColumnWidth(1,200)
        self.form.tableWidget_item_table.setColumnWidth(2,100)

        #self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.form.tableWidget_1.setColumnWidth(0, 150)
        self.form.tableWidget_1.setColumnWidth(1, 10)
        self.form.tableWidget_1.setColumnWidth(2, 140)
        self.form.tableWidget_1.setColumnWidth(3, 10)
        self.form.tableWidget_1.setColumnWidth(4, 170)
        self.form.tableWidget_1.setColumnWidth(5, 10)
        self.form.tableWidget_1.setColumnWidth(6, 200)

        self.form.tableWidget_2.setColumnWidth(0, 150)
        self.form.tableWidget_2.setColumnWidth(1, 10)
        self.form.tableWidget_2.setColumnWidth(2, 140)
        self.form.tableWidget_2.setColumnWidth(3, 10)
        self.form.tableWidget_2.setColumnWidth(4, 170)
        self.form.tableWidget_2.setColumnWidth(5, 10)
        self.form.tableWidget_2.setColumnWidth(6, 200)
        self.form.label_date.setText(current_date.strftime("Date: %d/%m/%Y"))

        layout = QVBoxLayout()
        self.form.widget_graph.setLayout(layout)
        # Create a PlotWidget

        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.plot_widget.setBackground((228, 235, 248))

        layout2 = QVBoxLayout()
        self.form.widget_graph_2.setLayout(layout2)
        self.plot_widget2 = pg.PlotWidget()
        layout2.addWidget(self.plot_widget2)
        self.plot_widget2.setBackground((228, 235, 248))

        #self.plot_widget.setLabel('left', 'Expense')  # Y-axis
        #self.plot_widget.setLabel('bottom', 'Days')   # X-axis
        self.form.lineEdit_calc.returnPressed.connect(self.calc)
        #self.graph_plotter(0,0)
        self.form.toolButton_save1.clicked.connect(self.plot_red_bar)
        self.form.toolButton_save2.clicked.connect(self.plot_blue_bar)
        self.form.toolButton_del_row.clicked.connect(self.delete_row)
        self.form.actionSave.triggered.connect(self.save_settings)
        self.form.actionRefresh.triggered.connect(self.refresher)
        
        self.form.actionSave_As.triggered.connect(self.save_notes)
        self.form.action_screenshot.triggered.connect(self.snap_save)
        self.form.actionExit.triggered.connect(self.closer)
        self.form.toolButton_del_row_2.clicked.connect(self.delete_row2)
        self.form.toolButton_expand.clicked.connect(self.hider)
        self.form.actionInfo.triggered.connect(self.info)
        self.form.actionLight.triggered.connect(self.theme_light)
        self.form.actionDakr.triggered.connect(self.theme_dark)
        
        self.form.comboBox_4.currentIndexChanged.connect(self.workspace)
        self.form.toolButton_add_item_button.clicked.connect(self.add_item_row)

        self.form.toolButton_save_button.clicked.connect(self.pdf_template2)
        self.bars = []
        self.index = 0
        self.bars2 = []
        self.index2 = 0

        self.load_csv1(filename)
        self.load_csv2(filename2)
        self.refresher()



        
        
        self.form.pushButton_add_stock_button.clicked.connect(self.add_stock)
        self.form.pushButton_delete_stock_button.clicked.connect(self.delete_stock)
        self.form.pushButton_load_button.clicked.connect(self.load_data_from_csv)
        self.form.listWidget_stock_list.itemClicked.connect(self.display_items)
        self.form.lineEdit_search_stock_input.textChanged.connect(self.update_stock_search)
        self.form.pushButton_add_item_button.clicked.connect(self.add_item)
        self.form.pushButton_delete_item_button.clicked.connect(self.delete_item)
        self.form.lineEdit_search_item_lineedit.textChanged.connect(self.search_item)
        
        #self.form.pushButton_save_button.clicked.connect(self.save_list_and_table_to_dict_and_csv)
        
        self.form.lineEdit_suggest_item.textChanged.connect(self.update_item_details)
        
        
        
        self.suggestion()
        
        #-------------------------------------Image_grid_Area---------------------------------/
        #self.main_layout = QVBoxLayout(self)
        
        
        self.selected_image_path = None

        # Output Folder
        self.output_folder = "saved_images"
        os.makedirs(self.output_folder, exist_ok=True)

        # CSV File Path
        self.csv_file1 = "products_data.csv"
        if not os.path.exists(self.csv_file1):
            # Create CSV file with headers if it doesn't exist
            pd.DataFrame(columns=["Image Name", "Description", "Date"]).to_csv(self.csv_file1, index=False)




        self.form.pushButton_refresh_image_grid.clicked.connect(self.image_refresher)
        self.form.pushButton_open_product_image.clicked.connect(self.select_image)
        self.form.pushButton_save_description.clicked.connect(self.save_product_data)
        self.form.pushButton_show_product_folder.clicked.connect(self.show_product_folder)
        #elf.form.scrollArea_image_grid = QScrollArea()
        self.form.scrollArea_image_grid.setWidgetResizable(True)
        
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(5)
        self.form.scrollArea_image_grid.setWidget(self.grid_widget)
        self.load_images_from_folder()
        
        
        
    def show_product_folder(self):
        # Specify the path to the folder
        # Get the current working directory
        current_dir = os.getcwd()

        # Define the folder path
        folder_path = os.path.join(current_dir, 'saved_images')

        # Open the folder using File Explorer
        os.startfile(folder_path)
        
        
    def select_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.selected_image_path = file_path
            self.form.label_image_show.setText(f"Selected: {os.path.basename(file_path)}")

            # Display image in QLabel
            pixmap = QPixmap(self.selected_image_path)
            
            scaled_pixmap = pixmap.scaled(
            self.form.label_image_show.width(),
            self.form.label_image_show.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
            
            self.form.label_image_show.setPixmap(scaled_pixmap)


        self.find_image_description()


    def save_product_data(self):
        if not self.selected_image_path:
            QMessageBox.warning(self, "Error", "No image selected!")
            return

        description = self.form.textEdit_image_description.toPlainText().strip()

        if not description:
            QMessageBox.warning(self, "Error", "Description is empty!")
            return

        # Generate unique image name
        unique_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{os.path.basename(self.selected_image_path)}"
        save_path = os.path.join(self.output_folder, unique_name)

        # Save the image
        try:
            shutil.copy(self.selected_image_path, save_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save image: {e}")
            return

        # Save details to CSV
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([{
            "Image Name": unique_name,
            "Description": description,
            "Date": date_str,
        }])

        try:
            df = pd.read_csv(self.csv_file1)
            updated_df = pd.concat([df, new_entry], ignore_index=True)
            updated_df.to_csv(self.csv_file1, index=False)
            self.label_status.setText("Descripion Saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data to CSV: {e}")
            self.label_status.setText("Descripion Saved.")
            return

        QMessageBox.information(self, "Success", "Image and description saved successfully!")
        
        
        
        self.form.textEdit_image_description.clear()
        self.selected_image_path = None
        print('done')
        self.label_status.setText("Done.")
        
        

        
    def find_image_description(self):
        if not self.selected_image_path:
            QMessageBox.warning(self, "Error", "No image selected to find details!")
            return

        image_name = os.path.basename(self.selected_image_path)
        try:
            df = pd.read_csv(self.csv_file1)
            row = df.loc[df["Image Name"].str.contains(image_name, na=False, case=False)]
            if not row.empty:
                # Display details
                description = row.iloc[0]["Description"]
                date = row.iloc[0]["Date"]
                #QMessageBox.information(
                #    self, "Image Details",
                #    f"Description: {description}\nDate: {date}"
                #)
                self.form.textEdit_image_description.setText(f"Description: {description}\n\nDate: {date}")
            else:
                #QMessageBox.warning(self, "Not Found", f"No details found for image: {image_name}")
                self.form.textEdit_image_description.setText("Not Found", f"No details found for image: {image_name}")
        except Exception as e:
            #QMessageBox.critical(self, "Error", f"Failed to read CSV file: {e}")
            self.form.textEdit_image_description.setText('No Description Found for this image, Add Description')
            print("Error", f"Failed to read CSV file: {e}")
            self.label_status.setText("Failed to read Csv")
        
        
    
    def image_refresher(self):
        try:
            
            self.load_images_from_folder()
            self.label_status.setText("Refreshed.")
        except:
            
            self.label_status.setText("Error!")
    def load_images_from_folder(self):
        # folder = QFileDialog.getExistingDirectory(self, "Select Image Folder")
        folder = 'C:\\Users\\Abhishek\\OneDrive\\Pictures\\Screenshots'
        if not folder:
            return

        # Clear existing items in the grid layout
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Load images from folder
        images = [f for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        for index, image_file in enumerate(images):
            # Load and scale the image
            image_path = os.path.join(folder, image_file)
            pixmap = QPixmap(image_path).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Create a label to display the image
            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            
            label.setStyleSheet("""
                border: 3px solid rgb(131, 144, 186);
                border-radius: 10px;
                background-color: rgb(65, 75, 119);
                color: rgb(255, 255, 255);
            """)  # Single border for the label

            # Set the tooltip with the image name (file name)
            label.setToolTip(image_file)

            # Connect double click to open the image in a new window
            
            label.mousePressEvent = lambda event, img_path=image_path, img_name=image_file: self.open_image_window(img_path, img_name)
            label.mouseDoubleClickEvent = lambda event, img_path=image_path, img_name=image_file: self.open_image_window2(img_path, img_name)
           

            # Add the label to the grid layout
            row = index // 4  # 4 images per row
            col = index % 4
            self.grid_layout.addWidget(label, row, col)
        
        print('Done')
        

    def open_image_window(self, image_path, image_name):
        # Load the image
        pixmap = QPixmap(image_path)

        # Scale the pixmap to fit the label_image_show size while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(
            self.form.label_image_show.width(),
            self.form.label_image_show.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.form.label_image_show.setStyleSheet("""
                border: 3px solid rgb(131, 144, 186);
                border-radius: 10px;
                background-color: rgb(65, 75, 119);
                color: rgb(255, 255, 255);
            """) 
        # Set the scaled pixmap to the label
        self.form.label_image_show.setPixmap(scaled_pixmap)
        self.form.label_image_show.setAlignment(Qt.AlignCenter)

        # Optionally, update the label text or tooltip with the image name
        self.form.label_image_show.setToolTip(image_name)


        #layout.addWidget(image_label)
        #layout.addWidget(name_label)

        # Adjust the dialog size to 25% of the main window
        #dialog.resize(scaled_pixmap.width(), scaled_pixmap.height() + name_label.sizeHint().height())
        #dialog.exec()
        
        
    def open_image_window2(self, image_path, image_name):
        dialog = QDialog(self)
        
        dialog.setWindowTitle(image_name)

        layout = QVBoxLayout(dialog)

        # Image Label
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.width(), self.height()-50, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        image_label = QLabel()
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        # Image Name Label
        name_label = QLabel(image_name)
        name_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(image_label)
        layout.addWidget(name_label)
        #Adjust the dialog size to 25% of the main window
        dialog.resize(scaled_pixmap.width(), scaled_pixmap.height() + name_label.sizeHint().height())
        dialog.exec()
        
        
    def suggestion(self):
        self.csv_file = "stock_data.csv"
        
        # Check if the CSV file exists
        if not os.path.exists(self.csv_file):
            # If the file does not exist, create it with the required header
            df = pd.DataFrame(columns=["Stock", "Item Name", "Rate (in Rs)", "Quantity"])
            df.to_csv(self.csv_file, index=False)
        else:
            # If the file exists, check if it has the correct headers
            df = pd.read_csv(self.csv_file)
            required_columns = ["Stock", "Item Name", "Rate (in Rs)", "Quantity"]
            
            # If the headers are not correct, overwrite the file with the correct headers
            if list(df.columns) != required_columns:
                df = pd.DataFrame(columns=required_columns)
                df.to_csv(self.csv_file, index=False)
        
        # Read the updated data from the CSV file
        self.df1 = pd.read_csv(self.csv_file)
        self.load_data_from_csv()

        # Extract Item Names and Quantities
        self.item_names = self.df1['Item Name'].tolist()
        self.quantities = self.df1['Quantity'].astype(str).tolist()
        self.rate = self.df1['Rate (in Rs)'].astype(str).tolist()
        
        # Setup completer for Item Name LineEdit
        self.model_item = QStringListModel(self.item_names)
        self.completer_item = QCompleter(self.model_item)
        self.form.lineEdit_suggest_item.setCompleter(self.completer_item)

        # Setup completer for Quantity LineEdit
        self.model_quantity = QStringListModel(self.quantities)
        self.completer_quantity = QCompleter(self.model_quantity)
        self.form.lineEdit_suggest_quantity.setCompleter(self.completer_quantity)

            
            

    def update_item_details(self):
        """Update the available quantity and rate based on item selection."""
        item_name = self.form.lineEdit_suggest_item.text()

        # Check if the item exists in the stock data
        row = self.df1[self.df1['Item Name'] == item_name]

        if not row.empty:
            # Get the current quantity and rate from the CSV
            available_quantity = row['Quantity'].values[0]
            rate = row['Rate (in Rs)'].values[0]

            # Update the available quantity and rate fields
            self.form.label_suggest_qty.setText(f"Available Quantity: {available_quantity}")
            self.form.lineEdit_suggest_rate.setText(f"{rate}")
        else:
            self.form.label_suggest_qty.setText("Available Quantity: N/A")
            self.form.lineEdit_suggest_rate.clear()

    def update_quantity(self):
        # Get entered item name and quantity
        item_name = self.form.lineEdit_suggest_item.text()
        quantity = self.form.label_suggest_qty.text()

        if item_name and quantity.isdigit():
            quantity = int(quantity)

            # Find the row matching the item name
            row = self.df1[self.df1['Item Name'] == item_name]

            if not row.empty:
                # Get the current quantity from the CSV
                current_quantity = row['Quantity'].values[0]

                # Check if entered quantity is smaller than the current quantity
                if quantity < current_quantity:
                    # Decrement the quantity
                    new_quantity = current_quantity - quantity

                    # Update the dataframe with the new quantity
                    self.df1.loc[self.df1['Item Name'] == item_name, 'Quantity'] = new_quantity

                    # Save the updated dataframe to CSV
                    self.df1.to_csv('stock_data.csv', index=False)

                    # Clear the quantity field after updating
                    self.form.lineEdit_suggest_quantity.clear()
                    print(f"Updated quantity for {item_name} to {new_quantity}.")
                else:
                    # Show message box if entered quantity is greater than available quantity
                    self.show_message("Error", "Entered quantity cannot be greater than available stock.")
            else:
                print(f"No item found with the name {item_name}.")
        else:
            print("Please enter a valid number for the quantity.")

    def show_message(self, title, message):
        """Shows a message box with the given title and message."""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

        #--------------------------------------------test-----------------------------/

        
        
        
        
    def search_item(self):
        search_text = self.form.lineEdit_search_item_lineedit.text().lower()
        for row in range(self.form.tableWidget_item_table.rowCount()):
            # Access the 'Name' column (assuming it's the first column)
            item_name = self.form.tableWidget_item_table.item(row, 0)

            if item_name:
                # Check if the search text is in the item's name
                if search_text in item_name.text().lower():
                    self.form.tableWidget_item_table.setRowHidden(row, False)
                else:
                    self.form.tableWidget_item_table.setRowHidden(row, True)
            else:
                self.form.tableWidget_item_table.setRowHidden(row, True)
                

    def add_stock(self):
        stock_name = self.form.lineEdit_stock_name_input.text().strip()
        if not stock_name:
            QMessageBox.warning(self, "Error", "Stock name cannot be empty!")
            return

        if stock_name in self.stocks:
            QMessageBox.warning(self, "Error", f"Stock '{stock_name}' already exists!")
            return

        self.stocks[stock_name] = []
        self.form.listWidget_stock_list.addItem(stock_name)
        self.form.lineEdit_stock_name_input.clear()
        #self.save_data_to_csv()

    import csv

    def delete_stock(self):
        selected_items = self.form.listWidget_stock_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "No stock selected for deletion!")
            return

        selected_stock = selected_items[0].text()
        confirmation = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete the stock '{selected_stock}' along with all its items?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmation == QMessageBox.Yes:
            if selected_stock in self.stocks:
                del self.stocks[selected_stock]

            list_items = self.form.listWidget_stock_list.findItems(selected_stock, Qt.MatchExactly)
            for item in list_items:
                self.form.listWidget_stock_list.takeItem(self.form.listWidget_stock_list.row(item))

            self.form.tableWidget_item_table.setRowCount(0)



            # Check if listWidget_stock_list has only one item
            print(self.form.listWidget_stock_list.count())
            if self.form.listWidget_stock_list.count() == 0:
                # Write a stock_data.csv with the specified header
                with open('stock_data.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Stock", "Item Name", "Rate (in Rs)", "Quantity"])
            else:
                # Call save_data_to_csv() if condition is not met
                self.save_data_to_csv()

            #QMessageBox.information(self, "Success", f"Stock '{selected_stock}' deleted!")
            self.label_status.setText(f"Stock '{selected_stock}' deleted!")
        
    
    
    def add_item(self):
        selected_items = self.form.listWidget_stock_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "No stock selected!")
            return

        stock_name = selected_items[0].text()
        item_name = self.form.lineEdit_item_name_input.text().strip()
        item_rate = self.form.lineEdit_item_rate_input.text().strip()
        item_quantity = self.form.lineEdit_item_quantity_input.text().strip()

        if not item_name or not item_rate:
            QMessageBox.warning(self, "Error", "Item name and rate cannot be empty!")
            return

        try:
            item_rate = float(item_rate)
            item_quantity = int(item_quantity) if item_quantity else 1
        except ValueError:
            QMessageBox.warning(self, "Error", "Rate must be a number and quantity must be an integer!")
            return

        self.stocks[stock_name].append({
            "name": item_name,
            "rate": item_rate,
            "quantity": item_quantity
        })
        self.label_status.setText(f"Item added to stock '{stock_name}'!")
        self.add_item_to_table(item_name, item_rate, item_quantity)
        self.form.lineEdit_item_name_input.clear()
        self.form.lineEdit_item_rate_input.clear()
        self.form.lineEdit_item_rate_input.clear()
        self.save_data_to_csv()

  


    def delete_item(self):
        selected_row = self.form.tableWidget_item_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "No item selected for deletion!")
            return

        selected_items = self.form.listWidget_stock_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "No stock selected!")
            return

        stock_name = selected_items[0].text()

        # Show confirmation dialog
        confirmation = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete the selected item from stock '{stock_name}'?",
            QMessageBox.Ok | QMessageBox.Cancel
        )

        if confirmation == QMessageBox.Ok:
            # Proceed with deletion
            del self.stocks[stock_name][selected_row]
            self.form.tableWidget_item_table.removeRow(selected_row)

            # Check if row count is less than 1
            if self.form.tableWidget_item_table.rowCount() < 1:
                # Write a stock_data.csv with the specified header
                with open('stock_data.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Stock", "Item Name", "Rate (in Rs)", "Quantity"])

            # Call save_data_to_csv() if row count is >= 1
            self.save_data_to_csv()

            #QMessageBox.information(self, "Success", f"Item deleted from stock '{stock_name}'!")
            self.label_status.setText(f"Item deleted from stock '{stock_name}'!")
        else:
            # If canceled, do nothing
            QMessageBox.information(self, "Action Canceled", "Deletion canceled.")
            self.label_status.setText("Deletion canceled.")



    def display_items(self, stock_item):
        stock_name = stock_item.text()
        self.form.tableWidget_item_table.setRowCount(0)
        if stock_name in self.stocks:
            for item in self.stocks[stock_name]:
                self.add_item_to_table(item['name'], item['rate'], item['quantity'])

    def add_item_to_table(self, name, rate, quantity):
        row = self.form.tableWidget_item_table.rowCount()
        self.form.tableWidget_item_table.insertRow(row)
        self.form.tableWidget_item_table.setItem(row, 0, QTableWidgetItem(name))
        self.form.tableWidget_item_table.setItem(row, 1, QTableWidgetItem(f"{rate:.2f}"))
        self.form.tableWidget_item_table.setItem(row, 2, QTableWidgetItem(str(quantity)))

    def update_stock_search(self, text):
        matches = self.form.listWidget_stock_list.findItems(text, Qt.MatchContains)
        for i in range(self.form.listWidget_stock_list.count()):
            item = self.form.listWidget_stock_list.item(i)
            item.setHidden(item not in matches)


    def save_data_to_csv(self):
        
        data = []
        for stock, items in self.stocks.items():
            for item in items:
                data.append({
                    "Stock": stock,
                    "Item Name": item['name'],
                    "Rate (in Rs)": item['rate'],
                    "Quantity": item['quantity']
                })
        df = pd.DataFrame(data)
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            df.to_csv(file, index=False)
            


        



    def load_data_from_csv(self):
        import os
        
        self.form.tableWidget_item_table.setRowCount(0)
        if self.form.listWidget_stock_list.count() > 0:
            # Select the first item (index 0)
            self.form.listWidget_stock_list.setCurrentRow(0)
        try:
            if not os.path.exists(self.csv_file) or os.path.getsize(self.csv_file) == 0:
               
                return

            df = pd.read_csv(self.csv_file)
            if df.empty:
                return

            self.stocks.clear()
            self.form.listWidget_stock_list.clear()

            for _, row in df.iterrows():
                stock = row['Stock']
                item_name = row['Item Name']
                item_rate = row['Rate (in Rs)']
                item_quantity = row['Quantity']

                if stock not in self.stocks:
                    self.stocks[stock] = []
                    self.form.listWidget_stock_list.addItem(stock)

                self.stocks[stock].append({
                    "name": item_name,
                    "rate": item_rate,
                    "quantity": item_quantity
                })
        except FileNotFoundError:
            pass
        except pd.errors.EmptyDataError:
            pass
        
        
    #-----------------------------------------Sell Bill with Gst Section------------------------------
    
    
    
    
    
    
    
        
        
        
        
        
        
    def add_item_row(self):
        """Add a new row to the item table."""
        row_position = self.form.table_item_table.rowCount()
        self.form.table_item_table.insertRow(row_position)

        # Create a new QLineEdit for suggestions for each row
        suggest_item_input = QLineEdit()
        # Apply the same functionality or setup for the new QLineEdit
        suggest_item_input.textChanged.connect(self.update_item_details1)
        self.setup_suggestions(suggest_item_input)
        
        suggest_item_input_qty = QLineEdit()
        suggest_item_input_qty.setValidator(QDoubleValidator(0, 999999, 2))  # Only allow valid rates
        self.setup_suggestions_qty(suggest_item_input_qty)
        suggest_item_input_qty.textChanged.connect(lambda: self.update_row_totals(row_position))
        

        spinbox_qty = QSpinBox()
        spinbox_qty.setMinimum(1)  # Set the minimum value to 1
        spinbox_qty.setValue(1) 
        
        spinbox_qty.valueChanged.connect(lambda: self.update_row_totals(row_position))
        
        # Add widgets to the row
        self.form.table_item_table.setCellWidget(row_position, 0, suggest_item_input)  # Description
        self.form.table_item_table.setCellWidget(row_position, 1, QLineEdit())  # HSN Code
        self.form.table_item_table.setCellWidget(row_position, 2, spinbox_qty)  # Quantity
        self.form.table_item_table.cellWidget(row_position, 2).setMaximum(99999)

        
        
        self.form.table_item_table.setCellWidget(row_position, 3, suggest_item_input_qty)  # Rate

        gst_rate_combo = QComboBox()
        gst_rate_combo.addItems(["0", "5", "12", "18", "28"])
        gst_rate_combo.currentIndexChanged.connect(
            lambda: self.update_row_totals(row_position)
        )
        self.form.table_item_table.setCellWidget(row_position, 4, gst_rate_combo)  # GST Rate

        self.form.table_item_table.setItem(row_position, 5, QTableWidgetItem("0.0"))  # CGST
        self.form.table_item_table.setItem(row_position, 6, QTableWidgetItem("0.0"))  # SGST
        self.form.table_item_table.setItem(row_position, 7, QTableWidgetItem("0.0"))  # Total



    def setup_suggestions(self, line_edit):
        """Set up suggestions for a QLineEdit."""
        



        self.model_item1 = QStringListModel(self.item_names)
        self.completer_item1 = QCompleter(self.model_item1)
        line_edit.setCompleter(self.completer_item1)
        
        
    def setup_suggestions_qty(self, line_edit1):
        
        self.model_quantity2 = QStringListModel(self.quantities)
        self.completer_quantity2 = QCompleter(self.model_quantity2)
        line_edit1.setCompleter(self.completer_quantity)
        
    '''    def setup_suggestions_rate(self,rate1):
            
            self.model_quantity = QStringListModel(self.rate)
            self.completer_quantity = QCompleter(self.model_quantity)
            self.form.lineEdit_suggest_quantity.setCompleter(self.completer_quantity)'''
        
        
    def update_item_details1(self):
        """Update the available quantity and rate based on item selection."""
        item_name = self.form.lineEdit_suggest_item.text()

        # Check if the item exists in the stock data
        row = self.df1[self.df1['Item Name'] == item_name]

        if not row.empty:
            # Get the current quantity and rate from the CSV
            available_quantity = row['Quantity'].values[0]
            rate = row['Rate (in Rs)'].values[0]

            # Update the available quantity and rate fields
            self.form.label_suggest_qty.setText(f"Available Quantity: {available_quantity}")
            self.form.lineEdit_suggest_rate.setText(f"{rate}")
        else:
            self.form.label_suggest_qty.setText("Available Quantity: N/A")
            self.form.lineEdit_suggest_rate.clear()
            
            
            

    def update_row_totals(self, row):
        """Update CGST, SGST, and total for a specific row."""
        try:
            quantity = self.form.table_item_table.cellWidget(row, 2).value()
            rate = float(self.form.table_item_table.cellWidget(row, 3).text() or 0)
            gst_rate = int(self.form.table_item_table.cellWidget(row, 4).currentText())

            # Calculate CGST and SGST
            taxable_value = quantity * rate
            cgst = taxable_value * (gst_rate / 2) / 100
            sgst = taxable_value * (gst_rate / 2) / 100
            total = taxable_value + cgst + sgst

            # Update table
            self.form.table_item_table.setItem(row, 5, QTableWidgetItem(f"{cgst:.2f}"))
            self.form.table_item_table.setItem(row, 6, QTableWidgetItem(f"{sgst:.2f}"))
            self.form.table_item_table.setItem(row, 7, QTableWidgetItem(f"{total:.2f}"))

        except ValueError:
            pass  # Gracefully handle invalid input
        
            



    def pdf_template2(self):
        
        try:
                
            output_path = "tax_invoice.pdf"
            # Create a PDF document
            pdf = SimpleDocTemplate(output_path, pagesize=A4)
            elements = []

            # Add a margin border
            def add_margin_border(canvas, doc):
                canvas.saveState()
                canvas.setStrokeColor(colors.black)
                canvas.setLineWidth(1)
                canvas.rect(10, 10, A4[0] - 20, A4[1] - 20)
                canvas.restoreState()

            styles = getSampleStyleSheet()
            
            grand_total = 0
            total_cgst = 0
            total_sgst = 0

            # Company and Invoice Details
            elements.append(Paragraph("<b>ABC Private Limited</b>", styles['Normal']))
            elements.append(Paragraph("<b>INVOICE RECEIPT</b>", styles['Title']))
            elements.append(Spacer(1, 20))

            # Display shop and contact details as text
            elements.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y')}", styles['Normal']))
            elements.append(Paragraph(f"<b>Shop Name:</b> {self.form.lineEdit_shop_name.text()}", styles['Normal']))
            elements.append(Paragraph(f"<b>Shop Address:</b> {self.form.lineEdit_shop_address.text()}", styles['Normal']))
            elements.append(Paragraph(f"<b>Aadhaar Number:</b> 1234-5678-9876", styles['Normal']))
            elements.append(Paragraph(f"<b>Mobile Number:</b> 9876543210", styles['Normal']))
            elements.append(Paragraph(f"<b>Email:</b> abc@gmail.com", styles['Normal']))
            elements.append(Spacer(1, 20))

            # Section 2: Billing and Shipping Address
            billing_details = [
                ["Billing Address", "Shipping Address"],
                [f"{self.form.lineEdit_shop_address.text()}, City", "456, Another St, City"],
                [f"GSTIN: {self.form.lineEdit_shop_gstin.text()}", "GSTIN: GST987654321"]
            ]

            billing_table = Table(billing_details, colWidths=[280, 280])
            billing_table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ]))
            elements.append(billing_table)
            elements.append(Spacer(1, 20))

            # Section 3: Items Table (Including CGST, SGST, and Total)
            item_data = [
                            ["Description"    ,"HSN CODE" ,"Qty", "Amount" , "Total" ,"GST Rate", "CGST" , "SGST","Total"]
            ]
            
            
            for row in range(self.form.table_item_table.rowCount()):
                description = self.form.table_item_table.cellWidget(row, 0).text()
                hsn = self.form.table_item_table.cellWidget(row, 1).text()
                quantity = self.form.table_item_table.cellWidget(row, 2).value()
                rate = float(self.form.table_item_table.cellWidget(row, 3).text() or 0)
                gst_rate = int(self.form.table_item_table.cellWidget(row, 4).currentText())
                cgst = float(self.form.table_item_table.item(row, 5).text())
                sgst = float(self.form.table_item_table.item(row, 6).text())
                total = float(self.form.table_item_table.item(row, 7).text())

                
                item_data.append([f'{description}'          ,hsn       ,quantity    , rate   , 843.23  , gst_rate  ,cgst  , sgst , total])
                grand_total += total
                total_cgst += cgst
                total_sgst += sgst
            

            items_table = Table(item_data, colWidths=[150, 70, 40, 50, 50, 50, 50, 50, 50])
            items_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
            ]))
            elements.append(items_table)

            # Section 4: Total GST and Invoice Amount
            total_cgst_sgst = grand_total  # Sum of CGST and SGST
            total_invoice = 11683.81

            elements.append(Spacer(1, 20))

            totals = [
                ["Total GST Amount:", "1748.95"],
                ["Total Invoice Amount:", "11683.81"],
                ["Total CGST + SGST:", f"{total_cgst_sgst:.2f}"]
            ]
            totals_table = Table(totals, colWidths=[460, 100])
            totals_table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('ALIGN', (0, 0), (-1, -1), 'RIGHT')
            ]))
            elements.append(totals_table)


            bank_name = self.form.lineEdit_bank_name.text()
            acc_no = self.form.lineEdit_account_number.text()
            ifsc = self.form.lineEdit_ifsc_code.text()
            branch = self.form.lineEdit_branch.text()
            
            # Section 5: Authorized Signatory and Bank Details
            elements.append(Spacer(1, 60))
            elements.append(Paragraph("<b>Authorized Signatory</b>", styles['Normal']))
            elements.append(Spacer(1, 20))
            elements.append(Paragraph(f"<i>Bank Details:</i> {bank_name}, A/C: {acc_no}, IFSC: {ifsc}, Branch: {branch}", styles['Normal']))
            elements.append(Paragraph("<i>Terms and Conditions:</i> Payment due within 30 days.", styles['Normal']))

            # Build PDF
            pdf.build(elements, onFirstPage=add_margin_border, onLaterPages=add_margin_border)

            print('Pdf saved as tax_invoice.pdf')
            self.label_status.setText("Pdf saved as tax_invoice.pdf")
            
            
        except Exception as e:
            print(f"An error occurred: {e}")
            QMessageBox.warning(self, "Error", "An error occurred while generating the PDF.")
            self.label_status.setText("An error occurred while generating the PDF.")
                   
    def pdf_template1(self):
        """Save the invoice data as a PDF."""
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        #pdf.set_auto_page_break(auto=True, margin=5)
        pdf.add_page()
       
        pdf.set_font("Arial", size=12)
        
        # Header
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Tax Invoice", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop Name: {self.form.lineEdit_shop_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop Address: {self.form.lineEdit_shop_address.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop GSTIN: {self.form.lineEdit_shop_gstin.text()}", ln=True, align="L")

        pdf.cell(100, 10, txt=f"Customer Name: {self.form.lineEdit_customer_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Customer Address: {self.form.lineEdit_customer_address.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Customer GSTIN: {self.form.lineEdit_customer_gstin.text()}", ln=True, align="L")

        # Add space
        pdf.set_xy(5, 100)
        # Table Header
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(40, 10, "Description", border=1, align="C")
        pdf.cell(30, 10, "HSN Code", border=1, align="C")
        pdf.cell(20, 10, "Quantity", border=1, align="C")
        pdf.cell(20, 10, "Rate", border=1, align="C")
        pdf.cell(20, 10, "GST%", border=1, align="C")
        pdf.cell(20, 10, "CGST", border=1, align="C")
        pdf.cell(20, 10, "SGST", border=1, align="C")
        pdf.cell(30, 10, "Total", border=1, align="C")
        pdf.ln()

        # Table Rows
        pdf.set_font("Arial", size=12)
        grand_total = 0
        total_cgst = 0
        total_sgst = 0
        
        
        
        

        for row in range(self.form.table_item_table.rowCount()):
            description = self.form.table_item_table.cellWidget(row, 0).text()
            hsn = self.form.table_item_table.cellWidget(row, 1).text()
            quantity = self.form.table_item_table.cellWidget(row, 2).value()
            rate = float(self.form.table_item_table.cellWidget(row, 3).text() or 0)
            gst_rate = int(self.form.table_item_table.cellWidget(row, 4).currentText())
            cgst = float(self.form.table_item_table.item(row, 5).text())
            sgst = float(self.form.table_item_table.item(row, 6).text())
            total = float(self.form.table_item_table.item(row, 7).text())

            pdf.set_x(5)
            
            pdf.cell(40, 10, description, border=1)
            pdf.cell(30, 10, hsn, border=1, align="C")
            pdf.cell(20, 10, str(quantity), border=1, align="C")
            pdf.cell(20, 10, f"{rate:.2f}", border=1, align="C")
            pdf.cell(20, 10, str(gst_rate), border=1, align="C")
            pdf.cell(20, 10, f"{cgst:.2f}", border=1, align="C")
            pdf.cell(20, 10, f"{sgst:.2f}", border=1, align="C")
            pdf.cell(30, 10, f"{total:.2f}", border=1, align="C")
            pdf.ln()

            # Update totals
            grand_total += total
            total_cgst += cgst
            total_sgst += sgst
            
            
        pdf.ln(10)  # Add space for banking details


        # Totals
        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(100, 10, "Grand Total", ln=True)
        pdf.cell(50, 10, f"Total CGST: {total_cgst:.2f}", ln=True)
        pdf.cell(50, 10, f"Total SGST: {total_sgst:.2f}", ln=True)
        pdf.cell(50, 10, f"Total: {grand_total:.2f}", ln=True)




        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Banking Details", ln=True, align="L")

        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=f"Bank Name: {self.form.lineEdit_bank_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Account Number: {self.form.lineEdit_account_number.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"IFSC Code: {self.form.lineEdit_ifsc_code.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Branch: {self.form.lineEdit_branch.text()}", ln=True, align="L")




        # Save the PDF
        file_name = f"Tax_Invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(file_name)
        print(f"Invoice saved as {file_name}")
        
        self.label_status.setText("Invoice Saved Successfully.")
        self.update_quantity()



    def update_quantity(self):
        # Load the CSV file
        df2 = pd.read_csv('stock_data.csv')

        # Loop through each row in the table
        for row in range(self.form.table_item_table.rowCount()):
            # Get the widget in the Description column
            widget_description = self.form.table_item_table.cellWidget(row, 0)
            description = widget_description.text() if widget_description is not None else ""

            # Get the widget in the Quantity column
            widget_quantity = self.form.table_item_table.cellWidget(row, 2)
            if widget_quantity is not None:
                quantity = widget_quantity.value()  # Get the value from the QSpinBox
            else:
                quantity = 0  # Handle the case when there's no widget

            # Check for matching description in CSV
            mask = df2['Item Name'].str.lower() == description.lower()
            if mask.any():  # If the description is found
                # Get the quantity from the CSV
                csv_quantity = df2.at[df2[mask].index[0], 'Quantity']

                if quantity > csv_quantity:
                    # Show a message box if quantity entered is greater than the CSV quantity
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f"The quantity entered ({quantity}) exceeds the available quantity ({csv_quantity}) in stock.")
                    msg.setWindowTitle("Quantity Exceeded")
                    msg.exec()
                else:
                    # Decrement the quantity in the dataframe
                    idx = df2[mask].index[0]  # Get the index of the matched item
                    df2.at[idx, 'Quantity'] = max(0, csv_quantity - quantity)  # Decrement quantity

                    # Update the table cell with the new quantity
                    self.form.table_item_table.cellWidget(row, 2).setValue(df2.at[idx, 'Quantity'])  # Update the table widget

                    # Optionally print the updated row for verification
                    print(f"Updated {description}: New Quantity = {df2.at[idx, 'Quantity']}")

        # Save the updated dataframe back to the CSV
        
        df2.to_csv('stock_data.csv', index=False)





    def workspace(self):
        if self.form.comboBox_4.currentIndex() <1:
            self.form.widget_5.setVisible(True)
            self.form.widget_6.setVisible(True)
            
            self.form.widget_6.setGeometry(0,382,1140,374)
            self.form.tableWidget_2.setGeometry(10,27,1121,306)
            self.form.lineEdit_get.move(12,341)
            self.form.lineEdit_for_what.move(137,341)
            self.form.lineEdit_giver.move(253,341)
            self.form.toolButton_save2.move(670,339)
            self.form.label_monthly_gains.move(738,335)
            self.form.label_total_gains.move(950,340)
            
            self.form.widget_5.setGeometry(0,0,1140,360)
            self.form.tableWidget_1.setGeometry(10,27,1121,301)
            self.form.lineEdit_spend.move(12,331)
            self.form.lineEdit_item.move(137,331)
            self.form.lineEdit_reciepent.move(253,331)
            self.form.toolButton_save1.move(670,329)
            self.form.label_total_expense.move(740,325)
            self.form.label_total_spends.move(972,331)
            
            
            
            
        elif self.form.comboBox_4.currentIndex()==1:
            self.form.widget_5.setVisible(False)
            
            self.form.widget_6.setVisible(True)
            self.form.widget_6.setGeometry(0,0,1140,760)
            self.form.tableWidget_2.setGeometry(10,27,1140,690)
            self.form.lineEdit_get.move(12,723)
            self.form.lineEdit_for_what.move(137,723)
            self.form.lineEdit_giver.move(253,723)
            self.form.toolButton_save2.move(670,723)
            self.form.label_monthly_gains.move(738,720)
            self.form.label_total_gains.move(950,723)
        
        elif self.form.comboBox_4.currentIndex()==2:
            self.form.widget_6.setVisible(False)
            
            self.form.widget_5.setVisible(True)
            
            self.form.widget_5.setGeometry(0,0,1140,760)
            self.form.tableWidget_1.setGeometry(10,27,1140,690)
            self.form.lineEdit_spend.move(12,723)
            self.form.lineEdit_item.move(137,723)
            self.form.lineEdit_reciepent.move(253,723)
            self.form.toolButton_save1.move(670,723)
            self.form.label_total_expense.move(738,720)
            self.form.label_total_spends.move(950,723)
        
    def theme_light(self):
        
        self.label1.setStyleSheet('color:black;')
        self.form.label.setStyleSheet(u"background-color: rgb(184, 184, 184);color: rgb(0, 0, 0);")
        self.form.lineEdit_income0.setStyleSheet(u"")
        self.form.widget.setStyleSheet(u"background-color: rgb(38, 38, 38);color: rgb(0, 0, 0);")
        self.form.calendarWidget.setStyleSheet(u"""
        background-color: rgb(221, 221, 221);
        font: 11pt "Segoe UI";
        color: rgb(49, 77, 107);
        border-color: rgb(95, 95, 95);
        selection-color: rgb(248, 248, 248);
        gridline-color: rgb(111, 111, 111);
        selection-background-color: rgb(126, 126, 126);""")



        
        
        self.form.widget_5.setStyleSheet(u"background-color: rgb(154, 154, 154);color: rgb(0, 0, 0);")
        self.form.tableWidget_1.setStyleSheet(u"background-color: rgb(230, 230, 230);color: rgb(0, 0, 0);")
        self.form.lineEdit_spend.setStyleSheet(u"background-color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.lineEdit_item.setStyleSheet(u"background-color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.lineEdit_reciepent.setStyleSheet(u"background-color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.toolButton_del_row.setStyleSheet(u"")
        self.form.toolButton_del_row_2.setStyleSheet(u"")
        
        self.form.label_total_expense.setStyleSheet(u"")
        self.form.label_monthly_gains.setStyleSheet(u"")
        
        self.form.toolButton_save1.setStyleSheet(u"")
        self.form.toolButton_save2.setStyleSheet(u"")
        
        self.form.lineEdit_income.setStyleSheet(u"")
        self.form.lineEdit_income0.setStyleSheet(u"")
        self.form.comboBox_4.setStyleSheet(u"")
        self.form.comboBox_3.setStyleSheet(u"")
        self.form.toolButton_expand.setStyleSheet(u"")
        self.form.lineEdit_calc.setStyleSheet(u"")
        
        self.form.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.form.textEdit.setStyleSheet(u"background-color: rgb(140, 140, 140);color: rgb(0, 0, 0);")
        self.form.label_name.setStyleSheet(u"color: rgb(83, 255, 206);color: rgb(0, 0, 0);")
        self.form.label_income.setStyleSheet(u"color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        
        self.form.label_expense.setStyleSheet(u"color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.label_savings.setStyleSheet(u"color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.label_gains.setStyleSheet(u"color: rgb(175, 198, 217);color: rgb(0, 0, 0);")
        self.form.widget_6.setStyleSheet(u"background-color: rgb(154, 154, 154);color: rgb(0, 0, 0);")
        self.form.tableWidget_2.setStyleSheet(u"background-color: rgb(230, 230, 230);color: rgb(0, 0, 0);")
        
        self.form.lineEdit_get.setStyleSheet(u"background-color: rgb(174, 197, 216);color: rgb(0, 0, 0);")
        self.form.lineEdit_for_what.setStyleSheet(u"background-color: rgb(174, 197, 216);color: rgb(0, 0, 0);")
        self.form.lineEdit_giver.setStyleSheet(u"background-color: rgb(174, 197, 216);color: rgb(0, 0, 0);")
        self.form.label_calc.setStyleSheet(u"color: rgb(83, 255, 206);color: rgb(0, 0, 0);")
        self.form.label_14.setStyleSheet(u"color: rgb(0, 0, 0);color: rgb(0, 0, 0);")
        self.form.widget_graph_2.setStyleSheet(u"background-color: rgb(28, 28, 28);color: rgb(0, 0, 0);")
        self.form.label_date.setStyleSheet(u"color: rgb(107, 139, 255);color: rgb(0, 0, 0);")
        self.form.menubar.setStyleSheet(u"background-color: rgb(175, 198, 217);\n"
        "border-color: rgb(130, 255, 213);\n"
        "alternate-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(98, 255, 156);\n"
        "selection-background-color: rgb(49, 49, 49);\n"
        "gridline-color: rgb(97, 46, 46);\n"
        "color: rgb(0, 0, 0);")
                
    def theme_dark(self):
        
        self.label1.setStyleSheet('color:white;')
        self.form.label.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.form.widget.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        
        self.form.calendarWidget.setStyleSheet(u"""
        
            color: rgb(119, 110, 242);
            alternate-background-color: rgb(57, 57, 91);
            font: 11pt "Segoe UI";
            background-color: rgb(31, 31, 49);
            border-color: rgb(95, 95, 95);
            selection-color: rgb(248, 248, 248);
            gridline-color: rgb(111, 111, 111);
            selection-background-color: rgb(28, 28, 28);
        
        """)
        
        
        self.form.textEdit_notes.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
        "color: rgb(98, 255, 156);")
        self.form.widget_5.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.form.label_expense_record.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_total_expense.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.form.label_total_spends.setStyleSheet(u"color: rgb(255, 133, 192);")
        self.form.tableWidget_1.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
        "border-color: rgb(130, 255, 213);\n"
        "\n"
        "\n"
        "selection-color: rgb(0, 0, 0);\n"
        "gridline-color: rgb(97, 46, 46);\n"
        "color: rgb(255, 193, 106);")
        
        self.form.lineEdit_spend.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
                
        self.form.toolButton_save1.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
        "color: rgb(0, 0, 0);")
        self.form.lineEdit_item.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
        
        
        self.form.lineEdit_reciepent.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
        
        self.form.toolButton_del_row.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
        "color: rgb(255, 0, 0);")
                
        self.form.label_13.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.textEdit.setStyleSheet(u"background-color: rgb(31, 31, 49);")
        
        self.form.label_name.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_income.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_expense.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_savings.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_gains.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.widget_6.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.form.label_extra_gains.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_monthly_gains.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.form.label_total_gains.setStyleSheet(u"color: rgb(174, 255, 82);")
        
        
        self.form.tableWidget_2.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
        "border-color: rgb(130, 255, 213);\n"
        "selection-background-color: rgb(75, 251, 175);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "gridline-color: rgb(29, 75, 46);\n"
        "color: rgb(75, 251, 175);")
                
        self.form.lineEdit_get.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
        
        self.form.toolButton_save2.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
        "color: rgb(0, 0, 0);")
                        
        self.form.lineEdit_for_what.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
        
        self.form.lineEdit_giver.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(83, 248, 195);asd")
                
        self.form.toolButton_del_row_2.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
        "color: rgb(255, 0, 0);")
                
        self.form.lineEdit_income.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 170, 0);")
                
        self.form.comboBox_3.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
        "selection-color: rgb(255, 255, 255);\n"
        "color: rgb(98, 255, 156);")     
        
        
        self.form.lineEdit_calc.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 170, 0);")
        self.form.label_calc.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.label_14.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.form.lineEdit_income0.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
        "alternate-background-color: rgb(225, 225, 225);\n"
        "selection-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 170, 0);")
        
        self.form.widget_graph.setStyleSheet(u"background-color: rgb(28, 28, 28);")
        self.form.widget_graph_2.setStyleSheet(u"background-color: rgb(28, 28, 28);")
        self.form.toolButton_expand.setStyleSheet(u"background-color: rgb(137, 143, 255);\n"
        "color: rgb(0, 0, 0);")    
        self.form.label_date.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.form.comboBox_4.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
        "selection-color: rgb(255, 255, 255);\n"
        "color: rgb(255, 255, 255);")
        
        self.form.menubar.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
        "border-color: rgb(130, 255, 213);\n"
        "alternate-background-color: rgb(137, 143, 255);\n"
        "selection-color: rgb(98, 255, 156);\n"
        "selection-background-color: rgb(49, 49, 49);\n"
        "gridline-color: rgb(97, 46, 46);\n"
        "color: rgb(255, 255, 255);")
                
                    
    def info(self):
        global k1
        k1 = about_form()
        k1.show()

        
    def hider(self):
        global win_width,win_height

        k_name = admin_name
        self.form.label_name.setText(k_name)
        
        self.animation = QPropertyAnimation(self, b"geometry")
            # Set the duration of the animation (1000 ms = 1 second)
        self.animation.setDuration(200)

        
        if self.width()>1300:

            
            # Set the start and end geometry
            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 1160, 850)   # Final size
            #self.resize(850,435)
            win_width,win_height = 1160,850
            
            self.save_settings()
        elif self.height()<440 and self.width()<1300:

            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 1500, 850)   # Final size
            #self.resize(850,435)
            win_width,win_height = 1500,850
            self.save_settings()
        else:
            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 1160, 435)
            #self.resize(1200,850)
            win_width,win_height = 1160,435
            self.save_settings()


        self.animation.setStartValue(start_geometry)
        self.animation.setEndValue(end_geometry)
        self.animation.start()

      


    def closer(self):
        QApplication.exit()

    def snap_save(self):
        
        save_path = r'snap\\'
        now1 = datetime.now().strftime('%d%b%y_%H%M')
    
       
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        screenshot = script()
        screenshot.save(os.path.join(save_path, f'{now1}.jpg'))
        
    def save_notes(self):
        html_content = self.form.textEdit_notes.toPlainText()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "TEXT Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(html_content)
                #self.form_notes.label.setText('Html Docs Saved.')
                #QMessageBox.information(self, "Saved", "HTML content saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save HTML content: {e}")
                #self.form_notes.label.setText('Html Docs Failed to save.')

    def plotter(self):
        k1 = pd.read_csv(filename)
        y2 = k1['curr_income']

        if len(y2)!=0:
            self.index = y2
            x1 = [p for p in range(len(y2))]
            
    
        
            # Plotting the bar 
            bar = pg.BarGraphItem(x=x1, height=y2, width=0.6, brush=QColor(165, 187, 230))
            self.plot_widget.addItem(bar)
            #self.bars.append(bar)


        k2 = pd.read_csv(filename2)
        y3 = k2['curr_gain']

        if len(y3)!=0:
            self.index2 = y3
            x2 = [p2 for p2 in range(len(y3))]
            
    
        
            # Plotting the bar
            bar2 = pg.BarGraphItem(x=x2, height=y3, width=0.6, brush=QColor(150, 200, 150))
            self.plot_widget2.addItem(bar2)
            #self.bars.append(bar)


    def refresher(self):
        global current_income,total_spends,win_width,win_height
        #global data_json
        
      
        
      
        with open("settings.json", "r") as json_file:
            data_json = json.load(json_file) 

        if data_json['theme']=='dark':
            pass
            #self.theme_dark()
        else:
            pass
            #self.theme_light()
            
        self.form.lineEdit_income.setText(data_json['current_income'])
        self.form.label_total_spends.setText(data_json['total_spends'])
        
        self.form.lineEdit_income0.setText(data_json['monthly_income'])
        
        self.form.textEdit_notes.setText(data_json['previous_note'])
        self.form.label_total_gains.setText(data_json['total_gains'])
      
        self.form.label_income.setText(data_json['monthly_income'])
        self.form.label_expense.setText(data_json['total_spends'])
        self.form.label_savings.setText(str(int(data_json['current_income'])-int(data_json['total_spends'])))
        self.form.label_gains.setText(data_json['total_gains'])
        self.form.label_name.setText(data_json["admin_name"])
        

        current_income = self.form.lineEdit_income.text()
        total_spends = data_json['total_spends']

        win_width = int(data_json['screen_width'])
        win_height = int(data_json['screen_height'])

        
    
    
        

       


        self.plotter()

    def save_settings(self):

        data = {
            
            
            "admin_name":admin_name,
            "gmail":gmail,
            "contact_no":contact_no,
            "company_name":company_name,
            "shop_name":shop_name,
            
            "current_income": str(self.form.lineEdit_income.text()),
            "total_spends": str(self.form.label_total_spends.text()),
            "monthly_income":str(self.form.lineEdit_income0.text()),
            "previous_note": str(self.form.textEdit_notes.toPlainText()),
            "total_gains": str(self.form.label_total_gains.text()),
            "screen_width": win_width,
            "screen_height": win_height,
            "others_show":True,
            "others_hide":False,
            "admin_name":str(self.form.label_name.text()),
            "theme":theme
           
        }
        
        
        

        # Saving the dictionary as a JSON file
        with open("settings.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data saved to data.json")
        self.label_status.setText("Data saved to data.json")
        self.refresher()

    def delete_row_from_csv(self, index1):
        file_path = filename
        index_from_end = index1+1
        # Read the content of the CSV file into a list
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Calculate the actual index from the start
        row_index = len(rows) - index_from_end

        # Check if the row index is valid
        if row_index < 1 or row_index >= len(rows):
            QMessageBox.warning(self, "No Selection", "Please select a Valid row to delete.")
            return

        item10 = self.form.tableWidget_1.item(index1, 0) 
    
        currincome = int(self.form.lineEdit_income.text())
        item_val = int(item10.text())
        new_income = currincome + item_val

        self.form.lineEdit_income.setText(str(new_income))
        # Delete the row at the calculated index
        del rows[row_index]

        # Write the modified rows back to the CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        #print(f"Row {index_from_end} from the end deleted successfully.")
      
        self.save_settings()

        

    def delete_row(self):
        # Get the selected row
        selected_row = self.form.tableWidget_1.currentRow()
       
        if selected_row >-1:  # -1 means no selection
            # Confirm the deletion
            reply = QMessageBox.question(self, 'Delete Row', 
                                         "Are you sure you want to delete the selected row?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Remove the selected row
                
                self.delete_row_from_csv(selected_row)
                self.form.tableWidget_1.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")

    #---------------------------------------------------------------------------
    def delete_row_from_csv2(self, index2):
        file_path2 = filename2
        index_from_end2 = index2+1
       
        with open(file_path2, 'r', newline='') as file2:
            reader2 = csv.reader(file2)
            rows2 = list(reader2)

       
        row_index2 = len(rows2) - index_from_end2

        if row_index2 < 1 or row_index2 >= len(rows2):
            QMessageBox.warning(self, "No Selection", "Please select a Valid row to delete.")
            return

        item12 = self.form.tableWidget_2.item(index2, 0) 
    
        currincome2 = int(self.form.lineEdit_income.text())
        item_val2 = int(item12.text())
        new_income2 = currincome2 + item_val2

        del rows2[row_index2]
        with open(file_path2, 'w', newline='') as file2:
            writer2 = csv.writer(file2)
            writer2.writerows(rows2)

        
        self.save_settings()


    def delete_row2(self):
       
        selected_row2 = self.form.tableWidget_2.currentRow()
       
        if selected_row2 >-1:  
           
            reply2 = QMessageBox.question(self, 'Delete Row', 
                                         "Are you sure you want to delete the selected row?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply2 == QMessageBox.Yes:
                # Remove the selected row
                
                self.delete_row_from_csv2(selected_row2)
                self.form.tableWidget_2.removeRow(selected_row2)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")



    def load_csv1(self, file_path):
        # Read the CSV file in reverse order
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))
            reader.reverse()  # Reverse the order of rows

            # Set the number of rows and columns
            self.form.tableWidget_1.setRowCount(len(reader))
            self.form.tableWidget_1.setColumnCount(len(reader[0])-1)

            # Populate QTableWidget with data
            for row_index, row_data in enumerate(reader):
                for column_index, cell_data in enumerate(row_data):
                    self.form.tableWidget_1.setItem(row_index, column_index, QTableWidgetItem(cell_data))
    
    def load_csv2(self, file_path2):
        # Read the CSV file in reverse order
        with open(file_path2, newline='', encoding='utf-8') as csvfile2:
            reader2 = list(csv.reader(csvfile2))
            reader2.reverse()  # Reverse the order of rows

            # Set the number of rows and columns
            self.form.tableWidget_2.setRowCount(len(reader2))
            self.form.tableWidget_2.setColumnCount(len(reader2[0])-1)

            # Populate QTableWidget with data
            for row_index2, row_data2 in enumerate(reader2):
                for column_index2, cell_data2 in enumerate(row_data2):
                    self.form.tableWidget_2.setItem(row_index2, column_index2, QTableWidgetItem(cell_data2))

    def calc(self):
        # Get the text from the line edit
        expression = self.form.lineEdit_calc.text()
        self.form.label_calc.setText(expression+' = ')
        try:
            # Evaluate the expression and display the result
            result = eval(expression)
            self.form.lineEdit_calc.setText(str(result))
        except Exception as e:
            self.form.lineEdit_calc.setText("Error: " + str(e))
    
    def plot_red_bar(self):
        global current_income
        self.form.tabWidget_2.setCurrentIndex(0)
        money = self.form.lineEdit_spend.text()
        remain1 = int(current_income)-int(money)
        
        y1_income.append(int(remain1))
        self.form.lineEdit_income.setText(str(remain1))
        current_income = remain1
        
        self.data_saver1()


    def plot_blue_bar(self):

        global current_income

        self.form.tabWidget_2.setCurrentIndex(1)
        money2 = self.form.lineEdit_get.text()
        remain2 = int(current_income)+int(money2)
        
        y1_income.append(int(remain2))
        self.form.lineEdit_income.setText(str(remain2))
        current_income = remain2
        
        self.data_saver2()

    def plot_bar(self, color,mon):
        x = [self.index]  # X position for the bar
        height = [mon]  # Height of the bar
        
        # Plotting the bar
        bar = pg.BarGraphItem(x=x, height=height, width=0.6, brush=color)
        self.plot_widget.addItem(bar)
        self.bars.append(bar)
        
        
        # Update the index for the next bar
        self.index += 1


    '''def graph_plotter(self,money,col):
        global y1_income,monthly_income
     

        remain1 = int(monthly_income)-int(money)
        
        y1_income.append(int(remain1))
        self.form.lineEdit_income.setText(str(remain1))
        monthly_income = remain1

        print(monthly_income)
        if len(y1_income)<=7:

            y = y1_income+[0 for ar in range(7-len(y1_income))]
            x = np.arange(1,8)
            # Set the bar color to rgb(107, 139, 255)
            
            # Create a bar graph item with the specified color
            if col==0:

                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush='r')
                
            else:
                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush='b')

            self.plot_widget.addItem(bg)
        else:
            y = y1_income
            x = np.arange(len(y))
            # Set the bar color to rgb(107, 139, 255)
            
            # Create a bar graph item with the specified color
            if col==0:

                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush=QColor(107, 139, 255))
            else:
                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush=QColor(0, 255, 0))

            self.plot_widget.addItem(bg)'''





    def data_saver1(self):
        global k0
        
        a1 = self.form.lineEdit_spend.text()
        a2 = self.form.lineEdit_item.text()
        a3 = self.form.lineEdit_reciepent.text()
        a5 = self.form.lineEdit_income.text()



        now = datetime.now()
        a4 = now.strftime("%d/%m/%Y %#I:%M%p")

        self.form.tableWidget_1.insertRow(0)

        self.form.tableWidget_1.setItem(0, 0, QTableWidgetItem(a1))
        self.form.tableWidget_1.setItem(0, 2, QTableWidgetItem(a2))
        self.form.tableWidget_1.setItem(0, 4, QTableWidgetItem(a3))
        self.form.tableWidget_1.setItem(0, 6, QTableWidgetItem(a4))
        k0+=1
        #self.graph_plotter(a1,0)

        spend_save(data1=[a1,' ',a2,' ',a3,' ',a4,a5],)

        self.save_settings()


    def data_saver2(self):
        global l0
        b1 = self.form.lineEdit_get.text()
        b2 = self.form.lineEdit_for_what.text()
        b3 = self.form.lineEdit_giver.text()

        b5 = self.form.label_total_gains.text()
        now1 = datetime.now()
        b4 = now1.strftime("%d/%m/%Y %#I:%M%p")

        self.form.tableWidget_2.insertRow(0)

        self.form.tableWidget_2.setItem(0, 0, QTableWidgetItem(b1))
        self.form.tableWidget_2.setItem(0, 2, QTableWidgetItem(b2))
        self.form.tableWidget_2.setItem(0, 4, QTableWidgetItem(b3))
        self.form.tableWidget_2.setItem(0, 6, QTableWidgetItem(b4))
        l0+=1
        #self.graph_plotter(-int(b1),1)

        gain_save(data2=[b1,' ',b2,' ',b3,' ',b4,b5],)

        self.save_settings()
       
#testing
from window_about import Ui_about
class about_form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_about()
        self.form.setupUi(self)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    if intro_show:
            
        widget_intro = window_name_intro()
        widget_intro.show()

    else:
        widget1 = window_main()
        widget1.show()
    sys.exit(app.exec())