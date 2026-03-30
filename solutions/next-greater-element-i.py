 # Problem: Next Greater Element I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/next-greater-element-i/
 # Tags: Array, Hash Table, Stack, Monotonic Stack

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums1Index = {n: i for i , n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                res[index] = curr
            if curr in nums1Index:
                stack.append(curr)
        return res
