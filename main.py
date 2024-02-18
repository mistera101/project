from fastapi import FastAPI

app = FastAPI()

# Define route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Student resource
students = {
    1: {"id": 1, "name": "Ajayi Gbadebo", "age": 30, "sex": "male", "height": 6.2},
    2: {"id": 2, "name": "Jesutofunmi Ajayi", "age": 29, "sex": "female", "height": 5.5},
}

# Endpoint to retrieve all students
@app.get("/students/")
def get_students():
    return list(students.values())

# Endpoint to retrieve a specific student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id)

# Endpoint to create a new student
@app.post("/students/")
def create_student(student: dict):
    new_id = max(students.keys()) + 1
    student["id"] = new_id
    students[new_id] = student
    return student

# Endpoint to update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: dict):
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id].update(student_update)
    return students[student_id]

# Endpoint to delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    deleted_student = students.pop(student_id)
    return deleted_student
