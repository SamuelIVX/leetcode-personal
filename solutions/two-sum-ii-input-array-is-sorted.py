 # Problem: Two Sum II - Input Array Is Sorted
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 # Tags: Array, Two Pointers, Binary Search

class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

