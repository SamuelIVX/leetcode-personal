 # Problem: Design HashSet
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/design-hashset/
 # Tags: Array, Hash Table, Linked List, Design, Hash Function

class MyHashSet(object):

    def __init__(self):
        self.list = []
        

    def add(self, key):
        if key not in self.list:
            self.list.append(key)

    def remove(self, key):
        for n in self.list:
            if n == key:
                self.list.remove(n)
        

    def contains(self, key):
        for n in self.list:
            if n == key:
                return True
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
