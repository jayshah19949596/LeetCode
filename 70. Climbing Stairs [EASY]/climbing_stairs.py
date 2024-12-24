class Solution:
    def climbStairs(self, n):
        # return self.climb_recursively(n, {})
        return self.climb_iteratively(n)

    def climb_recursively_brute_force(self, i, n):
        if i > n: return 0
        if i == n: return 1
        
        climb_one, climb_two = self.perform_climbing(i+1), self.perform_climbing(i+2)
        return climb_one + climb_two
    
    def climb_recursively_memo(self, i, n, memo):
        // memo will store the total number of steps FROM stair "i"
        if i in memo : return memo[n]
        if i > n: return 0
        if i == n: return 1
        
        climb_one, climb_two = self.perform_climbing(i+1), self.perform_climbing(i+2)
        results = climb_one + climb_two
        memo[i] = results
        return results
    
    def climb_iteratively(self, n):
        if n <= 0: return 0
        if n<= 2: return n

        tot_steps_till_stair_one, tot_steps_till_stair_two = 1, 2
        tot_steps_till_before_prev_stair, tot_steps_till_prev_stair = tot_steps_till_stair_one, tot_steps_till_stair_two
        
        for i in range(3, n+1):
            // tot_steps_till_cur_stair stores total steps TILL current stair. This will be addition of total steps TILL Prev Stair &&&& total steps TILL Before Prev Stair 
            tot_steps_till_cur_stair = tot_steps_till_before_prev_stair + tot_steps_till_prev_stair
            tot_steps_till_before_prev_stair = tot_steps_till_prev_stair
            tot_steps_till_prev_stair = tot_steps_till_cur_stair
        return tot_steps_till_cur_stair
