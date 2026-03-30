 # Problem: Palindrome Linked List
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/palindrome-linked-list/
 # Tags: Linked List, Two Pointers, Stack, Recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        start = head
        end = None
        prev = None

        while head:
            head.prev = prev
            prev = head
            head = head.next
        
        end = prev

        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.prev
        return True
