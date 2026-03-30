 # Problem: Replace Elements with Greatest Element on Right Side
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
 # Tags: Array

class Solution(object):
    def replaceElements(self, arr):
        rightMax = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr
        
