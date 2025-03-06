from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    is_offer = Column(String, nullable=False)  # Campo adicionado