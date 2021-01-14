import os
import shutil
import sys
import zipfile
import urllib.request
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication
import helper
from UI.widgetUpdate import Ui_widgetDownload


class Updater(QWidget):
    def __init__(self, parent=None):
        super(Updater, self).__init__(parent)
        self.widget = QWidget()
        self.widget.setWindowIcon(helper.get_icon())
        self.widget.ui = Ui_widgetDownload()
        self.widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.widget.ui.setupUi(self.widget)
        self.widget.ui.progressBar.hide()
        self.widget.ui.btnDownload.clicked.connect(self.download_latest_release)

    def Handle_Progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum * blocksize
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.widget.ui.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def download_latest_release(self, release_version=None):
        self.widget.ui.btnDownload.setDisabled(True)
        self.widget.ui.progressBar.show()
        self.widget.ui.progressBar.setValue(0)
        if release_version is False:
            release_version = helper.get_latest_version()
        file_name = "pyEMG_windows_x64_" + release_version + ".zip"
        link = "https://github.com/dimaunix/pyEMG/releases/download/" + release_version + "/" + file_name
        if self.download(link, file_name):
            if self.unpack(file_name):
                if self.replace_files():
                    self.restart_app()

    def download(self, link, filename):
        self.widget.ui.labelStatus.setText("Downloading...")
        if not os.path.exists("temp"):
            os.makedirs("temp")
        try:
            urllib.request.urlretrieve(link, "temp/"+filename, self.Handle_Progress)
            return True
        except Exception as e:
            self.widget.ui.labelStatus.setText("Download error: " + str(e))
            print(link, filename)
            self.widget.ui.progressBar.hide()
        return False

    def unpack(self, filename):
        self.widget.ui.labelStatus.setText("Unpacking new files...")
        try:
            with zipfile.ZipFile("temp/" + filename, 'r') as zip_ref:
                zip_ref.extractall("temp/update")
                return True
        except Exception as e:
            self.widget.ui.labelStatus.setText("Unpacking error: " + str(e))
        return False

    def replace_files(self):
        self.widget.ui.labelStatus.setText("Replacing files...")
        try:
            src = "temp/update/pyEMG"
            dst = "."
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            shutil.rmtree('temp')
            return True
        except Exception as e:
            self.widget.ui.labelStatus.setText("Replacing files error: " + str(e))
        return False

    def restart_app(self):
        self.widget.ui.labelStatus.setText("Restarting...")
        try:
            # os.execv(sys.argv[0], sys.argv)
            os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])
        except Exception as e:
            self.widget.ui.labelStatus.setText("Restart error: " + str(e))