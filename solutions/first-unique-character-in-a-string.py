 # Problem: First Unique Character in a String
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/first-unique-character-in-a-string/
 # Tags: Hash Table, String, Queue, Counting

class Solution(object):
    def firstUniqChar(self, s):
        mymap = {}
            
        for char in s:
            if char not in mymap:
                mymap[char] = 0
            mymap[char] += 1
        
        for index, value in enumerate(s):
            if mymap[value] == 1:
                return index
        return -1
