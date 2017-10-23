import numpy as np
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

"""
 Nodes in our decision tree. Each path from root-to-leaf represents a sequence of values
 Which can be chopped up according and assembled according to our partition.
    - Each has a value representing that choice of number in our CST
    - They are stateful keeping track of the number of values chosen so as 
      to not exceed the specified content.
    - Each keeps track of its children and parent
"""
class Node:
    def __init__(self, value, state):
        assert(state and value)
        self.value = value
        self.state = state
        self.children = []
        self.parent = None

    # Adds a child node to this node
    def add_child(self, node):
        node.parent = self
        self.children.append(node) 

    # Converts node to single-line string representation
    def to_s(self):
        return str(self.value) + " " + str(self.state) + ("*" if self.valid else "")

    # Prints the tree at and below this node
    def print_tree(self, offset):
        print((" " * offset) + node.to_s())
        for n in node.children:
            print_tree(n, offset + 3)


# This constructs our decision tree
def build_tree(node, values, partition, content, cst_list):
    # If we have not yet reached a leaf, continue to build the tree
    if (sum(node.state) != sum(content)):
        # Use only values for which capacity has not been reached
        for vidx, val in enumerate(values):
            if node.state[vidx] < content[vidx]:
                # create new decision node with given value
                new_state = node.state[:]
                new_state[vidx] += 1
                new_node = Node(val, new_state)
                new_node.parent = node
                # if adding this decision node does not break constraints, add it
                if (check_decision(new_node, partition)):
                    node.add_child(new_node)
                    build_tree(new_node, values, partition, content, cst_list)
    # This node is a leaf, extract the partition and add it to our CST list
    else:
        p = get_decisions(node)
        if sorted(content) == sorted(node.state):
            p.reverse()
            cst_list.append(p)

# checks whether making a decision to add a node will break CST properties
def check_decision(node, partition):
    arr = get_decisions(node)
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
  
# Retrieves an list of decisions(values) above this node
def get_decisions(node):
    n = node
    arr = [n.value]
    while n.parent:
        n = n.parent
        arr.append(n.value)
    arr.reverse()
    return arr

# Obtains the number of CSTs for the provided partition and content
def min_in_s(partition, content):
    state = [0] * len(content)
    state[0] = 1
    root = Node(1, state)
    values = list(range(1, len(content)+1))
    csts = []
    build_tree(root, values, partition, content, csts)
    return len(csts)

# Compute the kostka matrix for any set of partitions of n
def kostka(partitions):
    matr = np.zeros((len(partitions), len(partitions)), dtype=np.int)
    for row, content in enumerate(partitions):
        for col, partition in enumerate(partitions):
            matr[row][col] = min_in_s(partition, content)
    return matr

if __name__ == "__main__":
    partitions_4 = [ [4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1] ]
    partitions_5 = [ [5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1] ]
    print("Kostka n=4")
    print(kostka(partitions_4))
    print("Kostka n=5")
    print(kostka(partitions_5))


