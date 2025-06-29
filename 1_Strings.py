#Day1.py

#Challenge 1, Take input and reverse string
class Solution1:
    #Approach, slicing: [start stop step]
    #[::-1], takes entire string and traverses from end to beginning 
    def myFunction(self, str1: str)->str:
        return str1[::-1]
    
    #Approach, for loop in range
    def otherFunction(self, str1: str)->str:
        otherReversedString = ""
        for i in range(0,len(str1)):
            otherReversedString = otherReversedString + str1[len(str1)-1-i]
        return otherReversedString 

    #Approach, easy for loop
    def easyLoop(self, str1: str)->str:
        reverse = ""
        for char in str1:
            reverse = char + reverse
        return reverse

print("Sol1")
sol1 = Solution1()
reverseString = sol1.myFunction(str1="League Of Legends")
print(reverseString)
print()

#Challenge 2, Write a function to find the longest common prefix string amongst an array of strings.
# We can take the first word and then loop through all other words matching it to the first
class Solution2:
    def longestCommonPrefix(self, strs):
        #If string array is empty, then return empty string
        if not strs:
            return ""
        
        #Take first word as starting prefix
        prefix = strs[0]
        #Check if each string in the array is a current prefix of that string
        for string in strs[1:]:
            #While string does not start with prefix (flower), and (empty string = false, non-empty string = true)
            #Remove last character from (flower)
            while not string.startswith(prefix) and prefix:
                prefix = prefix[0:-1:1]
            #If prefix is false, return empty (empty = false, non-empty = true)
            if not prefix:
                return ""
        return prefix

print("Sol2")
sol = Solution2()
longCommon = sol.longestCommonPrefix(strs=["flower","flow","flight"])
print(longCommon)
print()

#Challenge 3, Roman to Integer
class Solution3:
    def romanToInt(self, str1: str) -> int:
        number = 0
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(len(str1) - 1):
            if romanDict[str1[i]] < romanDict[str1[i + 1]]:
                number -= romanDict[str1[i]]  
            else:
                number += romanDict[str1[i]]
        
        number += romanDict[str1[-1]]

        return number

print("Sol3")
sol3 = Solution3()
result = sol3.romanToInt("MCMIV")
print(result)
print()

class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

print("Sol4")
sol4 = Solution4()
result = sol4.strStr(haystack = "sadbutsad", needle = "sad")
print(result)
print()

class Solution5():
    def areOccurrencesEqual(self, s: str) -> bool:
        myDict = {}
        for char in s:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict.update({char : 0})
        first_value = next(iter(myDict.values()))
        for value in myDict.values():
            if value != first_value:
                return False
        
        return True

print("Sol5")
sol5 = Solution5()
result = sol5.areOccurrencesEqual(s= "aaabb")
print(result)
print()