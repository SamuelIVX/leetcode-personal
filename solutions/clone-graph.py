 # Problem: Clone Graph
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/clone-graph/
 # Tags: Hash Table, Depth-First Search, Breadth-First Search, Graph Theory

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        # BFS
        if not node: return node

        visited = {} # Original Node -> Deep Copy Node [A new node object]
        q = deque([node])
        visited[node] = Node(node.val, []) # A new Node object

        while q:
            curr = q.popleft() # The current node

            for neighbor in curr.neighbors: # Check it's neighbors
                if neighbor not in visited: # If a neighbor does not have a deep copy 
                    
                    # Create a deep copy of that neighbor: Original Neighbor -> Deep Copy Neighbor
                    visited[neighbor] = Node(neighbor.val, []) 

                    # Add the current neighbor to the q to repeat this process
                    q.append(neighbor)
                    
                # Add the deep copy neighbor to the current deep copy node
                visited[curr].neighbors.append(visited[neighbor]) 
                    
        # Return the deep copy of the original node
        return visited[node]
