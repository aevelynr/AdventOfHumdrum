import os
import argparse
import requests

DATA_URL = 'https://adventofcode.com/{}/day/{}/input'

if __name__ == "__main__":
    ADVENT_OF_CODE_YEAR = 2021
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
        pass


    def download(problem):
        '''
        Will go to adventofcode.com and get the puzzle input
        and then save it into a file.
        :param problem:
        :return:
        '''
        cookies = {
            'session': '53616c7465645f5f132cad5af280798cda1c1bfd5d3df3c4c25cb4a57b3cba00d7338e6dab18b6b158385945bb10cc78e113f60773defb657986ce10bfe6f4eb'}
        #response = requests.get('https://adventofcode.com/2021/day/1/input', cookies=cookies)
        response = requests.get(DATA_URL.format(ADVENT_OF_CODE_YEAR, problem), cookies=cookies)

        if response.ok:
            data_path = os.path.join(os.path.curdir, 'data', f'day_{problem}.txt')
            if not os.path.isfile(data_path):
                with open(data_path, 'w+') as data_file:
                    data_file.write(response.text)


    def setup(problem):
        '''
        Create a new problem script including the problem description from
        adventofcode.com as well as the data file already imported and opened.
        :param problem:
        :return:
        '''
        pass

    if args.run:
        run(args.problem)
    elif args.download:
        download(args.problem)
    elif args.setup:
        setup(args.problem)
