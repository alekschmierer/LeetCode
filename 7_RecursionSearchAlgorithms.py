def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)

# repeat_hello(5)

# print()

def repeat_hello_iterative(n):
    while n > 0:
        n -= 1
        print("Hello")

# repeat_hello_iterative(5)

#5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst.pop(len(lst)-1) + sum_list(lst)

# myList = [1, 2, 3, 4, 5]
# print(sum_list(myList))


def is_power_of_two(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    else:
        return is_power_of_two(n/2)
        
# print(is_power_of_two(0))
# print(is_power_of_two(5))


def binary_search(lst, target):
    leftPointer = 0
    rightPointer = len(lst)-1

    while leftPointer <= rightPointer:
        middleIndex = (rightPointer + leftPointer)//2
        if lst[middleIndex] == target:
            return middleIndex
        elif lst[middleIndex] < target: #Right Side Update
            leftPointer = middleIndex + 1
        else:
            rightPointer = middleIndex -1 #Left Side Update

    return -1

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# lst = [1,3,5,7,9,11,13,15]
# print(binary_search(lst, 13))

def find_last(lst, target):
    leftPointer = 0
    rightPointer = len(lst)-1
    middleIndexOccurence = None

    while leftPointer <= rightPointer:
        middleIndex = (rightPointer + leftPointer)//2
        if lst[middleIndex] == target:
            middleIndexOccurence = middleIndex
            break
        elif lst[middleIndex] < target: #Right Side Update
            leftPointer = middleIndex + 1
        else:
            rightPointer = middleIndex -1 #Left Side Update
    if middleIndexOccurence:
        return middleIndexOccurence
    else:
        return -1

# lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
# target = 11
# print(find_last(lst, target))

#(())    ((())) (()()())
def is_nested(paren_s):
    if paren_s == "":
        return True
    if paren_s[0] == '(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])
    return False

# print(is_nested(""))         # True
# print(is_nested("()"))       # True
# print(is_nested("(())"))     # True
# print(is_nested("(()())"))   
# print(is_nested("())("))     # False
# print(is_nested("((())"))    # False


# Example Input: [0, 0, 0, 0, 1, 1, 1]
def count_ones1(lst): #O(n) time
    counter = 0
    for index in range (len(lst)):
        if lst[index] == 1:
            counter += 1
    return counter

lst = [0, 0, 0, 0, 1, 1, 1]
# print(count_ones1(lst))

# Example Input: [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2 ,2]
def count_ones(lst):
    leftPointer = 0
    rightPointer = len(lst)-1
    counter = 0

    while leftPointer <= rightPointer:
        middleIndex = (rightPointer + leftPointer)//2
        if lst[middleIndex] == 1:
            counter +=1
        elif lst[middleIndex] < 1: #Right Side Update
            leftPointer = middleIndex + 1
        else:
            rightPointer = middleIndex -1 #Left Side Update

    return counter
lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(lst))

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
    result = [] # List to store the merged result
    i = j = 0 # Pointers to iterate over left and right input arrays

    # Compare elements from left and right halves of the list and add them to the
    # result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)

unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = merge_sort(unsorted_list)
# print(sorted_list)

def search(nums, target):
    leftPointer = 0
    rightPointer = len(nums)-1
    myArr = []

    while leftPointer <= rightPointer:
        middlePointer = (rightPointer + leftPointer) // 2

        if nums[middlePointer] == target:
            myArr.append(middlePointer)
            break
        elif nums[middlePointer] < target:
            leftPointer = middlePointer + 1
        else:
            rightPointer = middlePointer - 1
    
    if not myArr:
        return [-1,-1]
    
    newLeftPointer = 0
    newRightPointer = len(nums)-1
    
    while newLeftPointer <= newRightPointer:
        middlePointer = (newRightPointer + newLeftPointer) // 2

        if nums[middlePointer] == target:
            myArr.append(middlePointer)
            break
        elif nums[middlePointer] < target:
            newLeftPointer = middlePointer + 1
        else:
            newRightPointer = middlePointer - 1
    
    if not myArr:
        return [-1,-1]
    else:
        return myArr
    
    
nums = [5, 7, 7, 8, 8, 10]
target = 8

search(nums,target)




class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
	pass