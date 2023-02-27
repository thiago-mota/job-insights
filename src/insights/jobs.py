from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        csv_file = csv.DictReader(file)
        jobs = []
        for job_data in csv_file:
            jobs.append(job_data)
    return(jobs)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_by_job_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_by_job_type.append(job)
    return filter_by_job_type
