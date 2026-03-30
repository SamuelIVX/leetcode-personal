 # Problem: Linked List Cycle
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/linked-list-cycle/
 # Tags: Hash Table, Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False
