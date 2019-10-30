from sqlalchemy import Column, String

from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class BikeEntity(BaseEntity, QueryEntity):

    __tablename__ = "Bikes"

    name = Column(String(256), nullable=False, unique=True)

    def __init__(self):
        super().__init__()

    def create(self, name):
        self.name = name
        self._validate()

    def update(self, name):
        self.name = name

    def _read_fields(self):
        return BikeEntity.id.name



