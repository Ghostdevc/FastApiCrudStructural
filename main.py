from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class course():
    def __init__(self, course_id: int, course_title: str, course_instructor: str, course_rating: int, course_published_date: int):
        self.course_id = course_id
        self.course_title = course_title
        self.course_instructor = course_instructor
        self.course_rating = course_rating
        self.course_published_date = course_published_date
    
courses_db = [
    course(1, "Python for Beginners", "John Doe", 4, 2020),
    course(2, "Advanced Python", "Jane Smith", 5, 2021),
    course(3, "Data Science with Python", "Alice Johnson", 3, 2019),
    course(4, "Machine Learning", "Bob Brown", 4, 2022),
    course(5, "Web Development with Flask", "Charlie Davis", 5, 2023),
    course(6, "JavaScript Basics", "David Wilson", 4, 2020),
    course(7, "React for Beginners", "Eva Green", 5, 2021),
    course(8, "Node.js and Express", "Frank Harris", 3, 2019),
    course(9, "Full Stack Development", "Grace Lee", 4, 2022),
    course(10, "Django for Beginners", "Hannah Kim", 5, 2023),
]

@app.get("/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db