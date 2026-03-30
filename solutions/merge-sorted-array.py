 # Problem: Merge Sorted Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/merge-sorted-array/
 # Tags: Array, Two Pointers, Sorting

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        R = 0

        while R < n:
            nums1[m] = nums2[R]

            m += 1
            R += 1
            
        return nums1.sort()
