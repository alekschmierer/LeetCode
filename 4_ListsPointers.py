# Problem 1: Perfect Number
# Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

# For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.

# def is_perfect_number(n):
#     pass
# Example Usage:

# print(is_perfect_number(6))
# print(is_perfect_number(28))
# print(is_perfect_number(9))
# Example Output:

# True
# True
# False

# Perfect number is postive integer, equal to sum of proper divisors, does not include itself
# Essentially all divisors that compose a number, when added together must be equal to the number


# def is_perfect_number(n):
#     pass
#total = 0

#for divisor in range(1,number):
    #if number % divisor == 0:
        #total += divisor

#return total
    

def is_perfect_number(n):
    total = 0

    for divisor in range(1,n):
        if n % divisor == 0:
            total += divisor
    if total == n:
        return True
    else:
        return False

# print(is_perfect_number(6))
# print(is_perfect_number(28))
# print(is_perfect_number(9))

# Problem 2: 2-Pointer Palindrome
# Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

# The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

# def is_palindrome(s):
#     pass
# Example Usage:

# s = "amanaplanacanalpanama"
# s2 = "helloworld"

# print(is_palindrome(s))
# print(is_palindrome(s2))
# Example Output:

# True
# False

#Must use two pointer approach, checking if we have a palindrome (spelt the same forwards and backwards)
#racecar, when pointers equal each other then we can just state its True still
#peep, also fine 

def is_palindrome(s):
    leftPointer, rightPointer = 0, len(s)-1
    for _ in range(len(s)//2):
        if s[leftPointer] == s[rightPointer]:
            leftPointer +=1
            rightPointer -= 1
        else:
            return False
    return True
    
s = "amanaplanacanalpanama"
s2 = "helloworld"

# print(is_palindrome(s))
# print(is_palindrome(s2))

# Problem 1: Prime Number
# Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

# def is_prime(n):
#     pass
# Example Usage:

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))
# Example Output:

# True
# False
# False

# Modulo operator, prime numbers greater than 1, more than 1 and iteself
# Covering both positive and negative numbers
# True if prime, false if not 

#def is_prime(n):
    #mySet = {}
    #if n < 1:
        #return False
        
    #if n%2 == 0 or n != 2:
            #return False
            
    #for i in range(1,n+1):
        #if len(mySet) > 2:
            #return False
        #if n mod i:
            #mySet.add(i)
    
    #return True
    
def is_prime(n):
    mySet = set()
    if n < 1:
        return False
        
    if n%2 == 0:
        return False
            
    for i in range(1,n+1):
        if n % i == 0:
            mySet.add(i)
        if len(mySet) > 2:
            return False
    
    return True

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))


# Problem 2: Two-Pointer Reverse List
# Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

# Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

# def reverse_list(lst):
#     pass
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]

#LeftPointer, RightPointer, 
#while left_pointer < right_pointer:
    # pass
    # left_pointer += 1
    # right_pointer -= 1

def reverse_list(lst):
    leftPointer = 0
    rightPointer = len(lst)-1
    
    while leftPointer < rightPointer:
        tempVariable = lst[leftPointer]
        lst[leftPointer] = lst[rightPointer]
        lst[rightPointer] = tempVariable
        leftPointer += 1
        rightPointer -= 1
    
    return lst

# print(reverse_list([1, 2, 3, 4, 5]))


# Problem 4: Move Even Integers
# Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

# def sort_array_by_parity(nums):
#     pass
# Example Usage:

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))
# Example Output:

# [2,4,3,1]
# # Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
# [0]

#Two Pointer approach, this time advance pointers, switch when even is on rightPointer and odd is on the leftPointer
#Inplace

def sort_array_by_parity(nums):
    leftPointer = 0
    rightPointer = len(nums)-1
    
    while leftPointer < rightPointer:
        while nums[leftPointer] % 2 == 0:
            leftPointer += 1
        while nums[rightPointer] % 2 != 0:
            rightPointer -= 1
        if(leftPointer > rightPointer):
            return nums
        tempVariable = nums[leftPointer]
        nums[leftPointer] = nums[rightPointer]
        nums[rightPointer] = tempVariable
    return nums

# nums = [3,1,2,4]
# nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))


# You are given a string s consisting of lowercase English letters, and are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

# Write a function make_palindrome() that takes in a string s and turns it into a palindrome with the minimum number of operations as possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

# The function returns the resulting palindrome string.

# def make_palindrome(s):
#     pass
# Example 1:

# s = "egcfe"
# s_pal = make_palindrome(s_pal)
# # s_pal == "efcfe"
# # The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# # another palindrome possible is "egcge", but it is not lexicographically smaller
# Example 2:

