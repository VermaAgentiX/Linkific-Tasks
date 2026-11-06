import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import pyqtgraph as pg

class BarPlotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("Bar Plot with PyQtGraph and PySide6")
        self.setGeometry(100, 100, 800, 600)
        
        # Set up the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create a PyQtGraph plot widget
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        
        # Create buttons
        self.button_red = QPushButton("Plot Red Bar")
        self.button_blue = QPushButton("Plot Blue Bar")
        layout.addWidget(self.button_red)
        layout.addWidget(self.button_blue)
        
        # Connect buttons to methods
        self.button_red.clicked.connect(self.plot_red_bar)
        self.button_blue.clicked.connect(self.plot_blue_bar)
        
        # Initialize the plot data
        self.bars = []
        self.index = 0

        self.k = 0
    
    def plot_red_bar(self):
        self.k +=1
        self.plot_bar(color='g')
    def plot_blue_bar(self):
        self.k -=1
        self.plot_bar(color='r')
    def plot_bar(self, color):
        x = [self.index]  # X position for the bar
        height = [self.k]  # Height of the bar
        
        # Plotting the bar
        bar = pg.BarGraphItem(x=x, height=height, width=0.6, brush=color)
        self.plot_widget.addItem(bar)
        self.bars.append(bar)
        
        
        # Update the index for the next bar
        self.index += 1

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarPlotApp()
    window.show()
    sys.exit(app.exec())
