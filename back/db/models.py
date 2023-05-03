from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class DbUserCart(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    product_id = Column(Integer, ForeignKey('items.id'))

    
class DbItem(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(String)
    name = Column(String)
    param1 = Column(String)
    param2 = Column(String)
    param3 = Column(String)
    param4 = Column(String)
    param5 = Column(String)
    param6 = Column(String)
    param7 = Column(String)
    price = Column(String)
    image = Column(String)


















#works somehow

# class DbUser(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     email = Column(String)
#     password = Column(String)


# class DbUserCart(Base):
#     __tablename__ = 'cart_items'
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship('DbUser')
#     product_id = Column(Integer, ForeignKey('cpu_item.id'))
#     price = Column(String, ForeignKey('cpu_item.price'))
#     product = relationship('DbCpuItem', foreign_keys=[price])

    
# class DbCpuItem(Base):
#     __tablename__ = 'cpu_item'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     core = Column(String)
#     cpu_clock = Column(String)
#     socket = Column(String)
#     threads = Column(String)
#     tdp = Column(String)
#     nm = Column(String)
#     price = Column(String)
#     cpu_image = Column(String)