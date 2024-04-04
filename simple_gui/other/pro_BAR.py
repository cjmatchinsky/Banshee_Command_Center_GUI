import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal

# Custom Thread class to handle the progress bar update
class ProgressBarThread(QThread):
    update_signal = pyqtSignal(int)  # Signal to update the progress bar

    def __init__(self, progress_bar):
        super(ProgressBarThread, self).__init__()
        self.progress_bar = progress_bar

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # Simulate some work
            self.update_signal.emit(i)  # Emit the progress value

# Custom progress bar class with a thread
class CustomProgressBar(QWidget):
    def __init__(self, parent=None):
        super(CustomProgressBar, self).__init__(parent)

        # Create progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        # Create thread and connect signal to update progress bar
        self.thread = ProgressBarThread(self.progress_bar)
        self.thread.update_signal.connect(self.update_progress)

        # Create start button
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_thread)

        # Layout setup
        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

    def start_thread(self):
        self.thread.start()  # Start the thread when the button is clicked

    def update_progress(self, value):
        self.progress_bar.setValue(value)  # Update the progress bar

# Main application window
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create three custom progress bar instances
        self.progress_bar1 = CustomProgressBar(self)
        self.progress_bar2 = CustomProgressBar(self)
        self.progress_bar3 = CustomProgressBar(self)

        # Layout setup
        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar1)
        layout.addWidget(self.progress_bar2)
        layout.addWidget(self.progress_bar3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
