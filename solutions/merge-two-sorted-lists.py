 # Problem: Merge Two Sorted Lists
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/merge-two-sorted-lists/
 # Tags: Linked List, Recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        '''
        Create a temporary Node that will act as the new linked-list
        Create a dummy node to act as the return value
        '''
        dummy = temp = ListNode(-1) 

        while list1 and list2:
            # Depending on which node is smaller, they will be appended first
            if list1.val < list2.val: # Access their values
                temp.next = list1 # Append the actual NODE OBJECT itself, not only the value
                list1 = list1.next # Move to the next node
            else:
                temp.next = list2 # Append the actual NODE OBJECT itself, not only the value
                list2 = list2.next # Move to the next node
            temp = temp.next # Always move to the next node regardless

        '''
        Both linked-lists can be of different sizes.
        So append the rest of the nodes to our merged linked-lists
        '''
        temp.next = list1 or list2 

        '''
        1. You need to return the next node after the head node, because our head node was initialized
        to some dummy value which it's only purpose was so we can append other nodes into it.
        2. You can't return temp.next because that variable is actively changing throughout our algorithm.
        Which in this case, it's pointing to the end of our list...
        3. So by returning 'dummy.next', dummy was initilized as pointing to the head node of our dummy node and
        was never updated. Therefore we can return the rest of our linked-list AFTER our head node which
        contains our sorted merged list.
        '''
        return dummy.next 
