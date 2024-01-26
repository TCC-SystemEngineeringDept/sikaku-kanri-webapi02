from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースの設定
DB_USER = 'sikaku2'
DB_PASSWORD = 'Shikaku2'
DB_HOST = '192.168.54.231'
DB_NAME = 'sikaku2'

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String(4), index=True)
    item_name = Column(String(100), index=True)
    price = Column(Integer)

class exam(Base):
    __tablename__ = "exam"

    exam_id = Column(Integer, primary_key=True, index=True)
    exam_name = Column(String(30), index=True)


class sikaku(Base):
    __tablename__ = "sikaku"

    sikaku_id = Column(Integer, primary_key=True, index=True)
    sikaku_name = Column(String(50), index=True)
    sikaku_date = Column(DateTime)

class voucher(Base):
    __tablename__ = "voucher"

    voucher_id = Column(Integer, primary_key=True, index=True)
    voucher_name = Column(String(50), index=True)
    voucher_date = Column(DateTime)

class voucherType(Base):
    __tablename__ = "voucherType"

    voucherType_id = Column(Integer, primary_key=True, index=True)
    voucherType_name = Column(String(50), index=True)



# テーブルが存在しない場合は作成する
Base.metadata.create_all(bind=engine)
