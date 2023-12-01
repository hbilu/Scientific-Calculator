import sys
from functools import partial
from math import sqrt, pi, e, log, log10, sin, asin, radians, cos, acos, tan, atan, degrees, gamma
import re
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGraphicsColorizeEffect, QRadioButton
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class ScCalculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setFixedSize(750, 260)
        self.Layout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.Layout)
        self.setCentralWidget(centralWidget)
        self.createDisplay()
        self.createButtons()
        self.createActions()

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.Layout.addWidget(self.display)

    def createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [["Rad", "Deg", "+/-", "C", "Del", "(", ")", "+"],
                    ["sin", "sin\u00AF\u00B9", "π", "ln", "7", "8", "9", "-"],
                    ["cos", "cos\u00AF\u00B9", "e", "log", "4", "5", "6", "x"],
                    ["tan", "tan\u00AF\u00B9", "1/x",  "√", "1", "2", "3", "÷"],
                    ["x!", "x\u207F", "\u02B8√x", "0", "."]]
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(80, 40)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        eq_button = QPushButton("=")
        eq_button.setFixedSize(265, 40)
        buttonsLayout.addWidget(eq_button, 4, 5, 1, 3)
        color1 = QGraphicsColorizeEffect()
        color1.setColor(QColor('green'))
        eq_button.setGraphicsEffect(color1)
        eq_button.clicked.connect(self.act_equal)
        self.display.returnPressed.connect(self.act_equal)

        self.Layout.addLayout(buttonsLayout)

    def createActions(self):
        for keySymbol, button in self.buttonMap.items():
            if keySymbol not in {"=", "C", "Del", "x\u207F", "π", "x", "e", "+/-", "1/x", "\u02B8√x", "x!"}:
                button.clicked.connect(partial(self.bClicked, keySymbol))
        self.buttonMap["\u02B8√x"].clicked.connect(partial(self.bClicked, "√"))
        self.buttonMap["x\u207F"].clicked.connect(partial(self.bClicked, "**"))
        self.buttonMap["π"].clicked.connect(partial(self.bClicked, str(pi)))
        self.buttonMap["e"].clicked.connect(partial(self.bClicked, str(e)))
        self.buttonMap["x"].clicked.connect(partial(self.bClicked, "*"))
        self.buttonMap["x!"].clicked.connect(partial(self.bClicked, "!"))
        self.buttonMap["C"].clicked.connect(self.act_clear)
        self.buttonMap["Del"].clicked.connect(self.act_del)
        self.buttonMap["+/-"].clicked.connect(self.pos_neg)
        self.buttonMap["1/x"].clicked.connect(self.onedivx)

    def bClicked(self, symbol):
        expression = self.display.text() + symbol
        self.display.setFocus()
        self.display.setText(expression)
    
    def act_equal(self):
        expression = self.display.text()
        if "!" in expression:
            expression = re.sub(r'(\d+\.\d+|\d+)!', r'gamma(\1+1)', expression)
        if "÷" in expression:
            expression = expression.replace("÷", "/")
        if "√" in expression:
            expression = re.sub(r'(\d+)√(\d+\.\d+|\d+)', r'(\2)**(1/\1)', expression)
            expression = re.sub(r'√(\d+\.\d+|\d+)', r'sqrt(\1)', expression)
        if "ln" in expression:
            expression = re.sub(r'ln(\d+\.\d+|\d+)', r'log(\1, e)', expression)
            print(expression)
        if "log" in expression:
            expression = re.sub(r'log(\d+\.\d+|\d+)', r'log10(\1)', expression)
            print(expression)
        if "sin" in expression:
            if "sin¯¹" in expression:
                expression = re.sub(r'sin¯¹(\d+\.\d+|\d+)Deg', r'degrees(asin(\1))', expression)
                expression = re.sub(r'sin¯¹(\d+\.\d+|\d+)Rad', r'asin(\1)', expression)
            expression = re.sub(r'sin(\d+\.\d+|\d+)Deg', r'sin(radians(\1))', expression)
            expression = re.sub(r'sin(\d+\.\d+|\d+)Rad', r'sin(\1)', expression)
        if "cos" in expression:
            if "cos¯¹" in expression:
                expression = re.sub(r'cos¯¹(\d+\.\d+|\d+)Deg', r'degrees(acos(\1))', expression)
                expression = re.sub(r'cos¯¹(\d+\.\d+|\d+)Rad', r'acos(\1)', expression)
            expression = re.sub(r'cos(\d+\.\d+|\d+)Deg', r'cos(radians(\1))', expression)
            expression = re.sub(r'cos(\d+\.\d+|\d+)Rad', r'cos(\1)', expression)
        if "tan" in expression:
            if "tan¯¹" in expression:
                expression = re.sub(r'tan¯¹(\d+\.\d+|\d+)Deg', r'degrees(atan(\1))', expression)
                expression = re.sub(r'tan¯¹(\d+\.\d+|\d+)Rad', r'atan(\1)', expression)
            expression = re.sub(r'tan(\d+\.\d+|\d+)Deg', r'tan(radians(\1))', expression)
            expression = re.sub(r'tan(\d+\.\d+|\d+)Rad', r'tan(\1)', expression)
        try:
            result = eval(expression)
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Invalid Input(s)!")
    
    def pos_neg(self):
        text = self.display.text()
        if r'-(\d+\.\d+|\d+)$' in text:
            text = re.sub(r'-(\d+\.\d+|\d+)$', r'(\1)', text)
        else: 
            text = re.sub(r'(\d+\.\d+|\d+)$', r'-(\1)', text)
        self.display.setText(text)

    def onedivx(self):
        text = self.display.text()
        text = re.sub(r'(\d+\.\d+|\d+)$', r'1/(\1)', text)
        self.display.setText(text)

    def act_clear(self):
        self.display.setText("")
 
    def act_del(self):
        text = self.display.text()
        self.display.setText(text[:len(text)-1])

if __name__ == "__main__":
    app = QApplication([])
    window = ScCalculator()
    window.show()
    sys.exit(app.exec())