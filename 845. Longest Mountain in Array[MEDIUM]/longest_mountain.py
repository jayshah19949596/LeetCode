class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        max_ans = 0
        i = 1  # potential peak index range is [1, n-2]

        while i < n-1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l, r = i-1, i+1
                while l>0 and arr[l-1]<arr[l]:
                    l -= 1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r += 1
                max_ans = max(max_ans, r-l+1)
                i = r
            else:
                i += 1

        return max_ans
    
