import subprocess
import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from panel_gui.control_panel import Ui_MainWindow
from panel_gui.cunstom_widgets import ClickableLabel
from utils.pixmap_prep import images_prep_factory, array_to_QImage
from config import label_image_paths_dict, projects_command_dict, \
    projects_cwd_dict, projects_view_name_dict, projects_icon_position


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stop.triggered.connect(self.process_exit)
        self.fullScreen.triggered.connect(self.showFullScreen)
        self.exitFullScreen.triggered.connect(self.showNormal)
        self.setupMenu.triggered.connect(lambda: os.system("notepad config.py"))

        self.chen1.triggered.connect(self.label_1_clicked)
        self.chen2.triggered.connect(self.label_2_clicked)
        self.li.triggered.connect(self.label_3_clicked)
        self.yv1.triggered.connect(self.label_4_clicked)
        self.yv2.triggered.connect(self.label_5_clicked)
        self.wang.triggered.connect(self.label_6_clicked)
        self.pan.triggered.connect(self.label_7_clicked)
        self.yue.triggered.connect(self.label_8_clicked)

        self.label_1.clicked.connect(self.label_1_clicked)
        self.label_1.moved.connect(self.label_1_moved)

        self.label_2.clicked.connect(self.label_2_clicked)
        self.label_2.moved.connect(self.label_2_moved)

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

        # 各label当前的状态标志位
        # 0 -> 无鼠标移动到该区域且未启动程序
        # 1 -> 鼠标移动到该区域但未启动程序
        # 2 -> 已启动程序
        self.statuses = dict(zip(projects_cwd_dict.keys(), [0] * len(projects_cwd_dict)))

        # 系统程序进程对象
        self.processes = dict(zip(projects_cwd_dict.keys(), [None] * len(projects_cwd_dict)))

        self.label_images_dict = images_prep_factory(label_image_paths_dict, projects_view_name_dict)
        # 初始化界面图片，这里界面打开会调用自动调用重写的resizeEvent方法，不需要手动初始化
        # self.update_labels_pixmap()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.update_labels_pixmap(None)  # size设为None表示图片大小自适应

    @pyqtSlot(bool)
    def process_exit(self, trigger):
        sys.exit()

    # ------------ label 1 -------------
    @pyqtSlot(bool)
    def label_1_clicked(self, trigger):
        self.mouse_clicked_action(self.label_1, projects_icon_position[0])

    @pyqtSlot(tuple)
    def label_1_moved(self, position):
        self.mouse_moved_action(position, self.label_1, projects_icon_position[0])

    # ------------ label 2 -------------
    @pyqtSlot(bool)
    def label_2_clicked(self, trigger):
        self.mouse_clicked_action(self.label_2, projects_icon_position[1])

    @pyqtSlot(tuple)
    def label_2_moved(self, position):
        self.mouse_moved_action(position, self.label_2, projects_icon_position[1])

    # ------------ label 3 -------------
    @pyqtSlot(bool)
    def label_3_clicked(self, trigger):
        self.mouse_clicked_action(self.label_3, projects_icon_position[2])

    @pyqtSlot(tuple)
    def label_3_moved(self, position):
        self.mouse_moved_action(position, self.label_3, projects_icon_position[2])

    # ------------ label 4 -------------
    @pyqtSlot(bool)
    def label_4_clicked(self, trigger):
        self.mouse_clicked_action(self.label_4, projects_icon_position[3])

    @pyqtSlot(tuple)
    def label_4_moved(self, position):
        self.mouse_moved_action(position, self.label_4, projects_icon_position[3])

    # ------------ label 5 -------------
    @pyqtSlot(bool)
    def label_5_clicked(self, trigger):
        self.mouse_clicked_action(self.label_5, projects_icon_position[4])

    @pyqtSlot(tuple)
    def label_5_moved(self, position):
        self.mouse_moved_action(position, self.label_5, projects_icon_position[4])

    # ------------ label 6 -------------
    @pyqtSlot(bool)
    def label_6_clicked(self, trigger):
        self.mouse_clicked_action(self.label_6, projects_icon_position[5])

    @pyqtSlot(tuple)
    def label_6_moved(self, position):
        self.mouse_moved_action(position, self.label_6, projects_icon_position[5])

    # ------------ label 7 -------------
    @pyqtSlot(bool)
    def label_7_clicked(self, trigger):
        self.mouse_clicked_action(self.label_7, projects_icon_position[6])

    @pyqtSlot(tuple)
    def label_7_moved(self, position):
        self.mouse_moved_action(position, self.label_7, projects_icon_position[6])

    # ------------ label 8 -------------
    @pyqtSlot(bool)
    def label_8_clicked(self, trigger):
        self.mouse_clicked_action(self.label_8, projects_icon_position[7])

    @pyqtSlot(tuple)
    def label_8_moved(self, position):
        self.mouse_moved_action(position, self.label_8, projects_icon_position[7])

    def update_labels_pixmap(self, size=(551, 320)):
        self.set_label_pixmap(self.label_1, projects_icon_position[0], size)
        self.set_label_pixmap(self.label_2, projects_icon_position[1], size)
        self.set_label_pixmap(self.label_3, projects_icon_position[2], size)
        self.set_label_pixmap(self.label_4, projects_icon_position[3], size)
        self.set_label_pixmap(self.label_5, projects_icon_position[4], size)
        self.set_label_pixmap(self.label_6, projects_icon_position[5], size)
        self.set_label_pixmap(self.label_7, projects_icon_position[6], size)
        self.set_label_pixmap(self.label_8, projects_icon_position[7], size)

    def set_label_pixmap(self, label, name, size):
        if self.label_images_dict[name] is not None:
            if size is None:
                size = label.size()
            qimage = array_to_QImage(self.label_images_dict[name][0], size)
            label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_clicked_action(self, label: ClickableLabel, project_name: str):
        if self.statuses[project_name] == 2:
            if self.processes[project_name] is not None:
                self.processes[project_name].terminate()
                self.statuses[project_name] = 1
                msg = "终止系统 " + project_name
                print(msg)
                self.statusbar.showMessage("终止系统 " + project_name)

                if self.label_images_dict[project_name] is not None:
                    label_size = label.size()
                    qimage = array_to_QImage(self.label_images_dict[project_name][1], label_size)
                    label.setPixmap(QPixmap.fromImage(qimage))
            else:
                msg = "系统 " + project_name + " 进入启动状态但未开启进程!"
                print(msg)
                self.statusbar.showMessage(msg)
        else:
            if projects_command_dict[project_name] and projects_cwd_dict[project_name]:
                self.processes[project_name] = subprocess.Popen(projects_command_dict[project_name],
                                                                cwd=projects_cwd_dict[project_name])
                self.statuses[project_name] = 2
                msg = "启动系统 " + project_name
                print(msg)
                self.statusbar.showMessage(msg)

                if self.label_images_dict[project_name] is not None:
                    label_size = label.size()
                    qimage = array_to_QImage(self.label_images_dict[project_name][2], label_size)
                    label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_moved_action(self, position: tuple, label: ClickableLabel, project_name: str):
        width = label.size().width()
        height = label.size().height()
        if self.mouse_incoming(position, (width, height)):
            if self.statuses[project_name] == 0:
                self.statuses[project_name] = 1
                if self.label_images_dict[project_name] is not None:
                    label_size = label.size()
                    # print(label_size)
                    qimage = array_to_QImage(self.label_images_dict[project_name][1], label_size)
                    label.setPixmap(QPixmap.fromImage(qimage))
                else:
                    msg = "未配置系统 " + project_name + " 图片"
                    print(msg)
                    self.statusbar.showMessage(msg)
        else:
            if self.statuses[project_name] == 1:
                self.statuses[project_name] = 0
                if self.label_images_dict[project_name] is not None:
                    label_size = label.size()
                    qimage = array_to_QImage(self.label_images_dict[project_name][0], label_size)
                    label.setPixmap(QPixmap.fromImage(qimage))

    @staticmethod
    def mouse_incoming(mouse_pos: tuple, label_size: tuple) -> bool:
        x, y = mouse_pos
        width, height = label_size
        if 50 < x < width - 50 and 50 < y < height - 50:
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
