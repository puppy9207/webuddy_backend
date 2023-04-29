from fastapi import APIRouter, Depends
from app.db.schemas import Member
from app.db import crud
from app.db import base

from sqlalchemy.orm import Session

router = APIRouter()

@router.get("", tags=["common"],
summary="router 분리 테스트",
response_description="서버가 리턴하는 인사양식")
async def common_test():
    #TODO router내 로직은 Service폴더로 이동한다.
    # router는 router기능일 뿐 -> router의 기능은 서비스 로직으로 분리하는 게 유지보수에 좋음
    return ''

@router.get("/list", response_model=list[Member])
def member_list(db: Session = Depends(base.get_db)):
    _member_list = crud.get_member_list(db)
    return _member_list

@router.post("/create", response_model=Member)
def member_create(member: Member, db: Session = Depends(base.get_db)):
    created_member = crud.create_member(db, member)
    return created_member