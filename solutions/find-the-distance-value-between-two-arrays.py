 # Problem: Find the Distance Value Between Two Arrays
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
 # Tags: Array, Two Pointers, Binary Search, Sorting

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        left, right = 0, 0
        count = 0
        n1, n2 = len(arr1), len(arr2)
        while left < n1 and right < n2:
            if abs(arr1[left] - arr2[right]) > d:
                right += 1
            else:
                right = 0
                left += 1 

            if right > n2-1:
                left += 1
                right = 0
                count += 1
        return count
