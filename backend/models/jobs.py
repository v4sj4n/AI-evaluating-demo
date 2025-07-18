from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class Jobs(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    applicants = relationship("Applicants", back_populates="job", cascade="all, delete-orphan")
    skills = relationship("Skills", secondary="jobs_skills", back_populates="jobs")