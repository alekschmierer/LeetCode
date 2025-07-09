# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Understand
    #We have two linked lists that are reversed, and contain integers
    #Issues: Must track carry value, if we reach end of list and val with 0 and carry. 
        #If we are at the end of the list  still have a carry value then we must add another node with it to the end.
    #Goal: Add integers together and return in a reversed linked list of the answer

#Plan
#l3 = None
#pointerHead = l3
#carry_value = 0

#while l1 and l2:
    #value = l1.val + l2.val + carry
    #if value / 10 > 1:
        #value = value % 10
        #carry = 1
    #l3 = Node(value, None)
    #l3 = l3.next

#if l1:
    #while l1:
        #value = l1.val + carry
        #if value / 10 > 1:
            #value = value % 10
            #carry = 1
        #l3 = Node(value, None)
        #l3 = l3.next

#if l2:
    #while l2:
        #value = l2.val + carry
        #if value / 10 > 1:
            #value = value % 10
            #carry = 1
        #l3 = Node(value, None)
        #l3 = l3.next

#if carry:
    #l3 = Node(1, None)

#return pointerHead

#Implement
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointerHead = ListNode(0)
        l3 = pointerHead
        carry_value = 0

        while l1 and l2:
            value = l1.val + l2.val + carry_value
            if value / 10 >= 1:
                value = value % 10
                carry_value = 1
            else:
                carry_value = 0
            l3.next = ListNode(value, None)
            l3 = l3.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                value = l1.val + carry_value
                if value / 10 >= 1:
                    value = value % 10
                    carry_value = 1
                else:
                    carry_value = 0
                l3.next = ListNode(value, None)
                l3 = l3.next
                l1 = l1.next
        else:
            while l2:
                value = l2.val + carry_value
                if value / 10 >= 1:
                    value = value % 10
                    carry_value = 1
                else:
                    carry_value = 0
                l3.next = ListNode(value, None)
                l3 = l3.next
                l2 = l2.next

        if carry_value > 0:
            l3.next = ListNode(1, None)

        newHead = pointerHead.next
        return newHead
    
#Evaluate 
#Time Complexity: O(n), where n is len of max(l1,l2)
#Space Complexity: O(n), where n is len of max(l1,l2)
#Completed 7/5/25
#Time: 33:02