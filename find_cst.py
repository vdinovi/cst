#import numpy as np
import pdb as pdb

"""
def min_in_s(content, partition):
    arr = []
    num = 0
    for num, c in enumerate(content):
        arr.extend([num+1]*content[num])
    num = 0
    rows = []
    for p in partition:
        rows.append(arr[num:num+p])
        num += p
    return rows
"""

def min_in_s(content, partition):
    arr = [0] * sum(partition)
    for i in range(1, len(content)+1):



    """
    num = 0
    for num, c in enumerate(content):
        arr.extend([num+1]*content[num])
    num = 0
    rows = []
    for p in partition:
        rows.append(arr[num:num+p])
        num += p
    return rows
    """
    return arr



result = min_in_s([2,1,1], [3, 1])
print(result)
