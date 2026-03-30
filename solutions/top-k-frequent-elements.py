 # Problem: Top K Frequent Elements
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/top-k-frequent-elements/
 # Tags: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Count frequencies
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        # 2. Use a heap of size k
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))   # push (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap)             # maintain size k

        # 3. Extract results
        return [num for freq, num in heap]
