 # Problem: Subtree of Another Tree
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/subtree-of-another-tree/
 # Tags: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isIdentical(self, node, other):
        if not node and not other: return True
        if (not node or not other) or node.val != other.val: return False

        return (self.isIdentical(node.left, other.left) and 
                self.isIdentical(node.right, other.right))

    def isSubtree(self, root, subRoot):
        if not root: return False
        if not subRoot: return True
        
        if self.isIdentical(root, subRoot): return True

        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))
        
