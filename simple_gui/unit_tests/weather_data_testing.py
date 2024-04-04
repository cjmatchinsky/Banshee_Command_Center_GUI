import sys
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QComboBox,QLineEdit
)
from PyQt5.uic import loadUi

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("testing.ui", self)  # Load the UI file

        self.fruits = ["Apple", "Banana", "Orange", "Grapes"]

        self.combo_box = self.findChild(QComboBox, "comboBox")  # Find the combo box
        self.combo_box.setEditable(True)
        self.combo_box.addItems(self.fruits)
        #self.combo_box.lineEdit().returnPressed.connect(self.add_text_to_combobox)
        self.combo_box.currentIndexChanged.connect(self.update_textbox)

        self.text_box = self.findChild(QLineEdit, "textBox")  # Find the text box

        self.clear_button = self.findChild(QPushButton, "clearButton")  # Find the clear button
        self.clear_button.clicked.connect(self.clear_text)

    def add_text_to_combobox(self):
        new_text = self.combo_box.currentText()
        if new_text not in self.fruits:  # Avoid duplicates
            self.fruits.append(new_text)
            self.combo_box.addItem(new_text)

    def update_textbox(self, index):
        text = self.combo_box.currentText()
        self.text_box.setText(text)

    def clear_text(self):
        self.combo_box.clearEditText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
