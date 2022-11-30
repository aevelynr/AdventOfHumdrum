import os
import argparse
import requests
import importlib
import textwrap
from bs4 import BeautifulSoup
from utils.cookies import COOKIES


ADVENT_OF_CODE_YEAR = 2021
PROBLEM_URL = 'https://adventofcode.com/{}/day/{}'
DATA_URL = 'https://adventofcode.com/{}/day/{}/input'

MAIN_FUNCTION = '''
def main():
    print('Problem {} Main Function')

'''


def run(num):
    '''
    The run function will execute one of the problem scripts.
    :param num:
    :return:
    '''
    importlib.import_module(f'problems.problem_{num}').main()


def download(num):
    '''
    Will go to adventofcode.com and get the puzzle input
    and then save it into a file.
    :param num:
    :return:
    '''
    response = requests.get(DATA_URL.format(ADVENT_OF_CODE_YEAR, num), cookies=COOKIES)

    if response.ok:
        data_path = os.path.join(os.path.curdir, 'data', f'day_{num}.txt')
        with open(data_path, 'wb+') as data_file:
            data_file.write(response.content)


def setup(num):
    '''
    Create a new problem script including the problem description from
    adventofcode.com as well as the data file already imported and opened.
    :param num:
    :return:
    '''
    problem_path = os.path.join(os.path.curdir, 'problems', f'day_{num}.py')
    if os.path.isfile(problem_path):
        pass

    response = requests.get(PROBLEM_URL.format(ADVENT_OF_CODE_YEAR, num), cookies=COOKIES)

    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        problem_desc = soup.find('article', attrs={'class': 'day-desc'}).text
        with open(problem_path, 'w+') as problem_file:
            for line in problem_desc.splitlines():
                for line in textwrap.wrap(line):
                    problem_file.write(f'# {line}\n')

            problem_file.write(MAIN_FUNCTION.format(num))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='AdventOfHumdrum',
        description='Advent of Code'
    )

    parser.add_argument('problem', type=int)
    parser.add_argument('-r', '--run', action='store_true', default=False)
    parser.add_argument('-d', '--download', action='store_true', default=False)
    parser.add_argument('-s', '--setup', action='store_true', default=False)

    args = parser.parse_args()

    if args.run:
        run(args.problem)
    elif args.download:
        download(args.problem)
    elif args.setup:
        setup(args.problem)
