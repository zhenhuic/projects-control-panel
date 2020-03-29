import subprocess
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from panel_gui.control_panel import Ui_MainWindow
from panel_gui.cunstom_widgets import ClickableLabel
from utils.pixmap_prep import images_prep_factory, array_to_QImage
from config import label_image_paths_dict, projects_command_dict, \
    projects_cwd_dict, projects_view_name_dict


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
        self.statuses = [0] * 8

        # 系统程序进程对象
        self.processes = [None] * 8

        self.label_images_dict = images_prep_factory(label_image_paths_dict, projects_view_name_dict)
        self.init_labels_pixmap()

    # ------------ label 1 -------------
    @pyqtSlot(bool)
    def label_1_clicked(self, trigger):
        self.mouse_clicked_action(0, self.label_1, "chen_1")

    @pyqtSlot(tuple)
    def label_1_moved(self, position):
        self.mouse_moved_action(position, 0, self.label_1, "chen_1")

    # ------------ label 2 -------------
    @pyqtSlot(bool)
    def label_2_clicked(self, trigger):
        self.mouse_clicked_action(1, self.label_2, "chen_2")

    @pyqtSlot(tuple)
    def label_2_moved(self, position):
        self.mouse_moved_action(position, 1, self.label_2, "chen_2")

    # ------------ label 3 -------------
    @pyqtSlot(bool)
    def label_3_clicked(self, trigger):
        self.mouse_clicked_action(2, self.label_3, "li")

    @pyqtSlot(tuple)
    def label_3_moved(self, position):
        self.mouse_moved_action(position, 2, self.label_3, "li")

    # ------------ label 4 -------------
    @pyqtSlot(bool)
    def label_4_clicked(self, trigger):
        self.mouse_clicked_action(3, self.label_4, "yv_1")

    @pyqtSlot(tuple)
    def label_4_moved(self, position):
        self.mouse_moved_action(position, 3, self.label_4, "yv_1")

    # ------------ label 5 -------------
    @pyqtSlot(bool)
    def label_5_clicked(self, trigger):
        self.mouse_clicked_action(4, self.label_5, "yv_2")

    @pyqtSlot(tuple)
    def label_5_moved(self, position):
        self.mouse_moved_action(position, 4, self.label_5, "yv_2")

    # ------------ label 6 -------------
    @pyqtSlot(bool)
    def label_6_clicked(self, trigger):
        self.mouse_clicked_action(5, self.label_6, "wang")

    @pyqtSlot(tuple)
    def label_6_moved(self, position):
        self.mouse_moved_action(position, 5, self.label_6, "wang")

    # ------------ label 7 -------------
    @pyqtSlot(bool)
    def label_7_clicked(self, trigger):
        self.mouse_clicked_action(6, self.label_7, "pan")

    @pyqtSlot(tuple)
    def label_7_moved(self, position):
        self.mouse_moved_action(position, 6, self.label_7, "pan")

    # ------------ label 8 -------------
    @pyqtSlot(bool)
    def label_8_clicked(self, trigger):
        pass

    @pyqtSlot(tuple)
    def label_8_moved(self, position):
        pass

    def init_labels_pixmap(self):
        for i, name in enumerate(label_image_paths_dict.keys()):
            if i == 0:
                self.set_label_init_pixmap(self.label_1, name)
            elif i == 1:
                self.set_label_init_pixmap(self.label_2, name)
            elif i == 2:
                self.set_label_init_pixmap(self.label_3, name)
            elif i == 3:
                self.set_label_init_pixmap(self.label_4, name)
            elif i == 4:
                self.set_label_init_pixmap(self.label_5, name)
            elif i == 5:
                self.set_label_init_pixmap(self.label_6, name)
            elif i == 6:
                self.set_label_init_pixmap(self.label_7, name)

    def set_label_init_pixmap(self, label, name):
        if self.label_images_dict[name] is not None:
            qimage = array_to_QImage(self.label_images_dict[name][0], (551, 320))
            label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_clicked_action(self, index: int, label: ClickableLabel, project_name: str):
        if self.statuses[index] == 2:
            if self.processes[index] is not None:
                self.processes[index].terminate()
                self.statuses[index] = 1
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
                self.processes[index] = subprocess.Popen(projects_command_dict[project_name],
                                                         cwd=projects_cwd_dict[project_name])
                self.statuses[index] = 2
                msg = "启动系统 " + project_name
                print(msg)
                self.statusbar.showMessage(msg)

                if self.label_images_dict[project_name] is not None:
                    label_size = label.size()
                    qimage = array_to_QImage(self.label_images_dict[project_name][2], label_size)
                    label.setPixmap(QPixmap.fromImage(qimage))

    def mouse_moved_action(self, position: tuple, index: int, label: ClickableLabel, project_name: str):
        width = label.size().width()
        height = label.size().height()
        if self.mouse_incoming(position, (width, height)):
            if self.statuses[index] == 0:
                self.statuses[index] = 1
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
            if self.statuses[index] == 1:
                self.statuses[index] = 0
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
