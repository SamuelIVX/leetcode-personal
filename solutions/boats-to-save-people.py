 # Problem: Boats to Save People
 # Difficulty: Medium
 # Link: https://leetcode.com/problems/boats-to-save-people/
 # Tags: Array, Two Pointers, Greedy, Sorting

class Solution(object):
    def numRescueBoats(self, people, limit):
        numofBoats = 0 
        left, right = 0, len(people) - 1
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else: 
                right -= 1

            numofBoats += 1

        return numofBoats
            
