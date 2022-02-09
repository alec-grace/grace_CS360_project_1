# File: heap.py
# Author: Alec Grace
# Created on: 27 Jan 2022
# Purpose:
#   class to implement a heap in main

class Heap:
    def __init__(self, lst=None):

        if lst is None:
            lst = []
        if len(lst) > 0:
            self.list = []
            for item in lst:
                self.add(item)
        else:
            self.list = []

    def add(self, item):
        self.list.append(item)
        current = self.list.index(item)
        while (self.list[self.__calc_parent(current)][0] > item[0]) \
                and (self.__calc_parent(current) >= 0):
            parent_index = self.__calc_parent(current)
            temp = self.list[parent_index]
            self.list[parent_index] = item
            self.list[current] = temp
            current = self.__calc_parent(current)

    def peek(self) -> int:
        return self.list[0][0]

    def pop(self) -> int:
        popped = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        self.list.pop()
        self.__heapify(0)
        return popped

    def size(self) -> int:
        return len(self.list)

    def __heapify(self, loc):
        left_child_index = (2 * loc) + 1
        right_child_index = (2 * loc) + 2
        if (len(self.list) > left_child_index) and \
                (self.list[left_child_index][0] < self.list[loc][0]):
            smallest = left_child_index
        else:
            smallest = loc
        if (len(self.list) > right_child_index) and \
                (self.list[right_child_index][0] < self.list[smallest][0]):
            smallest = right_child_index
        if smallest != loc:
            temp = self.list[smallest]
            self.list[smallest] = self.list[loc]
            self.list[loc] = temp
            self.__heapify(smallest)

    def __calc_parent(self, child_index: int) -> int:
        return (child_index - 1) // 2
