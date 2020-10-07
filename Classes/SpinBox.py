from PyQt5 import QtWidgets


class SpinBox(QtWidgets.QSpinBox):
    def wheelEvent(self, event):
        event.ignore()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = SpinBox()
    w.show()
    sys.exit(app.exec_())
