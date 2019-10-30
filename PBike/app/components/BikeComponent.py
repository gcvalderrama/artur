from app.core.BikeEntity import BikeEntity
from app.repository.database import db_session


class BikeComponent:
    def __init__(self):
        pass

    def list(self):
        bikes = BikeEntity.query.all()
        result = list()
        for item in bikes:
            result.append(item.to_dict())
        return result

    def create(self, data):
        bike = BikeEntity()
        bike.create(data["name"])
        db_session.add(bike)
        db_session.commit()

    def update(self, key, data):
        bike = BikeEntity.query.filter(BikeEntity.id == key).first()
        bike.update(data["name"])
        db_session.commit()
        return bike.to_dict()


