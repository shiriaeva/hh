from pydantic import BaseModel
from sqlalchemy import DateTime


class VacancyBase(BaseModel):
    name: str
    location: str
    company: str
    salary_int: int
    url: str = None


class StatisticsBase(BaseModel):
    name: str
    vacancies_num: int
    average_salary: str
    median_salary: str
    demand_in_cities: str
    demand_for_skills: str


class VacancyCreate(VacancyBase):
    date: str


class Vacancy(VacancyBase):
    id: int

    class Config:
        orm_mode = True


class Statistics(StatisticsBase):
    id: int

    class Config:
        orm_mode = True


class VacancyUpdate(BaseModel):
    name: str
    location: str
    company: str
    salary_int: int
    url: str = None

    class Config:
        orm_mode = True