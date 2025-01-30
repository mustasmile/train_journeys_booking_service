from app import db

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String(100))
    arrival = db.Column(db.String(100))
    departure_time = db.Column(db.String(100))
    arrival_time = db.Column(db.String(100))
    seats_available = db.Column(db.Integer)
    class_type = db.Column(db.String(50))

    def __repr__(self):
        return f'<Train {self.id}>'

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'), nullable=False)
    travel_class = db.Column(db.String(50))
    ticket_type = db.Column(db.String(50))
    customer_name = db.Column(db.String(100))

    train = db.relationship('Train', back_populates='reservations')

    def __repr__(self):
        return f'<Reservation {self.id}>'

Train.reservations = db.relationship('Reservation', back_populates='train')
