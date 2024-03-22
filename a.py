import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

# بارگذاری UI و اجرای برنامه

loader = QUiLoader()
my_app = QApplication([])

my_window = loader.load("Assignment17/main_window.ui")
print(type(my_window))

def clear():
    my_window.txtbox.setText("")

def clear_entry():
    txt = my_window.txtbox.text()
    my_window.txtbox.setText(txt[:-1])

def result():
    expression = my_window.txtbox.text()
    try:
        result = eval(expression)
        my_window.txtbox.setText(str(result))
    except Exception as e:
        print(e)
        my_window.txtbox.setText("Error")

def square_root():
    value = float(my_window.txtbox.text())
    result = math.sqrt(value)
    my_window.txtbox.setText(str(result))

def square():
    value = float(my_window.txtbox.text())
    result = value ** 2
    my_window.txtbox.setText(str(result))

my_window.btn_ac.clicked.connect(clear)
my_window.btn_ce.clicked.connect(clear_entry)


my_window.show()
my_app.exec()
