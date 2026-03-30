 # Problem: Add Two Numbers
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/add-two-numbers/
 # Tags: Linked List, Math, Recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            '''
            The sum will be initialized to the carry at the start of every iteration.
            Basically doing addition manually, as we need to keep track of any carries
            and make sure to bring that to the next set of numbers.
            '''
            summ = carry

            # Simply add both node values to summ
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next

            # Grab the carry (if any) by doing floor division on summ
            carry = summ//10
            # Then we keep the remaining sum as a new ListNode and link it to our Linked-List
            curr.next = ListNode(summ%10)
            curr = curr.next
        return dummy.next
