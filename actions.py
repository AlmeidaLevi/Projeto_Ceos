from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas


def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.id == skill_id).first()


def get_skill_by_name(db: Session, skill_name: str):
    return db.query(models.Skill).filter(models.Skill.skill_name == skill_name).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()


def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(
        skill_name=skill.skill_name,
        description=skill.description
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def update_skill_name(db: Session, db_skill: schemas.SkillCreate, new_skill_name: str):
    skill = db_skill
    skill.skill_name = new_skill_name
    db.add(skill)
    db.commit()
    return skill


def update_skill_description(db: Session, db_skill: schemas.SkillCreate, new_skill_description: str):
    skill = db_skill
    skill.description = new_skill_description
    db.add(skill)
    db.commit()
    return skill


def delete_skill(db: Session, skill_id: int):
    skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"Result": "Skill deleted successfully"}
