from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    location = Column(String)
    company = Column(String)
    salary_int = Column(Integer)
    url = Column(String)
    date = Column(DateTime)

    def __repr__(self):
        return f"{self.name} | {self.salary}"


class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    date = Column(DateTime)
    vacancies_num = Column(Integer)
    average_salary = Column(String(64))
    median_salary = Column(String(64))
    demand_in_cities = Column(String)
    demand_for_skills = Column(String)

    def __repr__(self):
        return f"{self.name} | {self.average_salary}"

