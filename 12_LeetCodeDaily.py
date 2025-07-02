#Understand
#Problem is asking if the original array is sorted and in ascending order
#We can compare the shifted arrays to its sorted version to see if there are similar

#Match
#Lists

#Plan
#Create copy of list and check if its already sorted
#for length of the nums:
    #pop last element
    #insert last element to 0th index
    #compare sorted and shifted array
        #return True
#return False

#Implement
#Know how many positions a number can be in, so essentially the length of nums
#create a variable to compare if it ever is sorted in non decreasing order
#rotate array length of nums times to see if ever matches, else return false
def is_sorted_and_rotated(nums):
    sortedCopyOfNums = nums.copy()
    sortedCopyOfNums.sort()
    
    if sortedCopyOfNums == nums:
        return True
    
    #shift numbers to the right by 1 and compare with sortedNums
    for _ in range(len(nums)):
        poppedNum = nums.pop()
        nums.insert(0, poppedNum)
        if sortedCopyOfNums == nums:
            return True
    
    return False

#Evaluate
#Time Complexity O(n)
#Space Complexity O(n)