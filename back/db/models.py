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
    user = relationship('DbUser')
    product_id = Column(Integer, ForeignKey('cpu_item.id'))
    price = Column(String)
    name = Column(String)

    
class DbCpuItem(Base):
    __tablename__ = 'cpu_item'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    core = Column(String)
    cpu_clock = Column(String)
    socket = Column(String)
    threads = Column(String)
    tdp = Column(String)
    nm = Column(String)
    price = Column(String)
    cpu_image = Column(String)


















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