class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def convert_to_char(node):
    """
    Converts a linked list of int type nodes (0 to 9) to char type nodes ('A' to 'Z' or '#').
    """
    res = Node(None)
    ptr = res
    while node:
        val = node.val
        if val <= 0 or val > 26:
            val = ord('#')
        else:
            val = ord('A') + val - 1
        ptr.next = Node(chr(val))
        node = node.next
        ptr = ptr.next
    return res.next

# Example usage
lst0 = Node(1)
lst0.next = Node(2)
lst0.next.next = Node(2)
lst0.next.next.next = Node(1)
lst1 = Node(1)
lst1.next = Node(2)
lst1.next.next = Node(2)
lst1.next.next.next = Node(1)
lst2 = Node(1)
lst2.next = Node(22)
lst2.next.next = Node(1)
lst3 = Node(1)
lst3.next = Node(2)
lst3.next.next = Node(21)

# Convert the linked lists to char type nodes
char_lst0 = convert_to_char(lst0)
char_lst1 = convert_to_char(lst1)
char_lst2 = convert_to_char(lst2)
char_lst3 = convert_to_char(lst3)

# Print the results
def print_list(node):
    while node:
        print(node.val, end='->')
        node = node.next
    print('None')

print_list(char_lst0)  # A->B->B->A->None
print_list(char_lst1)  # A->B->B->A->None
print_list(char_lst2)  # A->V->A->None
print_list(char_lst3)  # A->B->U->None

'''
A->B->B->A->None
A->B->B->A->None
A->V->A->None
A->B->U->None
'''
