from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, voucher

app = FastAPI()

# 商品リストのデータ
vouchers = [
    {"ID": "FESG", "NAME": "FE/SG受験バウチャー", "DATE": "2024/06/20"},
    {"ID": "OR00", "NAME": "Oracle認定資格ピアソンVUE 配信監督なし試験用", "DATE": "2023/12/25"}
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/list")
def get_voucher_list(token:str , db:Session = Depends(get_db)):
    vouchers = db.query(voucher).all()
    return vouchers

@app.get("/{ID}")
def get_voucher_item(ID:str,token:str):
    voucher = db.query(voucher).filter(voucher)

    if Varchar:
        return {"voucher_id": Varchar.voucher_id,"voucher_name": Varchar.voucher_id,"voucher_date":Varchar.voucher_date}
    else:
        return HTTPException(status_code=484,datail="そんな資格はないよ")

@app.post("/add")
def add_voucher_item(ID:str,NAME:str,DATE:str,token:str,db: Session = Depends(get_db)):
    new_voucher = Varchar(voucher_id=ID, voucher_name=NAME,voucher_date=DATE)
    if new_voucher == "":
        return {"message":  "空なのでエラー"}
    else:
        db.add(new_voucher)
        db.commit()
        db.refresh(new_voucher)
        return {"message": "voucher was added successfully", "voucher": {"voucher_id": new_voucher.voucher_id ,"voucher_name" :new_voucher.voucher_name, "voucher_date": new_voucher.voucher_date}}
