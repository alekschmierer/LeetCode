#Understand
#Return empty string if nothing is found to be a common prefix

#Match
#Pointers/List

#Plan
#prefix = strs[0]
#for index in range(1,len(list))
    #while list[index] != prefix and prefix:
        #prefix = prefix[:len(prefix)-1]
#return prefix

#Implement
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for index in range(1,len(strs)):
            while not strs[index].startswith(prefix) and prefix:
                prefix = prefix[:len(prefix)-1]
        return prefix

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Completed 7/9/25
#Time: 10:52