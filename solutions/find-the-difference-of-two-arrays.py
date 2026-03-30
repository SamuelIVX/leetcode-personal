 # Problem: Find the Difference of Two Arrays
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
 # Tags: Array, Hash Table

class Solution(object):
    def findDifference(self, nums1, nums2):
        n1 , n2 = set(nums1), set(nums2)

        res1 = []
        res2 = []

        for n in n1:
            if n not in n2:
                res1.append(n)

        for n in n2:
            if n not in n1:
                res2.append(n)

        return [res1, res2]
        
