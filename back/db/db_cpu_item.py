from routers.schemas import CpuItemBase
from sqlalchemy.orm import Session
from db.models import DbCpuItem
from fastapi import HTTPException, status


def create_cpu(db: Session, request: CpuItemBase):
    new_cpu = DbCpuItem(
        name = request.name,
        core = request.core,
        cpu_clock = request.cpu_clock,
        socket = request.socket,
        threads = request.threads,
        tdp = request.tdp,
        nm = request.nm,
        price = request.price
    )
    db.add(new_cpu)
    db.commit()
    db.refresh(new_cpu)
    return new_cpu



def get_all_cpu(db: Session):
    return db.query(DbCpuItem).all()


def delete(db: Session, id: int):
    cpu = db.query(DbCpuItem).filter(DbCpuItem.id == id).first()
    if not cpu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Cpu with id {id} not found')
    db.delete(cpu)
    db.commit()
    return 'okay'