"""
735. Asteroid Collision [MEDIUM]
https://leetcode.com/problems/asteroid-collision

### 1. Question Explanation:
----------------------------
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

#### Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

#### Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.


### 2. Solution Explanation:
----------------------------

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N).
Space Complexity: O(N).
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i, stack = 0, []

        while i<len(asteroids):
            cur_aestroid = asteroids[i]

            if len(stack)>0 and stack[-1]>0 and cur_aestroid<0:
                while len(stack)>0 and stack[-1]>0 and cur_aestroid<0:
                    stack_top_aestroid = stack.pop()
                    if stack_top_aestroid > abs(cur_aestroid):
                        stack.append(stack_top_aestroid)
                        break
                    elif stack_top_aestroid<abs(cur_aestroid): continue
                    else: break
                else:
                    stack.append(cur_aestroid)
            else:
                stack.append(cur_aestroid)

            i += 1

        return stack
