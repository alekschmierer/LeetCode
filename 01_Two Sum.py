#Understand
#while going through problem, we can keep track of the difference between the curr value and target and if we find it in the list/dict then we have found the number

#key, is target - number, value is index

#Match
#Dictionary / List Problem

#Plan
#myDict = {} {key:value}
#For index in rage (len(nums)):
    #if myDict.get(nums[index]):
        #return [myDict[nums[index]], index]
    #myDict[target - number] = index

#Implement
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for index in range (len(nums)):
            if myDict.get(nums[index]) != None:
                return [myDict[nums[index]], index]
            else:
                myDict[target - nums[index]] = index

#Review
#Time Complexity: O(n)
#Space Complexity: O(n)

#Completed 7/5/25
#Time: Not Tracked