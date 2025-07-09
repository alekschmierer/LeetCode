# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Understand
#Merge two lists into one sorted list
#Return head of the linked list

#Match

#Plan
#dummyHead = ListNode(0)
#linkedList3 = dummyHead

#while list1 and list2:
    #if list1.val < list2.val:
        #linkedList3.next = ListNode(list1.val)
        #linkedList3 = linkedList3.next
    #else: 
        #linkedList3.next = ListNode(list2.val)
        #linkedList3 = linkedList3.next

#while list1:
    #linkedList3.next = ListNode(list1.val)
    #linkedList3 = linkedList3.next

#while list2:
    #linkedList3.next = ListNode(list1.val)
    #linkedList3 = linkedList3.next

#return dummyHead.next

#Implement
from typing import ListNode, Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        linkedList3 = dummyHead

        while list1 and list2:
            if list1.val < list2.val:
                linkedList3.next = list1
                linkedList3 = linkedList3.next
                list1 = list1.next
            else: 
                linkedList3.next = list2
                linkedList3 = linkedList3.next
                list2 = list2.next

        while list1:
            linkedList3.next = list1
            linkedList3 = linkedList3.next
            list1 = list1.next

        while list2:
            linkedList3.next = list2
            linkedList3 = linkedList3.next
            list2 = list2.next
        return dummyHead.next

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Completed 7/9/25
#Time: 5:19