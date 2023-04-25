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
    __tablename__ = 'user_cart'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser')
    product_id = Column(Integer, ForeignKey('cpu_item.id'))
    product = relationship('DbCpuItem')


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