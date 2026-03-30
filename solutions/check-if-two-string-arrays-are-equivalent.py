 # Problem: Check If Two String Arrays are Equivalent
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
 # Tags: Array, String

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        concat1 = concat2 = ""

        for char in word1:
            concat1 += char

        for char in word2:
            concat2 += char
        return concat1 == concat2
