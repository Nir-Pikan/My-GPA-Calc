from UI.ui import Ui_MainWindow
from Classes.Calculator import Calculator
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


def main():
    # Create Calculator brain
    calculator = Calculator()

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window, calculator)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
