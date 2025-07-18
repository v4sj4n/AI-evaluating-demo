from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from db.session import Base  # your declarative base
from models.applicants import Applicants  

class ApplicantsEmbedding(Base):
    __tablename__ = "applicants_embedding"

    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.id", ondelete="CASCADE"), nullable=False, index=True)

    # Vector column specifically for 1024-dimensional vectors
    embedding = Column(Vector(1024), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    applicant = relationship("Applicants", back_populates="embedding")

# Add back-populates on Applicants model as well:
Applicants.embedding = relationship(
    "ApplicantsEmbedding", back_populates="applicant", cascade="all, delete-orphan", uselist=False
)
