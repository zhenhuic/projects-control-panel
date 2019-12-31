import subprocess
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from panel_gui.control_panel import Ui_MainWindow
from pixmap_prep import images_prep_factory, array_to_QImage
from config import label_image_paths_dict


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_1.clicked.connect(self.label_1_clicked)
        self.label_1.moved.connect(self.label_1_moved)

        self.label_2.clicked.connect(self.label_2_clicked)
        self.label_2.moved.connect(self.label_2_moved)

        self.label_3.clicked.connect(self.label_3_clicked)
        self.label_3.moved.connect(self.label_3_moved)

        self.label_3.clicked.connect(self.label_3_clicked)
        self.label_3.moved.connect(self.label_3_moved)

        self.label_4.clicked.connect(self.label_4_clicked)
        self.label_4.moved.connect(self.label_4_moved)

        self.label_5.clicked.connect(self.label_5_clicked)
        self.label_5.moved.connect(self.label_5_moved)

        self.label_6.clicked.connect(self.label_6_clicked)
        self.label_6.moved.connect(self.label_6_moved)

        self.label_7.clicked.connect(self.label_7_clicked)
        self.label_7.moved.connect(self.label_7_moved)

        self.label_8.clicked.connect(self.label_8_clicked)
        self.label_8.moved.connect(self.label_8_moved)

        self.label_images_dict = images_prep_factory(label_image_paths_dict)

        # 各label当前的状态标志位
        # 0 -> 无鼠标移动到该区域且未启动程序
        # 1 -> 鼠标移动到该区域但未启动程序
        # 2 -> 已启动程序
        self.statuses = [0] * 8

        # 系统程序进程对象
        self.processes = [None] * 8

    # ------------ label 1 -------------
    @pyqtSlot(bool)
    def label_1_clicked(self, trigger):
        if self.statuses[0] == 2:
            if self.processes[0] is not None:
                self.processes[0].terminate()
                self.statuses[0] = 1

                label_size = self.label_1.size()
                qimage = array_to_QImage(self.label_images_dict["chen_1"][1], label_size)
                self.label_1.setPixmap(QPixmap.fromImage(qimage))
        else:
            self.processes[0] = subprocess.Popen(
                "D:\\Anaconda3\\envs\\pth\\python.exe E:\\Lab417\\xio-intrusion-detection\\gui_main.py",
                cwd="E:\\Lab417\\xio-intrusion-detection")
            self.statuses[0] = 2

            label_size = self.label_1.size()
            qimage = array_to_QImage(self.label_images_dict["chen_1"][2], label_size)
            self.label_1.setPixmap(QPixmap.fromImage(qimage))

    @pyqtSlot(tuple)
    def label_1_moved(self, position):
        width = self.label_1.size().width()
        height = self.label_1.size().height()

        if self.mouse_incoming(position, (width, height)):
            if self.statuses[0] == 0:
                self.statuses[0] = 1

                label_size = self.label_1.size()
                qimage = array_to_QImage(self.label_images_dict["chen_1"][1], label_size)
                self.label_1.setPixmap(QPixmap.fromImage(qimage))
        else:
            if self.statuses[0] == 1:
                self.statuses[0] = 0

                label_size = self.label_1.size()
                qimage = array_to_QImage(self.label_images_dict["chen_1"][0], label_size)
                self.label_1.setPixmap(QPixmap.fromImage(qimage))


    # ------------ label 2 -------------
    @pyqtSlot(bool)
    def label_2_clicked(self, trigger):
        pass

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
