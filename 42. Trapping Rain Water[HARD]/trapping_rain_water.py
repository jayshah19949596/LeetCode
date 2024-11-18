class Solution:
    def trap(self, height: List[int]) -> int:
        lft, ryt = 0, len(height)-1
        water = max_lft = max_ryt = 0
        while lft<ryt:
            # increment smaller pointer
            if height[lft]<height[ryt]:
                if height[lft]>max_lft:
                    max_lft = height[lft]
                else:
                    water = water + (max_lft - height[lft])
                lft += 1
            else:
                if height[ryt]>max_ryt:
                    max_ryt = height[ryt]
                else:
                    water = water + (max_ryt - height[ryt])
                ryt -= 1
        return water
