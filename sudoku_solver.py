#!/usr/bin/env python

from builtins import range

import argparse
import sys

try:
    import itertools.izip as zip
except ImportError:
    pass


# get characters from a file-like object f
def sudoku_chars(f):
    for line in f:
        for char in line:
            try:
                yield set([int(char)])
            except ValueError:
                if char == u'.': yield set(range(1,10))


# get all the chars as an array from infile
def read_input(f):
    chars = sudoku_chars(f)
    return list(next(chars) for n in range(81))


_square_indexes = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
        [3, 4, 5, 12, 13, 14, 21, 22, 23],
        [6, 7, 8, 15, 16, 17, 24, 25, 26],
        [0+27, 1+27, 2+27, 9+27, 10+27, 11+27, 18+27, 19+27, 20+27],
        [3+27, 4+27, 5+27, 12+27, 13+27, 14+27, 21+27, 22+27, 23+27],
        [6+27, 7+27, 8+27, 15+27, 16+27, 17+27, 24+27, 25+27, 26+27],
        [0+27+27, 1+27+27, 2+27+27, 9+27+27, 10+27+27, 11+27+27, 18+27+27, 19+27+27, 20+27+27],
        [3+27+27, 4+27+27, 5+27+27, 12+27+27, 13+27+27, 14+27+27, 21+27+27, 22+27+27, 23+27+27],
        [6+27+27, 7+27+27, 8+27+27, 15+27+27, 16+27+27, 17+27+27, 24+27+27, 25+27+27, 26+27+27]]


# get a row from a flat puzzle array
def row(puzzle, x):
    indexes = (x*9 + n for n in range(9))
    return list(puzzle[i] for i in indexes)


# get a column from a flat puzzle array
def col(puzzle, x):
    indexes = (n*9 + x for n in range(9))
    return list(puzzle[i] for i in indexes)


# 0|1|2
# -----
# 3|4|5
# -----
# 6|7|8
# return a single square
def square(puzzle, x):
    return list(puzzle[i] for i in _square_indexes[x])


def trim(row):
    known_items = [list(x)[0] for x in row if len(list(x)) == 1]
    for i in row:
        for item in known_items:
            if len(list(i)) == 1: continue
            try:
                i.remove(item)
            except KeyError:
                pass


def pretty_print_sudoku(puzzle):
    return '''
 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}

 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}

 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}
 {} {} {}   {} {} {}   {} {} {}
'''.format(*(list(x)[0] for x in puzzle))


def main():
    parser = argparse.ArgumentParser(description='Solve some sudoku',
            epilog='''Each input file must contain exactly 81 input digits.
            Use a dot (".") to represent unknown digits. All other characters
            are ignored.''')
    parser.add_argument('files', metavar='file', type=argparse.FileType('r'),
            help='a file contining a sudoku puzzle (default: read from stdin)',
            nargs='*', default=[sys.stdin])
    args = parser.parse_args()

    for puzzle_file in args.files:
        puzzle = read_input(puzzle_file)
        while any(len(x) > 1 for x in puzzle):
            for i in range(9):
                trim(row(puzzle, i))
                trim(col(puzzle, i))
                trim(square(puzzle, i))
        print(pretty_print_sudoku(puzzle))


if __name__ == '__main__':
    main()

