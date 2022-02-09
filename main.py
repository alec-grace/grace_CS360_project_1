# File: main.py
# Author: Alec Grace
# Created on: 7 Feb 2022
# Purpose:
#   driver for CS360 Project 1: Solving Rush Hour
from os.path import exists


def main():
    # board_file = None
    # solution_file = None
    # while board_file is None:
    #     board_file = input('Enter board file name: ')
    #     if not exists(board_file):
    #         print("File does not exist.")
    #         print("Please input a valid file.")
    #         board_file = None
    # while solution_file is None:
    #     solution_file = input('Enter solution file name: ')
    #     if not exists(solution_file):
    #         print("File does not exist.")
    #         print("Please input a valid file.")
    #         solution_file = None

    # represented with a dictionary
    test_board = {}
    for key in range(6):
        test_board[key] = []
        for i in range(6):
            test_board[key].append((i, 0))
    with open('test.board', 'r') as file:
        cars = {}
        first_line = True
        for line in file:
            line = line.rstrip('\n')
            if first_line:
                first_line = False
                continue
            if line == '':
                break
            line = line.split(',')
            # key = carID, value = [x, y, length, bool horizontal, bool goal car]
            cars[line[0]] = [line[1], line[2], line[4], (line[3] == 'H'), (line[5] == 'T')]
    file.close()
    for car in cars:
        print(car, cars[car])
        test_board[int(cars[car][0])][int(cars[car][1])] = car
    for key in test_board:
        print(str(key) + ': ', *test_board[key])



    # represented with nested lists
    test_list = []
    for i in range(6):
        test_list.append([])
        for j in range(6):
            test_list[i].append(-1)

    for car in cars:
        x = int(cars[car][0])
        y = int(cars[car][1])
        test_list[y][x] = car

    for row in test_list:
        print(*row)


if __name__ == '__main__':
    main()
