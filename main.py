import json
import re
import sys
from datetime import datetime
from types import SimpleNamespace
from collections import OrderedDict
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QLocale
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QPushButton

import helper
from eventWidget import MyEventWidget
from messageDialog import MessageDialog


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainWindow.ui', self)
        self.btnColorPicker = self.findChild(QPushButton, 'btnColorPicker')
        self.btnColorPicker.clicked.connect(self.open_color_picker)
        self.comboSelectGame.activated[str].connect(self.parse_selected_template)
        templates = helper.get_templates()
        self.generate_combo_items(templates)
        self.parse_selected_template(self.selected_template())
        self.btnAddEvent.clicked.connect(self.add_new_event)
        self.btnRemoveEvent.clicked.connect(self.remove_current_event)
        self.btnGenerate.clicked.connect(self.open_message_dialog)
        self.show()

    def open_message_dialog(self):
        widget = MessageDialog()
        try:
            widget.editMessage.setText("-ce " + self.get_generated_json())
        except Exception as e:
            print(e)
        widget.show()

    def get_message_dict(self):
        dict_message = OrderedDict()
        dict_message["title"] = self.inputTitle.text()
        dict_message["description"] = self.inputDescription.text()
        dict_message["url"] = self.inputURL.text()
        dict_message["color"] = helper.get_decimal_color(QColor(self.get_current_color()))
        dict_message["thumbnail"] = {"url": self.inputThumb.text()}
        dict_message["fields"] = []
        for w in range(self.stackedWidget.count()):
            if w > 0:
                widget = self.stackedWidget.widget(w)
                formatted_date_time = widget.dateTimeEvent.dateTime().toString("MMMM d, hh:mm") + " UTC"
                dict_message["fields"].append({
                    "name": self.selected_template() + " - " + formatted_date_time,
                    "value": "[" + widget.inputEventName.text() + "](" + widget.inputEventURL.text() + ") - Host: " + widget.inputHost.text()
                })
        return dict_message

    def get_generated_json(self):
        return json.dumps(self.get_message_dict(), indent=4)

    def remove_current_event(self):
        self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
        self.set_input_page_length()

    def set_input_page_length(self):
        self.inputPage.setMaximum(self.stackedWidget.count() - 1)
        if self.stackedWidget.count() > 1:
            self.inputPage.setMinimum(1)
            self.inputPage.setMaximum(self.stackedWidget.count() - 1)
        else:
            self.inputPage.setMinimum(0)
            self.inputPage.setMaximum(0)

    def add_new_event(self):
        new_widget = MyEventWidget(self.stackedWidget)
        self.stackedWidget.addWidget(new_widget)
        self.set_input_page_length()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.count() - 1)
        return new_widget

    def get_current_color(self):
        style = self.btnColorPicker.styleSheet()
        if style:
            return style.split(': ')[1]

    def selected_template(self):
        return self.comboSelectGame.currentText()

    def generate_combo_items(self, files):
        for file in files:
            self.comboSelectGame.addItem(file.replace('.json', ''))

    def clear_stacked_widgets(self):
        for w in range(self.stackedWidget.count()):
            if w > 0:
                self.stackedWidget.removeWidget(self.stackedWidget.widget(w))
        self.set_input_page_length()

    @pyqtSlot(str)
    def parse_selected_template(self, template):
        self.clear_stacked_widgets()
        if template:
            try:
                f = open("games/" + template + ".json", "r")
                json_str = f.read()
                obj = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))

                if obj:
                    if hasattr(obj, "title"):
                        self.inputTitle.setText(obj.title)
                    if hasattr(obj, "description"):
                        self.inputDescription.setText(obj.description)
                    if hasattr(obj, "url"):
                        self.inputURL.setText(obj.url)
                    if hasattr(obj, "thumbnail") and hasattr(obj.thumbnail, "url"):
                        self.inputThumb.setText(obj.thumbnail.url)
                    if hasattr(obj, "color"):
                        color = hex(obj.color).replace("0x", "")
                        self.btnColorPicker.setStyleSheet("background-color: #" + color)
                    if hasattr(obj, "fields") and isinstance(obj.fields, list):
                        length = len(obj.fields)
                        for i in range(length):
                            new_widget = self.add_new_event()
                            event_data = obj.fields[i]
                            date_time_str = (event_data.name.split("-")[1]).strip()
                            reddit_link = re.search(r"\[(.*?)]\((.*?)\)", event_data.value).groups()
                            host = event_data.value.split("Host:")[1].strip()
                            title = reddit_link[0]
                            url = reddit_link[1]
                            locale = QLocale(QLocale.English, QLocale.UnitedStates)
                            date_time = locale.toDateTime(str(datetime.now().year) + " " + date_time_str,
                                                          "yyyy MMMM d, hh:mm t")
                            if date_time.isValid():
                                new_widget.dateTimeEvent.setDateTime(date_time)
                            new_widget.inputEventName.setText(title)
                            new_widget.inputEventURL.setText(url)
                            new_widget.inputHost.setText(host)
            except json.decoder.JSONDecodeError:
                helper.show_error("JSON in " + template + ".json is invalid")

    def open_color_picker(self):
        color = QColorDialog.getColor()
        self.btnColorPicker.setStyleSheet("")
        self.btnColorPicker.setStyleSheet("background-color: " + color.name())


app = QApplication(sys.argv)
window = Ui()
app.exec_()
