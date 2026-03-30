 # Problem: Reorder List
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/reorder-list/
 # Tags: Linked List, Two Pointers, Stack, Recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if head.next == None: return head

        slow = fast = head
        prev_slow = None
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        # Disconnect the node behind the middle node to make
        # 2 seperate linked-lists
        prev_slow.next = None 

        # Reverse the second half of the linked-list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Head is pointing to the head of the original linked-list
        # prev2 is pointing to the head of the second-half

        while head and prev:
            # Save the next nodes of both linked-lists
            temp1, temp2 = head.next, prev.next
            head.next = prev
            # Only set prev.next = temp1 if temp1 is not None
            # Since this would cause the while loop to end early and miss any nodes 
            # in the second-half.
            if temp1: prev.next = temp1 
            # Move both head nodes 
            head = temp1
            prev = temp2
        
        return head
