from pydantic import BaseModel


class VacancyBase(BaseModel):
    name: str
    location: str
    company: str
    salary_int: int
    url: str = None


class VacancyCreate(VacancyBase):
    date: str


class Vacancy(VacancyBase):
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