import sys
from PyQt6.QtWidgets import QApplication
from gui import RPNCalculator
from tests import test_logic

if __name__ == "__main__":
    test_logic()
    app = QApplication(sys.argv)
    window = RPNCalculator()
    window.show()
    sys.exit(app.exec())