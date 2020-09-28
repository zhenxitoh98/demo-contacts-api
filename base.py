from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# The database
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    number = db.Column(db.String(120), unique=True, nullable=True)

    def __init__(self, id, name, height, age, email, number):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.email = email
        self.number = number

    def json(self):
        return {'ID': self.id, 'Name': self.name, 'Age': self.age, 'Height': self.height}

    def json2(self):
        return {'ID': self.id, 'Email': self.email, 'Number': self.number}

    def jsonAll(self):
        return {'ID': self.id, 'Name': self.name, 'Age': self.age, 'Height': self.height, 'Email': self.email, 'Number': self.number}

    # check if the user is in the database already
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

    # update the database
    def save_to(self):
        db.session.add(self)
        db.session.commit()

    # delete the database
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
