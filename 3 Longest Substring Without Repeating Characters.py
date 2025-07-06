#First Attempt (Will Come Back To)

#Understand
#Find longest substring without duplicate characters
#Solutions: Can create a list/set of seen characters then hold the longestSubstring

#Match
#List/set Question
#Two pointers

#Plan
#Base cases
#Intialize variables
#while head != len(s)
    #if rightPointer(s) in list
        #if len(myList) > len(longestList):
            #longestList = myList.copy()
        #myList.clear()
        #increment pointers
    #else
        #myList.append(s[rightPointer])
        #pointerRight += 1
    #return len(longestList)
    

#Implement
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Base Cases
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        
        #Two Pointer Method - Variables
        pointerLeft = 0
        pointerRight = 0
        myList = []
        longestList = []

        #Iterate
        while pointerLeft != len(s):
            if pointerRight < len(s):
                if s[pointerRight] in myList:
                    if len(myList) > len(longestList):
                        longestList = myList.copy()
                    myList.clear()
                    pointerLeft += 1
                    pointerRight = pointerLeft
                else:
                    myList.append(s[pointerRight])
                    pointerRight += 1
            else:
                if len(myList) > len(longestList):
                    longestList = myList.copy()
                pointerLeft +=1
                pointerRight = pointerLeft

        return len(longestList)
            
#Evalaute
#Time Complexity: Too Slow
#Space Complexity: O(n^2)
#Completed 7/6/25
#Time: 30:45