 # Problem: Sign of the Product of an Array
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/
 # Tags: Array, Math

def signFunc(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

class Solution(object):
    def arraySign(self, nums):
        product = 1
        for n in nums:
            product *= n
        return signFunc(product)
        
