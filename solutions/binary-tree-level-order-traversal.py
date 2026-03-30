 # Problem: Binary Tree Level Order Traversal
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
 # Tags: Tree, Breadth-First Search, Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque()
        res = []

        q.append(root)
        cur_level = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.popleft()
                res[cur_level].append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            cur_level += 1
        return res

        
