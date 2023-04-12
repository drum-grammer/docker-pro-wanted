from sqlalchemy.orm import Session
import models, schemas

# stock table insert
def create_stock(db : Session, stock : schemas.Stock):
    db_stock = models.Stock(
        ls_cd = stock.ls_cd,
        ls_dt = stock.ls_dt,
        barcode = stock.barcode,
        ex_dt = stock.ex_dt,
        ls_ct = stock.ls_ct
        )
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def get_stock_by_id(db:Session, ls_cd : str):
    return db.query(models.Stock).filter(models.Stock.ls_cd == ls_cd).first()

# stock table select
def get_stocks(db : Session, period_front: str, period_back:str):
    return db.query(models.Stock).filter(models.Stock.ls_dt.between(period_front, period_back)).order_by(models.Stock.ls_dt).all()


# item table insert
def create_item(db : Session, item : schemas.Item):
    db_item = models.Item(
        item_cd = item.item_cd,
        item_nm = item.item_nm,
        item_cat_nm = item.item_cat_nm,
        item_maker = item.item_maker
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# item table select
def get_items(db : Session, item_cd:str):
    if item_cd == None:
        return db.query(models.Item).all()
    else:
        return db.query(models.Item).filter(models.Item.item_cd == item_cd).all()

def get_ex_date(db : Session, today:str, ex_date : str):
    return db.query(models.Stock).filter(models.Stock.ex_dt.between(today, ex_date)).order_by(models.Stock.ex_dt).all()

def create_deliver(db : Session, deliver : schemas.Deliver):
    db_deliver = models.Deliver(
        ld_cd = deliver.ld_cd,
        ld_dt = deliver.ld_dt,
        barcode = deliver.barcode,
        ex_dt = deliver.ex_dt,
        ld_ct = deliver.ld_ct
        )
    db.add(db_deliver)
    db.commit()
    db.refresh(db_deliver)
    return db_deliver

def get_deliver_by_id(db:Session, ld_cd : str):
    return db.query(models.Deliver).filter(models.Deliver.ld_cd == ld_cd).first()

def get_delivers(db : Session, period_front: str, period_back:str):
    return db.query(models.Deliver).filter(models.Deliver.ld_dt.between(period_front, period_back)).order_by(models.Deliver.ld_dt).all()

