#import numpy as np
import pdb as pdb

"""
@author Vittorio Dinovi
@date 10/21/17

Implemented solution for HW4, problem 27 for MATH 435 with Dr. Mendes

min_in_s(partition, content) returns the number of CSTs for the given partition and content.

This solution uses stateful decision tree to determine the number of valid CSTs.
Only decisions that preserve strictly increasing columns and weaky decreasing rows
are allowed. This process results in all leafs being valid CSTs.
"""

class Node:
    def __init__(self, value, state):
        assert(state and value)
        self.value = value
        self.state = state
        self.children = []
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node) 

    def to_s(self):
        return str(self.value) + " " + str(self.state) + ("*" if self.valid else "")

def print_tree(node, offset):
    print((" " * offset) + node.to_s())
    for n in node.children:
        print_tree(n, offset + 3)

def build_tree(node, values, partition, content, result):
    if (sum(node.state) != sum(content)):
        vals = values[:]
        for part in content:
            if part in node.state:
                vals[node.state.index(part)] = None
            else:
                break
        for v in vals:
            if v:
                new_state = node.state[:]
                new_state[v-1] += 1
                new_node = Node(v, new_state)
                new_node.parent = node
                if (check_decision(new_node, partition)):
                    node.add_child(new_node)
                    build_tree(new_node, vals, partition, content, result)
    else:
        p = get_partition(node)
        if sorted(content) == sorted(node.state):
            p.reverse()
            result.append(p)

def check_decision(node, partition):
    arr = get_array(node)
    idx = len(arr)-1
    row = 0
    count = idx
    # Get the row that this element belongs to
    while count - partition[row] >= 0:
        count -= partition[row]
        row += 1
    # Check cell below for column-strictness
    if (row > 0) and (arr[idx] <= arr[idx - partition[row-1]]):
        return False
    # Check that row is weakly increasing
    if (idx - sum(partition[:row]) > 0) and (arr[idx] < arr[idx-1]):
        return False
    return True
  
def get_partition(leaf):
    node = leaf
    partition = [leaf.value]
    while node.parent:
        node = node.parent
        partition.append(node.value)
    return partition

def get_array(node):
    n = node
    arr = [n.value]
    while n.parent:
        n = n.parent
        arr.append(n.value)
    arr.reverse()
    return arr

def min_in_s(partition, content):
    state = [0] * len(content)
    state[0] = 1
    root = Node(1, state)
    values = list(range(1, len(content)+1))
    csts = []
    build_tree(root, values, partition, content, csts)
    return len(csts)

def print_result(partition, content, result):
    print("min_in_s(" + str(partition) + ", " + str(content) + ") = " + str(result))

