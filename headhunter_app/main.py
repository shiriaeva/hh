#from hh_parser import get_jobs
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from headhunter_app import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/vacancies/", response_model=schemas.Vacancy)
def create_vacancy(vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)):
    db_vacancy = crud.get_vacancy_by_name(db, name=vacancy.name)
    if db_vacancy and db_vacancy.salary_int == vacancy.salary_int:
        raise HTTPException(status_code=400, detail="Vacancy already exist")
    return crud.create_vacancy(db=db, vacancy=vacancy)


@app.get("/vacancies", response_model=List[schemas.Vacancy])
def read_vacancies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vacancies = crud.get_vacancies(db=db, skip=skip, limit=limit)
    return vacancies


@app.get("/vacancies/{vacancy_id}", response_model=schemas.Vacancy)
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    db_vacancy = crud.get_vacancy(db, vacancy_id=vacancy_id)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy


@app.get("/statistics", response_model=List[schemas.Statistics])
def read_statistics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stat = crud.get_statistics(db=db, skip=skip, limit=limit)
    return stat


@app.get("/statistics/{name}", response_model=schemas.Statistics)
def read_statistic(name: str, db: Session = Depends(get_db)):
    db_stat = crud.get_statistics_by_name(db, name=name)
    if db_stat is None:
        raise HTTPException(status_code=404, detail="Statistics not found")
    return db_stat


@app.put('/update_vacancy_details/{vacancy_id}', response_model=schemas.Vacancy)
def update_vacancy_details(vacancy_id: int, update_param: schemas.VacancyUpdate, db: Session = Depends(get_db)):
    is_exist = crud.get_vacancy(db=db, vacancy_id=vacancy_id)
    if not is_exist:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_vacancy_details(vacancy_id=vacancy_id, db=db, details=update_param)


@app.delete('/delete_vacancy_by_id/{vacancy_id}')
def delete_vacancy_by_id(vacancy_id: int, db: Session = Depends(get_db)):
    details = crud.get_vacancy(vacancy_id=vacancy_id, db=db)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_vacancy(vacancy_id=vacancy_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


#get_jobs(".net+framework")
#get_jobs("java")
#get_jobs("php")




