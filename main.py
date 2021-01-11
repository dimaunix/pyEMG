import json
import re
import sys
from datetime import datetime
from types import SimpleNamespace
from collections import OrderedDict
from PyQt5.QtCore import pyqtSlot, QLocale
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QPushButton

import helper
from eventWidget import MyEventWidget
from widgetMessage import WidgetMessage
from UI.mainWindow import Ui_mainWindow


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.btnColorPicker = self.findChild(QPushButton, 'btnColorPicker')
        self.ui.btnColorPicker.clicked.connect(self.open_color_picker)
        self.ui.comboSelectGame.activated[str].connect(self.parse_selected_template)
        templates = helper.get_templates()
        self.generate_combo_items(templates)
        self.parse_selected_template(self.selected_template())
        self.ui.btnAddEvent.clicked.connect(self.add_new_event)
        self.ui.btnRemoveEvent.clicked.connect(self.remove_current_event)
        self.ui.btnGenerate.clicked.connect(self.open_message_dialog)
        self.show()

    def open_message_dialog(self):
        try:
            widget = WidgetMessage()
            widget.ui.editMessage.setText("-ce " + self.get_generated_json())
            widget.show()
        except Exception as e:
            print(e)

    def get_message_dict(self):
        dict_message = OrderedDict()
        dict_message["title"] = self.ui.inputTitle.text()
        dict_message["description"] = self.ui.inputDescription.text()
        dict_message["url"] = self.ui.inputURL.text()
        dict_message["color"] = helper.get_decimal_color(QColor(self.get_current_color()))
        dict_message["thumbnail"] = {"url": self.ui.inputThumb.text()}
        dict_message["fields"] = []
        for w in range(self.ui.stackedWidget.count()):
            if w > 0:
                widget = self.ui.stackedWidget.widget(w)
                formatted_date_time = widget.ui.dateTimeEvent.dateTime().toString("MMMM d, hh:mm") + " UTC"
                dict_message["fields"].append({
                    "name": self.selected_template() + " - " + formatted_date_time,
                    "value": "[" + widget.ui.inputEventName.text() + "](" + widget.ui.inputEventURL.text() + ") - Host: " + widget.ui.inputHost.text()
                })
        return dict_message

    def get_generated_json(self):
        return json.dumps(self.get_message_dict(), indent=4)

    def remove_current_event(self):
        self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.currentWidget())
        self.ui.set_input_page_length()

    def set_input_page_length(self):
        self.ui.inputPage.setMaximum(self.ui.stackedWidget.count() - 1)
        if self.ui.stackedWidget.count() > 1:
            self.ui.inputPage.setMinimum(1)
            self.ui.inputPage.setMaximum(self.ui.stackedWidget.count() - 1)
        else:
            self.ui.inputPage.setMinimum(0)
            self.ui.inputPage.setMaximum(0)

    def add_new_event(self):
        new_widget = MyEventWidget(self.ui.stackedWidget)
        self.ui.stackedWidget.addWidget(new_widget)
        self.set_input_page_length()
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)
        return new_widget.ui

    def get_current_color(self):
        style = self.ui.btnColorPicker.styleSheet()
        if style:
            return style.split(': ')[1]

    def selected_template(self):
        return self.ui.comboSelectGame.currentText()

    def generate_combo_items(self, files):
        for file in files:
            self.ui.comboSelectGame.addItem(file.replace('.json', ''))

    def clear_stacked_widgets(self):
        for w in range(self.ui.stackedWidget.count()):
            if w > 0:
                self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(w))
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
                        self.ui.inputTitle.setText(obj.title)
                    if hasattr(obj, "description"):
                        self.ui.inputDescription.setText(obj.description)
                    if hasattr(obj, "url"):
                        self.ui.inputURL.setText(obj.url)
                    if hasattr(obj, "thumbnail") and hasattr(obj.thumbnail, "url"):
                        self.ui.inputThumb.setText(obj.thumbnail.url)
                    if hasattr(obj, "color"):
                        color = hex(obj.color).replace("0x", "")
                        self.ui.btnColorPicker.setStyleSheet("background-color: #" + color)
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
        self.ui.btnColorPicker.setStyleSheet("")
        self.ui.btnColorPicker.setStyleSheet("background-color: " + color.name())


app = QApplication(sys.argv)
window = Ui()
app.exec_()
