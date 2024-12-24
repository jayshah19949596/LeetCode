class Solution:
    def climbStairs(self, n):
        def climb_recursive(i):
            if i > n: return 0
            if i == n: return 1            
            one_step, two_step = climb_recursive(i+1), climb_recursive(i+2)
            climb_ways_from_cur_stair = one_step + two_step
            return climb_ways_from_cur_stair
        
        return climb_recursive(0)

class Solution:
    def climbStairs(self, n):
        memo = {}
        def climb_recursive_memo(i):
            if i in memo : return memo[i]
            if i > n: return 0
            if i == n: return 1            
            one_step, two_step = climb_recursive_memo(i+1), climb_recursive_memo(i+2)
            climb_ways_from_cur_stair = one_step + two_step
            memo[i] = climb_ways_from_cur_stair
            return memo[i]
        
        return climb_recursive_memo(0)

class Solution:
    def climb_iteratively(self, n):
        if n <= 0: return 0
        if n<= 2: return n

        tot_steps_till_stair_one, tot_steps_till_stair_two = 1, 2
        tot_steps_till_before_prev_stair, tot_steps_till_prev_stair = tot_steps_till_stair_one, tot_steps_till_stair_two
        
        for i in range(3, n+1):
            # tot_steps_till_cur_stair stores total steps TILL current stair. This will be addition of total steps TILL Prev Stair &&&& total steps TILL Before Prev Stair 
            tot_steps_till_cur_stair = tot_steps_till_before_prev_stair + tot_steps_till_prev_stair
            tot_steps_till_before_prev_stair = tot_steps_till_prev_stair
            tot_steps_till_prev_stair = tot_steps_till_cur_stair
        return tot_steps_till_cur_stair
