from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, sikaku

app = FastAPI()

# 商品リストのデータ
vouchers = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー", "DATE": "2024/06/20"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用", "DATE": "2023/12/25"}
]


@app.get("/list")
def get_passed_list(token:"str"):
    if ID == "FF00":
        return Passed 

@app.get("/{ID}") 
def get_passed_item(ID:str,token:str):
    if ID == "FF00"
        return Passed[0]
    elif ID == "0R00":
        return Passed[1]
    else:
        return {}
    
@app.post("/add")
def add_passed_item(ID:str,DATE:str,token:str):
    return {"message": "Passed was added succesfuly",
     "Passed" : {{"ID":"FE00", "DATE": "2022/06/18"},}}

