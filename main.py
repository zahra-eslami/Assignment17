from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math

class Calculator:
    def __init__(self, my_window):
        self.my_window = my_window
        self.showing_result = False
        self.operator = ''
        self.num1 = 0

    def connect_number_buttons(self):
        self.my_window.btn_num_0.clicked.connect(lambda: self.add_number('0'))
        self.my_window.btn_num_1.clicked.connect(lambda: self.add_number('1'))
        self.my_window.btn_num_2.clicked.connect(lambda: self.add_number('2'))
        self.my_window.btn_num_3.clicked.connect(lambda: self.add_number('3'))
        self.my_window.btn_num_4.clicked.connect(lambda:  self.add_number('4'))
        self.my_window.btn_num_5.clicked.connect(lambda:  self.add_number('5'))
        self.my_window.btn_num_6.clicked.connect(lambda:  self.add_number('6'))
        self.my_window.btn_num_7.clicked.connect(lambda:  self.add_number('7'))
        self.my_window.btn_num_8.clicked.connect(lambda:  self.add_number('8'))
        self.my_window.btn_num_9.clicked.connect(lambda:  self.add_number('9'))
        self.my_window.btn_dot.clicked.connect(lambda:  self.add_number('.'))


    def connect_operator_buttons(self):
        self.my_window.btn_sin.clicked.connect(lambda: self.trig_functions(self.my_window.btn_sin.text()))
        self.my_window.btn_cos.clicked.connect(lambda: self.trig_functions(self.my_window.btn_cos.text()))
        self.my_window.btn_tan.clicked.connect(lambda: self.trig_functions(self.my_window.btn_tan.text()))
        self.my_window.btn_cot.clicked.connect(lambda: self.trig_functions(self.my_window.btn_cot.text()))
        self.my_window.btn_log.clicked.connect(lambda: self.trig_functions(self.my_window.btn_log.text()))

        self.my_window.btn_ac.clicked.connect(self.ac)
        self.my_window.btn_ce.clicked.connect(self.ce)

        self.my_window.btn_div.clicked.connect(lambda: self.basic_operation('/'))
        self.my_window.btn_mul.clicked.connect(lambda: self.basic_operation('*'))
        self.my_window.btn_sub.clicked.connect(lambda: self.basic_operation('-'))
        self.my_window.btn_sum.clicked.connect(lambda: self.basic_operation('+'))

        self.my_window.btn_sqrt.clicked.connect(lambda: self.other_operation('sqrt'))
        self.my_window.btn_sqr.clicked.connect(lambda: self.other_operation('sqr'))
        self.my_window.btn_percent.clicked.connect(lambda: self.other_operation('%'))

        self.my_window.btn_plus_minues.clicked.connect(self.change_sign)
        self.my_window.btn_result.clicked.connect(self.equal)

    def add_number(self, number):
        if self.showing_result:
            self.ac() 
            self.showing_result = False 

        current_num = self.my_window.txtbox.text()

        if current_num == '0' and number.isdigit() and int(number) >= 0 and int(number) <= 9:
            current_num = ''

        if number == '.' and '.' in current_num:
            return

        new_num = current_num + number
        self.my_window.txtbox.setText(new_num)

    def ac(self):
        self.my_window.txtbox.setText('0')

    def ce(self):
        current_text = self.my_window.txtbox.text()
        if len(current_text) > 0:
            new_text = current_text[:-1]
            self.my_window.txtbox.setText(new_text)
        else:
            self.my_window.txtbox.setText('0')

    def basic_operation(self, opr):
        self.operator = opr
        self.num1 = float(self.my_window.txtbox.text())
        self.showing_result = True

    def other_operation(self, opr):
        self.operator = opr  
        self.num1 = float(self.my_window.txtbox.text())

    def trig_functions(self, btn_text):
        self.operator = btn_text
        self.num1 = float(self.my_window.txtbox.text())

    def equal(self):
        self.showing_result = True  

        if self.operator == '+':
            num2 = float(self.my_window.txtbox.text())
            result = self.num1 + num2

        elif self.operator == '-':
            num2 = float(self.my_window.txtbox.text())
            result = self.num1 - num2

        elif self.operator == '*':
            num2 = float(self.my_window.txtbox.text())
            result = self.num1 * num2

        elif self.operator == '/':
            num2 = float(self.my_window.txtbox.text())
            result = self.num1 / num2

        elif self.operator == 'sin':
            result = math.sin(self.num1)

        elif self.operator == 'cos':
            result = math.cos(self.num1)

        elif self.operator == 'tan':
            result = math.tan(self.num1)

        elif self.operator == 'cot':
            result = 1 / math.tan(self.num1)

        elif self.operator == 'log':
            result = math.log(self.num1)

        elif self.operator == 'sqrt':
            result = math.sqrt(self.num1)

        elif self.operator == 'sqr':
            result = self.num1 ** 2

        elif self.operator == '%':
            percent_value = float(self.my_window.txtbox.text())
            result = (percent_value / 100) * self.num1

        self.my_window.txtbox.setText(str(result))

    def change_sign(self):
        current_text = self.my_window.txtbox.text()
        if current_text:
            if current_text[0] == '-':
                new_text = current_text[1:]
            else:
                new_text = '-' + current_text
            self.my_window.txtbox.setText(new_text)


loader = QUiLoader()
my_app = QApplication([])

my_window = loader.load("Assignment17/main_window.ui")
my_window.show()
my_window.txtbox.setText('0')

calculator = Calculator(my_window)

calculator.connect_number_buttons()
calculator.connect_operator_buttons()

my_app.exec()
