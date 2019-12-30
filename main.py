import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.control_panel import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_1.clicked.connect(self.label_1_clicked)
        self.label_1.released.connect(self.label_1_released)
        self.label_1.moved.connect(self.label_1_moved)

        self.label_2.clicked.connect(self.label_2_clicked)
        self.label_2.released.connect(self.label_2_released)
        self.label_2.moved.connect(self.label_2_moved)

        self.label_3.clicked.connect(self.label_3_clicked)
        self.label_3.released.connect(self.label_3_released)
        self.label_3.moved.connect(self.label_3_moved)

        self.label_3.clicked.connect(self.label_3_clicked)
        self.label_3.released.connect(self.label_3_released)
        self.label_3.moved.connect(self.label_3_moved)

        self.label_4.clicked.connect(self.label_4_clicked)
        self.label_4.released.connect(self.label_4_released)
        self.label_4.moved.connect(self.label_4_moved)

        self.label_5.clicked.connect(self.label_5_clicked)
        self.label_5.released.connect(self.label_5_released)
        self.label_5.moved.connect(self.label_5_moved)

        self.label_6.clicked.connect(self.label_6_clicked)
        self.label_6.released.connect(self.label_6_released)
        self.label_6.moved.connect(self.label_6_moved)

        self.label_7.clicked.connect(self.label_7_clicked)
        self.label_7.released.connect(self.label_7_released)
        self.label_7.moved.connect(self.label_7_moved)

        self.label_8.clicked.connect(self.label_8_clicked)
        self.label_8.released.connect(self.label_8_released)
        self.label_8.moved.connect(self.label_8_moved)

    # ------------ label 1 -------------
    @pyqtSlot(bool)
    def label_1_clicked(self, trigger):
        pass

    @pyqtSlot(bool)
    def label_1_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_1_moved(self, position):
        width = self.label_1.size().width()
        height = self.label_1.size().height()
        
        print(position)
        print(width, height)

    # ------------ label 2 -------------
    @pyqtSlot(bool)
    def label_2_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_2_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_2_moved(self, position):
        width = self.label_2.size().width()
        height = self.label_2.size().height()
        print("moved")
        print(position)

    # ------------ label 3 -------------
    @pyqtSlot(bool)
    def label_3_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_3_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_3_moved(self, position):
        width = self.label_3.size().width()
        height = self.label_3.size().height()
        print("moved")
        print(position)

    # ------------ label 4 -------------
    @pyqtSlot(bool)
    def label_4_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_4_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_4_moved(self, position):
        width = self.label_4.size().width()
        height = self.label_4.size().height()
        print("moved")
        print(position)

    # ------------ label 5 -------------
    @pyqtSlot(bool)
    def label_5_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_5_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_5_moved(self, position):
        width = self.label_5.size().width()
        height = self.label_5.size().height()
        print("moved")
        print(position)

    # ------------ label 6 -------------
    @pyqtSlot(bool)
    def label_6_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_6_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_6_moved(self, position):
        width = self.label_6.size().width()
        height = self.label_6.size().height()
        print("moved")
        print(position)

    # ------------ label 7 -------------
    @pyqtSlot(bool)
    def label_7_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_7_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_7_moved(self, position):
        width = self.label_7.size().width()
        height = self.label_7.size().height()
        print("moved")
        print(position)

    # ------------ label 8 -------------
    @pyqtSlot(bool)
    def label_8_clicked(self, trigger):
        print("clicked")

    @pyqtSlot(bool)
    def label_8_released(self, trigger):
        print("released")

    @pyqtSlot(tuple)
    def label_8_moved(self, position):
        width = self.label_8.size().width()
        height = self.label_8.size().height()
        print("moved")
        print(position)
    
    @staticmethod
    def mouse_incoming(mouse_pos: tuple, label_size: tuple) -> bool:
        x, y = mouse_pos
        width, height = label_size
        if 30 < x < width - 30 and 30 < y < height - 30:
            return True
        else:
            return False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
