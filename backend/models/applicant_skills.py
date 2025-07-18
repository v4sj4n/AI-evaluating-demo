from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class ApplicantSkills(Base):
    __tablename__ = "applicant_skills"
    
    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id", ondelete="CASCADE"), nullable=False, index=True)
    proficiency_level = Column(Text, nullable=True)  # e.g., "beginner", "intermediate", "advanced", "expert"
    years_of_experience = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships to access the actual applicant and skill objects
    applicant = relationship("Applicants")
    skill = relationship("Skills")