from sqlalchemy import Column, Integer, String, Text, DateTime
from enum import Enum
from sqlalchemy import Enum as EnumSQL

from .base import Base

class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class MBTIEnum(Enum):
    ISTJ = "ISTJ"
    ISFJ = "ISFJ"
    INFJ = "INFJ"
    INTJ = "INTJ"
    ISTP = "ISTP"
    ISFP = "ISFP"
    INFP = "INFP"
    INTP = "INTP"
    ESTP = "ESTP"
    ESFP = "ESFP"
    ENFP = "ENFP"
    ENTP = "ENTP"
    ESTJ = "ESTJ"
    ESFJ = "ESFJ"
    ENFJ = "ENFJ"
    ENTJ = "ENTJ"

class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True)
    area = Column(String, nullable=False)
    birthday = Column(DateTime, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(EnumSQL(GenderEnum), nullable=False)
    mbti = Column(EnumSQL(MBTIEnum), nullable=False)
    mobileNumber = Column(String, nullable=False)
    name = Column(String, nullable=False)
    postCode = Column(String, nullable=False)

#위는 Question의 모델입니다 위를 고려하여 create_question을 다시 작성해주세요