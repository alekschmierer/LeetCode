# Problem 1: Calling Mississippi
# In a new Replit, copy and paste the following function:

# def count_mississippi(limit):
#     for num in range(1, limit):
# 		print( f"{num} mississippi")
# Call the function so that it prints out the following to the console (without calling the function more than once):

# 1 mississipi
# 2 mississipi
# 3 mississipi
# 4 mississipi
# 5 mississipi

#UPI
#For loop, no recur

def count_mississippi(limit):
    for num in range(1, limit):
 	    print( f"{num} mississippi")
      

# Problem 2: Swap Ends
# Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

# def swap_ends(my_str):
#     pass
# Example Usage:

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# Only first and last character change in the string
# 
# Call function swap_ends with string
    # If length of string is 0 return nothing
    # If length of string is 1 return character
    # tempVariable1, stores the index 0
    # tempVariable2, stores the last index
    # Set index to the temporary variables
    # return my_str

def swap_ends(my_str):
    if len(my_str) == 0:
        return ""
    if len(my_str) == 1:
        return my_str
    
    tempVariable1 = my_str[0]
    tempVariable2 = my_str[-1]
    
    newString =  tempVariable2 + my_str[1:len(my_str)-1] + tempVariable1
    
    return newString



# Problem 4: Reverse String
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

# def reverse_string(my_str):
#     pass
# Example Usage:

# my_str = "live"
# print(reverse_string(my_str))
# Example Output: evil

def reverse_string(my_str):
    reversedString = ""
    for index in range(len(my_str)-1,-1,-1):
        reversedString += my_str[index]
    return reversedString 
#print(reverse_string("evil"))


def reverse_string1(my_str):
    myList = list(my_str)
    myList.reverse()
    myString = "".join(myList)
    return myString
#print(reverse_string1("evil"))


# Problem 5: First Unique
# Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

# def first_unique_char(my_str):
#     pass
# Example Usage:

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))
# Example Output

# 0
# 2
# -1

def first_unique_char(my_str):
    # For index in range of string length
        # For iteratorIndex in range of string length + 1
            # If string[index] == iteratorIndex then go to next index
            # elif we are at the strings length return string[index]
    #return -1
    for index in range(0,len(my_str)):
        for iteratorIndex in range(0, len(my_str)):
            if my_str[index] == my_str[iteratorIndex] and index != iteratorIndex:
                break
            elif my_str[index] != my_str[iteratorIndex] and iteratorIndex == len(my_str)-1:
                return index
    return -1

#print(first_unique_char("leetcode"))
#print(first_unique_char("loveleetcode"))
#print(first_unique_char("aabb"))

# Problem 6: Minimum Distance
# Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.

# def min_distance(words, word1, word2):
#     pass
# Example Usage:

# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute",  "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)
# Example Output:

# 3
# 1
# 2

# Iterate through the list of words and find all indexs of word1, put indexes into list1
# Iterate through the list of words and find all indexs of word2, put indexes into list2

#min_distance = abs(list1[0] - list2[0])
#For num1 in list1:
    #For num2 in list2:
        #If abs(num1 - num2) < min_distance:
            # min_distance = abs(num1 - num2)


def min_distance(words, word1, word2):
    list1 = []
    list2 = []
    
    for index in range(0,len(words)):
        if words[index] == word1:
            list1.append(index)
        if words[index] == word2:
            list2.append(index)
            
    minDistance = abs(list1[0] - list2[0]) #Assumption that the word1 and word2 exist in the list
    
    for num1 in list1:
        for num2 in list2:
            if abs(num1 - num2) < minDistance:
                minDistance = abs(num1 - num2)
    
    return(minDistance)


# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute",  "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)


# Problem 1: Perfect Match
# In a new Replit, copy and paste the following function:

# def match_made(dictionary):
# 	for key, value in dictionary.items():
# 		print( f"{key} and {value} are a perfect match.")
# Add code to your Replit so that your program prints out the following to the console:

# Peanut butter and Jelly are a perfect match.
# Spongebob and Patrick are a perfect match.
# Ash and Pikachu are a perfect match.


def match_made(dictionary):
	for (key, value) in dictionary.items():
		print( f"{key} and {value} are a perfect match.")
  

dict = {"Peanut butter":"Jelly",
        "Spongebob":"Patrick",
        "Ash":"Pikachu"
        }

# match_made(dict)



# Problem 2: Remove Char
# Write a function remove_char() that takes in a string s and an integer n as parameters, The function returns a new string with the nth character removed where 0 < n < len(s).

# def remove_char(s, n):
#     pass
# Example Usage:

# s = "typpo"
# fixed_s = remove_char(s, 2)
# print(fixed_s)
# Example Output: typo

#n is an index, s is a string 
#must use slicing, and index into the string (strings arent mutuable so must create new string)
def remove_char(s, n):
    newString = s[0:n] + s[n+1::]
    return newString

s = "typpo"
# fixed_s = remove_char(s, 2)
# print(fixed_s)


# Problem 3: Count Vowels
# Write a function vowel_count() that takes in a string s as a parameter and returns the number of vowels in the given string.

# def vowel_count(s):
#     pass
# Example Usage:

# my_str = "hello world"
# my_str2 = "aAaAaAaAAA"
# my_str3 = "ths strng s mssng vwls"

# count1 = vowel_count(my_str)
# print(count1)
# count2 = vowel_count(my_str2)
# print(count2)
# count3 = vowel_count(my_str3)
# print(count3)
# Example Output:

# 3
# 10
# 0

def vowel_count(s):
    newS = s.lower()
    counter = 0
    for char in newS:
        if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            counter += 1
            
    return counter

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