# s = "abcd"
# s_pal = make_palindrome(s_pal)
# # s_pal == "abba"
# # The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# # a palindrome cannot be created in 1 operation
# Example 3:

# s = "seven"
# s_pal = make_palindrome(s_pal)
# # s_pal == "neven"
# # The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# # to get a palindrome that is lexographically smaller, it would take more operations


#Two pointer method
#Compare both pointers and change the pointers value to the value that is lexigraphically smaller than the other

def make_palindrome(s_pal):
    leftPointer = 0
    rightPointer = len(s_pal)-1
    
    #Base Case Start and End Index
    if s_pal[leftPointer] == s_pal[rightPointer]:
        leftPointer += 1
        rightPointer -= 1
    elif s_pal[leftPointer] < s_pal[rightPointer]:
        s_pal = s_pal[0:rightPointer] + s_pal[leftPointer]
        leftPointer += 1
        rightPointer -= 1
    else:
        s_pal = s_pal[rightPointer] + s_pal[leftPointer+1:]
        leftPointer += 1
        rightPointer -= 1
    
    while leftPointer < rightPointer:
        if s_pal[leftPointer] == s_pal[rightPointer]:
            leftPointer += 1
            rightPointer -= 1
        elif s_pal[leftPointer] < s_pal[rightPointer]:
            s_pal = s_pal[:rightPointer] + s_pal[leftPointer] + s_pal[rightPointer+1:]
            leftPointer += 1
            rightPointer -= 1
        else:
            s_pal = s_pal[:leftPointer] + s_pal[rightPointer] + s_pal[leftPointer+1:]
            leftPointer += 1
            rightPointer -= 1
    return s_pal
            
# s = "a"
# s_pal = make_palindrome(s)
# print(s_pal)

# s = "effec"
# s_pal = make_palindrome(s)
# print(s_pal)

# s = "seven"
# s_pal = make_palindrome(s)
# print(s_pal)


# Problem 5: Reverse Vowels
# Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.

# def reverse_vowels(s):
#     pass
# Example Usage:

# s1 = "hello"
# rev_s1 = reverse_vowels(s1)
# print(rev_s1)

# s2 = "leetcode"
# rev_s2 = reverse_vowels(s2)
# print(rev_s2)
# Example Output:

# holle
# leotcede

#Upper case and lower case vowels can appear, and need to be swapped


def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    leftPointer = 0
    rightPointer = len(s) - 1

    while leftPointer < rightPointer:
        while leftPointer < rightPointer and s[leftPointer] not in vowels:
            leftPointer += 1
        while leftPointer < rightPointer and s[rightPointer] not in vowels:
            rightPointer -= 1

        if leftPointer < rightPointer:
            # Swap using slicing since strings are immutable
            s = (
                s[:leftPointer] +
                s[rightPointer] +
                s[leftPointer + 1:rightPointer] +
                s[leftPointer] +
                s[rightPointer + 1:]
            )
            leftPointer += 1
            rightPointer -= 1

    return s


# s1 = "hello"
# rev_s1 = reverse_vowels(s1)
# print(rev_s1)

# s2 = "leetcode"
# rev_s2 = reverse_vowels(s2)
# print(rev_s2)

# Problem 6: Two-Pointer Remove Element
# The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

# Write a function removeElement() that takes in a list nums and a value val as parameters and removes all instances of that value in-place. The function returns the new length of nums.

# def removeElement(nums, val):
#     pass
# Example Usage:

# nums = [5, 4, 4, 3, 4, 1]
# nums_len = removeElement(nums, 4)
# print(nums) # same list
# print(nums_len)
# Example Output:

# [5, 3, 1]
# 3

#Return new length of nums list
#We are working on the list in-place, meaning we cant 

def removeElement(nums, val):
    leftPointer = 0
    rightPointer = len(nums)-1
    while(leftPointer <= rightPointer):
        if nums[leftPointer] == val:
            nums.pop(leftPointer)
            rightPointer -=1
        else:
            leftPointer +=1
    return len(nums)

# nums = [5, 4, 4, 3, 4, 1]
# nums_len = removeElement(nums, 4)
# print(nums) # same list
# print(nums_len)


# Write a function reverse_prefix() that takes in a 0-indexed string word and a character ch as parameters. The function reverses the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive) and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the resulting string.

# def reverse_prefix(word, ch):
#     pass

#Prefix changes from index 0 to the first occurnece of the character. It revereses this substring inside the string

def reverse_prefix(word, ch):
    rightPointer = word.index(ch)
    
    newString = word[:rightPointer+1][::-1] + word[rightPointer+1:]
    return newString

    
    
# word = "abcdefd"
# rev_word = reverse_prefix(word, "d")
# print(rev_word)
