 # Problem: Number of Students Unable to Eat Lunch
 # Difficulty: Easy
 # Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
 # Tags: Array, Stack, Queue, Simulation

class Solution(object):
    def countStudents(self, students, sandwiches):
        loop = 0
        while (sandwiches):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                loop = 0
            elif loop == len(students):
                break
            else:
                students.append(students.pop(0))
                loop += 1

        return len(students)
