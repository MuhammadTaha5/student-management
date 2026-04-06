from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="db",
        database="studentdb",
        user="postgres",
        password="postgres"
    )

# MODEL
class Student(BaseModel):
    first_name: str
    last_name: str
    registration_number: str
    subjects: str
    cgpa: float

# FETCH STUDENT
@app.get("/student/{reg_no}")
def get_student(reg_no: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE registration_number=%s", (reg_no,))
    data = cur.fetchone()

    cur.close()
    conn.close()

    if data:
        return {
            "first_name": data[1],
            "last_name": data[2],
            "registration_number": data[3],
            "subjects": data[4],
            "cgpa": data[5]
        }
    return {"message": "Not found"}


# INSERT STUDENT
@app.post("/student")
def add_student(student: Student):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (first_name,last_name,registration_number,subjects,cgpa)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        student.first_name,
        student.last_name,
        student.registration_number,
        student.subjects,
        student.cgpa
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Student added successfully"}

from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("app/templates/search.html")

@app.get("/insert.html")
def insert_page():
    return FileResponse("app/templates/insert.html")

@app.get("/search.html")
def search_page():
    return FileResponse("app/templates/search.html")