 # Problem: Search Insert Position
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/search-insert-position/
 # Tags: Array, Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            
        return mid+1 if nums[mid] < target else mid
