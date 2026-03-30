 # Problem: Largest Positive Integer That Exists With Its Negative
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
 # Tags: Array, Hash Table, Two Pointers, Sorting

class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        set_nums = set(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            if (nums[right]*-1) not in set_nums:
                right -= 1
            if (nums[left]*-1) in set_nums:
                return nums[left]*-1
            left += 1
        return -1
        # s=set(nums)
        # m=-1
        # for i in nums:
        #     if i>0 and -i in s:
        #         m=max(m,i)
        # return m      

