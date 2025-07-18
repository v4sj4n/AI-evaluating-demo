# jobs_skills.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.session import Base

class JobsSkills(Base):
    __tablename__ = "jobs_skills"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id", ondelete="CASCADE"), nullable=False, index=True)
    required_level = Column(Text, nullable=True)  # e.g., "beginner", "intermediate", "advanced", "expert"
    is_required = Column(Boolean, default=True)  # True for required skills, False for nice-to-have
    priority = Column(Integer, default=1)  # 1 = high priority, 2 = medium, 3 = low
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships to access the actual job and skill objects
    job = relationship("Jobs")
    skill = relationship("Skills")