"""
Inbound binary search

We binary search the eating speed between 1 and max(piles). 
For each candidate speed we compute the total hours using ceiling division. 
If the hours exceed h, the speed is too slow; otherwise we try smaller speeds. The smallest valid speed is the answer.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle_speed = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile_bananas in piles:
                hour_spent += math.ceil(pile_bananas / middle_speed)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle_speed
            else:
                left = middle_speed + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right

"""
Regular Binary Search

We binary search the eating speed between 1 and max(piles). 
For each candidate speed we compute the total hours using ceiling division. 
If the hours exceed h, the speed is too slow; otherwise we try smaller speeds. The smallest valid speed is the answer.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        ans = right = max(piles)
        while left <= right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle_speed = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile_bananas in piles:
                hour_spent += math.ceil(pile_bananas / middle_speed)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                ans = middle_speed
                right = middle_speed - 1
            else:
                left = middle_speed + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return ans
