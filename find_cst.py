import numpy as np

def min_in_s(content, partition):
    arr = []
    num = 0
    for num, c in enumerate(content):
        arr.extend([num+1]*content[num])
    mat = np.array(0)
    num = 0
    for p in partition:
        mat.append(arr[num:p])
        num += p
    #return arr
    return mat


result = min_in_s([2,1,1], [3, 1])
print(result)
