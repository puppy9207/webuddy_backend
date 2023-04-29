import datetime
from app.db import models

from pydantic import BaseModel


# id = Column(Integer, primary_key=True)
# area = Column(String, nullable=False)
# birthday = Column(DateTime, nullable=False)
# email = Column(String, nullable=False)
# gender = Column(EnumSQL(GenderEnum), nullable=False)
# mbti = Column(EnumSQL(MBTIEnum), nullable=False)
# mobileNumber = Column(String, nullable=False)
# name = Column(String, nullable=False)
# postCode = Column(String, nullable=False)
class Member(BaseModel):
    id: int
    area: str
    birthday: datetime.datetime
    email: str
    gender: models.GenderEnum
    mbti: models.MBTIEnum
    mobileNumber: str
    name: str
    postCode: str