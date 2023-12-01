from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sys
from math import sqrt
import re

class StdCalculator(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standard Calculator")
        self.setGeometry(500, 200, 430, 320)
        self.setFixedSize(430, 320)
        self.UIComponents()
    
    def UIComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 420, 60)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel {border : 1px solid gray; background : white; }")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label.setFont(QFont('Arial', 20))

        to_clear = QPushButton("Clear", self)
        to_clear.setGeometry(5, 80, 125, 40)
        to_clear.clicked.connect(self.act_clear)
 
        to_del = QPushButton("Del", self)
        to_del.setGeometry(135, 80, 120, 40)
        to_del.clicked.connect(self.act_del)

        open_brc = QPushButton("(", self)
        open_brc.setGeometry(260, 80, 80, 40)
        open_brc.clicked.connect(self.open_brc)

        close_brc = QPushButton(")", self)
        close_brc.setGeometry(345, 80, 80, 40)
        close_brc.clicked.connect(self.close_brc)
 
        number7 = QPushButton("7", self)
        number7.setGeometry(5, 130, 80, 40)
        number7.clicked.connect(self.num7)
 
        number8 = QPushButton("8", self)
        number8.setGeometry(90, 130, 80, 40)
        number8.clicked.connect(self.num8)
 
        number9 = QPushButton("9", self)
        number9.setGeometry(175, 130, 80, 40)
        number9.clicked.connect(self.num9)
 
        number4 = QPushButton("4", self)
        number4.setGeometry(5, 175, 80, 40)
        number4.clicked.connect(self.num4)
 
        number5 = QPushButton("5", self)
        number5.setGeometry(90, 175, 80, 40)
        number5.clicked.connect(self.num5)
 
        number6 = QPushButton("6", self)
        number6.setGeometry(175, 175, 80, 40)
        number6.clicked.connect(self.num6)
 
        number1 = QPushButton("1", self)
        number1.setGeometry(5, 220, 80, 40)
        number1.clicked.connect(self.num1)

        number2 = QPushButton("2", self)
        number2.setGeometry(90, 220, 80, 40)
        number2.clicked.connect(self.num2)

        number3 = QPushButton("3", self)
        number3.setGeometry(175, 220, 80, 40)
        number3.clicked.connect(self.num3)
 
        number0 = QPushButton("0", self)
        number0.setGeometry(5, 265, 80, 40)
        number0.clicked.connect(self.num0)

        add_point = QPushButton(".", self)
        add_point.setGeometry(90, 265, 80, 40)
        add_point.clicked.connect(self.act_point)

        op_mod = QPushButton("%", self)
        op_mod.setGeometry(175, 265, 80, 40)
        op_mod.clicked.connect(self.act_mod)
 
        op_plus = QPushButton("+", self)
        op_plus.setGeometry(260, 130, 80, 40)
        op_plus.clicked.connect(self.act_plus)

        op_minus = QPushButton("-", self)
        op_minus.setGeometry(260, 175, 80, 40)
        op_minus.clicked.connect(self.act_minus)
 
        op_mul = QPushButton("*", self)
        op_mul.setGeometry(260, 220, 80, 40)
        op_mul.clicked.connect(self.act_mul)

        op_div = QPushButton("÷", self)
        op_div.setGeometry(260, 265, 80, 40)
        op_div.clicked.connect(self.act_div)

        sqrt = QPushButton("\u221A", self)
        sqrt.setGeometry(345, 130, 80, 40)
        sqrt.clicked.connect(self.act_sqrt)

        power = QPushButton("x\u207F", self)
        power.setGeometry(345, 175, 80, 40)
        power.clicked.connect(self.act_power)

        op_equal = QPushButton("=", self)
        op_equal.setGeometry(345, 220, 80, 85)
        op_equal.clicked.connect(self.act_equal)

        color1 = QGraphicsColorizeEffect()
        color1.setColor(QColor('green'))
        op_equal.setGraphicsEffect(color1)

    
    def act_clear(self):
        self.label.setText("")
 
    def act_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text)-1])
    

    def act_equal(self):
        expression = self.label.text()
        if "÷" in expression:
            expression = expression.replace("÷", "/")
        if "√" in expression:
            expression = re.sub(r'√(\d+\.\d+|\d+)', r'sqrt(\1)', expression)
        try:
            result = eval(expression)
            self.label.setText(str(result))
        except Exception:
            self.label.setText("Invalid Input(s)!")
    
    def act_plus(self):
        text = self.label.text()
        self.label.setText(text + "+")
 
    def act_minus(self):
        text = self.label.text()
        self.label.setText(text + "-")

    def act_mul(self):
        text = self.label.text()
        self.label.setText(text + "*")
 
    def act_div(self):
        text = self.label.text()
        self.label.setText(text + "÷")
    
    def act_sqrt(self):
        text = self.label.text()
        self.label.setText(text + "√")
    
    def act_power(self):
        text = self.label.text()
        self.label.setText(text + "**")
    
    def act_mod(self):
        text = self.label.text()
        self.label.setText(text + "%")
 
    def act_point(self):
        text = self.label.text()
        self.label.setText(text + ".")
 
    def open_brc(self):
        text = self.label.text()
        self.label.setText(text + "(")
    
    def close_brc(self):
        text = self.label.text()
        self.label.setText(text + ")")

    def num0(self):
        text = self.label.text()
        self.label.setText(text + "0")
 
    def num1(self):
        text = self.label.text()
        self.label.setText(text + "1")
 
    def num2(self):
        text = self.label.text()
        self.label.setText(text + "2")
 
    def num3(self):
        text = self.label.text()
        self.label.setText(text + "3")
 
    def num4(self):
        text = self.label.text()
        self.label.setText(text + "4")
 
    def num5(self):
        text = self.label.text()
        self.label.setText(text + "5")
 
    def num6(self):
        text = self.label.text()
        self.label.setText(text + "6")
 
    def num7(self):
        text = self.label.text()
        self.label.setText(text + "7")
 
    def num8(self):
        text = self.label.text()
        self.label.setText(text + "8")
 
    def num9(self):
        text = self.label.text()
        self.label.setText(text + "9")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = StdCalculator()
    window.show()
    sys.exit(App.exec())