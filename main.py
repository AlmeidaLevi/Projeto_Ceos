from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import actions
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/skills/", response_model=list[schemas.Skill])  # type: ignore
async def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = actions.get_skills(db, skip=skip, limit=limit)
    return skills


@app.get("/skills/{skill_id}", response_model=schemas.Skill)
async def read_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = actions.get_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill


@app.post("/skills/create", response_model=schemas.Skill)
async def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = actions.get_skill_by_name(db, skill_name=skill.skill_name)
    if db_skill:
        raise HTTPException(status_code=400, detail="Skill already registered")
    return actions.create_skill(db=db, skill=skill)


@app.put("/skills/update/name/{skill_id}", response_model=schemas.Skill)
async def update_skill_name(skill_id: int, new_skill_name: str, db: Session = Depends(get_db)):
    db_skill = actions.get_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    actions.update_skill_name(db, db_skill, new_skill_name)
    return db_skill


@app.put("/skills/update/description/{skill_id}", response_model=schemas.Skill)
async def update_skill_description(skill_id: int, new_skill_description: str, db: Session = Depends(get_db)):
    db_skill = actions.get_skill(db, skill_id=skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    actions.update_skill_description(db, db_skill, new_skill_description)
    return db_skill


@app.delete("/skills/delete/{skill_id}", response_model=dict)
async def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    result = actions.delete_skill(db, skill_id)
    return result
