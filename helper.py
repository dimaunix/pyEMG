import fnmatch
import os

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox


def get_decimal_color(color: QColor):
    return (color.red() << 16) + (color.green() << 8) + (color.blue())


def show_error(text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(text)
    msg_box.setWindowTitle("Warning!")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()


def get_templates():
    if os.path.exists('games'):
        return fnmatch.filter(os.listdir('games'), '*.json')
    else:
        return []
