# File: main.py
# Author: Alec Grace
# Created on: 7 Feb 2022
# Purpose:
#   driver for CS360 Project 1: Solving Rush Hour
from functions import *


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

    # read test board into cars dict
    with open('test.board', 'r') as file:
        first_line = True
        cars = {}
        board_dimensions = [0, 0]
        for line in file:
            line = line.rstrip('\n')
            if first_line:
                board_dimensions = line.split(',')
                first_line = False
                continue
            if line == '':
                break
            line = line.split(',')
            # key = carID
            # value = [x, y, length, bool horizontal, bool goal car]
            cars[line[0]] = [int(line[1]), int(line[2]), int(line[4]), (line[3] == 'H'), (line[5] == 'T')]
    file.close()

    # board represented with nested lists
    test_list = []
    for i in range(int(board_dimensions[0])):
        test_list.append([])
        for j in range(int(board_dimensions[1])):
            test_list[i].append(-1)

    # place cars on the board
    for car in cars:
        if cars[car][4]:
            goal_car_id = car
        x = cars[car][0]
        y = cars[car][1]
        length = cars[car][2]
        if cars[car][3]:
            for i in range(length):
                test_list[y][x + i] = car
        else:
            for i in range(length):
                test_list[y + i][x] = car

    # print out board for debugging
    for row in test_list:
        for column in row:
            print(column, end='\t')
        print()

    print(a_star(cars, test_list, goal_car_id))


def a_star(cars: dict, initial_state: list, goal_car: str):
    visited = []
    prior_queue = heap.Heap()
    cost = 0
    current_state = deepcopy(initial_state)
    prior_queue.add([f(cost, calculate_heuristic(current_state, goal_car)), (), []])
    goal_state = False
    while not goal_state:
        cost += 1
        current_cars = {}
        current_node = prior_queue.pop()
        if current_node[1] in visited:
            continue
        else:
            # TODO: cannot populate visited with (car, move) has to be board state... dummy
            visited.append(current_node[1])
            current_cars, current_state = (move_cars(cars, current_node[2], initial_state)[i]
                                           for i in range(2))
            for car in current_cars:
                for move in can_move(current_cars, car, current_state):
                    try:
                        new_state = move_car(current_cars, car, move, current_state)
                        path = deepcopy(current_node[2])
                        path.append((car, move))
                        prior_queue.add([f(cost, calculate_heuristic(new_state, goal_car)), (car, str(move)),
                                         path])
                    except TypeError:
                        continue
        if is_goal_state(current_state, current_cars, goal_car):
            return current_node[2].append(current_node[1])


if __name__ == '__main__':
    main()
