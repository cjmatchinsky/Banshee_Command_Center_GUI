import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class CounterThread(QThread):
    update_signal = pyqtSignal(int)

    def run(self):
        for i in range(1, 11):
            self.update_signal.emit(i)
            self.msleep(500)  # Simulate some work
        self.finished.emit()

class TimerThread(QThread):
    update_signal = pyqtSignal(int)

    def run(self):
        for i in range(1, 6):
            self.update_signal.emit(i)
            self.msleep(1000)  # Simulate some work
        self.finished.emit()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QThread Example')
        self.setGeometry(100, 100, 300, 200)

        self.counter_label = QLabel('Counter: 0', self)
        self.timer_label = QLabel('Timer: 0', self)

        self.start_counter_button = QPushButton('Start Counter', self)
        self.start_timer_button = QPushButton('Start Timer', self)

        self.start_counter_button.clicked.connect(self.start_counter)
        self.start_timer_button.clicked.connect(self.start_timer)

        layout = QVBoxLayout(self)
        layout.addWidget(self.counter_label)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_counter_button)
        layout.addWidget(self.start_timer_button)

        self.counter_thread = CounterThread()
        self.timer_thread = TimerThread()

        self.counter_thread.update_signal.connect(self.update_counter_label)
        self.timer_thread.update_signal.connect(self.update_timer_label)

        self.counter_thread.finished.connect(self.thread_finished)
        self.timer_thread.finished.connect(self.thread_finished)

    def start_counter(self):
        self.start_counter_button.setEnabled(False)
        self.counter_thread.start()

    def start_timer(self):
        self.start_timer_button.setEnabled(False)
        self.timer_thread.start()

    def update_counter_label(self, count):
        self.counter_label.setText(f'Counter: {count}')

    def update_timer_label(self, count):
        self.timer_label.setText(f'Timer: {count}')

    def thread_finished(self):
        self.start_counter_button.setEnabled(True)
        self.start_timer_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
