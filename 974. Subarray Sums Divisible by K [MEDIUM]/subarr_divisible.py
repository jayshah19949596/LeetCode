class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = defaultdict(int) # Empty dictionary
        ans = prefix_sum = 0

        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k

            # 1. Manually check if the sum from index 0 is divisible
            if rem == 0: ans += 1
            
            # 2. Check for previous internal subarrays
            if rem in remainder_map:
                ans += remainder_map[rem]
            remainder_map[rem] += 1
                
        return ans
