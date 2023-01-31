import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader



operator=" "
statement=" "

def show():
        global statement
        window.lineEdit.setText(statement)

def zero():
        global statement
        statement +="0"
        show()
def one():
        global statement
        statement +="1"
        show()
def two():
        global statement
        statement +="2"
        show()
def three():
        global statement
        statement +="3"
        show()
def four():
        global statement
        statement +="4"
        show()
def five():
        global statement
        statement +="5"
        show()
def six():
        global statement
        statement +="6"
        show()
def seven():
        global statement
        statement +="7"
        show()
def eight():
        global statement
        statement +="8"
        show()
def nine():
        global statement
        statement +="9"
        show()



def sum():
        global operator
        operator="sum"
        calcute()
       
def sub():
        global operator
        operator="sub"
        calcute()

def mul():
        global operator
        operator="mul"
        calcute()

def div():
        global operator
        operator="div"
        calcute()

def sqrt():
        global operator
        operator="sqrt"
        calcute()

def percent():
      global operator
      operator="percent"
      calcute()  

def sin():
        global statement
        if statement != " " :
            firstnum = int(statement)
            show()
            statement = ""
            window.lineEdit.setText("")
            equal=math.sin(math.radians(firstnum))
            window.lineEdit.setText(str(equal))
            firstnum==""

def cos():
        global statement
        if statement != " " :
            firstnum = int(statement)
            if firstnum==90:
                window.lineEdit.setText("0")
            else:
                show()
                statement = ""
                window.lineEdit.setText("")
                equal=math.cos(firstnum)
                window.lineEdit.setText(str(equal))
                firstnum==""

def tan():
        global statement
        if statement != " " :
           firstnum = int(statement)
           if firstnum==90:
                window.lineEdit.setText("Undefined")
           elif firstnum==45:
                 window.lineEdit.setText("1")
           else:
                show()
                statement = ""
                window.lineEdit.setText("")
                equal=math.tan(firstnum)
                window.lineEdit.setText(str(equal))
                firstnum==""

def cot():
        global statement
        if statement != " " :
            firstnum = int(statement)
            if firstnum==90 or firstnum==0:
                window.lineEdit.setText("Undefined")
            elif firstnum==45:
                window.lineEdit.setText("1")
            else:
                show()
                statement = ""
                window.lineEdit.setText("")
                equal=1/math.tan(firstnum)
                window.lineEdit.setText(str(equal))
                firstnum==""


def sqrt():
       global statement
       global firstnum
       if statement != " " :
            firstnum = float(statement)
            if firstnum<=0:
                 window.lineEdit.setText("Enter a number greater than zero")
            show()
            statement = ""
            window.lineEdit.setText("")
            equal=math.sqrt(firstnum)
            window.lineEdit.setText(str(equal))
            firstnum==""

def log():
       global statement
       global firstnum
       if statement != " " :
            firstnum = float(statement)
            show()
            statement = ""
            window.lineEdit.setText("")
            equal=math.log10(firstnum)
            window.lineEdit.setText(str(equal))
            firstnum==""

def auditor():
        global statement
        global firstnum
        global ope
        global leftside
        global rightside
    
        if statement != " " :
            leftside = statement
            statement=""
            ope="."
            rightside=statement
            statement=leftside+ope+rightside
            show()
        


def changesign():
        global statement
        global firstnum
        global operator
        if statement != " " :
            firstnum = float(statement)
            statement= str(-1 * firstnum)
            show()
            
def clear():
        global statement
        window.lineEdit.setText("0")
        statement=""


def calcute():
        global statement
        global firstnum
        global operator
        if statement != " " :
            firstnum = float(statement)
            show()
            statement = ""
            window.lineEdit.setText("")
            
                    
def result():
        secoundnum=float(statement)
        if operator=="sum":
                equal=firstnum + secoundnum
                window.lineEdit.setText(str(equal))
                firstnum==""
                secoundnum==""
        elif operator=="sub":
                equal=firstnum - secoundnum
                window.lineEdit.setText(str(equal))
                firstnum==""
                secoundnum==""
        elif operator=="mul":
                equal=firstnum * secoundnum
                window.lineEdit.setText(str(equal))
                firstnum==""
                secoundnum==""
        elif operator=="div":
                equal=firstnum / secoundnum
                window.lineEdit.setText(str(equal))
                firstnum==""
                secoundnum==""
        elif operator=="percent":
                equal=(firstnum * secoundnum) / 100
                window.lineEdit.setText(str(equal))
                firstnum==""
                secoundnum==""


    
app=QApplication([])
loader=QUiLoader()
window=loader.load("my-project/session17/calculator.ui")
window.setWindowTitle("My Calculator")
window.setGeometry(900,200,250,300)

    
window.show()

window.btn0.clicked.connect(zero)
window.btn1.clicked.connect(one)
window.btn2.clicked.connect(two)
window.btn3.clicked.connect(three)
window.btn4.clicked.connect(four)
window.btn5.clicked.connect(five)
window.btn6.clicked.connect(six)
window.btn7.clicked.connect(seven)
window.btn8.clicked.connect(eight)
window.btn9.clicked.connect(nine)
window.btnsum.clicked.connect(sum)
window.btnsub.clicked.connect(sub)
window.btnmul.clicked.connect(mul)
window.btndiv.clicked.connect(div)
window.btnsqrt.clicked.connect(sqrt)
window.btnsin.clicked.connect(sin)
window.btncos.clicked.connect(cos)
window.btntan.clicked.connect(tan)
window.btncot.clicked.connect(cot)
window.btnsqrt.clicked.connect(sqrt)
window.btnac.clicked.connect(clear)
window.btn.clicked.connect(auditor)
window.btn100.clicked.connect(percent)
window.btnlog.clicked.connect(log)
window.btnsym.clicked.connect(changesign)











window.result.clicked.connect(result)
   
app.exec()