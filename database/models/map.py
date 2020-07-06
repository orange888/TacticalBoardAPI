from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database.data import Base
from marshmallow import Schema, fields


class Map(Base):
    __tablename__ = 'map'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    reference_id = Column(Integer, ForeignKey('reference.id'))
    reference = relationship('Reference', back_populates='maps')
    mapImages = relationship('MapImage', back_populates='map')