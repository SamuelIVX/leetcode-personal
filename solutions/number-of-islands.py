 # Problem: Number of Islands
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/number-of-islands/
 # Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

class Solution(object):
    def numIslands(self, grid):
        visited = {}
        island = 0
        list_of_dir = [(1,0), (-1, 0), (0,1), (0, -1)]

        def dfs(row, column, visited):
            if (row < 0 or row > len(grid)-1) or (column < 0 or column > len(grid[0])-1): return 
            elif grid[row][column] == '0': return 
            elif (row, column) in visited: return 

            visited[(row, column)] = True

            for r_dir, c_dir in list_of_dir:
                dfs(row + r_dir, column + c_dir, visited)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1' and (row, column) not in visited:
                    dfs(row, column, visited)
                    island += 1
        return island
            
