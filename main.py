# File: main.py
# Author: Alec Grace
# Created on: 7 Feb 2022
# Purpose:
#   driver for CS360 Project 1: Solving Rush Hour
import heap
from os.path import exists
from functions import *
from time import perf_counter


def main():
    # get valid file from the user for the board
    board_file = None
    while board_file is None:
        board_file = input('Enter board file name: ')
        if not exists(board_file):
            print("File does not exist.")
            print("Please input a valid file.")
            board_file = None

    # read test board into cars dict
    with open(board_file, 'r') as file:
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

    # set clock to time the length of my A* algorithm and call the algorithm
    t1_start = perf_counter()
    solution = a_star(cars, test_list, goal_car_id)
    t2_stop = perf_counter()
    total = t2_stop - t1_start
    print('Total time = %d seconds' % total)

    # write solution to file in a format compatible with visualize.py
    with open('my_solution.sol', 'w') as outfile:
        for pair in solution:
            outfile.write(str(pair[0]) + ',' + str(pair[1]) + '\n')
    outfile.close()
    print(solution)


# function to implement A* algorithm
# keeps priority queue of [f(n), current move to get to the state,
# list of moves to get to that state from the beginning]
# sorted by min heap on f(n)
# inputs: dictionary of cars and their information in initial state,
#       list of lists representing where the cars are in the initial state,
#       string of the car id number
# output: list of tuples describing the shortest solution to the rush-hour puzzle
#      each tuple is a (car id, move magnitude) pair
def a_star(cars: dict, initial_state: list, goal_car: str):
    visited = []
    prior_queue = heap.Heap()
    cost = 0
    current_state = deepcopy(initial_state)
    prior_queue.add([f(cost, calculate_heuristic(current_state, goal_car)), (), []])
    goal_state = False
    # write-up information collection
    expanded_nodes = 0
    while not goal_state:
        # empty cars dictionary and take the next state with the shortest path off the queue
        current_cars = {}
        current_node = prior_queue.pop()
        expanded_nodes += 1
        current_cars, current_state = (move_cars(cars, current_node[2], initial_state)[i]
                                       for i in range(2))
        if current_state in visited:
            continue
        else:
            # if the current state hasn't already been evaluated, add it to visited list
            visited.append(current_state)
            cost = len(current_node[2])
            # expand the state by adding each state that is possible to reach from current state to the queue
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
            print('Expanded nodes: %d' % expanded_nodes)
            print('Length of path: %d' % len(current_node[2]))
            return current_node[2]


if __name__ == '__main__':
    main()
