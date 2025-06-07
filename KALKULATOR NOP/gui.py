from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect
from logic import infix_to_rpn, evaluate_rpn
from keyboard import VirtualKeyboard

class RPNCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator ONP (PyQt6)")
        self.apply_dark_theme()

        self.input_label = QLabel("Wyrażenie:")
        self.input_field = QLineEdit()
        self.rpn_result = QLabel("ONP: ")
        self.value_result = QLabel("Wynik: ")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_field)

        keyboard = VirtualKeyboard(self.input_field, self.calculate, self.animate_button)
        main_layout.addLayout(keyboard.create())

        main_layout.addWidget(self.rpn_result)
        main_layout.addWidget(self.value_result)
        self.setLayout(main_layout)

    def calculate(self):
        expr = self.input_field.text()
        try:
            rpn = infix_to_rpn(expr)
            result = evaluate_rpn(rpn)
            self.rpn_result.setText(f"ONP: {' '.join(rpn)}")
            self.value_result.setText(f"Wynik: {result}")
        except Exception as e:
            QMessageBox.critical(self, "Błąd", str(e))

    def animate_button(self, btn):
        original = btn.geometry()
        shrink = QRect(original.x() + 2, original.y() + 2, original.width() - 4, original.height() - 4)

        anim = QPropertyAnimation(btn, b"geometry")
        anim.setDuration(100)
        anim.setStartValue(original)
        anim.setEndValue(shrink)
        anim.setEasingCurve(QEasingCurve.Type.InOutQuad)

        anim_back = QPropertyAnimation(btn, b"geometry")
        anim_back.setDuration(100)
        anim_back.setStartValue(shrink)
        anim_back.setEndValue(original)
        anim_back.setEasingCurve(QEasingCurve.Type.InOutQuad)

        anim.finished.connect(anim_back.start)
        anim.start()

    def apply_dark_theme(self):
        dark_palette = self.palette()
        dark_palette.setColor(QPalette.ColorRole.Window, QColor("#121212"))
        dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("#ffffff"))
        dark_palette.setColor(QPalette.ColorRole.Base, QColor("#1e1e1e"))
        dark_palette.setColor(QPalette.ColorRole.Text, QColor("#ffffff"))
        dark_palette.setColor(QPalette.ColorRole.Button, QColor("#333333"))
        dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
        dark_palette.setColor(QPalette.ColorRole.Highlight, QColor("#3d6afe"))
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#000000"))
        self.setPalette(dark_palette)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #ffffff;
                font-size: 16px;
            }
            QPushButton {
                background-color: #333333;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #444444;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #555555;
                padding: 4px;
            }
        """)