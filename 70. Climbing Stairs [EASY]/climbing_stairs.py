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

        stair_one_steps, stair_two_steps = 1, 2
        prev_before_stair_steps, prev_stair_steps = stair_one_steps, stair_two_steps
        
        for i in range(3, n+1):
            // cur_stair_steps stores total steps TILL current stair. This will be addition of total steps TILL Prev Stair &&&& total steps TILL Before Prev Stair 
            cur_stair_steps = prev_before_stair_steps + prev_stair_steps
            prev_before_stair_steps = prev_stair_steps
            prev_stair_steps = cur_stair_steps
        return cur_stair_steps
