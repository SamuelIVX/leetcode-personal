 # Problem: Find Most Frequent Vowel and Consonant
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
 # Tags: Hash Table, String, Counting

class Solution(object):
    def maxFreqSum(self, s):
        mp = {}
        maxFreqV, maxFreqC = 0,0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for c in s:
            if c not in mp:
                mp[c] = 0
            mp[c] += 1

            if c in vowels:
                if mp[c] > maxFreqV: maxFreqV = mp[c]
                # maxFreqV = max(maxFreqV, mp[c])
            elif c not in vowels:
                if mp[c] > maxFreqC: maxFreqC = maxFreqC = mp[c]

        return maxFreqV + maxFreqC




        
