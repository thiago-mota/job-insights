from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    jobs_salaries = []
    for job in data:
        if job["max_salary"].isdigit():
            jobs_salaries.append(int(job["max_salary"]))
    return max(jobs_salaries)


def get_min_salary(path: str) -> int:
    data = read(path)
    jobs_salaries = []
    for job in data:
        if job["min_salary"].isdigit():
            jobs_salaries.append(int(job["min_salary"]))
    return min(jobs_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        income_amount = salary
        min_salary = job['min_salary']
        max_salary = job['max_salary']
        salary_range = False

        if int(min_salary) > int(max_salary):
            raise ValueError('min_salary é maior que max_salary')
        elif int(min_salary) <= int(income_amount) <= int(max_salary):
            salary_range = True
        return salary_range
    except Exception:
        raise ValueError('Precisa ser um interger')



def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    
    jobs_on_salary_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_on_salary_range.append(job)
        except Exception:
            ValueError
    return jobs_on_salary_range