#Understand
#Brackets must be closed by their matching bracket and in the same order that they appeared

#Match
#Stack

#([{}])

#Plan
#myStack = []
#for char in s:
    #if char == "(" or char == "[" or char == "{":
        #myStack.append(char)
    #else:
        #if not stack:
            #return False
        #if (myStack.pop() == "(" and char != ")"):
            #return False
        #if (myStack.pop() == "[" and char != "]"):
            #return False
        #if (myStack.pop() == "{" and char != "}"):
            #return False
#return True

class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                myStack.append(char)
            else:
                if not myStack:
                    return False
                else:
                    poppedElement = myStack.pop()
                if (poppedElement == "(" and char != ")"):
                    return False
                elif(poppedElement == "[" and char != "]"):
                    return False
                elif(poppedElement == "{" and char != "}"):
                    return False
        if myStack:
            return False
        return True

#Evaluate
#Time Complexity: O(n)
#Space Complexity:O(n)
#Completed 7/9/25
#Time: 8:59