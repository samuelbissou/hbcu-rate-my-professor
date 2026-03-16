# imports
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import engine, get_db
import models

models.Base.metadata.create_all(bind=engine)

#app instance
app = FastAPI()

#pydantic models (classes)
class ReviewSchema(BaseModel):
    professor_name: str
    school: str
    course: str
    overall_rating: int = Field (ge=1 , le=5)
    assignment_frequency: str
    late_policy_rating: int = Field(ge=1, le=5)
    attendance_policy_rating: int = Field (ge=1, le=5)
    teaching_pace: str 
    comment: str

class BookmarkSchema(BaseModel):
    professor_name: str
    school: str

#hardcoded data


#endpoints
@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/professors")
def get_professors():
    return [
        {
            "id": 1,
            "name": "Bob Crafts",
            "school": "Huston-Tillotson University",
        },
        {
            "id": 2,
            "name": "John Lemons",
            "school": "Huston-Tillotson University",
        }
    ]

@app.get("/professors/{name}")
def get_professor(name: str):
    return {"name": name, "message": f"Showing profile for {name}"}

@app.get("/professors/{name}/reviews")
def get_professor_reviews(name: str, db: Session = Depends(get_db)):
    reviews = db.query(models.Review).filter(
        models.Review.professor_name == name
    ).all()
    return reviews

@app.post("/reviews")
def create_review(review: ReviewSchema, db: Session = Depends(get_db)):
   db_review = models.Review(
       professor_name=review.professor_name,
       school=review.school,
       course=review.course,
       overall_rating=review.overall_rating,
       assignment_frequency=review.assignment_frequency,
       late_policy_rating=review.late_policy_rating,
       attendance_policy_rating=review.attendance_policy_rating,
       teaching_pace=review.teaching_pace,
       comment=review.comment
   )
   db.add(db_review)
   db.commit()
   db.refresh(db_review)
   return db_review

@app.post("/professors/{name}/bookmark")
def bookmark_professor(name: str, bookmark: BookmarkSchema, db: Session = Depends(get_db)):
    db_bookmark = models.Bookmark(
        professor_name=name,
        school=bookmark.school
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return{"message": f"{name} has been bookmarked!"}

@app.get("/bookmarks")
def get_bookmarks(db: Session = Depends(get_db)):
    bookmarks = db.query(models.Bookmark).all()
    return bookmarks
