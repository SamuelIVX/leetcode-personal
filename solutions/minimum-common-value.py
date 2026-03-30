 # Problem: Minimum Common Value
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/minimum-common-value/
 # Tags: Array, Hash Table, Two Pointers, Binary Search

class Solution(object):
    def getCommon(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        left = right = 0
        while left < n1 and right < n2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            if nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return -1 
