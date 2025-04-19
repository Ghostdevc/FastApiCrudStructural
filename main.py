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

class CourseRequest(BaseModel):
    course_id: Optional[int] = Field(..., title="The ID of the course", ge=1)
    course_title: str = Field(..., title="The title of the course", max_length=100)
    course_instructor: str = Field(..., title="The instructor of the course", max_length=100)
    course_rating: int = Field(..., title="The rating of the course", ge=0, le=5)
    course_published_date: int = Field(..., title="The published date of the course", ge=1900, le=2025)

    model_config = {
        "json_schema_extra": {
            "example": {
                "course_id": 1,
                "course_title": "Python for Beginners",
                "course_instructor": "John Doe",
                "course_rating": 4,
                "course_published_date": 2020
            }
        }
    }

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

@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course_by_id(course_id: int = Path(gt=0, title="The ID of the course to retrieve")):
    for course in courses_db:
        if course.course_id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

@app.get("/courses/byrating/", status_code=status.HTTP_200_OK)
async def get_course_by_rating_by_query(rating: Optional[int] = Query(None, ge=0, le=5)):
    if rating is None:
        return courses_db
    filtered_courses = [course for course in courses_db if course.course_rating == rating]
    if not filtered_courses:
        raise HTTPException(status_code=404, detail="No courses found with the given rating")
    return filtered_courses

@app.get("/courses/bypublisheddate/", status_code=status.HTTP_200_OK)
async def get_course_by_published_date_by_query(published_date: Optional[int] = Query(None, ge=1900, le=2025)):
    if published_date is None:
        return courses_db
    filtered_courses = [course for course in courses_db if course.course_published_date == published_date]
    if not filtered_courses:
        raise HTTPException(status_code=404, detail="No courses found with the given published date")
    return filtered_courses

@app.post("/create_course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = course(**course_request.model_dump())
    courses_db.append(find_course_id(new_course))
    return new_course

def find_course_id(course: course):
    course.course_id = 1 if len(courses_db) == 0 else courses_db[-1].course_id + 1
    return course

@app.put("/courses/update_course", status_code=status.HTTP_200_OK)
async def update_course(course_request: CourseRequest):
    course_updated = False
    for i in range(len(courses_db)):
        if courses_db[i].course_id == course_request.course_id:
            courses_db[i] = course(**course_request.model_dump())
            course_updated = True
            break
        if not course_updated:
            raise HTTPException(status_code=404, detail="Course not found")
    return courses_db[i]

@app.delete("/courses/delete_course/{course_id}", status_code=status.HTTP_200_OK)
async def delete_course(course_id: int = Path(gt=0, title="The ID of the course to delete")):
    for i in range(len(courses_db)):
        if courses_db[i].course_id == course_id:
            deleted_course = courses_db.pop(i)
            return deleted_course
    raise HTTPException(status_code=404, detail="Course not found")