from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, exam

app = FastAPI()

# 資格リストのデータ
Exams = [
    {"ID": "FE00", "NAME": "基本情報技術者試験"},
    {"ID": "OR00", "NAME": "Java SE Bronze"}
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/list")
def get_exam_list(token:str, db: Session = Depends(get_db)):
    exams = db.query(Exam).all()
    return exams

@app.get("/{ID}")
def get_exam_item(ID:str,token:str):
    exam = db.query(Exam).filler(Exam.exam_id == ID).first()
    if exam:
        return {"exam_id": exam.exam_id, "exam_name": exam.exam_name}
    else:
        raise HTTPException(status_code=404, detail="そんな試験あるわけないだろ")

@app.post("/add")
def add_exam_item(ID:str,NAME:str,token:str,db: Session=Depends(get_db)):
    new_exam = Exam(exam_id = ID, exam_name=NAME)
    if new_exam == "":
        return {"message":"空なのでエラー"}
    else:
        db.add(new_exam)
        db.comit()
        db.refresh(new_exam)
        return {"message": "Exam added successfully", 
        "exam": {"exam_id":new_exam.exam_id,"exam_name":new_exam.exam_name}}
    