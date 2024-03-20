from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

import os

current_directory = os.path.dirname(os.path.abspath(__file__))

my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load(current_directory +"/main_window.ui")


my_window.show()

my_app.exec()




