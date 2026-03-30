 # Problem: Invert Binary Tree
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/invert-binary-tree/
 # Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, root):
        #BFS
        if not root: return None

        stack = [root]

        while stack:
            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)

        return root
        
        # DFS
        # def dfs(node):
        #     if not node: return None

        #     node.left, node.right = node.right, node.left

        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return root
