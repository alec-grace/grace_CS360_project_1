# File: myqueue.py
# Author: Alec Grace
# Created on: 29 Jan 2022
# Purpose:
#   class to implement a queue

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, obj):
        self.q.append(obj)

    def dequeue(self):
        obj = self.q[0]
        self.q.remove(obj)
        return obj

    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)

    def is_empty(self):
        if len(self.q) > 0:
            return False
        else:
            return True
