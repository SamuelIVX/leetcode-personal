 # Problem: Range Sum Query - Immutable
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/range-sum-query-immutable/
 # Tags: Array, Design, Prefix Sum

class NumArray(object):
    def __init__(self, nums):
        self.prefix = []
        curr = 0        
        for n in nums:
            curr += n
            self.prefix.append(curr)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        if left > 0:
            leftSum = self.prefix[left-1]
        else: 
            leftSum = 0
        return rightSum - leftSum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
