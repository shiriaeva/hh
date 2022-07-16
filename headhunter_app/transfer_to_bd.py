from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from models import Vacancy, Statistics

Base = declarative_base()


def Create_db():
    engine = create_engine("sqlite:///database.sqlite")
    Base.metadata.create_all(engine)
    return engine


def Bd_Transfer(title, salary_int, location, company, url, session):
    is_exist = session.query(Vacancy).filter(Vacancy.name == title).order_by(text('-Vacancy.date')).first()

    if not is_exist:
        session.add(
            Vacancy(name=title, date=datetime.now(), salary_int=salary_int,
                    location=location, company=company, url=url)
        )
        session.commit()
    else:
        if is_exist.salary_int != salary_int:
            session.add(
                Vacancy(name=title, date=datetime.now(), salary_int=salary_int,
                        location=location, company=company, url=url)
            )
            session.commit()


def Bd_Transfer_stats(title, vacancies_num, average_salary, median_salary,
                      demand_in_cities, demand_for_skills, session):
    is_exist = session.query(Statistics).filter(Statistics.name == title).order_by(text('-Statistics.date')).first()

    if not is_exist:
        session.add(
            Statistics(name=title, vacancies_num=vacancies_num, date=datetime.now(), average_salary=average_salary,
                       median_salary=median_salary, demand_in_cities=demand_in_cities,
                       demand_for_skills=demand_for_skills)
        )
        session.commit()
    else:
        if is_exist.vacancies_num != vacancies_num:
            session.add(
                Statistics(name=title, vacancies_num=vacancies_num, date=datetime.now(), average_salary=average_salary,
                           median_salary=median_salary, demand_in_cities=demand_in_cities,
                           demand_for_skills=demand_for_skills)
            )
            session.commit()

