 # Problem: Number of Distinct Averages
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/number-of-distinct-averages/
 # Tags: Array, Hash Table, Two Pointers, Sorting

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        distinct = set()
        left, right = 0, len(nums) - 1
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            distinct.add(avg)

            left += 1
            right -= 1
            
        return len(distinct)
