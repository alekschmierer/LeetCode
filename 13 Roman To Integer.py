#Understand
#Must go from symbol to value
#Use ruleset to get result

#Match
#List/Dictionary

#Plan
#total = 0
#romanSymbols = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D":500, "M":1000}
#for index in range(len(s)-1):
    #if s[index] == "I" and (s[index+1] == "V" or s[index+1] == "X"):
        #total -= 1
    #elif s[index] == "X" and (s[index+1] == "L" or s[index+1] == "C"):
        #total -= 10
    #elif s[index] == "C" and (s[index+1] == "D" or s[index+1] == "M"):
        #total -= 100
    #else:
        #total += romanSymbols.get(s[index])
#total += [s[len(s)]]

#Implement
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        romanSymbols = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D":500, "M":1000}
        for index in range(len(s)-1):
            if s[index] == "I" and (s[index+1] == "V" or s[index+1] == "X"):
                total -= 1
            elif s[index] == "X" and (s[index+1] == "L" or s[index+1] == "C"):
                total -= 10
            elif s[index] == "C" and (s[index+1] == "D" or s[index+1] == "M"):
                total -= 100
            else:
                total += romanSymbols.get(s[index])
        total += romanSymbols.get(s[len(s)-1])
        return total
    
#Evaluate
#Time Complexity: O(n)
#Space Complexity: O(1)
#Time: 8:12