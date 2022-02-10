# File: main.py
# Author: Alec Grace
# Created on: 7 Feb 2022
# Purpose:
#   driver for CS360 Project 1: Solving Rush Hour


def move_car(cars: dict, car_id: str, direction: int, board_state: list) -> list:
    car_x = cars[car_id][0]
    car_y = cars[car_id][1]
    car_length = cars[car_id][2]
    # horizontal moving forward 1
    if cars[car_id][3] and direction > 0:
        if board_state[car_y][car_x + car_length] == -1:
            board_state[car_y][car_x] = -1
            board_state[car_y][car_x + car_length] = car_id
            cars[car_id][0] = car_x + 1
        else:
            return None
    # horizontal moving backward 1
    elif cars[car_id][3] and direction < 0:
        if board_state[car_y][car_x - 1] == -1:
            board_state[car_y][car_x + car_length - 1] = -1
            board_state[car_y][car_x - 1] = car_id
            cars[car_id][0] = car_x - 1
        else:
            return None
    # vertical moving up 1
    elif not cars[car_id][3] and direction < 0:
        if board_state[car_y - 1][car_x] == -1:
            board_state[car_y + car_length - 1][car_x] = -1
            board_state[car_y - 1][car_x] = car_id
            cars[car_id][1] = car_y - 1
        else:
            return None
    # vertical moving down 1
    elif not cars[car_id][3] and direction > 0:
        if board_state[car_y + car_length][car_x] == -1:
            board_state[car_y][car_x] = -1
            board_state[car_y + car_length][car_x] = car_id
            cars[car_id][1] = car_y + 1
        else:
            return None
    return board_state


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
        for line in file:
            line = line.rstrip('\n')
            if first_line:
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
    for i in range(6):
        test_list.append([])
        for j in range(6):
            test_list[i].append(-1)

    # place cars on the board
    for car in cars:
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


if __name__ == '__main__':
    main()
