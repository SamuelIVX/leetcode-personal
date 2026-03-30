 // Problem: Number of Steps to Reduce a Number to Zero
 // Difficulty: Easy
 // Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
 // Tags: Math, Bit Manipulation

class Solution {
    public int numberOfSteps(int num) {
        int steps = 0;
        while(num > 0){
            if(num % 2 == 0){
                num/=2;
                steps++;
            } else {
                num-=1;
                steps++;
            }
        }
        return steps;
    }
}
