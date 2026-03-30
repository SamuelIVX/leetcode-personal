 # Problem: Valid Palindrome
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/valid-palindrome/
 # Tags: Two Pointers, String

class Solution(object):
    def isPalindrome(self, s):
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s2 = s2.lower()        
        left = 0
        right = len(s2) -1
        while(left < right):
            if s2[left] != s2[right]:
                return False
            left += 1
            right -= 1
        return True
        # s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        # s2 = s2.lower()
        # s3 = s2[::-1]
        # return s3 == s2
