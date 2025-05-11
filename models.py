from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


class Skill(Base):
    __tablename__ = "Skill"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    skill_name = Column(String, unique=True, index=True)
    description = Column(String)
