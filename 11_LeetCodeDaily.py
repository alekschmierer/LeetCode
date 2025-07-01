# 3330. Find the Original Typed String I
    # Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
    # Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
    # You are given a string word, which represents the final output displayed on Alice's screen.
    # Return the total number of possible original strings that Alice might have intended to type.


#Understand
# Original word counts as a possible string
# Increase count per duplicated character in a row

#Match
#Pointers

#Plan
#total_count = 1
#base cases for word length of 1 or 2, so I can use pointers correctly at positons 0,1
#pointerLeft, pointerRight = 0,1
#while pointerRight does not equal length of word
    #check if leftPointer equals right pointer
        #increase total_count
#return

#Implement
class Solution:
    def possibleStringCount(self, word: str) -> int:
        total_count = 1

        if len(word) == 1:
            return total_count
        if len(word) == 2:
            if word[0] == word[1]:
                return 2
            return 1
        
        pointerLeft = 0
        pointerRight = 1

        while pointerRight != len(word):
            if word[pointerLeft] == word[pointerRight]:
                total_count += 1

            pointerLeft += 1
            pointerRight += 1
        
        return total_count

#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)


