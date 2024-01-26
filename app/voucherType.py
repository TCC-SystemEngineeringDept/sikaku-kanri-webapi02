from fastapi import FastAPI

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
        db.close():

@app.get("/list")
def get_voucherTyper_list(token:str Session = Depends(get_db)):
    voucherType = db.query(VoucherType).all()
    return voucherType

@app.get("/{ID}")
def get_voucherType_item(ID:str,token:str):
    Varchar = db.query(VoucherType).filter(Varchar)

    if Varchar:
        return {"voucherType_id": VoucherType.voucherType_id,"voucherType_name": VoucherType.voucherType_name}
    else:
        return HTTPException(status_code=484,datail="そんな資格はないよ")

@app.post("/add")
def add_voucher_item(ID:str,NAME:str,DATE:str,token:str,db: Session = Depends(get_db)):
    new_voucherType = VoucherType(voucherType_id=ID, voucherType_name=NAME)
    if new_voucherType == "":
        return {"message":  "空なのでエラー"}
else:
    db.add(new_voucherType)
    db.commit()
    db.refresh(new_voucherType)
	    return {"message": "voucher was added successfully", "voucher": {{"voucherType_id": new_voucherType.voucherType_id ,"voucherType_name" :new_voucherType.voucherType_name}}}
