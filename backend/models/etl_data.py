from sqlalchemy import Column, Integer, String
from backend.models.base import Base

class EtlData(Base):
    __tablename__ = "etl_data"

    id = Column(Integer, primary_key=True, index=True)
    uf = Column(String, nullable=True)
    vendedor = Column(String, nullable=True)
