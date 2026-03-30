 # Problem: Intersection of Two Arrays
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/intersection-of-two-arrays/
 # Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
            
            

        
