# File: graph.py
# Author: Alec Grace
# Created on: 27 Jan 2022
# Purpose:
#   class to implement a graph in main

from myqueue import Queue


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, label: str):
        self.graph[label] = []

    def add_arc(self, src: str, dest: str, label: str = None):
        if src in self.graph.keys():
            self.graph[src].append(dest)
        else:
            self.add_node(dest)
            self.graph[src] = [dest]

    def add_arc_undirected(self, src: str, dest: str, label: str = None):
        if src not in self.graph:
            self.graph[src] = [dest]
        else:
            self.graph[src].append(dest)

        if dest not in self.graph:
            self.graph[dest] = [src]
        else:
            self.graph[dest].append(src)

    def remove_node(self, label: str):
        self.graph.pop(label, 0)
        for key in self.graph:
            if label in self.graph[key]:
                self.graph[key].remove(label)

    def remove_arc(self, src: str, dest: str):
        if src in self.graph:
            if dest in self.graph[src]:
                self.graph[src].remove(dest)

    def reachable(self, src: str, dest: str) -> bool:
        if self.shortest_path(src, dest) is not None:
            return True
        else:
            return False

# TODO: Figure out the algorithm we were given
    def shortest_path(self, src: str, dest: str) -> list[str]:
        if src not in self.graph.keys() or dest not in self.graph.keys():
            return None
        Q = Queue()
        Q.enqueue((src, []))
        visited = []
        current = Q.dequeue()
        visited.append(current[0])
        while current[0] != dest:
            for neighbor in self.graph[current[0]]:
                if neighbor not in visited:
                    pair = (neighbor, current[1]+[current[0]])
                    visited.append(neighbor)
                    Q.enqueue(pair)
            if Q.is_empty():
                break
            current = Q.dequeue()
        if current[0] == dest:
            return current[1]+[current[0]]
        else:
            return None
