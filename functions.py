# File: functions.py
# Author: Alec Grace
# Created on: 13 Feb 2022
# Purpose:
#   file for CS360 Project 1: Solving Rush Hour functions
from copy import deepcopy


# checks a specific move to see if that move is valid
# input: dictionary of cars w/ information, id of the car to move,
#   direction to move the car, current board_state
# output: true if move is legal/false if not
def valid_move(cars: dict, car_id: str, direction: int, board_state: list) -> bool:
    car_x = cars[car_id][0]
    car_y = cars[car_id][1]
    car_length = cars[car_id][2]
    # check if car is horizontal
    if cars[car_id][3]:
        if direction > 0:
            if car_x + car_length == len(board_state) or \
                    int(board_state[car_y][car_x + car_length]) >= 0:
                return False
        elif direction < 0:
            if car_x == 0 or int(board_state[car_y][car_x - 1]) >= 0:
                return False
    # check if car is vertical
    elif not cars[car_id][3]:
        if direction > 0:
            if car_y + car_length == len(board_state) or \
                    int(board_state[car_y + car_length][car_x]) >= 0:
                return False
        elif direction < 0:
            if car_y == 0 or int(board_state[car_y - 1][car_x]) >= 0:
                return False
    return True


# checks if a car can move in either direction
# input: dictionary of cars w/ information, id of car to move,
#   current board state
# output: list of magnitudes the car can move (only 1 and/or -1)
def can_move(cars: dict, car_id: str, board_state: list) -> list:
    return_list = []
    if valid_move(cars, car_id, -1, board_state):
        return_list.append(-1)
    if valid_move(cars, car_id, 1, board_state):
        return_list.append(1)
    return return_list


# moves a car on the given board
# input: dictionary of cars w/ information, id of car to move, magnitude of the move,
#   current board state
# output: new board after the car has moved
def move_car(cars: dict, car_id: str, direction: int, board_state: list) -> list:
    new_state = deepcopy(board_state)
    new_cars = deepcopy(cars)
    if not valid_move(new_cars, car_id, direction, new_state):
        return None
    car_x = new_cars[car_id][0]
    car_y = new_cars[car_id][1]
    car_length = new_cars[car_id][2]
    # horizontal moving forward 1
    if new_cars[car_id][3] and direction > 0:
        if new_state[car_y][car_x + car_length] == -1:
            new_state[car_y][car_x] = -1
            new_state[car_y][car_x + car_length] = car_id
            new_cars[car_id][0] = car_x + 1
        else:
            return None
    # horizontal moving backward 1
    elif new_cars[car_id][3] and direction < 0:
        if new_state[car_y][car_x - 1] == -1:
            new_state[car_y][car_x + car_length - 1] = -1
            new_state[car_y][car_x - 1] = car_id
            new_cars[car_id][0] = car_x - 1
        else:
            return None
    # vertical moving up 1
    elif not new_cars[car_id][3] and direction < 0:
        if new_state[car_y - 1][car_x] == -1:
            new_state[car_y + car_length - 1][car_x] = -1
            new_state[car_y - 1][car_x] = car_id
            new_cars[car_id][1] = car_y - 1
        else:
            return None
    # vertical moving down 1
    elif not new_cars[car_id][3] and direction > 0:
        if new_state[car_y + car_length][car_x] == -1:
            new_state[car_y][car_x] = -1
            new_state[car_y + car_length][car_x] = car_id
            new_cars[car_id][1] = car_y + 1
        else:
            return None
    return new_state


# moves cars in a sequence dictated by user
# input: dictionary of cars w/ information, list of (car_id, move direction) tuples,
#   current board state
# output: list with the updated cars dictionary and board state
def move_cars(cars: dict, car_direction: list, board_state: list) -> list:
    new_cars = deepcopy(cars)
    new_state = deepcopy(board_state)
    for pair in car_direction:
        car_x = new_cars[pair[0]][0]
        car_y = new_cars[pair[0]][1]
        car_length = new_cars[pair[0]][2]
        # horizontal moving forward 1
        if new_cars[pair[0]][3] and pair[1] > 0:
            if new_state[car_y][car_x + car_length] == -1:
                new_state[car_y][car_x] = -1
                new_state[car_y][car_x + car_length] = pair[0]
                new_cars[pair[0]][0] = car_x + 1
            else:
                return None
        # horizontal moving backward 1
        elif new_cars[pair[0]][3] and pair[1] < 0:
            if new_state[car_y][car_x - 1] == -1:
                new_state[car_y][car_x + car_length - 1] = -1
                new_state[car_y][car_x - 1] = pair[0]
                new_cars[pair[0]][0] = car_x - 1
            else:
                return None
        # vertical moving up 1
        elif not new_cars[pair[0]][3] and pair[1] < 0:
            if new_state[car_y - 1][car_x] == -1:
                new_state[car_y + car_length - 1][car_x] = -1
                new_state[car_y - 1][car_x] = pair[0]
                new_cars[pair[0]][1] = car_y - 1
            else:
                return None
        # vertical moving down 1
        elif not new_cars[pair[0]][3] and pair[1] > 0:
            if new_state[car_y + car_length][car_x] == -1:
                new_state[car_y][car_x] = -1
                new_state[car_y + car_length][car_x] = pair[0]
                new_cars[pair[0]][1] = car_y + 1
            else:
                return None
    return [new_cars, new_state]


# calculate the heuristic for a given state
# input: current state, id of goal car
# output: heuristic value
def calculate_heuristic(state: list, goal_car_id: str) -> float:
    goal_state = 4.0
    goal_x = 0
    for row in state:
        if goal_car_id in row:
            goal_x = row.index(goal_car_id)
    current_state = goal_x
    return goal_state - current_state
    # for breadth first search, replace with:
    # return 0.0


# evaluation function to determine placement of item in priority queue
# input: cost to get to the state, heuristic of state
# output: f(n) for current state
def f(cost_to_state: int, heuristic: float):
    return cost_to_state + heuristic
    # for weighted optimal weighted heuristic:
    # return cost_to_state + (13 * heuristic)


# checks if the current state is the goal state i.e. game over
# input: current state, dictionary of cars w/ information, id of goal car
# output: true if goal state/false if not
def is_goal_state(check_state: list, car_info: dict, goal_car_id: str) -> bool:
    goal_car_x = car_info[goal_car_id][0]
    goal_car_length = car_info[goal_car_id][2]
    if goal_car_x + goal_car_length == len(check_state[0]):
        return True
    else:
        return False
