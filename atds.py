#!/usr/bin/env python3

"""
atds.py
holds data structures
"""

__author__ = "Roy Otamura"
__version__ = "2024-02-13"

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, item):
       self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        if(len(self.stack) > 0):
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def size(self):
        return len(self.stack)
    def is_empty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
        
class Queue(object):
    def __init__(self):
        self.q = []
    def enqueue(self, item):
        self.q.append(item)
    def dequeue(self):
        if len(self.q) != 0:
            return self.q.pop(0)
        else:
            return None
    def peek(self):
        return self.q[0]
    def size(self):
        return len(self.q)
    def is_empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False
