from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    __tablename__ = 'leads'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    interest = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, telefone, latitude, longitude, temperature, interest):
        self.name = name
        self.email = email
        self.telefone = telefone
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.interest = interest

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'telefone': self.telefone,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'temperature': self.temperature,
            'interest': self.interest
        }
