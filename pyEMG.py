import json
import re
import sys
from datetime import datetime, timedelta
from types import SimpleNamespace
from collections import OrderedDict
from PyQt5.QtCore import pyqtSlot, QLocale, QTime, QDateTime
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QPushButton

import helper
from eventWidget import MyEventWidget
from widgetMessage import WidgetMessage
from UI.mainWindow import Ui_mainWindow
from updater import Updater
from widgetAuth import WidgetAuth
from db import DB


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_loading = True
        self.db = DB()
        self.setWindowTitle("Event Message Generator - " + helper.get_version())
        self.setWindowIcon(helper.get_icon())
        self.ui.btnRefresh.setIcon(QIcon(helper.resource_path("resources/refresh.png")))
        self.ui.btnAuth.setIcon(QIcon(helper.resource_path("resources/login.png")))
        self.ui.btnSaveTemplate.setIcon(QIcon(helper.resource_path("resources/save.png")))
        self.ui.btnColorPicker = self.findChild(QPushButton, 'btnColorPicker')
        self.ui.btnColorPicker.clicked.connect(self.open_color_picker)
        self.ui.comboSelectGame.activated[str].connect(self.parse_selected_template)
        self.locale = QLocale(QLocale.English, QLocale.UnitedStates)
        templates = helper.get_templates()
        self.generate_combo_items(templates)
        self.parse_selected_template(self.selected_template())
        self.ui.btnAddEvent.clicked.connect(self.add_new_event)
        self.ui.btnRemoveEvent.clicked.connect(self.remove_current_event)
        self.ui.btnGenerate.clicked.connect(self.open_message_dialog)
        self.ui.btnSaveTemplate.clicked.connect(self.save_data)
        self.ui.btnAuth.clicked.connect(self.open_auth)
        self.show()
        self.check_version()

    def open_auth(self):
        try:
            w = WidgetAuth({"parent": self, "db": self.db})
            w.widget.exec_()
            if self.db.user:
                self.ui.btnAuth.setDisabled(True)
        except Exception as e:
            print(e)

    def check_version(self):
        if helper.check_for_new_version():
            try:
                updater = Updater(self)
                updater.widget.show()
            except Exception as e:
                print(e)

    def save_data(self):
        json_template = self.get_generated_json()
        if self.db.user:
            self.save_db(json_template)
            self.save_offline(json_template)
        else:
            self.save_offline(json_template)

    def save_db(self, json_data):
        try:
            self.db.set_data(self.ui.comboSelectGame.currentText(), json_data)
        except Exception as e:
            print(e)

    def save_offline(self, json_data):
        try:
            with open("games/" + self.ui.comboSelectGame.currentText() + ".json", "w") as new_file:
                new_file.write(json_data)
                new_file.close()
                helper.show_message("Template was successfully saved!")
        except Exception as e:
            print(e)

    def open_message_dialog(self):
        try:
            widget = WidgetMessage(self)
            widget.dialog.ui.editMessage.setText("-ce " + self.get_generated_json())
            widget.dialog.show()
        except Exception as e:
            print(e)

    def set_events_count(self):
        if self.ui.stackedWidget.count() - 1 != -1:
            self.ui.lblCount.setNum(self.ui.stackedWidget.count() - 1)
        else:
            self.ui.lblCount.setNum(0)

    @property
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
                formatted_date_time = self.locale.toString(widget.ui.dateTimeEvent.dateTime(), "MMMM d, hh:mm") + " UTC"
                if widget.ui.inputEventName.text() == "" and widget.ui.inputEventURL.text() == "" and widget.ui.inputHost.text() == "":
                    value = "Open"
                else:
                    value = "[" + widget.ui.inputEventName.text() + "](" + widget.ui.inputEventURL.text() + ") - Host: " + widget.ui.inputHost.text()

                dict_message["fields"].append({
                    "name": self.selected_template() + " - " + formatted_date_time,
                    "value": value
                })
        return dict_message

    def get_generated_json(self):
        return json.dumps(self.get_message_dict, indent=4)

    def remove_current_event(self):
        if self.ui.stackedWidget.count() > 1:
            widget = self.ui.stackedWidget.currentWidget()
            self.ui.stackedWidget.removeWidget(widget)
            self.set_input_page_length()
            self.set_events_count()

    def set_input_page_length(self):
        if self.ui.stackedWidget.count() > 1:
            self.ui.inputPage.setMinimum(1)
            self.ui.inputPage.setMaximum(self.ui.stackedWidget.count() - 1)
        else:
            self.ui.inputPage.setMinimum(0)
            self.ui.inputPage.setMaximum(0)

    def add_new_event(self):
        new_widget = MyEventWidget(self.ui.stackedWidget)
        widget_count = self.ui.stackedWidget.count() - 1
        datetime_event = datetime.now()

        if widget_count > 0:
            w = self.ui.stackedWidget.widget(widget_count)
            datetime_event = self.locale.toDateTime(w.ui.dateTimeEvent.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                                                    "yyyy-MM-dd HH:mm:ss")
            datetime_event = datetime_event.addDays(1)
        else:
            friday = 4
            datetime_event = QDateTime(datetime_event + timedelta(friday - datetime_event.weekday()))
            datetime_event.setTime(QTime(20, 0))
        new_widget.ui.dateTimeEvent.setDateTime(datetime_event)
        self.ui.stackedWidget.addWidget(new_widget)
        self.set_input_page_length()
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)
        self.set_events_count()
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
        try:
            while self.ui.stackedWidget.count() > 1:
                widget = self.ui.stackedWidget.widget(self.ui.stackedWidget.count() - 1)
                self.ui.stackedWidget.removeWidget(widget)
        except Exception as e:
            print(e)
        self.set_input_page_length()

    @pyqtSlot(str)
    def parse_selected_template(self, template):
        self.clear_stacked_widgets()
        if template:
            try:
                with open("games/" + template + ".json", "r") as f:
                    json_str = f.read()
                    f.close()
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
                            date_time = self.locale.toDateTime(str(datetime.now().year) + " " + date_time_str,
                                                               "yyyy MMMM d, hh:mm t")
                            if date_time.isValid():
                                new_widget.dateTimeEvent.setDateTime(date_time)
                            new_widget.inputEventName.setText(title)
                            new_widget.inputEventURL.setText(url)
                            new_widget.inputHost.setText(host)
            except json.decoder.JSONDecodeError:
                helper.show_error("JSON in " + template + ".json is invalid")
        self.init_loading = False

    def open_color_picker(self):
        color = QColorDialog.getColor()
        self.ui.btnColorPicker.setStyleSheet("")
        self.ui.btnColorPicker.setStyleSheet("background-color: " + color.name())


app = QApplication(sys.argv)
window = Ui()
app.exec_()
