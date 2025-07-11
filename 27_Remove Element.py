#Understand
#array of nums, with target val, remove all in placed
#return number of elements which are not equal to val

#Match
#Pointer Method

#plan
# while pointer < len(nums):
#     if nums[pointer] == val:
#         nums.pop(pointer)
#     else:
#         pointer += 1
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == val:
                nums.pop(pointer)
            else:
                pointer += 1
        return len(nums)

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Completed 7/11/25
#Time: 4:58