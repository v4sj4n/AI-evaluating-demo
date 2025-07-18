from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Applicants(Base):
    __tablename__ = "applicants"
    
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(Text)
    lastname = Column(Text)
    birthdate = Column(Date)
    email = Column(Text)
    phone = Column(Text)
    address = Column(Text)
    years_of_work = Column(Integer)
    developer_type = Column(Text)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="SET NULL"), nullable=True)
    
    job = relationship("Jobs", back_populates="applicants")
    embedding = relationship(
        "ApplicantsEmbedding",
        back_populates="applicant",
        cascade="all, delete-orphan",
        uselist=False
    )
    
    skills = relationship("Skills", secondary="applicant_skills", back_populates="applicants")