 # Problem: Reverse Prefix of Word
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/reverse-prefix-of-word/
 # Tags: Two Pointers, String, Stack

class Solution(object):
    def reversePrefix(self, word, ch):
        res = list(word)
        if ch in word:
            left = 0
            right = word.index(ch)
            while left <= right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
        return "".join(res)
            
