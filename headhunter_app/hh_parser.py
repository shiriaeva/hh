from pydantic import json

from transfer_to_bd import *
import re
import statistics
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session


headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
salaries = []
cities = {}
skills = {}


def extract_max_page(skill):
    URL = F'https://hh.ru/search/vacancy?text={skill}'
    hh_request = requests.get(URL, headers=headers)

    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    pages = []

    paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

    for page in paginator:
        pages.append(int(page.find('a').text))

    return pages[-1]


def extract_salary(salary):
    if salary is None:
        return None
    else:
        salary = salary.text
        if "–" in salary:
            salary = re.split('\D+', salary)
            try:
                return int(salary[0] + salary[1])
            except ValueError:
                return None
        salary = salary.split()
        try:
            return int(salary[1] + salary[2])
        except ValueError:
            return None


def extract_job(html):
    title = html.find('a').text
    # link = html.find('a')['href']

    url = html.find('a',
                    {'data-qa': 'vacancy-serp__vacancy-title'})['href']

    salary = html.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
    salary = extract_salary(salary)
    if salary is not None:
        salaries.append(salary)

    company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text
    company = "".join(company.split())

    location = html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})
    if location is None:
        location = 'No type'
    else:
        location = location.text
    location = location.partition(',')[0]
    upgrade_the_statistic_dict(location, cities)

    return {'title': title, 'company': company, 'location': location, 'salary': salary, 'url': url}


def extract_hh_jobs(last_page, skill):
    jobs = []
    URL = F'https://hh.ru/search/vacancy?text={skill}'
    session = Session(bind=Create_db())

    for page in range(last_page):
        print(f'Парсинг страницы {page}')
        result = requests.get(f'{URL}&page={page}', headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'vacancy-serp-item'})

        for result in results:
            job = extract_job(result)
            extract_key_skills(job['url'])
            Bd_Transfer(job['title'], job['salary'], job['location'], job['company'], job['url'], session)
            jobs.append(job)

    Bd_Transfer_stats(skill, len(jobs), str(sum(salaries)/len(salaries)),
                      str(statistics.median(salaries)), get_the_sorted_dict_with(cities, 6),
                      get_the_sorted_dict_with(skills, 10), session)

    return jobs


def extract_key_skills(url):
    result = requests.get(f'{url}', headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('span',
                            {'data-qa': 'bloko-tag__text'})
    for value in results:
        upgrade_the_statistic_dict(value.text, skills)


def upgrade_the_statistic_dict(key, dictionary):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def get_the_sorted_dict_with(smth_dict, howmuch=3):
    sorted_values = list(sorted(smth_dict.values(),
                                reverse=True))[:howmuch]
    sorted_dict = {}

    for i in sorted_values:
        for k in smth_dict.keys():
            if smth_dict[k] == i:
                sorted_dict[k] = smth_dict[k]
                break

    return str(sorted_dict)


def get_jobs(skill):
    max_page = extract_max_page(skill)
    jobs = extract_hh_jobs(max_page, skill)
    return jobs

