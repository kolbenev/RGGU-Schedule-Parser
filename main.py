from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from conf import params, pars_time, url
from models import Raspis, engine, Base, session


def get_schedule(url: str, params: Dict) -> List[List[str]]:
    response = requests.post(url=url, data=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    schedule = [
        [cell.get_text(strip=True) for cell in row.find_all('td')]
        for row in rows if row.find_all('td')
    ]

    if schedule:
        return schedule
    else:
        raise ValueError('Расписание пустое.')

def add_in_db(new_line: Raspis):
    session.add(new_line)
    session.commit()


def main(params: Dict, pars_list: Dict, url: str):
    schedule: List[List[str]] = get_schedule(url, params)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session.commit()

    date = ''
    para = ''

    for line in schedule[1::]:
        if len(line) == 8:
            date = line[0]
            para = line[1]
        elif len(line) == 7:
            para = line[0]

        add_in_db(Raspis(
            date = date,
            para = para,
            lecture_time = pars_time[para],
            audience = line[-4],
            lesson = line[-3],
            type_lesson = line[-2],
            teacher_name = line[-1]
        ))


if __name__ == '__main__':
    main(params, pars_time, url)