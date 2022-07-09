from chan import db
import datetime


class Board(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    board_short_name = db.Column(db.String(length=10), nullable=False, unique=True)
    board_name = db.Column(db.String(length=50), nullable=False, unique=True)
    board_description = db.Column(db.String(length=256), nullable=False, unique=True)


class Thread(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), default="Anonymous")
    datetime = db.Column(db.DateTime())
    board = db.Column(db.Integer(), db.ForeignKey("board.id"))
    text = db.Column(db.String(length=564), nullable=False)
    image_file = db.Column(db.String)

    @property
    def format_datetime(self):
        return self.datetime.strftime("%-d/%-m/%-y (%a) %H:%M")

    @property
    def name_check(self):
        return self.name

    @name_check.setter
    def name_check(self, name):
        if name == "":
            self.name = "Anonymous"
        else:
            self.name = name


class Replies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), default="Anonymous")
    datetime = db.Column(db.DateTime())
    text = db.Column(db.String(length=564), nullable=False)
    image_file = db.Column(db.String)
    thread = db.Column(db.Integer(), db.ForeignKey("thread.id"))

    @property
    def format_datetime(self):
        return self.datetime.strftime("%-d/%-m/%-y (%a) %H:%M")

    @property
    def name_check(self):
        return self.name

    @name_check.setter
    def name_check(self, name):
        if name == "":
            self.name = "Anonymous"
        else:
            self.name = name
