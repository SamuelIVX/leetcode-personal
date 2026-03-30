 # Problem: Find First Palindromic String in the Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
 # Tags: Array, Two Pointers, String

class Solution(object):
    def firstPalindrome(self, words):
        reversed = ""
        for word in words:
            reversed = word[::-1]
            if reversed == word:
                return word
        return ""     
        
