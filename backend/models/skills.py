from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class Skills(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=True)
    category = Column(Text, nullable=True)  # e.g., "programming", "framework", "database", etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Many-to-many relationships
    applicants = relationship("Applicants", secondary="applicant_skills", back_populates="skills")
    jobs = relationship("Jobs", secondary="jobs_skills", back_populates="skills")