#UMPIRE

#Understand/Plan
#Sort list least to greatest, find as many negative numbers to negate within k range
#If no negative numbers exist at this point then negate smallest number if k is odd, if k is even then ignore this

#Match
#N/A (Reflecting, now I know its a heap based question, in which I could alwys find the smallest element that way)

#Implement
from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        #Flip as many negative numbers as possible
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        #If k odd, flip the smallest element
        nums.sort()
        if k % 2 == 1:
            nums[0] = -nums[0]

        return sum(nums)

#Evaluation 
#Time complexity is O(n), we are iterating through the list nums of n values and performing O(1) operations inside loop
#Space complexity is O(1) since we are not creating any new data structures or lists, we are modifying in place

nums = [2,-3,-1,5,-4]
k = 2
newObject = Solution()
print(newObject.largestSumAfterKNegations(nums,k))