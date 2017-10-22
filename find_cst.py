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

    def add_child(self, node):
        self.children.append(node) 

    def to_s(self):
        return str(self.value) + " " + str(self.state)

def build_tree(node, values, partition, content):
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
                #check_valid
                new_node = Node(v, new_state)
                node.add_child(new_node)
                build_tree(new_node, vals, partition, content)

# DEBUG -- print tree
def print_tree(node, offset):
    print((" " * offset) + node.to_s())
    for n in node.children:
        print_tree(n, offset + 3)

def min_in_s(partition, content):
    root = Node(1, [1,0,0])
    # [possible values] == [1 .. length of content]
    values = list(range(1, len(content)+1))
    build_tree(root, values, partition, content)
    print_tree(root, 0)
    print("")
    # @TODO once tree is assembled, (# CSTs) == (# of leafs)
    # result = find_partitions(root)
    result = 0
    return result


if __name__ == "__main__":
    partition = [3,2]
    content = [2,2,1]
    # Partition and content must have same sum
    assert(sum(partition) == sum(content))
    result = min_in_s(partition, content)
    print("Valid CSTs: " + str(result))

