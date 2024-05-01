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

    def hash_function(self, key):
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
    
    def __repr__(self):
        return "Keys: " + str(self.slots) + "\n" + "Values: " + str(self.data)

            
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

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is
        connected.
        """
        self.id = key
        self.connected_to = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     # discovery time
        self.finish_time = 0        # finish time  
    
    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the
        dictionary, to which this vertex is connected by an edge. 
        If a weight is not indicated, default weight is 0.
        """
        self.connected_to[neighbor_vertex] = weight
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance
    
    def set_pred(self, predecessor):
        self.predecessor = predecessor
    
    def get_pred(self):
        return self.predecessor
    
    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def get_discovery(self):
        return self.discovery_time
    
    def set_finish(self, finish_time):
        self.finish_time = finish_time
    
    def get_finish(self):
        return self.finish_time
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
              + '] connected_to: ' + str([x.id for x in self.connected_to]) 
    
    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connected_to.keys()
    
    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id
    
    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex 
        with another.
        """
        return self.connected_to[neighbor_vertex]    
class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        """Initializes an empty dictionary of Vertex objects
        """
        self.graph = {}

    def add_vertex(self, key):
        """Creates a new "key-value" dictionary entry with the string "key"
        key as the dictionary key, and the Vertex object itself as the value.
        Returns the new vertex as a result.
        """
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.graph.keys()

    def add_edge(self, from_key, to_key, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_key not in self.get_vertices():
            self.add_vertex(from_key)
        # if the to_key doesn't yet have a vertex, create it
        if to_key not in self.get_vertices():
            self.add_vertex(to_key)
        # now we can create the edge between the two
        self.get_vertex(from_key).add_neighbor(self.get_vertex(to_key), weight)

    def get_vertices(self):
        """Returns a list of the Graph's Vertex keys"""
        return self.graph.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.graph.values())
        