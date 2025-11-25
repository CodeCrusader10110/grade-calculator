"""
TODO docstring
"""
import sys
from PyQt6.QtWidgets import QApplication
from logic import GuiLogic

def main():
    """
    TODO docstring
    """
    app = QApplication(sys.argv)
    window = GuiLogic()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()