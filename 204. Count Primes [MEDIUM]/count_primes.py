class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        # Initialize the sieve list: 1 represents a prime number
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        
        for i in range(2, n):
            if is_prime[i]:
                # Multiples of i smaller than i*i are already marked
                start_node = i * i
                
                # Iterate through multiples of i starting from i*i
                for multiple in range(start_node, n, i):
                    is_prime[multiple] = 0
                    
        return sum(is_prime)           
                
