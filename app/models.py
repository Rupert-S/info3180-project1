from . import db


class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    location = db.Column(db.String(255))
    bathroom_no = db.Column(db.Integer)
    bedroom_no = db.Column(db.Integer)
    type = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    pic = db.Column(db.String(255))


    def __init__(self, title, location, bathroom_no, bedroom_no, type, description, price, pic):
        self.title = title
        self.location = location
        self.bathroom_no = bathroom_no
        self.bedroom_no = bedroom_no
        self.type = type
        self.description = description
        self.price = price
        self.pic = pic

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support