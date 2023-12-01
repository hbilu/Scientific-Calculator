import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow
from StdCal import StdCalculator
from ScCal import ScCalculator

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(500, 200, 200, 150)
        self.setFixedSize(200, 150)
        self.UIComponents()

    def UIComponents(self):

        std_cal = QPushButton("Standard Calculator", self)
        std_cal.setGeometry(10, 5, 180, 70)
        std_cal.clicked.connect(self.std_Cal)

        sc_cal = QPushButton("Scientific Calculator", self)
        sc_cal.setGeometry(10,75, 180, 70)
        sc_cal.clicked.connect(self.sc_Cal)

    def std_Cal(self):
        self.new_window = StdCalculator()
        self.new_window.show()
    
    def sc_Cal(self):
        self.new_window = ScCalculator()
        self.new_window.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(App.exec())