class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for i,n in enumerate(nums):
            streak,curr = 0,n
            while curr in seen:
                streak+=1
                curr+=1
            res = max(res,streak)
        return res