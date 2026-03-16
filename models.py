from sqlalchemy import Column, Integer, String
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    professor_name = Column(String, nullable=False)
    school = Column(String, nullable=False)
    course = Column(String, nullable=False)
    overall_rating = Column(Integer, nullable=False)
    assignment_frequency = Column(String, nullable=False)
    late_policy_rating = Column(Integer, nullable=False)
    attendance_policy_rating = Column(Integer, nullable=False)
    teaching_pace = Column(String, nullable=False)
    comment = Column(String, nullable=False)

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    professor_name = Column(String, nullable=False)
    school = Column(String, nullable=False)
