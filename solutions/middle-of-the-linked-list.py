 # Problem: Middle of the Linked List
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/middle-of-the-linked-list/
 # Tags: Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise
