 # Problem: Valid Palindrome II
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/valid-palindrome-ii/
 # Tags: Two Pointers, String, Greedy

class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]: return True
    
        left, right = 0, len(s) - 1
        
        while left <= right:

            if s[left] != s[right]:
                left_s = s[:left] + s[left+1:]
                right_s = s[:right] + s[right+1:]
            
                return left_s == left_s[::-1] or right_s == right_s[::-1]

            left += 1
            right -= 1

        return True
