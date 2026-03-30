 # Problem: Sort an Array
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/sort-an-array/
 # Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort

class Solution(object):
    def merge(self, left_half, right_half):
        merged_list = []
        i, j = 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged_list.append(left_half[i])
                i += 1
            else:
                merged_list.append(right_half[j])
                j += 1

        ## Add any remaining elements from the left half
        while i < len(left_half):
            merged_list.append(left_half[i])
            i += 1

        ## Add any remaining elements from the right half
        while j < len(right_half):
            merged_list.append(right_half[j])
            j += 1
        
        return merged_list

    def mergesort(self, nums):
        if len(nums) <= 1: return nums

        # Divide the array into two halves
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Recursively sort the two halves
        left_half = self.mergesort(left_half)
        right_half = self.mergesort(right_half)

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    def sortArray(self, nums):
        '''
        Using mergesort [Divide & Conquer Algorithm]
        that recursively divides the array, sorts the left and right sub array's
        and merges them back together
        '''
        return self.mergesort(nums)