# count1 = vowel_count(my_str)
# print(count1)
# count2 = vowel_count(my_str2)
# print(count2)
# count3 = vowel_count(my_str3)
# print(count3)


# Problem 4: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence as a parameter and returns the string with the sentence but with the order of the words reversed. The sentence will only contain alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function returns the original string.

# def reverse_sentence(sentence):
#     pass
# Example Input: sentence = "I solemnly swear I am up to no good"

# Example Output: "good no to up am I swear solemnly I"

def reverse_sentence(sentence):
    splitSentence = sentence.split()
    splitSentence.reverse()
    for word in splitSentence:
        print(word, end=' ')

# reverse_sentence("I solemnly swear I am up to no good")

# Problem 5: String Compression
# Write a function that takes in a string my_str as a parameter and performs basic string compression using counts of repeated characters.

# For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string does not become smaller than the original string, return the original string. Assume the string only has alphabetic characters.

# def compress_string(my_str):
#     pass
# Example Usage:

# my_str = "aaaaabbcccd"
# compressed_Str = compress_string(my_str)
# print(compressed_Str)

# my_str2 = "abcde"
# compressed_Str2 = compress_string(my_str2)
# print(compressed_Str2)
# Example Output:

# a5b2c3d1
# abcde 
# did not convert my_str2 because `a1b1c1d1e1` is double the length

# Compress the strings, by reading left to right and put (character)(count) in the new string
# If the "compressed string" is longer in length the original string

# Prev character = string[0]
# newString = ''
# counter = 0
# For character in string:
    #if prev character = character:
        #counter += 1
    #else:
        # newString = previous character + counter
        # prevCharacter = character
        # counter = 1
# If len(newString) < len(string):
    # return newString
# else:
    # return oldString
def compress_string(my_str):
    previousCharacter = my_str[0]
    newString = ""
    counter = 0
    for character in my_str:
        if previousCharacter == character:
            counter += 1
        else: 
            newString += previousCharacter + str(counter)
            previousCharacter = character
            counter = 1
    if len(newString) < len(my_str):
        return newString
    else:
        return my_str

# print(compress_string("aabcccccaaa"))
# print(compress_string("abcde"))

# Problem 6: Needle in a Haystack
# Write a function find_the_needle() that takes in two string parameters: a needle and a haystack. The function returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# def find_the_needle(haystack, needle):
#     pass
# Example Usage:

# haystack = "tobeornottobe"
# needle = "be"
# print(find_the_needle(haystack, needle))

# haystack2 = "leetcode"
# needle2 = "leeto"
# print(find_the_needle(haystack2, needle2))
# Example Output:

# 2
# -1

def find_the_needle(haystack, needle):
    try:
        return haystack.index(needle)
    except:
        return -1
    
# haystack = "tobeornottobe"
# needle = "be"
# print(find_the_needle(haystack, needle))

# haystack2 = "leetcode"
# needle2 = "leeto"
# print(find_the_needle(haystack2, needle2))


# Problem 5: Longest Substring
# Write a function that takes in a string s and returns the length of the longest substring without repeating characters.

# def length_of_longest_substring(s):
# 	pass
# Example Usage:

# s = "abcdeefghhhhh"
# count = length_of_longest_substring(s)
# print(count)

# s2 = "aaaaaaaaaaaaaaa"
# count = length_of_longest_substring(s2)
# print(count)
# Example Output:

# 5
# 0

#All characters in substring must be distinct 
#Finding the longest substring of non-repeating characters
#Codepath messed up at put 0 for "aaaaaaaa" which should be 1, because a counts as "a" substring with no repeating 

# holdingString = ""
# longestStringLength = 0
# for character in string 
    # if holdingString.find(character):
        # if len(holdingString) > longestStringLength:
            #longestStringLength = len(holdingString)
        # holdingString = character
    # else:
        # holdingString += character
#return longestStringLength

def length_of_longest_substring(s):
    holdingString = ""
    longestStringLength = 0
    for character in s:
        if holdingString.find(character) >= 0:
            if len(holdingString) > longestStringLength:
                longestStringLength = len(holdingString)
            holdingString = character
        else:
            holdingString += character
    return longestStringLength

# s = "abcdeefghhhhh"
# count = length_of_longest_substring(s)
# print(count)

# s2 = "aaaaaaaaaaaaaaa"
# count = length_of_longest_substring(s2)
# print(count)

# Problem 6: Roman to Integer

def characterToInt(character):
    if character == "I":
        return 1
    if character == "V":
        return 5
    if character == "X":
        return 10
    if character == "L":
        return 50
    if character == "C":
        return 100
    if character == "D":
        return 500
    if character == "M":
        return 1000
    

# def roman_to_int(s):
    #for character in s:
        #if character == I and (nextCharacter == V or nextCharacter == X):
            #total -= 1
        #elif character == X and (nextCharacter == L or nextCharacter == C):
            #total -= 10
        #elif character == C and (nextCharacter == D or nextCharacter == M):
            #total -= 100
        #else:
            #total += characterToInt(character)

def roman_to_int(s):
    total = 0
    for index in range(0,len(s)):
        if index == len(s)-1:
            total+= characterToInt(s[index])
        elif s[index] == "I" and (s[index+1] == "V" or s[index+1] == "X"):
            total -= 1
        elif s[index] == "X" and (s[index+1] == "L" or s[index+1] == "C"):
            total -= 10
        elif s[index] == "C" and (s[index+1] == "D" or s[index+1] == "M"):
            total -= 100
        else:
            total += characterToInt(s[index])
    return total


# s = "XL"
# print(roman_to_int(s))

# s2 = "LVIII"
# print(roman_to_int(s2))

# s3 = "MCMXCIV"
# print(roman_to_int(s3))