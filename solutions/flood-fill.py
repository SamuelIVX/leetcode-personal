 # Problem: Flood Fill
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/flood-fill/
 # Tags: Array, Depth-First Search, Breadth-First Search, Matrix

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def changeColor(r, c, original_color):
            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                image[row][col] = color

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if (nr < 0 or nr > len(image)-1) or (nc < 0 or nc > len(image[0])-1): 
                        continue

                    if image[nr][nc] == original_color:
                        image[nr][nc] = color
                        q.append((nr, nc))
                    else: continue

        if image[sr][sc] == color: return image

        changeColor(sr, sc, image[sr][sc])
        return image
