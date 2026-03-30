 # Problem: Find Words Containing Character
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/find-words-containing-character/
 # Tags: Array, String

class Solution(object):
    def findWordsContaining(self, words, x):
        return [index for index, s in enumerate(words) if x in s]
        
