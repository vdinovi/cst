#import numpy as np
import pdb as pdb


class Node:
    def __init__(self, value, state):
        assert(state and value)
        self.value = value
        self.state = state
        self.valid = False
        self.children = []
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def to_s(self):
        s = str(self.value) + " " + str(self.state)
        if self.valid: s += " ** "
        return s


def build_tree(node, values, partition, content):
    if (sum(node.state) == sum(content)):
        node.valid = check_valid(node)
        return 
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
            node.add_child(new_node)
            build_tree(new_node, vals, partition, content)


def print_tree(node, offset):
    print((" " * offset) + node.to_s())
    for n in node.children:
        print_tree(n, offset + 3)

def gather_valid(node, result):
    if node.valid:
        result += 1
    else:
        for c in node.children:
            gather_valid(c, result)

def check_valid(leaf, partition):
    values = get_partition(leaf)
    print(values)
    # Check column strict
    for col in range(0, partition[0]):
        for row in range(0, len(partition)-1):
            if values[partition[row]+col] < 

    # check for each row from bot to top-1
    for row in range(0, len(partition)-1):
        for col in range(0, partition[row]):
            if values[partition





def get_partition(leaf):
    node = leaf
    partition = [node.value]
    while node.parent:
        node = node.parent
        partition.append(node.value)
    partition.reverse()
    return partition



#result = min_in_s([2,1,1], [3, 1])
#print(result)
if __name__ == "__main__":
    partition = [3,1]
    content = [2,1,1]
    root = Node(1, [1,0,0])
    values = list(range(1, len(content)+1))
    build_tree(root, values, partition, content)
    print_tree(root, 0)
    result = 0
    gather_valid(root, result)
    print("\nValid CSTs: " + str(result))

