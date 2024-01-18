import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sqrt, factorial

num = 0.0
newNum = 0.0
sumIt = 0.0
sumAll = 0.0
operator = ""

opVar = False

class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()
    
    def initUI(self):
        self.resize(640, 480)
        self.setWindowTitle('SCV Calculator')
        self.line = QLineEdit(self)
        self.line.move(5, 5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMaxLength(30)

        font = QFont("Arial")
        font.setPointSize(16)
        self.line.setFont(font)
        self.line.resize(580, 50)
        self.line.move(30, 30)

        # Class for buttons to calculator
        zero = QPushButton("0", self)
        zero.setFont(font)
        zero.move(40, 360)
        zero.resize(240, 75)

        plusminus = QPushButton("±", self)
        plusminus.setFont(font)
        plusminus.move(280, 360)
        plusminus.resize(80, 75)
        plusminus.clicked.connect(self.PlusMinus)

        point = QPushButton(".", self)
        point.setFont(font)
        point.move(360, 360)
        point.resize(80, 75)
        point.clicked.connect(self.Point)

        divide = QPushButton("÷", self)
        divide.setFont(font)
        divide.move(440, 280)
        divide.resize(80, 80)

        equal = QPushButton("=", self)
        equal.setFont(font)
        equal.move(440, 360)
        equal.resize(160, 75)
        equal.clicked.connect(self.Equal)

        one = QPushButton("1", self)
        one.setFont(font)
        one.move(40, 280)
        one.resize(80, 80)

        two = QPushButton("2", self)
        two.setFont(font)
        two.move(120, 280)
        two.resize(80, 80)

        three = QPushButton("3", self)
        three.setFont(font)
        three.move(200, 280)
        three.resize(80, 80)

        four = QPushButton("4", self)
        four.setFont(font)
        four.move(40, 200)
        four.resize(80, 80)

        five = QPushButton("5", self)
        five.setFont(font)
        five.move(120, 200)
        five.resize(80, 80)

        six = QPushButton("6", self)
        six.setFont(font)
        six.move(200, 200)
        six.resize(80, 80)

        seven = QPushButton("7", self)
        seven.setFont(font)
        seven.move(40, 120)
        seven.resize(80, 80)

        eight = QPushButton("8", self)
        eight.setFont(font)
        eight.move(120, 120)
        eight.resize(80, 80)

        nine = QPushButton("9", self)
        nine.setFont(font)
        nine.move(200, 120)
        nine.resize(80, 80)

        multi = QPushButton("×", self)
        multi.setFont(font)
        multi.move(520, 280)
        multi.resize(80, 80)

        minus = QPushButton("-", self)
        minus.setFont(font)
        minus.move(520, 200)
        minus.resize(80, 80)

        plus = QPushButton("+", self)
        plus.setFont(font)
        plus.move(440, 200)
        plus.resize(80, 80)

        factorial = QPushButton("!", self)
        factorial.setFont(font)
        factorial.move(280, 280)
        factorial.resize(80, 80)
        factorial.clicked.connect(self.Factorial)

        fraction = QPushButton("1⁄𝑥", self)
        fraction.setFont(font)
        fraction.move(360, 280)
        fraction.resize(80, 80)
        fraction.clicked.connect(self.Fraction)

        expo = QPushButton("x²", self)
        expo.setFont(font)
        expo.move(280, 200)
        expo.resize(80, 80)
        expo.clicked.connect(self.Expo)

        quad = QPushButton("x³", self)
        quad.setFont(font)
        quad.move(280, 120)
        quad.resize(80, 80)
        quad.clicked.connect(self.Quad)

        sqroot = QPushButton("√x", self)
        sqroot.setFont(font)
        sqroot.move(360, 200)
        sqroot.resize(80, 80)
        sqroot.clicked.connect(self.Sqroot)

        cbroot = QPushButton("∛x", self)
        cbroot.setFont(font)
        cbroot.move(360, 120)
        cbroot.resize(80, 80)
        cbroot.clicked.connect(self.Cbroot)

        delete = QPushButton("DEL", self)
        delete.setFont(font)
        delete.move(520, 120)
        delete.resize(80, 80)
        delete.clicked.connect(self.Delete)

        clear = QPushButton("C", self)
        clear.setFont(font)
        clear.move(440, 120)
        clear.resize(80, 80)
        clear.clicked.connect(self.Clear)

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]
        operators = [plus, minus, multi, divide, equal]
        tific = [expo, quad, sqroot, cbroot, factorial, fraction]
        others = [plusminus, point, clear, delete]

        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Num)

        for i in operators:
            i.setStyleSheet("color:red;")
            i.clicked.connect(self.operator)

        for i in tific:
            i.setStyleSheet("color:green;")
        
        for i in others:
            i.setStyleSheet("color:purple;")

    def Num(self):
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(setNum)
            opVar = False
            
    def operator(self):
        global sumIt
        global num
        global opVar
        global operator

        sumIt += 0

        if sumIt > 1:
            self.Equal()

        num = self.line.text()
        sender = self.sender()
        operator = sender.text()

        opVar = True
            
    def Point(self):
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
            
    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar

        newNum = self.line.text()

        if operator == "+":
            sumAll = float(num) + float(newNum)

        elif operator == "-":
            sumAll = float(num) - float(newNum)

        elif operator == "×":
            sumAll = float(num) * float(newNum)

        elif operator == "÷":
            sumAll = float(num) / float(newNum)

        self.line.setText(str(sumAll))
        opVar = True

    def Expo(self):
        global num

        num = float(self.line.text())
        num = num ** 2
        self.line.setText(str(num))

    def Quad(self):
        global num

        num = float(self.line.text())
        num = num ** 3
        self.line.setText(str(num))

    def Sqroot(self):
        global num

        num = float(self.line.text())
        num = sqrt(num)
        self.line.setText(str(num))

    def Cbroot(self):
        global num

        num = float(self.line.text())
        num = num ** (1 / 3)
        self.line.setText(str(num))

    def PlusMinus(self):
        global num

        num = float(self.line.text())
        num = -num
        self.line.setText(str(num))

    def Delete(self):
        global num

        self.line.backspace()

    def Clear(self):
        global num
        global newNum
        global sumAll
        global operator

        self.line.clear()

        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""

    def Fraction(self):
        global num

        num = float(self.line.text())
        num = 1 / num
        self.line.setText(str(num))
    
    def Factorial(self):
        global num

        num = int(self.line.text())
        num = factorial(num)
        self.line.setText(str(num))
        
if __name__ == "__main__":
    widget = QApplication(sys.argv)

    form = Calc()
    form.show()

    widget.exec_()