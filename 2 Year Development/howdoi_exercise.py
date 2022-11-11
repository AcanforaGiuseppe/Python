from PySide2.QTWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QWidget, QPushButton, QTextEdit
from PySide2.QtCore import Qt, Signal
import sys
from howdoi import howdoi


class MainWindow(QMainWindow):

    myClicked = Signal(QWidget)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget App")
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.q_label = QLabel()
        self.q_label.setText("Enter your question:")
        self.q_label.setAlignment(Qt.AlignTop)
        self.q_lineEdit = QLineEdit()
        self.q_lineEdit.setAlignment(Qt.AlignTop)
        self.h_layout.addWidget(self.q_label)
        self.h_layout.addWidget(self.q_lineEdit)
        self.v_layout.addLayout(self.h_layout)
        a_textEdit = QTextEdit()
        a_textEdit.setMinimumSize(600, 600)
        a_textEdit.setPlaceholderText("Waiting fot a question...")
        a_textEdit.setAlignment(Qt.AlignTop)

        ask_button = QPushButton("Ask")
        ask_button.clicked.connect(lambda: self.myClicked.emit(a_textEdit))
        self.myClicked.connect(self.mouse_clicked)
        self.v_layout.addWidget(a_textEdit)
        self.v_layout.addWidget(ask_button)

        widget = QWidget()
        widget.setLayout(self.v_layout)
        self.setCentralWidget(widget)

        def mouse_clicked(self, text_edit):
            question = self.q_lineEdit.text()
            answer = howdoi.howdoi(question)
            text_edit.setText(answer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit((app.exec_()))
