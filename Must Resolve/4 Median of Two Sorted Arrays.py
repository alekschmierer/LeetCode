#Understand
#We have two sorted arrays and must find the median when the arrays are combined
#Must have a strict time complexity

#Match
#Two pointer apprach

#Plan
#pointer1 = 0
#pointer2 = 0
#nums3 = []

#while pointer1 < len(nums1) and pointer2 < len(nums2):
    #if nums1[pointer1] < nums2[pointer2]:
        #nums3.append(nums1)
        #pointer1 += 1
    #if nums2[pointer2] < nums1[pointer1]:
        #nums3.append(nums2)
        #pointer2 += 1

#while pointer1 < len(nums1):
    #nums3.append(nums1)
    #pointer1 += 1

#while pointer2 < len(nums2):
    #nums3.append(nums2)
    #pointer2 += 1

#Find Middle Element
#if len(nums3) % 2 == 0:
    #return [(nums3[len(nums3)/2 + nums3[(len(nums3)/2)+1) / 2]
#else:
    #return [nums3[len(nums3)/2]]

#Implement
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pointer1 = 0
        pointer2 = 0
        nums3 = []

        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                nums3.append(nums1[pointer1])
                pointer1 += 1
            else:
                nums3.append(nums2[pointer2])
                pointer2 += 1

        while pointer1 < len(nums1):
            nums3.append(nums1[pointer1])
            pointer1 += 1

        while pointer2 < len(nums2):
            nums3.append(nums2[pointer2])
            pointer2 += 1

        if len(nums3) % 2 == 0:
            return (nums3[len(nums3)//2-1] + nums3[(len(nums3)//2)]) / 2
        else:
            return nums3[len(nums3)//2]

#Evaluate
#Time Complexity: O(m + n), 
    #Must use binary serach to get to log(m+n), RESOLVE TO FULLY ANSWER QUESTION
#Space Complexity: O(n)
#Completed 7/6/25
#Time: 18:02