import os
import sys
import textwrap
import requests
from bs4 import BeautifulSoup

from utils.cookies import COOKIES

if __name__ == '__main__':
    PROBLEM_URL = 'https://adventofcode.com/{}/day/{}'
    DATA_LOAD = '''\ndata = open('data.txt', 'r')\n'''
    advent_year, problem_number = sys.argv[1:]
    problem_path = os.path.join(os.path.dirname(__file__), 'problems', str(advent_year), str(problem_number))
    response = requests.get(PROBLEM_URL.format(advent_year, problem_number), cookies=COOKIES)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        with open(os.path.join(problem_path, 'main.py'), 'w+') as problem_file:
            for element in soup.find('article', attrs={'class': 'day-desc'}):
                for line in element.get_text().splitlines():
                    for line in textwrap.wrap(line):
                        problem_file.write(f'# {line}\n')
            problem_file.write(DATA_LOAD)