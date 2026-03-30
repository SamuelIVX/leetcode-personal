 # Problem: Intersection of Two Linked Lists
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
 # Tags: Hash Table, Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curr, other = headA, headB
        
        while curr != other:
            curr = curr.next if curr else headB
            other = other.next if other else headA
        return curr
