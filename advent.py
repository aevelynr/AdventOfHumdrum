import os
import argparse
import requests
from utils.cookies import COOKIES
import importlib
import bs4


ADVENT_OF_CODE_YEAR = 2021
DATA_URL = 'https://adventofcode.com/{}/day/{}/input'
SOUP_URL = 'https://adventofcode.com/{}/day/{}'

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

    def run(problem):
        '''
        The run function will execute one of the problem scripts.
        :param problem:
        :return:
        '''
        problem = importlib.import_module(f'problems.day_{problem}')
        problem.main()

    def download(problem):
        '''
        Will go to adventofcode.com and get the puzzle input
        and then save it into a file.
        :param problem:
        :return:
        '''
        response = requests.get(DATA_URL.format(ADVENT_OF_CODE_YEAR, problem), cookies=COOKIES)

        if response.ok:
            data_path = os.path.join(os.path.curdir, 'data', f'day_{problem}.txt')
            with open(data_path, 'wb+') as data_file:
                data_file.write(response.content)


    def setup(problem):
        '''
        Create a new problem script including the problem description from
        adventofcode.com as well as the data file already imported and opened.
        :param problem:
        :return:
        '''

        response = requests.get(SOUP_URL.format(ADVENT_OF_CODE_YEAR, problem), cookies=COOKIES)
        #print(response.text)
        if response.ok:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            boiled_soup = soup.find('article', attrs={'class': 'day-desc'})
            text_path = os.path.join(os.path.curdir, 'problems', f'day_{problem}.py')
            with open(text_path, 'w+') as text_file:
                for lines in boiled_soup.get_text().splitlines():
                    text_comment = '#' + lines + '\n'
                    text_file.write(text_comment)
                text_file.write(f"def main():\n    print('problem{problem}')")
    if args.run:
        run(args.problem)
    elif args.download:
        download(args.problem)
    elif args.setup:
        setup(args.problem)
