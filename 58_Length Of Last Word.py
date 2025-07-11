#Understand
#given string, return length of last word

#Match/Plan
#s.split, return length of last word

#Implement
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        myList = s.split()
        return len(myList[-1])

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Completed 7/11/25
#Time: 1:01 