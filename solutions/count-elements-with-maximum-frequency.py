 # Problem: Count Elements With Maximum Frequency
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
 # Tags: Array, Hash Table, Counting

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        maxFreq = 0

        for n in nums:
            if n not in mp:
                mp[n] = 0
            mp[n] += 1
            maxFreq = max(maxFreq, mp[n])

        for key, value in mp.items():
            if value == maxFreq: 
                res += value

        return res
