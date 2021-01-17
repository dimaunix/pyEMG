import json
import pyrebase
import requests

import helper


class DB:
    def __init__(self):
        firebase = pyrebase.initialize_app(helper.get_config())
        self.auth = self.db.auth()
        self.db = firebase.database()

    def sign_in(self, email, password):
        try:
            self.auth.sign_in_with_email_and_password(email, password)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            helper.show_error(error)

    def get_data(self, game):
        return self.db.child("games").child(game).get()

    def set_date(self, game, data):
        self.db.child('games').child(game).set(data)
