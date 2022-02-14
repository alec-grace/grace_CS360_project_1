# File: functions.py
# Author: Alec Grace
# Created on: 13 Feb 2022
# Purpose:
#   file for CS360 Project 1: Solving Rush Hour functions
from copy import deepcopy
import graph
import heap


def valid_move(cars: dict, car_id: str, direction: int, board_state: list) -> bool:
    car_x = cars[car_id][0]
    car_y = cars[car_id][1]
    car_length = cars[car_id][2]
    if cars[car_id][3]:
        if direction > 0:
            if car_x + car_length == len(board_state):
                return False
        elif direction < 0:
            if car_x == 0:
                return False
    elif not cars[car_id][3]:
        if direction > 0:
            if car_y + car_length == len(board_state):
                return False
        elif direction < 0:
            if car_y == 0:
                return False
    return True


def can_move(cars: dict, car_id: str, board_state: list) -> list:
    return_list = []
    if valid_move(cars, car_id, -1, board_state):
        return_list.append(-1)
    if valid_move(cars, car_id, 1, board_state):
        return_list.append(1)
    return return_list


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


def calculate_heuristic(state: list, goal_car_id: str) -> float:
    goal_state = 4.0
    for row in state:
        if goal_car_id in row:
            goal_y = state.index(row)
            goal_x = row.index(goal_car_id)
    current_state = goal_x
    return goal_state - current_state


def f(cost_to_state: int, heuristic: float):
    return cost_to_state + heuristic


def is_goal_state(check_state: list, car_info: dict, goal_car_id: str) -> bool:
    goal_car_x = car_info[goal_car_id][0]
    goal_car_length = car_info[goal_car_id][2]
    if goal_car_x + goal_car_length == len(check_state[0]) - 1:
        return True
    else:
        return False


