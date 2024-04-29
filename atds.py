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
        
class Deque(object):
    def __init__(self):
        self.dq = []
    def add_front(self, item):
        if len(self.dq) == 0:
            self.dq.append(item)
        else:
            self.dq.append(self.dq[len(self.dq) - 1])
            i = len(self.dq) - 2
            while(i > 0):
                self.dq[i] = self.dq[i - 1]
                i -= 1
            self.dq[0] = item
    def add_rear(self, item):
        self.dq.append(item)
    def remove_front(self):
        return self.dq.pop(0)
    def remove_rear(self):
        return self.dq.pop()
    def size(self):
        return len(self.dq)
    def is_empty(self):
        return len(self.dq) == 0

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

class UnorderedList(object):
    def __init__(self):
        self.head = None
    def add(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
    def remove(self, data):
        curr = self.head
        if curr.get_data() == data:
            self.head = curr.get_next()
        while curr.get_next() != None:
            if (curr.get_next()).get_data() == data:
                curr.set_next((curr.get_next()).get_next())
            else:
                curr = curr.get_next()
    def search(self, item):
        curr = self.head
        while curr != None:
            if curr.get_data() == item:
                return True
            curr = curr.get_next()
        return False
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def length(self):
        count = 0
        curr = self.head
        while curr != None:
            curr = curr.get_next()
            count += 1
        return count
    def append(self, item):
        curr = self.head
        while curr.get_next() != None:
            curr = curr.get_next()
        curr.set_next(Node(item))
    def index(self, item):
        i = 0
        curr = self.head
        while curr.get_data() != item:
            curr = curr.get_next()
            i += 1
        return i
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            curr = self.head
            i = 1
            while i < pos:
                curr = curr.get_next()
                i += 1
            holder = curr.get_next()
            curr.set_next(Node(item))
            curr.get_next().set_next(holder)
    def pop(self, pos = -1):
        prev = self.head
        if pos == -1:
            pos = self.length() - 1
        if pos == 0:
            self.head = prev.get_next()
            return prev
        else:
            curr = prev.get_next()
            i = 1
            while i < pos:
                prev = curr
                curr = curr.get_next()
                i += 1
            prev.set_next(curr.get_next())
            return curr
    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

class ULStack(object):
    def __init__(self):
        self.stack = UnorderedList()
    def push(self, item):
       self.stack.add(item)
    def pop(self):
        print(self.stack)
        popped = self.stack.pop()

        return popped.get_data()
    def peek(self):
        holder = self.stack.pop(0)
        self.stack.add(holder)
        return holder.get_data()
    def size(self):
        return self.stack.length()
    def is_empty(self):
        return self.stack.is_empty()

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def hash_fuction(self, key):
        return key % self.size
    def put(self, key, value):
        index = self.hash_function(key)
        while self.slots[index] != None and self.slots[index] != key:
            index += 1
        if self.slots[index] == key:
            self.data[index] = value
        else:
            self.slots[index] = key
            self.data[index] = value
    def get(self, key):
        index = self.hash_function(key)
        while self.slots[index] != None:
                if self.slots[index] == key:
                    return self.data[index]
                else:
                    index += 1
        return None
            
class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    def get_root_val(self):
        return self.root
    def set_root_val(self, value):
        self.root = value
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def insert_left(self, value):
        new_left = BinaryTree(value)
        new_left.left = self.left
        self.left = new_left
    def insert_right(self, value):
        new_right = BinaryTree(value)
        new_right.right = self.right
        self.right = new_right
        