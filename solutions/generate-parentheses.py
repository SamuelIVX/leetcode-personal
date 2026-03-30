 # Problem: Generate Parentheses
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/generate-parentheses/
 # Tags: String, Dynamic Programming, Backtracking

class Solution(object):
    def generateParenthesis(self, n):
        res, path = [],[]
        o, c = 0,0
        def recur(i, n, o, c):
            if i == 2*n:
                res.append("".join(path))
                return

            if o > c:
                path.append(')')
                recur(i + 1, n, o, c + 1)
                path.pop()

            if o < n:
                path.append('(')
                recur(i + 1, n, o + 1, c)
                path.pop()
            
        recur(0, n, o, c)
        return res
        
