import fnmatch
import os
import sys
from datetime import datetime

import requests
import keyring
import base64
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMessageBox
from packaging import version
from keyring.backends import Windows

keyring.set_keyring(Windows.WinVaultKeyring())


def get_decimal_color(color: QColor):
    return (color.red() << 16) + (color.green() << 8) + (color.blue())


def show_error(text):
    msg_box = QMessageBox()
    msg_box.setWindowIcon(get_icon())
    msg_box.setText(text)
    msg_box.setWindowTitle("Error!")
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()


def show_message(text, buttons=QMessageBox.Ok):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(text)
    msg_box.setWindowTitle("Notification")
    msg_box.setStandardButtons(buttons)
    msg_box.exec()


def show_question(text, buttons=QMessageBox.Yes | QMessageBox.No):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    ret = msg_box.question(msg_box, "Question", text, buttons)
    return ret == QMessageBox.Yes


def check_for_new_version():
    try:
        if version.parse(get_latest_version()) > version.parse(get_version()):
            return show_question("New version is available! Do you want to update now?")
    except Exception as e:
        write_log("Couldn't check for latest version. Message: " + str(e))


def get_icon():
    return QIcon(resource_path("resources/icon.ico"))


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
    with open(resource_path("version.txt"), "r") as f:
        version_number = (f.readline()).strip()
        if version_number:
            return "v" + version_number
        else:
            return "unknown"


def get_latest_version():
    response = requests.get("https://api.github.com/repos/dimaunix/pyEMG/releases/latest")
    return response.json()["tag_name"]


def get_config():
    return {
        "apiKey": "AIzaSyAG8-KjfregQT81eoSscKaTGS2r8_xh8_I",
        "authDomain": "pyegm-5eb0f.firebaseapp.com",
        "databaseURL": "https://pyegm-5eb0f-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "pyegm-5eb0f",
        "storageBucket": "pyegm-5eb0f.appspot.com",
        "messagingSenderId": "593853163742",
        "appId": "1:593853163742:web:5593bd3dac9060ed107a4f"
    }


def current_datetime():
    return datetime.utcnow().strftime("%Y%m%d%H%M%S")


def set_credentials(email, password):
    try:
        keyring.set_password("pyEMG", email, password)
        with open(".l", "wb") as f:
            enc = base64.b64encode(email.encode())
            f.write(enc)
    except Exception as e:
        write_log(e)


def get_credentials():
    try:
        if os.path.exists(".l"):
            with open(".l", "rb") as f:
                b = f.read()
                email = base64.b64decode(b)
                password = keyring.get_password("pyEMG", email.decode())
                return email.decode(), password
        else:
            return None, None
    except Exception as e:
        write_log(e)
        return None, None


def write_log(err):
    is_str = isinstance(err, str)
    if is_str:
        crash = err
    else:
        crash = ["Error on line {}".format(sys.exc_info()[-1].tb_lineno), "\n", err]
    if "PYCHARM_HOSTED" in os.environ:
        print(crash)
    else:
        if os.path.exists("logs") is False:
            os.mkdir("logs")
        with open(r"logs/" + current_datetime() + ".txt", "w") as f:
            if is_str:
                f.write(crash)
            else:
                for i in crash:
                    f.write(str(i))
