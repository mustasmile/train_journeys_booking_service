from app import app, db
from app.models import Train

# Créer un contexte d'application Flask
with app.app_context():
    # Crée les tables dans la base de données
    db.create_all()

    # Créer des trains pour tester
    train1 = Train(
        departure="Paris", 
        arrival="London", 
        departure_time="2025-01-30 08:00:00", 
        arrival_time="2025-01-30 10:00:00", 
        seats_available=5, 
        class_type="First"
    )
    train2 = Train(
        departure="Paris", 
        arrival="London", 
        departure_time="2025-01-30 09:00:00", 
        arrival_time="2025-01-30 11:00:00", 
        seats_available=10, 
        class_type="First"
    )
    train3 = Train(
        departure="Paris", 
        arrival="Berlin", 
        departure_time="2025-01-30 07:00:00", 
        arrival_time="2025-01-30 12:00:00", 
        seats_available=3, 
        class_type="Business"
    )
    train4 = Train(
        departure="London", 
        arrival="Berlin", 
        departure_time="2025-01-30 14:00:00", 
        arrival_time="2025-01-30 18:00:00", 
        seats_available=8, 
        class_type="Standard"
    )

    # Ajouter et valider dans la base de données
    db.session.add(train1)
    db.session.add(train2)
    db.session.add(train3)
    db.session.add(train4)
    db.session.commit()

    print("Trains ajoutés avec succès")
