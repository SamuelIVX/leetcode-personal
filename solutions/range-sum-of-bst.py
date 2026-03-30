 # Problem: Range Sum of BST
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/range-sum-of-bst/
 # Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        res = []
        def dfs(node, low, high):
            if not node:
                return

            if node.val < low:
                dfs(node.right, low, high)
            elif node.val > high:
                dfs(node.left, low, high)
            elif node.val >= low and node.val <= high:
                res.append(node.val)
                dfs(node.left, low, high)
                dfs(node.right, low, high)

        dfs(root,low, high)
        return sum(res)
