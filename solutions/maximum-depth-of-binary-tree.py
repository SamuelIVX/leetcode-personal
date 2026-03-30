 # Problem: Maximum Depth of Binary Tree
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
 # Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
