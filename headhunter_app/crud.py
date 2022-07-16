from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas


def get_vacancy(db: Session, vacancy_id: int):
    return db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()


def get_vacancy_by_name(db: Session, name: str):
    return db.query(models.Vacancy).filter(
        models.Vacancy.name == name
    ).order_by(models.Vacancy.date).desc().first()


def get_vacancies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vacancy).offset(skip).limit(limit).all()


def create_vacancy(db: Session, vacancy: schemas.VacancyCreate):
    dt = datetime.now()
    db_vacancy = models.Vacancy(
        name=vacancy.name,
        location=vacancy.location,
        company=vacancy.company,
        salary_int=vacancy.salary_int,
        url=vacancy.url,
        datetime=dt
    )
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy


def update_vacancy_details(vacancy_id: int, db: Session, details: schemas.VacancyUpdate):
    db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).update(vars(details))
    db.commit()
    return db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()


def delete_vacancy(vacancy_id: int, db: Session):
    try:
        db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

