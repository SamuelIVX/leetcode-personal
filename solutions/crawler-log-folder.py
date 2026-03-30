 # Problem: Crawler Log Folder
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/crawler-log-folder/
 # Tags: Array, String, Stack

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []    
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)
