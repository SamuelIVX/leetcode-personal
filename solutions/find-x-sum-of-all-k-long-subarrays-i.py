 # Problem: Find X-Sum of All K-Long Subarrays I
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
 # Tags: Array, Hash Table, Sliding Window, Heap (Priority Queue)

from collections import Counter
class Solution(object):
    def XSum(self, window, x, answer):
        freq = sorted(window.items(), key=lambda item: (-item[1], -item[0]))
        top_most_x = freq[:x]
        total = sum(val * freq for val, freq in top_most_x)
        answer.append(total)
        
    def findXSum(self, nums, k, x):
        l = 0
        answer = []
        for r in range(k, len(nums)+1):
            window = Counter(nums[l:r])
            self.XSum(window, x, answer)
            l += 1
    
        return answer

        # answer = []
        # for i in range(0, len(nums)-k+1):
        #     freqq = Counter(nums[i:i+k])
        #     sorted_freqq = sorted(freqq.items(), key=lambda item: (-item[1], -item[0]))
        #     top_x = sorted_freqq[:x]
        #     total = sum(val * freq for val, freq in top_x)
        #     answer.append(total)
        
        # return answer
