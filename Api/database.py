from flask_sqlalchemy import SQLAlchemy

class DatabaseConnection:
    def __init__(self, app):
        self.app = app
        self.db = SQLAlchemy(app)

    def initialize_db(self):
        with self.app.app_context():
            self.db.create_all()

    def get_db(self):
        return self.db

    def close_db(self):
        self.db.session.close()
