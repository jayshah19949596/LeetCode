class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = float('inf')
        nums.sort()
        i = 0
        
        while i < len(nums)-2 :
            
            j = i+1
            k = len(nums)-1
            
            while j<k:
                triple = nums[i] + nums[j] + nums[k]
                
                if triple == target:
                    return triple
                if abs(triple - target) < abs(closest - target):
                    closest = triple
                
                if triple - target > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        
        return closest
                
