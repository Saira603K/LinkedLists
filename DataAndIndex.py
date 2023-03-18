#Write a function/method to insert an element by index to linked list in array structure
#with a char type node.

import numpy as np
class Node:
    def __init__(self, data, idx):
        self.data=data
        self.idx=idx


def insertElem(ls, idx, data):
    new_node = Node(data, None)
    if idx == 0:
        new_node.idx = ls[0].idx
        ls[0] = new_node
    else:
        prev_node = ls[idx - 1]
        next_node = ls[idx]
        prev_node.idx = new_node.idx
        new_node.idx = next_node.idx
        prev_node.next = new_node
        ls[idx] = new_node
        for i in range(idx + 1, len(ls)):
            if ls[i] is None or ls[i].idx is None:
                break
            ls[i].idx += 1


# create the linked list array
elm0 = Node("head", 1)
elm1 = Node("S", 2)
elm2 = Node("t", 3)
elm3 = Node("i", 4)
elm4 = Node("n", 5)
elm5 = Node("g", None)
ls = np.array([elm0, elm1, elm2, elm3, elm4, elm5])

# print the original linked list
print([node.data for node in ls if node is not None])

# insert a new node with data 'r' at index 3
insertElem(ls, 3, 'r')

# print the updated linked list
print([node.data for node in ls if node is not None])
