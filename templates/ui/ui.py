import os
import sys

import asyncio
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel

class UiApp(QMainWindow):

    future = None

    def __init__(self): 
        super().__init__()

        self.setWindowTitle("UiApp")
        self.define_window_size()
        self.create_input_label()
        self.create_input_field()
        self.create_increment_button()
        self.create_decrement_button()
        self.create_result_label()
        self.create_layout()
        self.create_widgets()
        self.create_signals()

    def define_window_size(self):
        self.setGeometry(0, 0, 500, 300)

    def create_input_label(self):
        self.inputFieldLabel = QLabel(self)
        self.inputFieldLabel.setText('Value:')

    def create_input_field(self):
        self.inputField = QLineEdit(self)

    def create_increment_button(self):
        self.incrementBtn = QPushButton("Increment", self)
        self.incrementBtn.setCheckable(True)
    
    def create_decrement_button(self):
        self.decrementBtn = QPushButton("Decrement", self)
        self.decrementBtn.setCheckable(True)

    def create_result_label(self):
        self.resultLabel = QLabel("Result", self)
        self.resultLabel.setAlignment(Qt.AlignCenter)

    def create_layout(self):
        self.hlayout1 = QHBoxLayout()
        self.hlayout1.addWidget(self.inputFieldLabel)
        self.hlayout1.addWidget(self.inputField)
        self.hlayout1.addWidget(self.incrementBtn)
        self.hlayout1.addWidget(self.decrementBtn)

        self.hlayout2 = QHBoxLayout()
        self.hlayout2.addWidget(self.resultLabel)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.hlayout1)
        self.layout.addLayout(self.hlayout2)

    def create_widgets(self):
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.show()

    def incrementBtn_pressed(self):
        resultValue = "Incremented value" #TODO: fetch value from API
        self.resultLabel.setText(resultValue)

    def decrementBtn_pressed(self):
        resultValue = "Decremented value" #TODO: fetch value from API
        self.resultLabel.setText(resultValue)

    def create_signals(self):
        self.incrementBtn.clicked.connect(self.incrementBtn_pressed)
        self.decrementBtn.clicked.connect(self.decrementBtn_pressed)


def closeApplication(self):
        sys.exit()

def main():
    App = QApplication(sys.argv)
    ui = UiApp()
    ui.show()
    exit_code = App.exec()
    sys.exit(exit_code)

if __name__ == '__main__': 
    main()