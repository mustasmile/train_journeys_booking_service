#routes.py

from app import app, db
from flask import render_template, request, jsonify
from app.models import Train

@app.route('/search_trains', methods=['GET'])
def search_trains():
    departure = request.args.get('departure')
    arrival = request.args.get('arrival')
    travel_class = request.args.get('travel_class')

    trains = Train.query.filter_by(departure=departure, arrival=arrival, class_type=travel_class).all()

    if not trains:
        return render_template('search_trains.html', message="No available trains.")
    
    result = []
    for train in trains:
        result.append({
            'train_id': train.id,
            'departure_time': train.departure_time,
            'arrival_time': train.arrival_time,
            'seats_available': train.seats_available,
            'class_type': train.class_type
        })

    return render_template('search_trains.html', trains=result)

# Route pour réserver un train
@app.route('/reserve_train', methods=['POST'])
def reserve_train():
    data = request.get_json()
    train_id = data['train_id']
    travel_class = data['travel_class']
    ticket_type = data['ticket_type']
    customer_name = data['customer_name']

    train = Train.query.get(train_id)

    if not train or train.seats_available <= 0:
        return jsonify({'message': 'Train not available.'}), 400

    reservation = Reservation(train_id=train_id, travel_class=travel_class, ticket_type=ticket_type, customer_name=customer_name)
    train.seats_available -= 1
    db.session.add(reservation)
    db.session.commit()

    return jsonify({'message': 'Reservation successful!'}), 200
