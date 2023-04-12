from sqlalchemy import Column, Integer, String
from database import Base

class Stock(Base):
    '''
    입고일자, 유효기간, 바코드 번호, 수량
    '''
    
    __tablename__ = "stock"
    
    ls_cd = Column(String(20), primary_key=True) # datetime.today().strftime("%Y%m%d%H%M%S%f")
    ls_dt = Column(String(10))
    barcode = Column(String(13))
    ex_dt = Column(String(10))
    ls_ct = Column(Integer)
    
class Item(Base):
    __tablename__ = "item"
    
    item_cd = Column(String(13), primary_key=True) # =barcode
    item_nm = Column(String(100))
    item_cat_nm = Column(String(100))
    item_maker = Column(String(100))
    
class Deliver(Base):
    __tablename__ = "deliver"
    
    ld_cd = Column(String(20), primary_key=True) # datetime.today().strftime("%Y%m%d%H%M%S%f")
    ld_dt = Column(String(10))
    barcode = Column(String(13))
    ex_dt = Column(String(10))
    ld_ct = Column(Integer)
     
    
    