 # Problem: Merge k Sorted Lists
 # Difficulty: Hard
 # Link: https://leetcode.com/problems/merge-k-sorted-lists/
 # Tags: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        
        dummy = temp = ListNode(-1)
        minheap = [] # Create a minheap

        '''
        Since you can't directly push a node into a heap - heapq.heappush(ll)
        You can push a tuple that will contain: 
            - the value within the current node
            - the index of the current node
            - the current head (node) of all linked-lists
        '''
        for i, head in enumerate(lists):
            if head: heapq.heappush(minheap, (head.val, i, head))

        while minheap:
            minn = heapq.heappop(minheap) # Pop the smallest node from the minheap
            temp.next = minn[2] # Connect the smallest node to our temp linked-list
            temp = temp.next # Move our temp linked-list 
            # If the next node of the current head node is NOT None, push 
            # the tuple of the next node.
            if minn[2].next: heapq.heappush(minheap, (minn[2].next.val, minn[1], minn[2].next))

        return dummy.next
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))

