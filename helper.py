import fnmatch
import os
import sys

from PyQt5.QtGui import QColor, QIcon
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


def show_message(text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(text)
    msg_box.setWindowTitle("Notification")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()


def get_icon():
    return QIcon(resource_path("icon.ico"))


def get_templates():
    if os.path.exists('games'):
        return fnmatch.filter(os.listdir('games'), '*.json')
    else:
        return []


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
    return os.path.join(base_path, relative_path)


def get_version():
    f = open(resource_path("version.txt"), "r")
    version = f.read()
    if version:
        return "v" + version
    else:
        return "unknown"
