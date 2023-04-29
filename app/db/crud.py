from app.db.models import Member
from app.db import schemas
from sqlalchemy.orm import Session
from datetime import datetime


def get_member_list(db: Session):
    member_list = db.query(Member)\
        .order_by(Member.id.desc())\
        .all()
    return member_list

def create_member(db: Session, member: schemas.Member):
    # 새로운 질문 생성
    db_member = Member(subject=member.subject, content=member.content, create_date=datetime.now())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member