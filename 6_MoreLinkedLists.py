class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        

head = Node(1, Node(2, Node(2, None)))
# while(head is not None):
#     print(head.value, end=' ')
#     head = head.next
# print()

# def count_element(head, val):
#     counter = 0
#     while head is not None: #O(n) operations
#         if(head.value == val): #O(1) operations
#             counter +=1
#         head = head.next
#     return counter
# print(count_element(head, 2))

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find the middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow.next
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Compare two halves
    left = head
    right = prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True


# print(is_palindrome(head))

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev, curr = None, head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev

head = Node(1, Node(2, Node(3)))
reversedList = reverse_linked_list(head)

while reversedList:
    print(reversedList.value, end=' ')
    reversedList = reversedList.next
