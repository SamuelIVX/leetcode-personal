 # Problem: Guess Number Higher or Lower
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/guess-number-higher-or-lower/
 # Tags: Binary Search, Interactive

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left+right)//2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
