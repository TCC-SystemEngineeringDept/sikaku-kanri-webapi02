from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, voucherType
app = FastAPI()

# 商品リストのデータ
voucherTypes = [
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
def get_voucherType_list(token:str , db:Session = Depends(get_db)):
    voucherTypes = db.query(VoucherType).all()
    return voucherType

@app.get("/{ID}")
def get_voucherType_item(ID:str,token:str):
    VoucherType = db.query(VoucherType).filter(VoucherType)

    if Varchar:
        return {"voucher_id": VoucherType.voucher_id,"voucher_name": VoucherType.voucher_name}
    else:
        return HTTPException(status_code=484,datail="そんな資格はないよ")

@app.post("/add")
def add_voucher_item(ID:str,NAME:str,DATE:str,token:str,db: Session = Depends(get_db)):
    new_voucherType = VoucherType(voucher_id=ID, voucher_name=NAME)
    if new_voucherType == "":
        return {"message":  "空なのでエラー"}
    else:
        db.add(new_voucherType)
        db.commit()
        db.refresh(new_voucherType)
        return {"message": "voucher was added successfully", "voucher": {"voucher_id": new_voucherType.voucher_id ,"voucher_name" :new_voucherType.voucher_name}}
