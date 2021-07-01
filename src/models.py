from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship("Favorite",backref="user")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250),unique=False,nullable=False)
    character_id = db.Column(db.Integer,unique=True,nullable=False)
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Planet_name = db.Column(db.String(250),unique=False,nullable=False)
    Planet_id = db.Column(db.Integer,unique=True,nullable=False)
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(250),unique=False,nullable=False)
    vehicle_id = db.Column(db.Integer,unique=True,nullable=False)
    


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_name = db.Column(db.String(250), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
