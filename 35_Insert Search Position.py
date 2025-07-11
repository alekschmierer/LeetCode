#Understand
#return index of target or where it should be

#Match/Plan
#Use bindary serach for O(logn)
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pointerLeft = 0
        pointerRight = len(nums)-1
        middlePointer = 0

        while pointerLeft <= pointerRight:
            middlePointer = (pointerRight + pointerLeft) // 2

            if nums[middlePointer] == target:
                return middlePointer
            elif nums[middlePointer] > target:
                pointerRight = middlePointer - 1
            else:
                pointerLeft = middlePointer + 1
        
        if nums[middlePointer] > target:
            return middlePointer 
        else:
            return middlePointer + 1
#Evaluate
#Time Complexity: O(logn)
#Space Complexity: O(1)
#Completed 7/11/25
#Time: 6:11 