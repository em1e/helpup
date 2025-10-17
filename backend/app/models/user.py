from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # 'youth' or 'adult'
    rating = Column(Numeric, nullable=True)

    requests = relationship("Request", back_populates="posted_by_user")
