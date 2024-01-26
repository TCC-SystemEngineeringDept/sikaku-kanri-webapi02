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
def get_sikaku_list(token:str Session = Depends(get_db)):
    sikaku = db.query(Sikaku).all()
    return sikaku

@app.get("/{ID}")
def get_sikaku_item(ID:str,token:str):
    sikaku = db.query(Sikaku).filter(Sikaku)

    if Sikaku:
        return {"sikaku_id": Sikaku.sikaku_id,"sikaku_name": Sikaku.sikaku_name}
    else:
        return HTTPException(status_code=484,datail="そんな資格はないよ")

@app.post("/add")
def add_sikaku_item(ID:str,NAME:str,token:str,db: Session = Depends(get_db)):
    new_sikaku = Sikaku(sikaku_id=ID, sikaku_name=NAME)
    if new_sikaku == "":
        return {"message":  "空なのでエラー"}
else:
    db.add(sikaku)
    db.commit()
    db.refresh(new_sikaku)
	    return {"message": "voucher was added successfully", "voucher": {{"voucher_id": new_voucher.voucher_id ,"voucher_name" :new_voucher.voucher_name, "voucher_date": new_voucher.voucher_date}}}
