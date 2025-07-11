#Understand
#remove elements from a sorted list

#Match
#Two Pointer Approach

#Plan/Implement
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Base Case 0,1
        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]
        
        #Case 2+
        pointerLeft = 0
        pointerRight = 1
        while pointerRight < len(nums):
            if nums[pointerLeft] == nums[pointerRight]:
                nums.pop(pointerRight)
            else:
                pointerLeft += 1
                pointerRight += 1
#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Completed 7/10/25
#Time: Not Collected

#New Faster Method learned, Creates set, turns into list, becomes sorted, then [:] is replaced in-place
#nums[:]=sorted(list(set(nums)))
# return  len(nums)