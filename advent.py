import argparse
import requests

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
        pass


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
