# load application vars
from system.libraries.database import db


class User:
    @staticmethod
    def get_users():
        records = db.get('users')

        return records


example_model = User()