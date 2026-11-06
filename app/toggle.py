from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint




class ToggleExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toggle Button Example")
        self.setFixedSize(200, 100)

        # Add the toggle button
        self.toggle = ToggleButton(self)
        self.toggle.move(70, 35)


if __name__ == "__main__":
    app = QApplication([])

    window = ToggleExample()
    window.show()

    app.exec()
