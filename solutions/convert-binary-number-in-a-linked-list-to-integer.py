 # Problem: Convert Binary Number in a Linked List to Integer
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 # Tags: Linked List, Math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        res = ""
        curr = head

        while curr:
            res += str(curr.val)
            curr = curr.next

        return int(res, 2)        
