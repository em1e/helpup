from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class RequestStatus(enum.Enum):
    open = "open"
    accepted = "accepted"
    completed = "completed"

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(Text, nullable=False)
    price = Column(Numeric, nullable=True)
    posted_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(RequestStatus), default=RequestStatus.open, nullable=False)

    posted_by_user = relationship("User", back_populates="requests")
