 # Problem: Find the K-Beauty of a Number
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-the-k-beauty-of-a-number/
 # Tags: Math, String, Sliding Window

class Solution(object):
    def divisorSubstrings(self, num, k):
        l = kb = 0
        str_num = str(num)
        for r in range(k, len(str_num) + 1):
            window = int(str_num[l:r])
            if (window != 0) and (num % window == 0): 
                kb += 1
            l += 1
        return kb
        
