import json
import pyrebase
import requests
import helper


class DB:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(helper.get_config())
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.user = None
        self.token = None

    def sign_in(self, email, password):
        try:
            self.user = self.auth.sign_in_with_email_and_password(email, password)
            dict_user = dict(self.user)
            self.token = dict_user.get("idToken")
            return True
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)["error"]["message"]
            helper.show_error(error)
        return False

    def get_data(self, game):
        return self.db.child("games").child(game).child("data").get(self.token).val()

    def set_data(self, game, data):
        self.db.child("games").child(game).child("data").set(data, self.token)
        self.db.child("games").child(game).child("changed_at").set(helper.current_datetime(), self.token)

    def get_games(self):
        try:
            games = self.db.child("games").shallow().get(self.token)
            if games:
                return games.val()
        except Exception as e:
            print(e)
            return None
