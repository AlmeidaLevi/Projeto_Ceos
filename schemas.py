from pydantic import BaseModel


class SkillBase(BaseModel):
    skill_name: str


class SkillCreate(SkillBase):
    skill_name: str
    description: str


class Skill(SkillBase):
    id: int
    description: str


class Config:
    orm_mode = True
