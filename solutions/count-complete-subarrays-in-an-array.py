 # Problem: Count Complete Subarrays in an Array
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
 # Tags: Array, Hash Table, Sliding Window

class Solution(object):
    def countCompleteSubarrays(self, nums):
        l, r, valid = 0,0,0
        distinct = len(set(nums))
        window = []

        while r < len(nums):
            window.append(nums[r])

            if len(set(window)) == distinct:
                valid += len(nums) - r
                l += 1
                r = l
                del window[:] 
            else: r += 1

        return valid
        
