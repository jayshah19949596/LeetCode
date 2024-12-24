class Solution:
    def climbStairs(self, n):
        def climb_recursive(idx):
            if idx > n: return 0
            if idx == n: return 1            
            one_step, two_step = climb_recursive(idx+1), climb_recursive(idx+2)
            climb_ways_from_cur_stair = one_step + two_step
            return climb_ways_from_cur_stair
        
        return climb_recursive(0)

class Solution:
    def climbStairs(self, n):
        memo = {}
        def climb_recursive_memo(idx):
            if idx in memo : return memo[idx]
            if idx > n: return 0
            if idx == n: return 1            
            one_step, two_step = climb_recursive_memo(idx+1), climb_recursive_memo(idx+2)
            climb_ways_from_cur_stair = one_step + two_step
            memo[idx] = climb_ways_from_cur_stair
            return memo[idx]
        
        return climb_recursive_memo(0)

class Solution:
    def climbStairs(self, n):
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
