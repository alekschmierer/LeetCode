#Understand
#Given an integer determine if it reads the same forward and backwards (palidrome)

#Match
#Two Pointer Method

#Plan
#pointerLeft 
#pointerRight
#while pointerLeft <= pointerRight:
    #if pointerLeft != pointerRight:
        #return False
    #pointerLeft += 1
    #pointerRight -= 1
#return True

#Implement
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        pointerLeft = 0
        pointerRight = len(stringX)-1 
        while pointerLeft < pointerRight:
            if stringX[pointerLeft] != stringX[pointerRight]:
                return False
            pointerLeft += 1
            pointerRight -= 1
        return True

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(n)